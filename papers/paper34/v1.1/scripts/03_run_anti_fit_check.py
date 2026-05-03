#!/usr/bin/env python3
"""
Paper 34 v1.1 reproducibility script 03.

Purpose:
    Reproduce the compact anti-fit backstop table for the six (method, alpha,n)
    assignments. In particular, verify that GW sirens stay at (1,0) even though
    (3/2,1) is numerically closer on the admissible grid.

Inputs:
    - data/imported_constants.json
    - results/hext_grid_results.json

Outputs:
    - results/anti_fit_check_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / anti-fit diagnostic. This script does not prove the extension
    premises; it verifies the assignments are not changed after seeing the
    measurements.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
GRID_PATH = BUNDLE_ROOT / "results" / "hext_grid_results.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "anti_fit_check_results.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def pull(prediction: float, observed: float, sigma: float) -> float:
    return (prediction - observed) / sigma


def nearest_grid_point(measurement: dict, grid_rows: list[dict]) -> dict:
    candidates = []
    for row in grid_rows:
        row_pull = pull(row["H_ext"], measurement["observed_H0"], measurement["sigma"])
        candidates.append(
            {
                "alpha": row["alpha"],
                "n": row["n"],
                "H_ext": row["H_ext"],
                "pull_sigma": row_pull,
                "abs_pull": abs(row_pull),
            }
        )
    return min(candidates, key=lambda item: item["abs_pull"])


def h_eff(h0_active: float, f_gamma: float, alpha: float) -> float:
    return h0_active * (f_gamma ** (1.0 - alpha))


def h_ext(h0_active: float, f_gamma: float, x_value: float, alpha: float, n_legs: int, payload: float) -> float:
    return h_eff(h0_active, f_gamma, alpha) * (x_value ** ((n_legs / 2.0) * payload))


def payload_rivals(constants: dict) -> dict:
    h0_active = constants["H0_active"]
    f_gamma = constants["f_Gamma"]
    x_value = constants["x"]
    gamma_bi = constants["gamma_BI"]
    q_value = constants["Q"]
    k_gauge = constants["K_gauge"]
    rivals = {
        "K_gauge": k_gauge,
        "gamma_squared": gamma_bi**2,
        "K_gauge_over_2": k_gauge / 2.0,
        "zero_payload": 0.0,
        "Q": q_value,
    }
    return {
        name: {
            "payload": payload,
            "TRGB_direct_alpha_1p5_n1": h_ext(h0_active, f_gamma, x_value, 1.5, 1, payload),
            "SH0ES_TRGBSN_alpha_2_n2": h_ext(h0_active, f_gamma, x_value, 2.0, 2, payload),
        }
        for name, payload in rivals.items()
    }


def main() -> int:
    data = load_json(DATA_PATH)
    grid_payload = load_json(GRID_PATH)
    grid_rows = grid_payload["grid"]
    lookup = {(row["alpha"], row["n"]): row for row in grid_rows}

    rows = []
    assigned_equal_nearest = 0
    for item in data["published_h0_measurements"]:
        alpha = float(item["assigned_alpha"])
        n_legs = int(item["assigned_n"])
        assigned = lookup[(alpha, n_legs)]
        assigned_pull = pull(assigned["H_ext"], item["observed_H0"], item["sigma"])
        best = nearest_grid_point(item, grid_rows)
        is_nearest = alpha == best["alpha"] and n_legs == best["n"]
        assigned_equal_nearest += int(is_nearest)
        rows.append(
            {
                "method": item["method"],
                "assigned": {
                    "alpha": alpha,
                    "n": n_legs,
                    "H_ext": assigned["H_ext"],
                    "pull_sigma": assigned_pull,
                    "assignment_basis": item["assignment_basis"],
                },
                "nearest_admissible_grid_point": best,
                "assigned_is_nearest_grid_point": is_nearest,
            }
        )

    results = {
        "paper": data["paper"],
        "classification": "verified / public-reproducibility-support",
        "claim_boundary": "anti-fit diagnostic, not an independent proof of the extension premises",
        "method_rows": rows,
        "payload_rivals": payload_rivals(data["framework_constants"]),
        "summary": {
            "method_count": len(rows),
            "assigned_equal_nearest_grid_points": assigned_equal_nearest,
            "gw_sirens_assigned_grid_point": [1.0, 0],
            "gw_sirens_nearest_grid_point": [
                next(row for row in rows if row["method"] == "GW sirens")["nearest_admissible_grid_point"]["alpha"],
                next(row for row in rows if row["method"] == "GW sirens")["nearest_admissible_grid_point"]["n"],
            ],
            "highest_audit_risk": "SH0ES: assigned (2,2) is also numerically nearest; accepted only inside the two-leg extension premise package.",
        },
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH), "rows": len(rows)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
