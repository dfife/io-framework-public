#!/usr/bin/env python3
"""Paper 3 v2.0 script 05: validate expected outputs.

Purpose:
    Referee entry point. Validate frozen JSON outputs against explicit expected
    constants, theorem flags, and arithmetic values.

Inputs:
    results/*.json

Outputs:
    PASS/FAIL lines plus final summary. Exit code 0 only if all checks pass.

Claim boundary:
    Bundle validation only. Passing this script verifies reproducibility of the
    shipped arithmetic and theorem-surface flags; it does not independently
    validate upstream Paper 10 / Paper 29 branch derivations.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


CHECKS: list[dict[str, Any]] = [
    {"id": "r_s", "file": "active_branch_constants_results.json", "path": ("headline", "r_s_m"), "expected": 6.6835442422068e26, "tolerance": 1e15},
    {"id": "R_U", "file": "active_branch_constants_results.json", "path": ("headline", "R_U_m"), "expected": 4.3999922594663554e26, "tolerance": 1e15},
    {"id": "gamma_temp", "file": "active_branch_constants_results.json", "path": ("headline", "gamma_temp"), "expected": 6.430555234663423e30, "tolerance": 1e18},
    {"id": "thermal_invariant", "file": "active_branch_constants_results.json", "path": ("headline", "thermal_invariant_K_m"), "expected": 1.1717964823462745e27, "tolerance": 1e15},
    {"id": "T_at_R_U", "file": "active_branch_constants_results.json", "path": ("headline", "T_at_R_U_K"), "expected": 2.6631785086103616, "tolerance": 1e-12},
    {"id": "a0", "file": "active_branch_constants_results.json", "path": ("headline", "a0_m_s2"), "expected": 1.344728404820229e-10, "tolerance": 1e-22},
    {"id": "z_eq_rehomed", "file": "active_branch_constants_results.json", "path": ("headline", "z_eq_active_branch"), "expected": 3810.083811083811, "tolerance": 1e-9},
    {"id": "eta_s", "file": "transfer_table_results.json", "path": ("constants", "eta_s"), "expected": 1.8930071296185438, "tolerance": 1e-12},
    {"id": "table_row_count", "file": "transfer_table_results.json", "path": ("rows",), "expected_len": 7, "tolerance": 0},
    {"id": "current_row_flag", "file": "transfer_table_results.json", "path": ("rows", "3", "current_spatial_epoch"), "expected": True, "tolerance": 0},
    {"id": "current_row_R", "file": "transfer_table_results.json", "path": ("rows", "3", "R_m"), "expected": 4.3999922594663554e26, "tolerance": 1e15},
    {"id": "current_row_H", "file": "transfer_table_results.json", "path": ("rows", "3", "H_km_s_Mpc"), "expected": 67.58309424841266, "tolerance": 1e-9},
    {"id": "endpoint_H", "file": "transfer_table_results.json", "path": ("rows", "6", "H_km_s_Mpc"), "expected": 59.557043568918125, "tolerance": 1e-9},
    {"id": "radicand_status", "file": "radicand_positivity_monotonicity_results.json", "path": ("status",), "expected": "DERIVED/THEOREM inside admitted active branch", "tolerance": 0},
    {"id": "Q_endpoint", "file": "radicand_positivity_monotonicity_results.json", "path": ("radicand", "Q_endpoint_y_min"), "expected": 0.7766581202434925, "tolerance": 1e-12},
    {"id": "Q_lower_bound", "file": "radicand_positivity_monotonicity_results.json", "path": ("radicand", "Omega_m_over_x_plus_Omega_k"), "expected": 0.1837579312569536, "tolerance": 1e-15},
    {"id": "Q_positive_flag", "file": "radicand_positivity_monotonicity_results.json", "path": ("radicand", "strictly_positive_on_domain"), "expected": True, "tolerance": 0},
    {"id": "dQ_endpoint", "file": "radicand_positivity_monotonicity_results.json", "path": ("monotonicity", "dQ_dy_endpoint_y_min"), "expected": 0.3933090729054952, "tolerance": 1e-12},
    {"id": "dQ_lower_bound", "file": "radicand_positivity_monotonicity_results.json", "path": ("monotonicity", "three_Omega_m_over_x_plus_two_Omega_k"), "expected": 0.5972737937708609, "tolerance": 1e-15},
    {"id": "dQ_positive_flag", "file": "radicand_positivity_monotonicity_results.json", "path": ("monotonicity", "dQ_dy_strictly_positive_on_domain"), "expected": True, "tolerance": 0},
    {"id": "junction_status", "file": "sharp_eos_junction_limit_results.json", "path": ("status",), "expected": "DERIVED/CONDITIONAL_VERIFIED", "tolerance": 0},
    {"id": "junction_verdict", "file": "sharp_eos_junction_limit_results.json", "path": ("verdict",), "expected": "SURVIVES as a sharp-EOS limiting statement of the Paper 5 continuous mixed-fluid interior", "tolerance": 0},
    {"id": "junction_ratio", "file": "sharp_eos_junction_limit_results.json", "path": ("raychaudhuri_limit", "acceleration_magnitude_ratio_radiation_to_dust"), "expected": 2.0, "tolerance": 0},
    {"id": "extrinsic_curvature_guard", "file": "sharp_eos_junction_limit_results.json", "path": ("matching_conditions", "extrinsic_curvature_continuity"), "expected": "continuous extrinsic curvature follows from continuous first derivative adot, not from continuous acceleration addot", "tolerance": 0}
]


def read_path(obj: Any, path: tuple[str, ...]) -> Any:
    cur = obj
    for part in path:
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def passes(actual: Any, check: dict[str, Any]) -> bool:
    if "expected_len" in check:
        return len(actual) == check["expected_len"]
    expected = check["expected"]
    tolerance = check["tolerance"]
    if isinstance(expected, bool):
        return actual is expected
    if isinstance(expected, str):
        return actual == expected
    return math.isclose(float(actual), float(expected), rel_tol=0.0, abs_tol=tolerance)


def main() -> int:
    pass_count = 0
    fail_count = 0
    for check in CHECKS:
        payload = json.loads((RESULTS / check["file"]).read_text())
        actual = read_path(payload, check["path"])
        ok = passes(actual, check)
        if ok:
            pass_count += 1
            state = "PASS"
        else:
            fail_count += 1
            state = "FAIL"
        expected = check["expected"] if "expected" in check else f"len={check['expected_len']}"
        print(f"{state} {check['id']}: actual={actual!r} expected={expected!r} tol={check['tolerance']}")
    total = pass_count + fail_count
    print(f"SUMMARY total_checks={total} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
