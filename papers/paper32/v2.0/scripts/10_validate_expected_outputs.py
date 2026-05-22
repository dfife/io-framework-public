#!/usr/bin/env python3
"""
Paper 32 v2.0 reproducibility script 10.

Purpose:
    Fast validation of the frozen JSON outputs shipped in the Paper 32 v2.0
    support bundle, including the R4/FIRAS repair.

Inputs:
    - results/framework_constants_results.json
    - results/recollapse_acceleration_results.json
    - results/x_crit_identity_results.json
    - results/recollapse_cycle_timescales_results.json
    - results/kb7_source_block_validation_results.json
    - results/n_s_derivation_results.json
    - results/a_s_derivation_results.json
    - results/universal_gmp_classification_results.json
    - results/r4_firas_impact_audit_results.json

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
    ("framework_constants_results.json", ("derived", "Q"), 1.05640625, 1e-15),
    ("framework_constants_results.json", ("derived", "K_gauge"), 0.05487281774291466, 1e-15),
    ("framework_constants_results.json", ("derived", "Delta"), 5.624216852624105, 1e-12),
    ("framework_constants_results.json", ("derived", "R4_FIRAS"), 1.0031014644105183, 1e-15),
    ("framework_constants_results.json", ("derived", "sigma_R4_FIRAS_only"), 0.009596597151571828, 1e-15),
    ("framework_constants_results.json", ("derived", "T_obs_FIRAS_fixed_K"), 2.7255, 1e-12),
    ("framework_constants_results.json", ("derived", "T_obs_R4_equals_1_K"), 2.725306096638128, 1e-12),
    ("recollapse_acceleration_results.json", ("clamp", "Rddot_m_s2"), -6.722177851434687e-11, 1e-24),
    ("x_crit_identity_results.json", ("x_crit",), 0.9863754613328337, 1e-15),
    ("recollapse_cycle_timescales_results.json", ("results", "clamp_to_crunch_Gyr"), 110.9932628887098, 1e-10),
    ("recollapse_cycle_timescales_results.json", ("results", "cycle_Gyr"), 221.9865257774196, 1e-10),
    ("kb7_source_block_validation_results.json", ("consistency_checks", "Z_e_to_x_equals_Q"), True, 0),
    ("n_s_derivation_results.json", ("n_s",), 0.963875696021781, 1e-15),
    ("a_s_derivation_results.json", ("A_s",), 2.0072459972737347e-09, 1e-22),
    ("universal_gmp_classification_results.json", ("domains", 2, "gmp_status"), "false_as_universal_statement", 0),
    ("r4_firas_impact_audit_results.json", ("numeric_change", "R4_FIRAS"), 1.0031014644105183, 1e-15),
    ("r4_firas_impact_audit_results.json", ("global_verdict", "cmb_prediction_retired"), True, 0),
    ("r4_firas_impact_audit_results.json", ("global_verdict", "paper32_core_results_changed"), False, 0),
]


def descend(payload, path):
    """Return a nested value from dict/list JSON payloads."""
    cur = payload
    for key in path:
        cur = cur[key]
    return cur


def check_value(actual, expected, tolerance):
    """Compare a result value to its frozen expected value."""
    if isinstance(expected, bool):
        return actual is expected
    if isinstance(expected, str):
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
        print(json.dumps({"state": "failed", "checks": len(CHECKS), "failures": failures}, indent=2, sort_keys=True))
        return 1
    print(json.dumps({"state": "passed", "checks": len(CHECKS)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
