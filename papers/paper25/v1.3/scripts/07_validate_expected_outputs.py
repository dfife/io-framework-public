#!/usr/bin/env python3
"""Validate every frozen Paper 25 v1.3 bundle output.

This is the referee-facing one-command validator. It reruns the numbered
scripts, loads the generated JSON files, and checks the live Paper 25 values
against explicit tolerances. The script exits with status 0 only if every check
passes.

Run from the repository root:

    python3 papers/paper25/v1.3/scripts/07_validate_expected_outputs.py

or from the bundle root:

    python3 scripts/07_validate_expected_outputs.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "01_v_vs_vprime_constants.py",
    "02_core_theorem_ledger.py",
    "03_two_time_correlator_closure.py",
    "04_bbn_branch_scorecards.py",
    "05_paper22_correction_boundary.py",
    "06_kappa_audit_summary.py"
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
    constants = load_json("v_vs_vprime_constants_results.json")
    ledger = load_json("core_theorem_ledger_results.json")
    closure = load_json("two_time_correlator_closure_results.json")
    bbn = load_json("bbn_branch_scorecards_results.json")
    correction = load_json("paper22_correction_boundary_results.json")
    audit = load_json("kappa_audit_summary_results.json")

    record(checks, "gamma_BI", close(constants["constants"]["gamma_BI"], 0.2375, 1.0e-15))
    record(checks, "Q", close(constants["constants"]["Q"], 1.05640625, 1.0e-15))
    record(checks, "K_gauge", close(constants["constants"]["K_gauge"], 0.05487281774291466, 1.0e-15))
    record(checks, "V_prime", close(constants["constants"]["V_prime"], 0.475, 1.0e-15))
    record(checks, "V_double_prime", close(constants["constants"]["V_double_prime"], 2.1128125, 1.0e-15))
    record(checks, "epsilon_w_quadratic", close(constants["amplitudes"]["epsilon_w_quadratic_Kgauge_L1"], 0.012300778733811872, 1.0e-15))
    record(checks, "epsilon_w_linear", close(constants["amplitudes"]["epsilon_w_linear_Kgauge_sqrtL1"], 0.025980346217022963, 1.0e-15))
    record(checks, "epsilon_w_vprime", close(constants["amplitudes"]["epsilon_w_vprime_sqrtL1"], 0.22489576735248612, 1.0e-15))
    record(checks, "epsilon_n", close(constants["amplitudes"]["epsilon_n_Kmean_over_10_L2"], 0.02384221534546833, 1.0e-15))
    record(checks, "theorem_count", len(ledger["theorems"]) == 12)
    record(checks, "killed_route_count", ledger["killed_route_count"] == 29)
    record(checks, "rate_ratio_matches_Q", close(closure["constructed_extension"]["rate_ratio"], 1.05640625, 1.0e-15))
    record(checks, "log_rate_ratio_matches_Kgauge", closure["constructed_extension"]["matches_K_gauge"] is True)
    active = bbn["rows"]["active_exact_log_quadratic_branch"]
    linear = bbn["rows"]["linear_exact_log_branch"]
    vprime = bbn["rows"]["vprime_branch"]
    record(checks, "active_D_over_H_sigma", close(active["D_over_H_sigma"], -0.5687060744245984, 1.0e-15))
    record(checks, "active_Y_p_sigma", close(active["Y_p_sigma"], 0.6797578254354383, 1.0e-15))
    record(checks, "active_Li7_sigma", close(active["Li7_over_H_sigma"], 0.5512343431325627, 1.0e-15))
    record(checks, "active_chi2", close(active["chi2_3obs"], 1.0893566013769407, 1.0e-15))
    record(checks, "linear_chi2", close(linear["chi2_3obs"], 1.991998955082098, 1.0e-15))
    record(checks, "vprime_chi2", close(vprime["chi2_3obs"], 401.7433381288046, 1.0e-12))
    record(checks, "active_all_three_within_one_sigma", bbn["comparisons"]["active_all_three_within_one_sigma"] is True)
    record(checks, "paper22_correction_ratio", close(correction["correction"]["old_divided_by_new"], 2.112089549713569, 1.0e-15))
    record(checks, "kappa_no_hidden_parameter", audit["hidden_continuous_parameter_found"] is False)

    pass_count = sum(1 for _, passed, _ in checks if passed)
    fail_count = len(checks) - pass_count
    print(f"SUMMARY total_checks={len(checks)} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
