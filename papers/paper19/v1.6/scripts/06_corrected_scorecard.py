from __future__ import annotations

import json
import math
import tarfile
import urllib.request
from pathlib import Path

import mpmath as mp
import numpy as np
from camb import get_results, model
from classy import Class
from scipy.integrate import quad
from scipy.stats import chi2 as chi2_dist

"""
Reproduce the Paper 19 corrected scorecard on the repaired R4/FIRAS convention.

This script is a heavy optional rerun. It requires CAMB, CLASS, scipy, numpy,
and external BAO mean/covariance files. DESI/BAO files are not redistributed in
this bundle; set ``BAO_MEAN_PATH`` and ``BAO_COV_PATH`` or place them under
``../data/external/desi_bao/`` with the filenames documented in
``data/external_data_sources.md``.

The observer-side temperature is the FIRAS-fixed datum from Paper 17 v1.5, not
an independent CMB-temperature prediction.

Output:
    ../results/corrected_scorecard_results.json
"""

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT
OUT = BUNDLE_ROOT / "results" / "corrected_scorecard_results.json"

import os

BAO_MEAN = Path(os.environ.get("BAO_MEAN_PATH", BUNDLE_ROOT / "data" / "external" / "desi_bao" / "desi_2024_gaussian_bao_ALL_GCcomb_mean.txt"))
BAO_COV = Path(os.environ.get("BAO_COV_PATH", BUNDLE_ROOT / "data" / "external" / "desi_bao" / "desi_2024_gaussian_bao_ALL_GCcomb_cov.txt"))

TMP = BUNDLE_ROOT / "data" / "external" / "boss_fullshape_tmp"
ARCHIVE = TMP / "Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz"
DATA_ROOT = TMP / "public_material_RSD"

C_KM_S = 299792.458
C_M_S = 299792458.0
R_S_M = 6.685e26

GAMMA = 0.2375
X = 1.51899
DELTA = X**4 * (1 + GAMMA**2)
K_GAUGE = math.log(1.0 + GAMMA**2)
T_IO_BULK = 2.6635
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255

H0_IO = 68.91
OMEGA_M_IO = 0.335
OMEGA_K_IO = -0.006
# Observer-side temperature is not an independent Paper 19 prediction.
# Paper 19 v1.6 inherits Paper 17 v1.5: FIRAS fixes the unique optical
# readout normalization R4, and the frozen observer-side thermal datum is
# propagated without retuning.
T0_IO = T_FIRAS

# Keep the Paper 18 background branch fixed for this audit.
N_EFF_PAPER18 = 5.62421685262410640625

# Exact baryon branches from Paper 19 artifacts.
OMEGA_B_ALPHA_3_OVER_2 = 0.01705304256634875548471202990379874811457514160441
OMEGA_B_ALPHA_1 = 0.02101741663588963
OMEGA_B_OLD_BAD = 0.04974483580619357
OMEGA_B_OLD_PAPER18_GEOM = 0.02108

H0_LCDM = 67.36
OMEGA_M_LCDM = 0.3153
OMEGA_K_LCDM = 0.0
T0_LCDM = 2.7255
N_EFF_LCDM = 3.046
OMEGA_B_LCDM = 0.02237
R_D_IO_FIXED = 143.3

A_S = 2.1e-9
N_S = 0.9649
TAU_REIO = 0.0544
M_NU = 0.06


def omega_r(t0: float, n_eff: float, h: float) -> float:
    omega_gamma_h2 = 2.4728e-5 * (t0 / 2.7255) ** 4
    omega_r_h2 = omega_gamma_h2 * (1 + 0.22710731766 * n_eff)
    return omega_r_h2 / h**2


def e_z(z: float, omega_m: float, omega_k: float, omega_r_val: float) -> float:
    omega_lambda = 1 - omega_m - omega_k - omega_r_val
    return math.sqrt(
        omega_r_val * (1 + z) ** 4
        + omega_m * (1 + z) ** 3
        + omega_k * (1 + z) ** 2
        + omega_lambda
    )


