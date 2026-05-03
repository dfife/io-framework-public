#!/usr/bin/env python3
"""
Paper 34 v1.1 reproducibility script 02.

Purpose:
    Compute Paper 34's six-method H0 scorecard and signed sigma pulls.

Inputs:
    - data/imported_constants.json
    - results/hext_grid_results.json

Outputs:
    - results/published_measurements_comparison_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / comparison arithmetic. The method-to-(alpha,n) assignments are
    scoped claims audited separately by script 03 and by the kappa-audit report.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
GRID_PATH = BUNDLE_ROOT / "results" / "hext_grid_results.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "published_measurements_comparison_results.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def pull(prediction: float, observed: float, sigma: float) -> float:
    return (prediction - observed) / sigma


def grid_lookup(grid_payload: dict) -> dict[tuple[float, int], dict]:
    return {(row["alpha"], row["n"]): row for row in grid_payload["grid"]}


def main() -> int:
    constants = load_json(DATA_PATH)
    grid_payload = load_json(GRID_PATH)
    lookup = grid_lookup(grid_payload)

    scorecard = []
    chi2 = 0.0
    for item in constants["published_h0_measurements"]:
        alpha = float(item["assigned_alpha"])
        n_legs = int(item["assigned_n"])
        prediction = lookup[(alpha, n_legs)]["H_ext"]
        row_pull = pull(prediction, item["observed_H0"], item["sigma"])
        chi2 += row_pull**2
        scorecard.append(
            {
                "method": item["method"],
                "observed_H0": item["observed_H0"],
                "sigma": item["sigma"],
                "assigned_alpha": alpha,
                "assigned_n": n_legs,
                "predicted_H0": prediction,
                "pull_sigma": row_pull,
                "assignment_basis": item["assignment_basis"],
                "source": item["source"],
                "doi": item.get("doi"),
                "arxiv": item.get("arxiv"),
                "url": item["url"],
            }
        )

    results = {
        "paper": constants["paper"],
        "classification": "verified / public-reproducibility-support",
        "formula": constants["formula"],
        "scorecard": scorecard,
        "summary": {
            "method_count": len(scorecard),
            "chi2_six_methods": chi2,
            "rms_pull": (chi2 / len(scorecard)) ** 0.5,
            "max_abs_pull": max(abs(row["pull_sigma"]) for row in scorecard),
        },
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH), "rows": len(scorecard)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
