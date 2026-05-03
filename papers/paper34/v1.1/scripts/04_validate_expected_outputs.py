#!/usr/bin/env python3
"""
Paper 34 v1.1 reproducibility script 04.

Purpose:
    Fast validation of the frozen JSON outputs shipped in the Paper 34 v1.1
    support bundle.

Inputs:
    - results/hext_grid_results.json
    - results/published_measurements_comparison_results.json
    - results/anti_fit_check_results.json

Outputs:
    Prints a JSON pass/fail summary to stdout.

External dependencies:
    Python standard library only.

Claim boundary:
    verified / validation of frozen public bundle outputs.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"

CHECKS = [
    ("hext_grid_results.json", ("grid", 0, "H_ext"), 67.57585653582628, 1e-12),
    ("hext_grid_results.json", ("grid", 4, "H_ext"), 70.25677881443751, 1e-12),
    ("hext_grid_results.json", ("grid", 6, "H_ext"), 71.38755719355022, 1e-12),
    ("hext_grid_results.json", ("grid", 8, "H_ext"), 73.04406074030152, 1e-12),
    ("published_measurements_comparison_results.json", ("scorecard", 0, "pull_sigma"), 0.35171307165254007, 1e-12),
    ("published_measurements_comparison_results.json", ("scorecard", 1, "pull_sigma"), -0.5668642595545683, 1e-12),
    ("published_measurements_comparison_results.json", ("scorecard", 4, "pull_sigma"), 0.04406074030151785, 1e-12),
    ("published_measurements_comparison_results.json", ("summary", "max_abs_pull"), 0.5668642595545683, 1e-12),
    ("anti_fit_check_results.json", ("summary", "assigned_equal_nearest_grid_points"), 5, 0),
    ("anti_fit_check_results.json", ("summary", "gw_sirens_nearest_grid_point", 0), 1.5, 0),
    ("anti_fit_check_results.json", ("summary", "gw_sirens_nearest_grid_point", 1), 1, 0),
]


def descend(payload, path):
    cur = payload
    for key in path:
        cur = cur[key]
    return cur


def check_value(actual, expected, tolerance):
    if isinstance(expected, int):
        return actual == expected
    return math.isclose(float(actual), float(expected), rel_tol=0.0, abs_tol=tolerance)


def main() -> int:
    failures = []
    for filename, path, expected, tolerance in CHECKS:
        payload = json.loads((RESULTS / filename).read_text())
        actual = descend(payload, path)
        if not check_value(actual, expected, tolerance):
            failures.append(
                {
                    "file": filename,
                    "path": path,
                    "actual": actual,
                    "expected": expected,
                    "tolerance": tolerance,
                }
            )
    if failures:
        print(json.dumps({"state": "failed", "failures": failures}, indent=2, sort_keys=True))
        return 1
    print(json.dumps({"state": "passed", "checks": len(CHECKS)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
