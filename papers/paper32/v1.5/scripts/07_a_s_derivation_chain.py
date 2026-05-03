#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 07.

Purpose:
    Reproduce the definitive native scalar-amplitude arithmetic used in
    Corollary 32.A.3:

        A_s = (25/9) * [gamma^2/(1+gamma^2)] * (1/sqrt(2))
              * 1/(exp(4*pi*sqrt(2)) - 1).

Inputs:
    - data/imported_constants.json

Outputs:
    - results/a_s_derivation_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction. The theorem status of the Hawking
    boundary-state and quotient selection is documented in the accompanying
    Paper 32 reports.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "a_s_derivation_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    constants = payload["framework_constants"]
    gamma = constants["gamma_BI"]
    q = 1.0 + gamma**2
    hawking_occupation = 1.0 / (math.exp(4.0 * math.pi * math.sqrt(2.0)) - 1.0)
    gauge_ratio = gamma**2 / q
    bridge_factor = 1.0 / math.sqrt(2.0)
    normalization = 25.0 / 9.0
    a_s = normalization * gauge_ratio * bridge_factor * hawking_occupation

    obs = constants["planck_A_s_obs"]
    sigma = constants["planck_A_s_sigma"]

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction",
        "formula": "A_s = (25/9) * (gamma^2/(1+gamma^2)) * (1/sqrt(2)) * 1/(exp(4*pi*sqrt(2))-1)",
        "factors": {
            "normalization_25_over_9": normalization,
            "gauge_ratio_gamma2_over_Q": gauge_ratio,
            "bridge_factor_1_over_sqrt2": bridge_factor,
            "hawking_occupation": hawking_occupation
        },
        "A_s": a_s,
        "comparison": {
            "Planck_A_s_obs": obs,
            "Planck_A_s_sigma": sigma,
            "fractional_difference_vs_obs": (a_s - obs) / obs,
            "pull_sigma": (a_s - obs) / sigma
        },
        "scope_boundary": "DERIVED/SCOPED on the lowest-shell quotient per Paper 32; not a full-spectrum C_ell validation"
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

