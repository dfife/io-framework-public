#!/usr/bin/env python3
"""Validate every frozen JSON output in the Paper 28 v2.0 bundle."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from _common import RESULTS_DIR, assert_close


SCRIPT_DIR = Path(__file__).resolve().parent

SCRIPT_TO_RESULT = {
    "01_line_scale_root_uniqueness.py": "line_scale_root_uniqueness_results.json",
    "02_one_form_trace_log_extension.py": "one_form_trace_log_extension_results.json",
    "03_dtn_hessian_spectral_index.py": "dtn_hessian_spectral_index_results.json",
    "04_dtn_remainder_and_o1_exclusion.py": "dtn_remainder_and_o1_exclusion_results.json",
    "05_jwst_clock_map.py": "jwst_clock_map_results.json",
    "06_kappa_r4_audit_summary.py": "kappa_r4_audit_summary_results.json",
}


def run_script(script_name: str) -> None:
    path = SCRIPT_DIR / script_name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.write_result(SCRIPT_TO_RESULT[script_name], module.compute())


def load_result(filename: str) -> dict:
    return json.loads((RESULTS_DIR / filename).read_text(encoding="utf-8"))


def main() -> int:
    for script in SCRIPT_TO_RESULT:
        run_script(script)

    checks = 0
    passed = 0

    line = load_result("line_scale_root_uniqueness_results.json")
    checks += 1
    assert_close("q_line", line["q_line"], 0.5, 0.0)
    passed += 1

    trace = load_result("one_form_trace_log_extension_results.json")
    checks += 1
    assert_close("trace_log_equal_branch", trace["pivot_ns_values"]["equal_branch_average"], 0.963883481680499, 1e-15)
    passed += 1

    dtn = load_result("dtn_hessian_spectral_index_results.json")
    checks += 1
    assert_close("beta_K_over_x", dtn["beta_K_over_x"], 0.036124303978219, 1e-15)
    passed += 1
    checks += 1
    assert_close("dtn_equal_branch_average", dtn["pivot_values"]["dtn_equal_branch_average"], 0.963908849852, 1e-12)
    passed += 1

    rem = load_result("dtn_remainder_and_o1_exclusion_results.json")
    checks += 1
    assert rem["o1_shell_deformations_excluded_on_flat_collar"] is True
    passed += 1
    checks += 1
    assert_close("A=100 slope bound", rem["slope_error_bounds"]["100"], 1.4254604564015358e-05, 1e-15)
    passed += 1

    jwst = load_result("jwst_clock_map_results.json")
    expected = {10: 0.7023379333, 12: 0.5450883247, 14: 0.4388659557, 17: 0.3331013378, 20: 0.2639107601}
    for row in jwst["rows"]:
        checks += 1
        assert_close(f"JWST z={row['z']}", row["t_form_gyr"], expected[row["z"]], 5e-10)
        passed += 1

    audit = load_result("kappa_r4_audit_summary_results.json")
    checks += 1
    assert_close("R4_FIRAS", audit["R4_FIRAS"], 1.0031014644, 1e-12)
    passed += 1
    checks += 1
    assert audit["active_independent_CMB_temperature_prediction"] is False
    passed += 1

    print(f"PASS Paper 28 v2.0 validation: total checks={checks}, pass count={passed}, fail count=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