def distances(z: float, *, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float) -> tuple[float, float, float]:
    h = h0 / 100.0
    omega_r_val = omega_r(t0, n_eff, h)
    chi, _ = quad(lambda zp: 1.0 / e_z(zp, omega_m, omega_k, omega_r_val), 0, z, epsabs=1e-12, epsrel=1e-12, limit=200)
    d_h = C_KM_S / (h0 * e_z(z, omega_m, omega_k, omega_r_val))
    d_c = (C_KM_S / h0) * chi
    if abs(omega_k) < 1e-14:
        d_m = d_c
    elif omega_k > 0:
        s = math.sqrt(omega_k) * chi
        d_m = (C_KM_S / h0) * math.sinh(s) / math.sqrt(omega_k)
    else:
        s = math.sqrt(-omega_k) * chi
        d_m = (C_KM_S / h0) * math.sin(s) / math.sqrt(-omega_k)
    d_v = (z * d_m * d_m * d_h) ** (1.0 / 3.0)
    return d_m, d_h, d_v


def load_bao() -> tuple[list[tuple[float, float, str]], np.ndarray]:
    if not BAO_MEAN.exists() or not BAO_COV.exists():
        raise FileNotFoundError(
            "DESI BAO mean/covariance files are not bundled. Set BAO_MEAN_PATH "
            "and BAO_COV_PATH, or place the files under data/external/desi_bao/. "
            "See data/external_data_sources.md."
        )
    triples: list[tuple[float, float, str]] = []
    for line in BAO_MEAN.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        z, value, quantity = line.split()
        triples.append((float(z), float(value), quantity))
    covariance = np.loadtxt(BAO_COV)
    return triples, np.linalg.inv(covariance)


def bao_chi2(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float, r_d: float) -> tuple[float, float]:
    triples, inv_cov = load_bao()
    obs = np.array([value for _, value, _ in triples])
    pred = []
    for z, _, quantity in triples:
        d_m, d_h, d_v = distances(z, h0=h0, omega_m=omega_m, omega_k=omega_k, t0=t0, n_eff=n_eff)
        if quantity == "DM_over_rs":
            pred.append(d_m / r_d)
        elif quantity == "DH_over_rs":
            pred.append(d_h / r_d)
        elif quantity == "DV_over_rs":
            pred.append(d_v / r_d)
        else:
            raise ValueError(quantity)
    diff = np.array(pred) - obs
    chi2 = float(diff @ inv_cov @ diff)
    return chi2, float(chi2_dist.sf(chi2, len(obs)))


def run_class_model(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float, omega_b: float) -> dict[str, float]:
    h = h0 / 100.0
    omega_m_h2 = omega_m * h * h
    omega_nu = M_NU / 93.14
    omega_cdm = omega_m_h2 - omega_b - omega_nu
    cosmo = Class()
    cosmo.set(
        {
            "output": "mPk",
            "P_k_max_h/Mpc": 10.0,
            "z_pk": "0",
            "h": h,
            "omega_b": omega_b,
            "omega_cdm": omega_cdm,
            "Omega_k": omega_k,
            "A_s": A_S,
            "n_s": N_S,
            "tau_reio": TAU_REIO,
            "T_cmb": t0,
            "N_ur": n_eff - 1.0132,
            "N_ncdm": 1,
            "m_ncdm": M_NU,
        }
    )
    cosmo.compute()
    sigma8 = float(cosmo.sigma8())
    s8 = sigma8 * math.sqrt(omega_m / 0.3)
    rs_drag = float(cosmo.rs_drag())
    return {
        "h": h,
        "omega_m_h2": omega_m_h2,
        "omega_b": omega_b,
        "omega_nu": omega_nu,
        "omega_cdm": omega_cdm,
        "sigma8": sigma8,
        "S8": s8,
        "rs_drag_Mpc": rs_drag,
    }


def age_at_z(H0: mp.mpf, Or: mp.mpf, Om: mp.mpf, Ok: mp.mpf, Ol: mp.mpf, z: mp.mpf) -> mp.mpf:
    h = H0 / 100
    hubble_time_gyr = mp.mpf("9.778130") / h
    a = 1 / (1 + z)
    integrand = lambda a_: 1 / (a_ * mp.sqrt(Or / a_**4 + Om / a_**3 + Ok / a_**2 + Ol))
    return hubble_time_gyr * mp.quad(integrand, [0, a])


