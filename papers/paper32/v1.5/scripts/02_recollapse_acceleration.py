#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 02.

Purpose:
    Reproduce the local hidden-support acceleration law and the Lambda-dropout
    mechanism used in Paper 32:

        Rddot = -c^2 r_s / (2 R^2)
        Rddot(r_s) = -c^2 / (2 r_s).

Inputs:
    - data/imported_constants.json

Outputs:
    - results/recollapse_acceleration_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic and symbolic bookkeeping. This is the physical
    hidden-support variable equation, not a current-epoch Friedmann acceleration
    theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "recollapse_acceleration_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    c = payload["physical_constants"]["c_m_s"]
    r_s = payload["framework_constants"]["r_s_harmonized_m"]

    def rddot(R: float) -> float:
        return -(c**2) * r_s / (2.0 * R**2)

    sample_radii = {
        "R_equals_r_s": r_s,
        "R_equals_half_r_s": 0.5 * r_s,
        "R_equals_quarter_r_s": 0.25 * r_s,
    }

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction",
        "equation": "Rddot = -c^2 r_s / (2 R^2)",
        "velocity_integral": "Rdot^2 = c^2 (r_s/R - 1 + C_Lambda)",
        "lambda_dropout_mechanism": "If rho_Lambda scales as R^-2, its contribution to Rdot^2 is an R-independent constant C_Lambda; differentiating the velocity integral removes that constant from Rddot.",
        "inputs": {
            "c_m_s": c,
            "r_s_m": r_s,
        },
        "clamp": {
            "R_m": r_s,
            "Rddot_m_s2": rddot(r_s),
            "formula": "-c^2/(2 r_s)",
            "inward": rddot(r_s) < 0.0,
        },
        "samples": [
            {"label": label, "R_m": R, "R_over_r_s": R / r_s, "Rddot_m_s2": rddot(R)}
            for label, R in sample_radii.items()
        ],
        "scope_boundary": "physical hidden-support local equation; not observer-side Friedmann acceleration",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

