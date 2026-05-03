#!/usr/bin/env python3
"""
Paper 34 v1.1 reproducibility script 01.

Purpose:
    Compute the full admissible (alpha,n) grid for the Paper 34 H_ext formula:

        H_ext(alpha,n) = H0_active * f_Gamma^(1-alpha)
                         * x^((n/2)*K_gauge)

Inputs:
    - data/imported_constants.json

Outputs:
    - results/hext_grid_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction of the scoped Paper 34 H_ext grid.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "hext_grid_results.json"


def load_constants() -> dict:
    return json.loads(DATA_PATH.read_text())


def h_eff(h0_active: float, f_gamma: float, alpha: float) -> float:
    return h0_active * (f_gamma ** (1.0 - alpha))


def h_ext(h0_active: float, f_gamma: float, x_value: float, k_gauge: float, alpha: float, n_legs: int) -> float:
    return h_eff(h0_active, f_gamma, alpha) * (x_value ** ((n_legs / 2.0) * k_gauge))


def main() -> int:
    payload = load_constants()
    constants = payload["framework_constants"]

    h0_active = constants["H0_active"]
    gamma_bi = constants["gamma_BI"]
    q_value = constants["Q"]
    k_gauge = constants["K_gauge"]
    f_gamma = constants["f_Gamma"]
    x_value = constants["x"]

    consistency = {
        "Q_matches_1_plus_gamma_squared": math.isclose(q_value, 1.0 + gamma_bi**2, rel_tol=0.0, abs_tol=1e-15),
        "K_gauge_matches_log_Q": math.isclose(k_gauge, math.log(q_value), rel_tol=0.0, abs_tol=1e-15),
        "f_Gamma_matches_exp_minus_K": math.isclose(f_gamma, math.exp(-k_gauge), rel_tol=0.0, abs_tol=1e-15),
    }

    rows = []
    for alpha in constants["alpha_grid"]:
        for n_legs in constants["n_grid"]:
            rows.append(
                {
                    "alpha": alpha,
                    "n": n_legs,
                    "H_eff": h_eff(h0_active, f_gamma, alpha),
                    "H_ext": h_ext(h0_active, f_gamma, x_value, k_gauge, alpha, n_legs),
                }
            )

    results = {
        "paper": payload["paper"],
        "classification": "verified / public-reproducibility-support",
        "formula": payload["formula"],
        "constants": constants,
        "consistency_checks": consistency,
        "grid": rows,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH), "rows": len(rows)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
