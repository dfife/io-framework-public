#!/usr/bin/env python3
"""
Paper 24 v2.3 reproducibility script 04.

Purpose:
    Fast validation of the frozen JSON outputs shipped in the Paper 24 v2.3
    support bundle. This script is intended for reviewers who want to confirm
    that the bundle contains the expected headline values without installing
    PRyMordial.

Inputs:
    - results/qtrans_carrier_results.json
    - results/final_excited_branch_results.json
    - results/excited_state_import_recomputation_results.json

Outputs:
    Prints a JSON pass/fail summary to stdout.

External dependencies:
    Python standard library only.

Claim boundary:
    verified / validation of frozen public bundle outputs.

Run:
    python3 scripts/04_validate_expected_outputs.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


CHECKS = [
    ("qtrans_carrier_results.json", ("framework_geometry", "target_translation", "Q_trans_required_exact_barn"), 0.04002982724908853, 1e-15),
    ("qtrans_carrier_results.json", ("li_predictions", "from_measured_Q7Li", "Li7_H"), 1.5814456055566964e-10, 1e-22),
    ("final_excited_branch_results.json", ("kernel_excited_state", "amp_weighted_avg_F0"), 0.24320694787438585, 1e-15),
    ("final_excited_branch_results.json", ("network_cases", 3, "Li7_H"), 1.7513106468462057e-10, 1e-22),
    ("excited_state_import_recomputation_results.json", ("source_values", "henderson_2019", "B_E2_down_corrected_e2fm4"), 52.0, 1e-12),
    ("excited_state_import_recomputation_results.json", ("import_cases", 0, "q_trans_ex_b"), 0.017537902422203915, 1e-18),
    ("excited_state_import_recomputation_results.json", ("import_cases", 0, "R_ex_T9eff"), 0.5987463992430407, 1e-15),
    ("excited_state_import_recomputation_results.json", ("import_cases", 0, "Li7_H"), 1.7239845810965594e-10, 1e-22),
]


def descend(payload, path):
    """Follow a tuple path through nested dict/list JSON payloads."""

    cur = payload
    for key in path:
        cur = cur[key]
    return cur


def main() -> int:
    """Validate selected public-bundle values against pinned expectations."""

    failures = []
    for filename, path, expected, tol in CHECKS:
        payload = json.loads((RESULTS / filename).read_text())
        actual = descend(payload, path)
        if not math.isclose(float(actual), expected, rel_tol=0.0, abs_tol=tol):
            failures.append(
                {
                    "file": filename,
                    "path": path,
                    "actual": actual,
                    "expected": expected,
                    "tolerance": tol,
                }
            )
    if failures:
        print(json.dumps({"state": "failed", "failures": failures}, indent=2, sort_keys=True))
        return 1
    print(json.dumps({"state": "passed", "checks": len(CHECKS)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
