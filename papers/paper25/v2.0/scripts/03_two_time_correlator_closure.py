#!/usr/bin/env python3
"""Reproduce the Paper 25 v2.0 two-time weak-rate closure arithmetic.

Paper 25's structural claim is that the physical weak freeze-out modification is
a rate, represented by a centered two-time KMS correlator. In the selected
quasi-free CCR package the bridge correlator is bilinear in F_0, so there is no
linear bridge channel for V' = 2 gamma.

This script records the closure arithmetic:

    Gamma_w(gamma) / Gamma_w(0) = (1 + gamma^2) * R(gamma)

with R(gamma) = 1 on the constructed extension, hence

    log[Gamma_w(gamma) / Gamma_w(0)] = log(1 + gamma^2) = K_gauge.

R4/FIRAS boundary:

    The bridge covariance uses the fixed BBN branch temperature T_IO inherited
    from the Paper 21/Paper 22 BBN construction. It does not use the
    observer-side CMB readout normalization R4_FIRAS and does not count the CMB
    temperature as a prediction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "two_time_correlator_closure_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    gamma = data["framework_constants"]["gamma_BI"]
    q = 1.0 + gamma * gamma
    r_gamma = 1.0
    rate_ratio = q * r_gamma
    log_rate_ratio = math.log(rate_ratio)

    result = {
        "paper": "Paper 25 v2.0",
        "structural_claims": {
            "weak_rate_object": "centered two-time KMS correlator",
            "bridge_correlator_bilinear_in_F0": True,
            "linear_bridge_channel_exists": False,
            "V_prime_channel_excluded": True
        },
        "constructed_extension": {
            "R_gamma": r_gamma,
            "R_gamma_status": "DERIVED/CONDITIONAL_VERIFIED on H1 and H2",
            "rate_ratio": rate_ratio,
            "log_rate_ratio": log_rate_ratio,
            "K_gauge": data["framework_constants"]["K_gauge"],
            "matches_K_gauge": abs(log_rate_ratio - data["framework_constants"]["K_gauge"]) < 1.0e-15
        },
        "premise_boundary": {
            "H1": data["premises"]["H1"],
            "H2": data["premises"]["H2"],
            "H3": data["premises"]["H3"]
        },
        "R4_boundary": data["framework_constants"]["R4_boundary"]
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
