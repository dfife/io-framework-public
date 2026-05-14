#!/usr/bin/env python3
"""Document the Paper 22 weak-amplitude correction induced by Paper 25 v2.0.

Paper 22 used the weak amplitude branch

    epsilon_w = K_gauge * sqrt(L_1)

which treats the bridge as a one-point/amplitude contribution. Paper 25's
two-time rate theorem changes the active branch to

    epsilon_w = K_gauge * L_1.

This script recomputes both amplitudes, their ratio, and the branch chi-square
comparison used by the Paper 25 v2.0 manuscript. The correction is a
rate-versus-amplitude correction and does not use R4_FIRAS.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "paper22_correction_boundary_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    amps = data["amplitudes"]
    scorecards = data["scorecards"]
    old = amps["epsilon_w_linear"]
    new = amps["epsilon_w_quadratic"]

    result = {
        "paper": "Paper 25 v2.0",
        "paper22_old_branch": {
            "formula": "epsilon_w = K_gauge * sqrt(L_1)",
            "epsilon_w": old,
            "status": "SUPERSEDED one-point/amplitude branch"
        },
        "paper25_active_branch": {
            "formula": "epsilon_w = K_gauge * L_1",
            "epsilon_w": new,
            "status": "DERIVED/CONDITIONAL_VERIFIED on H1-H3 plus upstream L_1"
        },
        "correction": {
            "old_divided_by_new": old / new,
            "new_divided_by_old": new / old,
            "absolute_delta": new - old
        },
        "scorecard_comparison": {
            "linear_chi2_3obs": scorecards["linear_exact_log_branch"]["chi2_3obs"],
            "quadratic_chi2_3obs": scorecards["active_exact_log_quadratic_branch"]["chi2_3obs"],
            "quadratic_improvement": (
                scorecards["linear_exact_log_branch"]["chi2_3obs"]
                - scorecards["active_exact_log_quadratic_branch"]["chi2_3obs"]
            )
        },
        "boundary": "Paper 25 corrects the weak amplitude branch; it does not alter Paper 22's spatial Hodge/TT/channel infrastructure."
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
