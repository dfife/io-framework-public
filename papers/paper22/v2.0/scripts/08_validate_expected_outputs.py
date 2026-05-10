#!/usr/bin/env python3
"""Validate every frozen Paper 22 v2.0 bundle output.

This is the referee-facing one-command validator. It reruns the numbered
scripts, loads the generated JSON files, and checks the live Paper 22 values
against explicit tolerances. The script exits with status 0 only if every
check passes.

Run from the repository root:

    python3 papers/paper22/v2.0/scripts/08_validate_expected_outputs.py

or from the bundle root:

    python3 scripts/08_validate_expected_outputs.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "01_r4_firas_dependency_audit.py",
    "02_spatial_hodge_complex.py",
    "03_tt_channel_floor.py",
    "04_gauge_placement_and_channel_architecture.py",
    "05_no_go_and_rate_paradigm_ledger.py",
    "06_amplitude_scorecard_and_comparators.py",
    "07_kappa_audit_summary.py",
]


def load_json(name: str) -> Any:
    return json.loads((BUNDLE_ROOT / "results" / name).read_text(encoding="utf-8"))


def close(actual: float, expected: float, tol: float) -> bool:
    return abs(actual - expected) <= tol


def record(checks: list[tuple[str, bool, str]], name: str, passed: bool, detail: str = "") -> None:
    checks.append((name, passed, detail))
    status = "PASS" if passed else "FAIL"
    print(f"{status} {name}{(' ' + detail) if detail else ''}")


def main() -> int:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(BUNDLE_ROOT / "scripts" / script)], check=True)

    checks: list[tuple[str, bool, str]] = []
    r4 = load_json("r4_firas_dependency_audit_results.json")
    hodge = load_json("spatial_hodge_complex_results.json")
    tt = load_json("tt_channel_floor_results.json")
    gauge = load_json("gauge_placement_and_channel_architecture_results.json")
    nogo = load_json("no_go_and_rate_paradigm_ledger_results.json")
    amp = load_json("amplitude_scorecard_and_comparators_results.json")
    audit = load_json("kappa_audit_summary_results.json")

    record(checks, "R4_FIRAS", close(r4["active_readout"]["R4_FIRAS_frozen"], 1.0031014644, 1.0e-12))
    record(checks, "active_T_obs_matches_FIRAS", r4["checks"]["active_T_obs_matches_firas_with_rounding"])
    record(checks, "paper22_scorecard_not_R4_dependent", r4["checks"]["paper22_scorecard_not_R4_dependent"])
    record(checks, "R_U_m", close(hodge["framework_constant_recompute"]["R_U_m"], 4.40092802727914e26, 1.0e12))
    record(checks, "x", close(hodge["framework_constant_recompute"]["x"], 1.51899780195519, 1.0e-12))
    record(checks, "coexact_vector_n1_multiplicity", hodge["checks"]["coexact_vector_n1_multiplicity"] == 6)
    record(checks, "mult_TT_n2", tt["lowest_TT_block"]["multiplicity"] == 10)
    record(checks, "tt_rough_n2", tt["lowest_TT_block"]["rough_laplacian_eigenvalue_unit_radius"] == 6)
    record(checks, "vector_floor", gauge["channel_architecture"]["vector"]["diagonal_floor"] == 1)
    record(checks, "tensor_floor", gauge["channel_architecture"]["tensor_TT"]["diagonal_floor"] == 2)
    record(checks, "DeltaNeff_equivalent", close(nogo["full_radiation_scaling"]["DeltaNeff_equivalent"], 2.74641841463744, 1.0e-12))
    record(checks, "theta_bound", nogo["checks"]["one_window_theta_bound_less_than_1e_minus_6"])
    record(checks, "epsilon_w", close(amp["amplitudes"]["epsilon_w"], 0.012300778733811872, 1.0e-15))
    record(checks, "epsilon_n", close(amp["amplitudes"]["epsilon_n"], 0.02384221534546833, 1.0e-15))
    record(checks, "Y_p_sigma", close(amp["corrected_scorecard"]["Y_p_sigma"], 0.7045360432106975, 1.0e-15))
    record(checks, "D_over_H_sigma", close(amp["corrected_scorecard"]["D_over_H_sigma"], -0.5529801681809717, 1.0e-15))
    record(checks, "Li7_over_H_sigma", close(amp["corrected_scorecard"]["Li7_over_H_sigma"], 12.204309073285641, 1.0e-15))
    record(checks, "chi2_DH_plus_Yp", close(amp["corrected_scorecard"]["chi2_DH_plus_Yp"], 0.8021581025844415, 1.0e-15))
    record(checks, "comparator_chi2", close(amp["two_parameter_comparator"]["chi2_DH_plus_Yp"], 1.9345853017600352, 1.0e-15))
    record(checks, "li7_fraction", close(amp["li7_uniform_benchmark"]["absolute_fractional_difference"], 0.005093424637516164, 1.0e-15))
    record(checks, "kappa_no_hidden_parameter", audit["checks"]["hidden_continuous_parameter_found"] is False)
    record(checks, "GMP_visible", audit["checks"]["GMP_visible"] is True)
    record(checks, "TBS_visible", audit["checks"]["TBS_visible"] is True)

    pass_count = sum(1 for _, passed, _ in checks if passed)
    fail_count = len(checks) - pass_count
    print(f"SUMMARY total_checks={len(checks)} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
