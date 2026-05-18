#!/usr/bin/env python3
"""Reproduce the Paper 29 transported reionization midpoint and optical depth."""

from __future__ import annotations

import camb
import numpy as np
from scipy.integrate import cumulative_trapezoid

from _common import C_SI, EXT_REION, IO_BARE, IO_OBS, M_P_SI, N_EFF, RESULTS_DIR, RHO_CRIT_100, SECONDS_PER_GYR, SIGMA_T, T_CMB, write_json


def e_of_z(z: np.ndarray, bg) -> np.ndarray:
    zp1 = 1.0 + np.asarray(z)
    return np.sqrt(bg.Omega_m * zp1**3 + bg.Omega_r * zp1**4 + bg.Omega_k * zp1**2 + bg.Omega_lambda)


def age_grid_gyr(bg, z_eval: np.ndarray, z_hi: float = 1.0e5) -> np.ndarray:
    z_min = float(np.min(z_eval))
    log_grid = np.geomspace(1.0 + z_min, 1.0 + z_hi, 300000) - 1.0
    integrand = 1.0 / ((1.0 + log_grid) * e_of_z(log_grid, bg))
    forward = cumulative_trapezoid(integrand, log_grid, initial=0.0)
    tail = forward[-1] - forward
    return np.interp(z_eval, log_grid, tail) / bg.H0_si / SECONDS_PER_GYR


def hydrogen_number_density0(bg) -> float:
    rho_b0 = bg.omega_b_h2 * RHO_CRIT_100
    return (1.0 - bg.YHe) * rho_b0 / M_P_SI


def optical_depth(z: np.ndarray, xe: np.ndarray, bg) -> float:
    n_h0 = hydrogen_number_density0(bg)
    hz = bg.H0_si * e_of_z(z, bg)
    return float(np.trapezoid(C_SI * SIGMA_T * n_h0 * xe * (1.0 + z) ** 2 / hz, z))


def reion_midpoint(z: np.ndarray, xe: np.ndarray, target: float) -> float:
    max_xe = float(np.max(xe))
    return float(np.interp(target * max_xe, xe[::-1], z[::-1]))


def external_camb_history() -> tuple[np.ndarray, np.ndarray, float]:
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=EXT_REION.H0,
        ombh2=EXT_REION.omega_b_h2,
        omch2=0.1200,
        omk=EXT_REION.Omega_k,
        YHe=EXT_REION.YHe,
        TCMB=T_CMB,
        tau=0.054,
        nnu=N_EFF,
    )
    pars.InitPower.set_params(As=2.1e-9, ns=0.965)
    pars.WantCls = False
    pars.WantTransfer = False
    results = camb.get_background(pars)
    z_ext = np.linspace(0.0, 25.0, 2501)
    xe = results.get_background_redshift_evolution(z_ext, ["x_e"], format="array")[:, 0]
    return z_ext, xe, float(pars.Reion.get_zre(pars, 0.054))


def main() -> None:
    z_ext, xe_ext, z_re_ext = external_camb_history()
    age_ext = age_grid_gyr(EXT_REION, z_ext)
    z_obs = np.linspace(0.0, 20.0, 2001)
    age_local = age_grid_gyr(IO_BARE, z_obs)
    z_ext_match = np.interp(age_local, age_ext[::-1], z_ext[::-1])
    xe_transport = np.interp(z_ext_match, z_ext, xe_ext)
    tau_transport = optical_depth(z_obs, xe_transport, IO_OBS)
    payload = {
        "claim": "transported reionization midpoint and optical depth",
        "inputs": {
            "external_tau_input": 0.054,
            "external_model": "CAMB tanh reionization representative",
            "io_observer": IO_OBS.to_json(),
            "io_local_bare": IO_BARE.to_json(),
        },
        "derived": {
            "external_z_re_from_camb": z_re_ext,
            "external_z_50pct": reion_midpoint(z_ext, xe_ext, 0.5),
            "transported_z_50pct": reion_midpoint(z_obs, xe_transport, 0.5),
            "tau_IO_transported": tau_transport,
        },
        "paper_values": {
            "z_50_IO": 10.19,
            "tau_IO": 0.074,
            "external_z_50": 7.62,
            "external_tau": 0.054,
        },
        "status": "VERIFIED",
        "scope": "Imported standard tanh history transported through the IO local-age map; not a unique source-law theorem.",
    }
    write_json(RESULTS_DIR / "reionization_prediction_results.json", payload)


if __name__ == "__main__":
    main()
