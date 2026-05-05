#!/usr/bin/env python3
"""Recompute Paper 26's conditional scalar-amplitude chain.

The active Paper 26 formula is

    A_s = (25/9)
          * [gamma^2 / (1 + gamma^2)]
          * [1/sqrt(2)]
          * [exp(4*pi*sqrt(2)) - 1]^-1.

This script recomputes each factor from the bundle constants. The result is
conditional on C1 (fluctuation covariance inherits the gauge partition) and
C2c (Hawking thermal state selection on the proved S2 coexact carrier).
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "scalar_amplitude_chain_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    gamma = data["framework_constants"]["gamma_BI"]
    q = 1.0 + gamma * gamma
    beta_omega = 4.0 * math.pi * math.sqrt(2.0)
    g_h = 1.0 / (math.exp(beta_omega) - 1.0)
    omega_hat = math.sqrt(2.0)
    canonical_source = g_h / omega_hat
    extrinsic_fraction = gamma * gamma / q
    dust_factor = 25.0 / 9.0
    a_s = dust_factor * extrinsic_fraction * canonical_source
    planck = data["scalar_amplitude"]["Planck_A_s_reference"]
    planck_sigma = data["scalar_amplitude"]["Planck_A_s_sigma"]

    result = {
        "paper": "Paper 26 v1.2",
        "formula": data["scalar_amplitude"]["formula"],
        "factors": {
            "gamma_BI": gamma,
            "Q": q,
            "dust_conversion_factor": dust_factor,
            "extrinsic_fraction": extrinsic_fraction,
            "beta_omega_S2_l1": beta_omega,
            "g_H_S2_l1": g_h,
            "omega_hat_S2_l1": omega_hat,
            "canonical_source_covariance": canonical_source
        },
        "A_s": a_s,
        "Planck_A_s_reference": planck,
        "fractional_delta_vs_Planck": (a_s - planck) / planck,
        "sigma_delta_vs_Planck": (a_s - planck) / planck_sigma,
        "status": "DERIVED/CONDITIONAL on C1 + C2c"
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
