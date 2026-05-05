#!/usr/bin/env python3
"""Reproduce the Paper 25 public BBN branch scorecards.

The public bundle does not redistribute or require PRyMordial. It freezes the
audited PRyMordial rows in `data/imported_constants.json` and recomputes the
sigma-plane chi-square arithmetic from those rows.

Rows:

- active_exact_log_quadratic_branch: Paper 25 v1.2/v1.3 active branch.
- linear_exact_log_branch: retired one-point/amplitude comparator.
- vprime_branch: tangent-readout comparator, catastrophically excluded.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "bbn_branch_scorecards_results.json"


def chi2_3obs(row: dict[str, float]) -> float:
    return (
        row["D_over_H_sigma"] ** 2
        + row["Y_p_sigma"] ** 2
        + row["Li7_over_H_sigma"] ** 2
    )


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    scorecards = data["scorecards"]

    rows = {}
    for key, row in scorecards.items():
        recomputed = chi2_3obs(row)
        rows[key] = {
            **row,
            "chi2_3obs_recomputed_from_sigmas": recomputed,
            "chi2_delta_recomputed_minus_frozen": recomputed - row["chi2_3obs"]
        }

    active = rows["active_exact_log_quadratic_branch"]
    linear = rows["linear_exact_log_branch"]
    vprime = rows["vprime_branch"]

    result = {
        "paper": "Paper 25 v1.3",
        "observational_conventions": data["observational_conventions"],
        "rows": rows,
        "comparisons": {
            "linear_minus_active_chi2": linear["chi2_3obs"] - active["chi2_3obs"],
            "vprime_minus_active_chi2": vprime["chi2_3obs"] - active["chi2_3obs"],
            "active_all_three_within_one_sigma": all(
                abs(active[name]) < 1.0
                for name in ["D_over_H_sigma", "Y_p_sigma", "Li7_over_H_sigma"]
            ),
            "vprime_catastrophic": vprime["chi2_3obs"] > 100.0
        },
        "claim_boundary": "The scorecard is verified computational support, not the theorem proof."
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