def jwst_ages(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float) -> dict[str, str]:
    mp.mp.dps = 80
    H0_m = mp.mpf(str(h0))
    Om_m = mp.mpf(str(omega_m))
    Ok_m = mp.mpf(str(omega_k))
    T0_m = mp.mpf(str(t0))
    Neff_m = mp.mpf(str(n_eff))
    h = H0_m / 100
    Or = mp.mpf("2.4728e-5") * (T0_m / mp.mpf("2.7255")) ** 4
    Or *= 1 + mp.mpf("0.22710731766") * Neff_m
    Or /= h**2
    Ol = 1 - Om_m - Ok_m - Or
    ages = {str(z): str(age_at_z(H0_m, Or, Om_m, Ok_m, Ol, mp.mpf(z)) * 1000) for z in [6, 10, 14, 20]}
    ages["today_Gyr"] = str(age_at_z(H0_m, Or, Om_m, Ok_m, Ol, mp.mpf("0")))
    return ages


def ensure_boss_data() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    if not ARCHIVE.exists():
        urllib.request.urlretrieve(
            "https://fbeutler.github.io/static/Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz",
            ARCHIVE,
        )
    if not DATA_ROOT.exists():
        with tarfile.open(ARCHIVE, "r:gz") as tf:
            tf.extractall(TMP)


def read_pk(path: Path) -> np.ndarray:
    rows = []
    start = False
    with path.open() as handle:
        for line in handle:
            s = line.strip()
            if s.startswith("4 columns:"):
                start = True
                continue
            if not start or not s:
                continue
            parts = s.split()
            if len(parts) >= 4:
                rows.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])])
    return np.array(rows)


def read_cov(path: Path) -> tuple[np.ndarray, np.ndarray]:
    arr = np.loadtxt(path, skiprows=4)
    mono = np.unique(arr[arr[:, 0] < 60, 0].astype(int))
    cov = np.zeros((len(mono), len(mono)))
    for i, ii in enumerate(mono):
        for j, jj in enumerate(mono):
            mask = (arr[:, 0] == ii) & (arr[:, 1] == jj)
            if mask.any():
                cov[i, j] = arr[mask, 4][0]
    return mono, cov


def load_boss_samples() -> list[tuple[str, float, np.ndarray, np.ndarray, np.ndarray]]:
    ensure_boss_data()
    samples = []
    z_map = {"z1": 0.38, "z2": 0.51, "z3": 0.61}
    for cap in ["NGC", "SGC"]:
        for z_label, z_eff in z_map.items():
            pk_path = DATA_ROOT / f"Beutleretal_pk_monopole_DR12_{cap}_{z_label}_prerecon_120.dat"
            cov_path = DATA_ROOT / (
                f"Beutleretal_cov_patchy_{z_label}_{cap}_1_15_1_15_1_10_"
                f"{2045 if cap == 'NGC' else 2048}_60.dat"
            )
            data_all = read_pk(pk_path)
            mono_idx, cov = read_cov(cov_path)
            rows = data_all[mono_idx - 1]
            samples.append((f"{cap}_{z_label}", z_eff, rows[:, 1], rows[:, 2], cov))
    return samples


def make_linear_pk(*, H0: float, ombh2: float, omch2: float, omk: float, Tcmb: float, Neff: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    pars = model.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, omk=omk, TCMB=Tcmb, nnu=Neff, mnu=0.0, tau=TAU_REIO)
    pars.InitPower.set_params(As=A_S, ns=N_S)
    pars.set_matter_power(redshifts=[0.61, 0.51, 0.38], kmax=0.3)
    pars.NonLinear = model.NonLinear_none
    res = get_results(pars)
    return res.get_linear_matter_power_spectrum(hubble_units=True, k_hunit=True)


def theory_interp(k_data: np.ndarray, z_eff: float, kh: np.ndarray, z_grid: np.ndarray, pk_grid: np.ndarray) -> np.ndarray:
    iz = int(np.argmin(np.abs(z_grid - z_eff)))
    return np.interp(k_data, kh, pk_grid[iz])


def fit_linear_nuisance(data: np.ndarray, cov: np.ndarray, theory: np.ndarray, k: np.ndarray) -> float:
    X = np.column_stack([theory, np.ones_like(k), k**2, k])
    cov_inv = np.linalg.inv(cov)
    coeff = np.linalg.solve(X.T @ cov_inv @ X, X.T @ cov_inv @ data)
    resid = data - X @ coeff
    return float(resid.T @ cov_inv @ resid)


