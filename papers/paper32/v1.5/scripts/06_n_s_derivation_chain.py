#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 06.

Purpose:
    Reproduce the scalar-index derivation:

        n_s = 1 - K_gauge / x.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/n_s_derivation_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction of the active source-block scalar-index
    formula.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "n_s_derivation_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    constants = payload["framework_constants"]
    gamma = constants["gamma_BI"]
    x = constants["x"]
    q = 1.0 + gamma**2
    k_gauge = math.log(q)
    n_s = 1.0 - k_gauge / x
    obs = constants["planck_n_s_obs"]
    sigma = constants["planck_n_s_sigma"]

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction",
        "formula": "n_s = 1 - K_gauge/x",
        "inputs": {"gamma_BI": gamma, "x": x, "Q": q, "K_gauge": k_gauge},
        "n_s": n_s,
        "comparison": {
            "Planck_n_s_obs": obs,
            "Planck_n_s_sigma": sigma,
            "pull_sigma": (n_s - obs) / sigma
        },
        "scope_boundary": "active scalar source-block spectral-index derivation"
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

