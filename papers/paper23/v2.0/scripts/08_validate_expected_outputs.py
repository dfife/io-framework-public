#!/usr/bin/env python3
"""Validate every frozen Paper 23 v2.0 bundle output.

This is the referee-facing one-command validator. It reruns the numbered
scripts, loads the generated JSON files, and checks the live Paper 23 values
against explicit tolerances. The script exits with status 0 only if every check
passes.

Run from the repository root:

    python3 papers/paper23/v2.0/scripts/08_validate_expected_outputs.py

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
    "02_scalar_perturbation_equations.py",
    "03_bridge_operator_and_uniqueness.py",
    "04_white_baseline_and_hopf_selection.py",
    "05_no_doubling_and_spectral_index.py",
    "06_tensor_perturbations.py",
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

    r4 = load_json("r4_firas_dependency_audit_results.json")
    scalar = load_json("scalar_perturbation_equations_results.json")
    bridge = load_json("bridge_operator_and_uniqueness_results.json")
    white = load_json("white_baseline_and_hopf_selection_results.json")
    ns = load_json("no_doubling_and_spectral_index_results.json")
    tensor = load_json("tensor_perturbations_results.json")
    audit = load_json("kappa_audit_summary_results.json")

    checks: list[tuple[str, bool, str]] = []
    record(checks, "R4_FIRAS", close(r4["r4_readout"]["R4_FIRAS_frozen"], 1.0031014644, 1.0e-12))
    record(checks, "active_T_obs_matches_FIRAS", r4["checks"]["active_T_obs_matches_FIRAS_with_rounding"])
    record(checks, "paper23_spectral_index_not_R4_dependent", r4["checks"]["paper23_spectral_index_not_R4_dependent"])
    record(checks, "lambda_2", scalar["checks"]["lambda_2"] == 8)
    record(checks, "lambda_2_minus_3", scalar["checks"]["lambda_2_minus_3"] == 5)
    record(checks, "multiplicity_2", scalar["checks"]["multiplicity_2"] == 9)
    record(checks, "physical_start_n", scalar["checks"]["physical_start_n"] == 2)
    record(checks, "OS_a_dd_over_a", close(scalar["OS_branch"]["a_double_prime_over_a"], -0.24050109902240538, 1.0e-14))
    record(checks, "scalar_hom_space_dimension", bridge["checks"]["scalar_hom_space_dimension"] == 1)
    record(checks, "epsilon_candidate_not_independent", bridge["checks"]["epsilon_candidate_independent"] is False)
    record(checks, "sample_n5_targets", bridge["checks"]["sample_n5_targets"] == [4, 6])
    record(checks, "weighted_Neff_over_N", close(white["checks"]["weighted_Neff_over_N"], 0.7696, 1.0e-15))
    record(checks, "hopf_ell2_shell_n", white["checks"]["hopf_ell2_shell_n"] == 4)
    record(checks, "K_gauge", close(ns["constants"]["K_gauge"], 0.054872817742914665, 1.0e-15))
    record(checks, "one_minus_ns", close(ns["active_result"]["one_minus_ns"], 0.03612435625139463, 1.0e-15))
    record(checks, "n_s", close(ns["active_result"]["n_s"], 0.9638756437486053, 1.0e-15))
    record(checks, "ns_sigma_residual", close(ns["active_result"]["sigma_residual"], 0.24389434557015036, 1.0e-15))
    record(checks, "doubled_sigma_residual", close(ns["rejected_doubled_route"]["sigma_residual"], 8.844931548283158, 1.0e-15))
    record(checks, "shell_factor_n2", close(ns["checks"]["shell_factor_n2"], 5.0 / 6.0, 1.0e-15))
    record(checks, "shell_factor_n3", close(ns["checks"]["shell_factor_n3"], 1.0, 1.0e-15))
    record(checks, "pivot_shell_k0_05", close(ns["checks"]["pivot_shell_k0_05"], 712.1246248214703, 1.0e-12))
    record(checks, "mult_TT_n2", tensor["checks"]["mult_TT_n2"] == 10)
    record(checks, "rough_laplacian_n2", tensor["checks"]["rough_laplacian_n2"] == 6)
    record(checks, "lichnerowicz_n2", tensor["checks"]["lichnerowicz_n2"] == 12)
    record(checks, "tensor_jacobian_n30", close(tensor["checks"]["tensor_jacobian_n30"], 31.0 / 32.0, 1.0e-15))
    record(checks, "audit_no_hidden_parameter", audit["checks"]["hidden_continuous_parameter_found"] is False)
    record(checks, "audit_r4_not_active", audit["checks"]["r4_active_dependency"] is False)
    record(checks, "PSRP_visible", audit["checks"]["PSRP_visible_as_open"] is True)
    record(checks, "boundary_covariance_visible", audit["checks"]["boundary_covariance_visible_as_open"] is True)
    record(checks, "CCR_lift_visible", audit["checks"]["CCR_lift_visible_as_open"] is True)

    pass_count = sum(1 for _, passed, _ in checks if passed)
    fail_count = len(checks) - pass_count
    print(f"SUMMARY total_checks={len(checks)} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