def boss_fullshape_chi2(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float, omega_b: float) -> float:
    h = h0 / 100.0
    omega_b_frac = omega_b / (h * h)
    omega_cdm = omega_m - omega_b_frac
    kh, z_grid, pk_grid = make_linear_pk(
        H0=h0,
        ombh2=omega_b,
        omch2=omega_cdm * h * h,
        omk=omega_k,
        Tcmb=t0,
        Neff=n_eff,
    )
    total = 0.0
    for _, z_eff, k, p0, cov in load_boss_samples():
        theory = theory_interp(k, z_eff, kh, z_grid, pk_grid)
        total += fit_linear_nuisance(p0, cov, theory, k)
    return total


def branch_summary(name: str, omega_b: float, *, class_summary: bool = True) -> dict[str, object]:
    model_info = None
    bao_chi2_val = None
    bao_pte = None
    if class_summary:
        model_info = run_class_model(
            h0=H0_IO,
            omega_m=OMEGA_M_IO,
            omega_k=OMEGA_K_IO,
            t0=T0_IO,
            n_eff=N_EFF_PAPER18,
            omega_b=omega_b,
        )
        bao_chi2_val, bao_pte = bao_chi2(
            h0=H0_IO,
            omega_m=OMEGA_M_IO,
            omega_k=OMEGA_K_IO,
            t0=T0_IO,
            n_eff=N_EFF_PAPER18,
            r_d=model_info["rs_drag_Mpc"],
        )
    boss_chi2_val = boss_fullshape_chi2(
        h0=H0_IO,
        omega_m=OMEGA_M_IO,
        omega_k=OMEGA_K_IO,
        t0=T0_IO,
        n_eff=N_EFF_PAPER18,
        omega_b=omega_b,
    )
    return {
        "name": name,
        "omega_b": omega_b,
        "Omega_b": omega_b / (H0_IO / 100.0) ** 2,
        "sigma8": None if model_info is None else model_info["sigma8"],
        "S8": None if model_info is None else model_info["S8"],
        "rs_drag_Mpc": None if model_info is None else model_info["rs_drag_Mpc"],
        "bao_chi2_desi_dr1": bao_chi2_val,
        "bao_pte_desi_dr1": bao_pte,
        "boss_fullshape_chi2": boss_chi2_val,
        "class_note": None if model_info is not None else "CLASS summary skipped for this branch because omega_b is outside the default BBN-helium interpolation table.",
    }


