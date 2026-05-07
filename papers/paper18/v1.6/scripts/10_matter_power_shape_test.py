"""Run the Paper 18 BOSS DR12 full-shape matter-power diagnostic.

This is the expensive/optional external-data script behind Paper 18's
`N_eff = Delta` no-go. It fetches the public Beutler et al. BOSS DR12
full-shape package, runs CAMB for the conditional IO branch and a LambdaCDM
reference, then fits simple nuisance templates to the monopole samples.

Paper 18 v1.6 repairs only the observer-side thermal input. The old
`T0 = 2.7253 K` shorthand from implicit `R4 = 1` is replaced by the Paper 17
v1.5 FIRAS-fixed readout `R4_FIRAS = 1.0031014644`, i.e. `T0 = 2.7255 K`.
The catastrophic P(k) failure remains a conditional-branch no-go, not an active
framework prediction.
"""

import json
import tarfile
import urllib.request
from pathlib import Path

import numpy as np
from camb import get_results, model


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
BASE = BUNDLE_ROOT
TMP = BASE / "data" / "boss_fullshape_tmp"
ARCHIVE = TMP / "Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz"
DATA_ROOT = TMP / "public_material_RSD"
OUT_JSON = BASE / "results" / "paper18_matter_power_shape_test_checks.json"

GAMMA_BI = 0.2375
X_R4_SOURCE = 1.519
K_GAUGE = np.log(1.0 + GAMMA_BI**2)
R4_FIRAS = 1.0031014644
T_IO_BULK = 2.6635
T_FIRAS = 2.7255
T_OBS_R4 = T_IO_BULK * (X_R4_SOURCE ** (R4_FIRAS * K_GAUGE))


def ensure_data() -> None:
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


def make_linear_pk(
    *,
    H0: float,
    ombh2: float,
    omch2: float,
    omk: float,
    Tcmb: float,
    Neff: float,
    As: float,
    ns: float,
    tau: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    pars = model.CAMBparams()
    pars.set_cosmology(
        H0=H0,
        ombh2=ombh2,
        omch2=omch2,
        omk=omk,
        TCMB=Tcmb,
        nnu=Neff,
        mnu=0.0,
        tau=tau,
    )
    pars.InitPower.set_params(As=As, ns=ns)
    pars.set_matter_power(redshifts=[0.61, 0.51, 0.38], kmax=0.3)
    pars.NonLinear = model.NonLinear_none
    res = get_results(pars)
    return res.get_linear_matter_power_spectrum(hubble_units=True, k_hunit=True)


def theory_interp(
    k_data: np.ndarray,
    z_eff: float,
    kh: np.ndarray,
    z_grid: np.ndarray,
    pk_grid: np.ndarray,
) -> np.ndarray:
    iz = int(np.argmin(np.abs(z_grid - z_eff)))
    return np.interp(k_data, kh, pk_grid[iz])


def fit_linear_nuisance(
    data: np.ndarray,
    cov: np.ndarray,
    theory: np.ndarray,
    k: np.ndarray,
    mode: str,
) -> tuple[float, np.ndarray]:
    columns = [theory, np.ones_like(k)]
    if mode in {"amp_const_k2", "amp_const_k_k2"}:
        columns.append(k**2)
    if mode == "amp_const_k_k2":
        columns.append(k)
    X = np.column_stack(columns)
    cov_inv = np.linalg.inv(cov)
    coeff = np.linalg.solve(X.T @ cov_inv @ X, X.T @ cov_inv @ data)
    resid = data - X @ coeff
    chi2 = float(resid.T @ cov_inv @ resid)
    return chi2, coeff


def main() -> None:
    ensure_data()

    As = 2.1e-9
    ns = 0.9649
    tau = 0.0544

    io = {
        "H0": 68.91,
        "Omega_m": 0.335,
        "Omega_k": -0.006,
        "T0": T_OBS_R4,
        "N_eff": 5.62421685262410640625,
        "f_b": 0.3127,
        "R4_FIRAS": R4_FIRAS,
        "T_FIRAS": T_FIRAS,
        "T0_minus_FIRAS": T_OBS_R4 - T_FIRAS,
        "thermal_status": "FIRAS-fixed observer readout; not an independent CMB-temperature prediction.",
    }
    io["Omega_b"] = io["Omega_m"] * io["f_b"]
    io_h = io["H0"] / 100.0
    io["ombh2"] = io["Omega_b"] * io_h * io_h
    io["omch2"] = (io["Omega_m"] - io["Omega_b"]) * io_h * io_h

    lcdm = {
        "H0": 67.36,
        "Omega_m": 0.3153,
        "Omega_k": 0.0,
        "T0": 2.7255,
        "N_eff": 3.046,
        "ombh2": 0.02237,
        "omch2": 0.1200,
    }

    io_pk = make_linear_pk(
        H0=io["H0"],
        ombh2=io["ombh2"],
        omch2=io["omch2"],
        omk=io["Omega_k"],
        Tcmb=io["T0"],
        Neff=io["N_eff"],
        As=As,
        ns=ns,
        tau=tau,
    )
    lcdm_pk = make_linear_pk(
        H0=lcdm["H0"],
        ombh2=lcdm["ombh2"],
        omch2=lcdm["omch2"],
        omk=lcdm["Omega_k"],
        Tcmb=lcdm["T0"],
        Neff=lcdm["N_eff"],
        As=As,
        ns=ns,
        tau=tau,
    )

    samples = []
    z_map = {"z1": 0.38, "z2": 0.51, "z3": 0.61}
    modes = ["amp_const", "amp_const_k2", "amp_const_k_k2"]
    totals = {mode: {"IO": 0.0, "LCDM": 0.0} for mode in modes}

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
            k = rows[:, 1]
            p0 = rows[:, 2]

            theory_io = theory_interp(k, z_eff, *io_pk)
            theory_lcdm = theory_interp(k, z_eff, *lcdm_pk)

            sample_payload = {
                "sample": f"{cap}_{z_label}",
                "z_eff": z_eff,
                "k_min": float(k.min()),
                "k_max": float(k.max()),
                "n_bins": int(len(k)),
                "fits": {},
            }

            for mode in modes:
                chi2_io, coeff_io = fit_linear_nuisance(p0, cov, theory_io, k, mode)
                chi2_lcdm, coeff_lcdm = fit_linear_nuisance(p0, cov, theory_lcdm, k, mode)
                totals[mode]["IO"] += chi2_io
                totals[mode]["LCDM"] += chi2_lcdm
                sample_payload["fits"][mode] = {
                    "chi2_IO": chi2_io,
                    "chi2_LCDM": chi2_lcdm,
                    "coeff_IO": coeff_io.tolist(),
                    "coeff_LCDM": coeff_lcdm.tolist(),
                }
            samples.append(sample_payload)

    n_data = sum(s["n_bins"] for s in samples)
    dof = {
        "amp_const": n_data - 2 * len(samples),
        "amp_const_k2": n_data - 3 * len(samples),
        "amp_const_k_k2": n_data - 4 * len(samples),
    }

    payload = {
        "data_source": {
            "archive": str(ARCHIVE),
            "public_url": "https://fbeutler.github.io/static/Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz",
            "description": "Beutler et al. public BOSS DR12 full-shape monopole data and covariance",
        },
        "io_params": io,
        "lcdm_params": lcdm,
        "primordial_borrowed": {"A_s": As, "n_s": ns, "tau_reio": tau},
        "n_data_points": n_data,
        "degrees_of_freedom": dof,
        "totals": totals,
        "samples": samples,
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
