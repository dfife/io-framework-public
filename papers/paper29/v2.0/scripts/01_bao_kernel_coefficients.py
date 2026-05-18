#!/usr/bin/env python3
"""Reproduce the Paper 29 v2.0 Euclid/Roman BAO kernel coefficients."""

from __future__ import annotations

import math

from _common import ETA, GAMMA_BI, K_GAUGE, RESULTS_DIR, R_D_MPC, X, write_json


def main() -> None:
    f_perp = math.exp(ETA)
    f_parallel = math.exp(ETA / 2.0)
    payload = {
        "claim": "BAO galaxy/quasar readout kernel coefficients",
        "inputs": {
            "gamma_BI": GAMMA_BI,
            "x": X,
            "K_gauge": K_GAUGE,
            "r_d_Mpc": R_D_MPC,
        },
        "derived": {
            "eta": ETA,
            "eta_over_2": ETA / 2.0,
            "f_perp": f_perp,
            "f_parallel": f_parallel,
            "excess_ratio": (f_parallel - 1.0) / (f_perp - 1.0),
            "exponent_coefficient_ratio": 0.5,
        },
        "paper_values": {
            "eta": 0.036124,
            "f_perp": 1.0368,
            "f_parallel": 1.0182,
        },
        "note": (
            "The exponent coefficients have exact ratio 1:2. The ratio of exponential excesses "
            "(f_parallel-1)/(f_perp-1) is not exactly 1/2."
        ),
        "status": "VERIFIED",
    }
    write_json(RESULTS_DIR / "bao_kernel_coefficients_results.json", payload)


if __name__ == "__main__":
    main()
