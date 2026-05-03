#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 03.

Purpose:
    Reproduce the observer-domain boundary identity:

        x_crit = Q^(-1/4) = 0.9863754613328337.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/x_crit_identity_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction on the active reduced scalar
    optical-history observer class.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "x_crit_identity_results.json"


def c_visibility(x_value: float, q_value: float, x0: float) -> float:
    return math.log(q_value * x_value**4) / math.log(q_value * x0**4)


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    gamma = payload["framework_constants"]["gamma_BI"]
    x0 = payload["framework_constants"]["x"]
    q = 1.0 + gamma**2
    x_crit = q ** (-0.25)

    samples = []
    for label, value in [
        ("current_x0", x0),
        ("x_equals_one", 1.0),
        ("x_crit", x_crit),
        ("x_0p95", 0.95),
    ]:
        c_vis = c_visibility(value, q, x0)
        status = "admissible" if c_vis > 0 else "boundary_zero_visibility" if math.isclose(c_vis, 0.0, abs_tol=1e-14) else "inadmissible"
        samples.append({"label": label, "x": value, "Delta": q * value**4, "c_visibility": c_vis, "status": status})

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction",
        "formula": "x_crit = Q^(-1/4), Q = 1 + gamma_BI^2",
        "inputs": {"gamma_BI": gamma, "Q": q, "x0": x0},
        "x_crit": x_crit,
        "samples": samples,
        "scope_boundary": "active reduced scalar optical-history observer class only",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

