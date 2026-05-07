"""Reproduce Paper 18's Bogoliubov coefficient packet checks.

This script evaluates the Planck/KMS occupation factors and corresponding
Araki-Woods `alpha`/`beta` coefficients used by Paper 18's Modular
Bogoliubov Spectrum theorem. It keeps two temperatures separate:

* `T_IO = 2.6635 K`, the bulk/interior Hawking scale inherited from Paper 1.
* `T_obs`, the observer-side thermal readout.

Paper 18 v1.5 implicitly used `R4 = 1`, i.e. `T_obs = T_IO*x^K_gauge`.
Paper 18 v1.6 inherits the Paper 17 v1.5 repair: FIRAS fixes the unique
observer-side readout normalization

    R4_FIRAS = 1.0031014644

inside `T_obs(R4) = T_IO*x^(R4*K_gauge)`. The observed CMB temperature is
therefore not counted here as an independent IO prediction; it is the empirical
thermal datum fixing the readout normalization.

Run with the lab environment:

    /opt/cosmology-lab/env/bin/python paper18_bogoliubov_coefficients_checks.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT / "results"

HBAR = 1.054571817e-34
H = 6.62607015e-34
KB = 1.380649e-23

GAMMA_BI = 0.2375
X = 1.51899
X_R4_SOURCE = 1.519
K_GAUGE = math.log(1.0 + GAMMA_BI**2)
T_IO = 2.6635
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255
T_OBS = T_IO * (X_R4_SOURCE ** (R4_FIRAS * K_GAUGE))
Y_SAMPLES = [0.5, 1.0, 2.8214393721220787, 5.0]


def packet_data(temperature: float) -> list[dict[str, float]]:
    rows = []
    for y in Y_SAMPLES:
        omega = y * KB * temperature / HBAR
        nu_hz = y * KB * temperature / H
        n = 1.0 / math.expm1(y)
        alpha = math.sqrt(1.0 + n)
        beta = math.sqrt(n)
        rows.append(
            {
                "y": y,
                "omega_rad_per_s": omega,
                "nu_hz": nu_hz,
                "n_planck": n,
                "alpha_abs": alpha,
                "beta_abs": beta,
                "alpha2_minus_beta2_minus_1": alpha * alpha - beta * beta - 1.0,
                "aw_gamma_minus_exp_minus_y": n / (1.0 + n) - math.exp(-y),
            }
        )
    return rows


def main() -> None:
    io_rows = packet_data(T_IO)
    obs_rows = packet_data(T_OBS)

    beta_diag = np.diag([row["beta_abs"] for row in io_rows])
    alpha_diag = np.diag([row["alpha_abs"] for row in io_rows])
    ccr_residual = alpha_diag @ alpha_diag - beta_diag @ beta_diag - np.eye(len(io_rows))

    peak_io = io_rows[2]
    peak_obs = obs_rows[2]

    payload = {
        "inputs": {
            "gamma_BI": GAMMA_BI,
            "x": X,
            "x_R4_source": X_R4_SOURCE,
            "K_gauge": K_GAUGE,
            "R4_FIRAS": R4_FIRAS,
            "T_IO_K": T_IO,
            "T_FIRAS_K": T_FIRAS,
            "T_obs_K": T_OBS,
            "T_obs_minus_FIRAS_K": T_OBS - T_FIRAS,
            "temperature_status": "FIRAS-fixed observer readout; not an independent CMB-temperature prediction.",
        },
        "theorem_formulas": {
            "continuum_beta_squared_IO": "|beta_{w,w'}|^2 = delta(w-w') / (exp(hbar*w/(k_B*T_IO)) - 1)",
            "continuum_beta_squared_obs": "|beta_{w,w'}|^2 = delta(w-w') / (exp(hbar*w/(k_B*T_obs)) - 1)",
            "continuum_alpha_squared": "|alpha_{w,w'}|^2 = delta(w-w') * exp(hbar*w/(k_B*T)) / (exp(hbar*w/(k_B*T)) - 1)",
        },
        "io_packets": io_rows,
        "obs_packets": obs_rows,
        "wavepacket_matrix_checks": {
            "beta_diag_IO": beta_diag.tolist(),
            "alpha_diag_IO": alpha_diag.tolist(),
            "max_ccr_residual": float(np.max(np.abs(ccr_residual))),
        },
        "peak_examples": {
            "radiance_peak_y": Y_SAMPLES[2],
            "IO_peak_frequency_GHz": peak_io["nu_hz"] / 1.0e9,
            "IO_peak_beta_squared": peak_io["n_planck"],
            "obs_peak_frequency_GHz": peak_obs["nu_hz"] / 1.0e9,
            "obs_peak_beta_squared": peak_obs["n_planck"],
        },
    }

    (ROOT / "paper18_bogoliubov_coefficients_checks.json").write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