def main() -> None:
    omega_r_io = omega_r(T0_IO, N_EFF_PAPER18, H0_IO / 100.0)
    z_eq_io = OMEGA_M_IO / omega_r_io - 1.0
    ages = jwst_ages(h0=H0_IO, omega_m=OMEGA_M_IO, omega_k=OMEGA_K_IO, t0=T0_IO, n_eff=N_EFF_PAPER18)
    fixed_ruler_bao_chi2, fixed_ruler_bao_pte = bao_chi2(
        h0=H0_IO,
        omega_m=OMEGA_M_IO,
        omega_k=OMEGA_K_IO,
        t0=T0_IO,
        n_eff=N_EFF_PAPER18,
        r_d=R_D_IO_FIXED,
    )

    alpha_3_over_2 = branch_summary("alpha_3_over_2_clustering", OMEGA_B_ALPHA_3_OVER_2)
    alpha_1 = branch_summary("alpha_1_geometric_comparison", OMEGA_B_ALPHA_1)
    old_bad = branch_summary("old_bad_projected_mapping", OMEGA_B_OLD_BAD, class_summary=False)
    old_paper18_geom = branch_summary("paper18_geometric_scorecard_value", OMEGA_B_OLD_PAPER18_GEOM)

    lcdm_ref = run_class_model(
        h0=H0_LCDM,
        omega_m=OMEGA_M_LCDM,
        omega_k=OMEGA_K_LCDM,
        t0=T0_LCDM,
        n_eff=N_EFF_LCDM,
        omega_b=OMEGA_B_LCDM,
    )
    bao_lcdm_chi2, bao_lcdm_pte = bao_chi2(
        h0=H0_LCDM,
        omega_m=OMEGA_M_LCDM,
        omega_k=OMEGA_K_LCDM,
        t0=T0_LCDM,
        n_eff=N_EFF_LCDM,
        r_d=lcdm_ref["rs_drag_Mpc"],
    )
    boss_lcdm = boss_fullshape_chi2(
        h0=H0_LCDM,
        omega_m=OMEGA_M_LCDM,
        omega_k=OMEGA_K_LCDM,
        t0=T0_LCDM,
        n_eff=N_EFF_LCDM,
        omega_b=OMEGA_B_LCDM,
    )

    payload = {
        "inputs": {
            "gamma": GAMMA,
            "x": X,
            "Delta": DELTA,
            "K_gauge": K_GAUGE,
            "R4_FIRAS": R4_FIRAS,
            "T_IO_bulk_K": T_IO_BULK,
            "T_FIRAS_K": T_FIRAS,
            "temperature_status": "IMPORTED/EMPIRICAL FIRAS datum fixing Paper 17 v1.5 R4; not an independent CMB prediction",
            "H0_IO": H0_IO,
            "Omega_m_IO": OMEGA_M_IO,
            "Omega_k_IO": OMEGA_K_IO,
            "T0_IO": T0_IO,
            "N_eff_background_kept_from_paper18": N_EFF_PAPER18,
            "omega_b_alpha_3_over_2": OMEGA_B_ALPHA_3_OVER_2,
            "omega_b_alpha_1_exact": OMEGA_B_ALPHA_1,
            "omega_b_old_paper18_geometric_value": OMEGA_B_OLD_PAPER18_GEOM,
            "omega_b_old_bad_projected_mapping": OMEGA_B_OLD_BAD,
        },
        "equality_redshift": {
            "statement": "With H0, Omega_m, T0, and N_eff held fixed, z_eq is independent of the baryon split.",
            "z_eq_alpha_3_over_2": z_eq_io,
            "z_eq_alpha_1": z_eq_io,
            "z_eq_old_paper18_branch": z_eq_io,
        },
        "bao_observable_split": {
            "paper18_framework_fixed_ruler": {
                "r_d_IO_fixed_Mpc": R_D_IO_FIXED,
                "chi2_desi_dr1": fixed_ruler_bao_chi2,
                "pte_desi_dr1": fixed_ruler_bao_pte,
                "statement": "This is the original Paper 18 geometric-ruler BAO observable, so the late-time clustering omega_b remapping does not change it.",
            },
            "standard_sound_horizon_readout_lcdm_reference": {
                "rs_drag_Mpc": lcdm_ref["rs_drag_Mpc"],
                "chi2_desi_dr1": bao_lcdm_chi2,
                "pte_desi_dr1": bao_lcdm_pte,
            },
        },
        "jwst_ages_myr": ages,
        "branches": {
            "alpha_3_over_2": alpha_3_over_2,
            "alpha_1": alpha_1,
            "paper18_geometric_scorecard": old_paper18_geom,
            "old_bad_projected_mapping": old_bad,
            "lcdm_reference": {
                "sigma8": lcdm_ref["sigma8"],
                "S8": lcdm_ref["S8"],
                "rs_drag_Mpc": lcdm_ref["rs_drag_Mpc"],
                "bao_chi2_desi_dr1": bao_lcdm_chi2,
                "bao_pte_desi_dr1": bao_lcdm_pte,
                "boss_fullshape_chi2": boss_lcdm,
            },
        },
        "n_independent_observables": {
            "T_CMB": {
                "affected_by_clustering_omega_b_change": False,
                "value_K": T0_IO,
                "status": "IMPORTED/EMPIRICAL FIRAS-fixed observer-side thermal datum; not counted as an independent prediction",
            },
            "D_over_H": {
                "affected_by_clustering_omega_b_change": False,
                "reason": "Paper 19 only changes the late-time matter-transfer baryon slot, not the BBN microphysical branch.",
            },
            "Y_p": {
                "affected_by_clustering_omega_b_change": False,
                "reason": "Same as D/H: the BBN sector is not recomputed by the clustering Jacobian.",
            },
            "w": {
                "affected_by_clustering_omega_b_change": False,
                "value": -1.0,
            },
            "a0": {
                "affected_by_clustering_omega_b_change": False,
                "value_m_per_s2": C_M_S**2 / R_S_M,
            },
        },
    }

    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
