"""Recompute Paper 18's legacy observable branch with repaired thermal input.

Paper 18 v1.5 carried a conditional `N_eff = Delta` branch and evaluated BAO,
sigma8/S8, apparent dark-energy, and MOND-scale diagnostics. The v1.5 script
used `T0_IO = 2.7253 K`, inherited from the retired `R4 = 1` observer readout.

Paper 18 v1.6 keeps the branch conditionality unchanged, but observer-side
radiation calculations now inherit Paper 17 v1.5:

    T_obs(R4) = T_IO*x^(R4_FIRAS*K_gauge), R4_FIRAS = 1.0031014644.

This evaluates to the FIRAS empirical thermal datum `2.7255 K`. The CMB
temperature is not reported as an IO prediction in v1.6; it is an empirical
input fixing the observer readout normalization. CLASS/DESI computations in
this script therefore use `T0_IO = T_FIRAS`.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

import numpy as np
from classy import Class
from scipy.integrate import quad
from scipy.stats import chi2 as chi2_dist


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT / "results"
BAO_MEAN = Path(
    os.environ.get(
        "PAPER18_DESI_BAO_MEAN",
        BUNDLE_ROOT / "data" / "external" / "desi_2024_gaussian_bao_ALL_GCcomb_mean.txt",
    )
)
BAO_COV = Path(
    os.environ.get(
        "PAPER18_DESI_BAO_COV",
        BUNDLE_ROOT / "data" / "external" / "desi_2024_gaussian_bao_ALL_GCcomb_cov.txt",
    )
)

C_KM_S = 299792.458
C_M_S = 299792458.0
GAMMA = 0.2375
X = 1.51899
X_R4_SOURCE = 1.519
DELTA = X**4 * (1 + GAMMA**2)
K_GAUGE = math.log(1.0 + GAMMA**2)
R4_FIRAS = 1.0031014644
T_IO_BULK = 2.6635
T_FIRAS = 2.7255
H0_IO = 68.91
OMEGA_M_IO = 0.335
OMEGA_K_IO = -0.006
T0_IO = T_IO_BULK * (X_R4_SOURCE ** (R4_FIRAS * K_GAUGE))
N_EFF_IO = DELTA
F_B = 2 * GAMMA / X
OMEGA_B_GEOM_H2 = 0.02108
OMEGA_B_ACOUSTIC_H2 = 0.02910
OMEGA_B_GEOM = OMEGA_B_GEOM_H2 / (H0_IO / 100.0) ** 2
OMEGA_B_ACOUSTIC = OMEGA_B_ACOUSTIC_H2 / (H0_IO / 100.0) ** 2
H0_LCDM = 67.36
OMEGA_M_LCDM = 0.3153
OMEGA_K_LCDM = 0.0
T0_LCDM = 2.7255
N_EFF_LCDM = 3.046
R_D_IO = 143.3
R_D_LCDM = 147.09
R_S_M = 6.685e26


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


def load_bao():
    if not BAO_MEAN.exists() or not BAO_COV.exists():
        raise FileNotFoundError(
            "DESI DR1 Gaussian BAO files are not redistributed in this bundle. "
            "Download them from the DESI public release, place them under "
            "papers/paper18/v1.6/data/external/, or set PAPER18_DESI_BAO_MEAN "
            "and PAPER18_DESI_BAO_COV to local file paths. See "
            "data/external_data_sources.md."
        )
    triples: list[tuple[float, float, str]] = []
    for line in BAO_MEAN.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        z, value, quantity = line.split()
        triples.append((float(z), float(value), quantity))
    covariance = np.loadtxt(BAO_COV)
    inv_cov = np.linalg.inv(covariance)
    return triples, covariance, inv_cov


def bao_prediction(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float, r_d: float) -> np.ndarray:
    triples, _, _ = load_bao()
    values = []
    for z, _, quantity in triples:
        d_m, d_h, d_v = distances(z, h0=h0, omega_m=omega_m, omega_k=omega_k, t0=t0, n_eff=n_eff)
        if quantity == "DM_over_rs":
            values.append(d_m / r_d)
        elif quantity == "DH_over_rs":
            values.append(d_h / r_d)
        elif quantity == "DV_over_rs":
            values.append(d_v / r_d)
        else:
            raise ValueError(quantity)
    return np.array(values)


def bao_chi2(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float, r_d: float) -> tuple[float, float]:
    triples, _, inv_cov = load_bao()
    obs = np.array([value for _, value, _ in triples])
    pred = bao_prediction(h0=h0, omega_m=omega_m, omega_k=omega_k, t0=t0, n_eff=n_eff, r_d=r_d)
    diff = pred - obs
    chi2 = float(diff @ inv_cov @ diff)
    pte = float(chi2_dist.sf(chi2, len(obs)))
    return chi2, pte


def run_class_model(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float, omega_b: float, a_s: float = 2.1e-9, n_s: float = 0.9649, tau_reio: float = 0.0544, m_nu: float = 0.06) -> dict[str, float]:
    h = h0 / 100.0
    omega_m_h2 = omega_m * h * h
    omega_nu = m_nu / 93.14
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
            "A_s": a_s,
            "n_s": n_s,
            "tau_reio": tau_reio,
            "T_cmb": t0,
            "N_ur": n_eff - 1.0132,
            "N_ncdm": 1,
            "m_ncdm": m_nu,
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
        "rs_drag_CLASS": rs_drag,
    }


def main() -> None:
    bao_io_chi2, bao_io_pte = bao_chi2(
        h0=H0_IO,
        omega_m=OMEGA_M_IO,
        omega_k=OMEGA_K_IO,
        t0=T0_IO,
        n_eff=N_EFF_IO,
        r_d=R_D_IO,
    )
    bao_lcdm_chi2, bao_lcdm_pte = bao_chi2(
        h0=H0_LCDM,
        omega_m=OMEGA_M_LCDM,
        omega_k=OMEGA_K_LCDM,
        t0=T0_LCDM,
        n_eff=N_EFF_LCDM,
        r_d=R_D_LCDM,
    )

    io_sigma8 = run_class_model(
        h0=H0_IO,
        omega_m=OMEGA_M_IO,
        omega_k=OMEGA_K_IO,
        t0=T0_IO,
        n_eff=N_EFF_IO,
        omega_b=OMEGA_B_GEOM_H2,
    )
    io_sigma8_eff = run_class_model(
        h0=H0_IO,
        omega_m=OMEGA_M_IO,
        omega_k=OMEGA_K_IO,
        t0=T0_IO,
        n_eff=N_EFF_IO,
        omega_b=OMEGA_B_ACOUSTIC_H2,
    )
    lcdm_sigma8 = run_class_model(
        h0=67.4,
        omega_m=0.315,
        omega_k=0.0,
        t0=2.7255,
        n_eff=3.046,
        omega_b=0.02237,
    )

    omega_r_io = omega_r(T0_IO, N_EFF_IO, H0_IO / 100.0)
    omega_lambda_io = 1 - OMEGA_M_IO - OMEGA_K_IO - omega_r_io
    w0_apparent = -1 + (2.0 / 3.0) * OMEGA_K_IO / (OMEGA_K_IO + omega_lambda_io)

    a0 = C_M_S**2 / R_S_M

    payload = {
        "inputs": {
            "gamma": GAMMA,
            "x": X,
            "x_R4_source": X_R4_SOURCE,
            "Delta": DELTA,
            "K_gauge": K_GAUGE,
            "R4_FIRAS": R4_FIRAS,
            "T_IO_bulk": T_IO_BULK,
            "T_FIRAS": T_FIRAS,
            "H0_IO": H0_IO,
            "Omega_m_IO": OMEGA_M_IO,
            "Omega_k_IO": OMEGA_K_IO,
            "T0_IO": T0_IO,
            "T0_IO_minus_FIRAS": T0_IO - T_FIRAS,
            "thermal_status": "FIRAS-fixed observer readout; not an independent CMB-temperature prediction.",
            "N_eff_IO": N_EFF_IO,
            "f_b": F_B,
            "Omega_b_geom": OMEGA_B_GEOM,
            "Omega_b_acoustic": OMEGA_B_ACOUSTIC,
            "omega_b_geom": OMEGA_B_GEOM_H2,
            "omega_b_eff": OMEGA_B_ACOUSTIC_H2,
            "r_d_IO": R_D_IO,
        },
        "bao": {
            "dataset": "DESI DR1 all GCcomb 12-point Gaussian BAO covariance",
            "IO_chi2": bao_io_chi2,
            "IO_pte": bao_io_pte,
            "LCDM_like_chi2": bao_lcdm_chi2,
            "LCDM_like_pte": bao_lcdm_pte,
        },
        "sigma8": {
            "assumption": "Primordial A_s, n_s, tau_reio borrowed from Planck-like LCDM, as in Paper 6.",
            "IO_geometric_baryons": io_sigma8,
            "IO_acoustic_baryons_sensitivity_only": io_sigma8_eff,
            "LCDM_reference": lcdm_sigma8,
        },
        "w": {
            "w_true": -1.0,
            "omega_r_IO": omega_r_io,
            "omega_lambda_IO": omega_lambda_io,
            "w0_apparent_flat_CPL_misread": w0_apparent,
        },
        "mond": {
            "r_s_m": R_S_M,
            "a0_IO_m_per_s2": a0,
            "canonical_observed_a0_m_per_s2": 1.2e-10,
            "percent_high_vs_canonical": 100 * (a0 / 1.2e-10 - 1),
        },
    }
    (ROOT / "paper18_legacy_observables_recalculation_checks.json").write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
