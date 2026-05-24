#!/usr/bin/env python3
"""Paper 1 v4.1 script 06: validate expected outputs.

Purpose:
    Referee entry point. Validate every frozen JSON result against explicit
    expected values and audit flags.

Inputs:
    results/*.json

Outputs:
    PASS/FAIL lines plus final summary. Exit code 0 only if all checks pass.

Claim boundary:
    Bundle validation only. Passing this script verifies reproducibility of the
    shipped arithmetic and audit flags; it does not validate later-paper
    inherited theorem claims.
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
    {"id": "r_s", "file": "foundation_constants_results.json", "path": ("headline", "r_s_m"), "expected": 6.6835442422068e26, "tolerance": 1e15},
    {"id": "x", "file": "foundation_constants_results.json", "path": ("headline", "x"), "expected": 1.5189873277742727, "tolerance": 1e-15},
    {"id": "gamma_geometric", "file": "foundation_constants_results.json", "path": ("headline", "gamma_geometric"), "expected": 6.430555234663423e30, "tolerance": 1e18},
    {"id": "Q", "file": "foundation_constants_results.json", "path": ("headline", "Q"), "expected": 1.05640625, "tolerance": 1e-15},
    {"id": "K_gauge", "file": "foundation_constants_results.json", "path": ("headline", "K_gauge"), "expected": 0.05487281774291466, "tolerance": 1e-15},
    {"id": "Delta", "file": "foundation_constants_results.json", "path": ("headline", "Delta"), "expected": 5.624029175326855, "tolerance": 1e-12},
    {"id": "K_mean", "file": "foundation_constants_results.json", "path": ("headline", "K_mean"), "expected": 1.7270483421419307, "tolerance": 1e-15},
    {"id": "x_crit", "file": "foundation_constants_results.json", "path": ("headline", "x_crit"), "expected": 0.9863754613328337, "tolerance": 1e-15},
    {"id": "T_Hawking", "file": "temperature_chain_results.json", "path": ("headline", "T_Hawking_K"), "expected": 2.726445932982825e-31, "tolerance": 1e-43},
    {"id": "T_IO", "file": "temperature_chain_results.json", "path": ("headline", "T_IO_K"), "expected": 2.6631738235142604, "tolerance": 1e-12},
    {"id": "T_planck_identity", "file": "temperature_chain_results.json", "path": ("headline", "T_planck_identity_K"), "expected": 2.6631736518020115, "tolerance": 1e-8},
    {"id": "T_local", "file": "temperature_chain_results.json", "path": ("headline", "T_local_K"), "expected": 4.141436822062615e-31, "tolerance": 1e-43},
    {"id": "FIRAS_readout_ratio", "file": "temperature_chain_results.json", "path": ("headline", "FIRAS_readout_ratio"), "expected": 1.0234029697706684, "tolerance": 1e-12},
    {"id": "CMB_independent_prediction_false", "file": "temperature_chain_results.json", "path": ("claim_boundary", "independent_CMB_temperature_prediction"), "expected": False, "tolerance": 0},
    {"id": "spectral_Gamma", "file": "spectral_theorem_flags_results.json", "path": ("Gamma_omega",), "expected": 1.0, "tolerance": 0.0},
    {"id": "spectral_no_greybody", "file": "spectral_theorem_flags_results.json", "path": ("greybody_attenuation_present",), "expected": False, "tolerance": 0},
    {"id": "rho_torsion_formula", "file": "dark_energy_chain_results.json", "path": ("headline", "rho_Lambda_torsion_kg_m3"), "expected": 2.5213519352125205e-27, "tolerance": 1e-39},
    {"id": "rho_eff_formula", "file": "dark_energy_chain_results.json", "path": ("headline", "rho_Lambda_eff_kg_m3"), "expected": 5.817572055422853e-27, "tolerance": 1e-39},
    {"id": "rho_eff_formula_vs_observed_percent", "file": "dark_energy_chain_results.json", "path": ("headline", "formula_vs_observed_percent"), "expected": -2.389730613710524, "tolerance": 1e-12},
    {"id": "dark_energy_mismatch_flag", "file": "dark_energy_chain_results.json", "path": ("audit_finding", "formula_reproduces_manuscript_dark_energy_values"), "expected": False, "tolerance": 0},
    {"id": "rho_eff_formula_minus_manuscript_percent", "file": "dark_energy_chain_results.json", "path": ("audit_finding", "rho_eff_formula_minus_manuscript_percent"), "expected": -3.841784207886722, "tolerance": 1e-12},
    {"id": "paper32_sha_sync_flag", "file": "cross_paper_consistency_results.json", "path": ("audit_flags", "paper32_manuscript_sha_prefix_matches_current_repo_manifest"), "expected": False, "tolerance": 0},
    {"id": "paper34_hubble_anchor", "file": "cross_paper_consistency_results.json", "path": ("inherited_values", "paper34_v1_2_hubble_scorecard", "max_abs_pull_sigma"), "expected": 0.57, "tolerance": 1e-12},
    {"id": "paper35_desi_anchor", "file": "cross_paper_consistency_results.json", "path": ("inherited_values", "paper35_v2_0_four_problems_anchor", "desi_delta_chi2_layer2"), "expected": -3.58, "tolerance": 1e-12},
    {"id": "theorem_1Y_E_total", "file": "total_energy_density_accounting_results.json", "path": ("headline", "E_total_J"), "expected": 4.0443983043156795e70, "tolerance": 1e58},
    {"id": "theorem_1Y_V_S3_R_U", "file": "total_energy_density_accounting_results.json", "path": ("headline", "V_S3_R_U_m3"), "expected": 1.6814647626047918e81, "tolerance": 1e69},
    {"id": "theorem_1Y_rho_avg_R_U", "file": "total_energy_density_accounting_results.json", "path": ("headline", "rho_avg_at_R_U_kg_m3"), "expected": 2.6762380634304562e-28, "tolerance": 1e-40},
    {"id": "theorem_1Y_not_component_budget", "file": "total_energy_density_accounting_results.json", "path": ("accounting_separation", "rho_avg_is_component_budget"), "expected": False, "tolerance": 0},
    {"id": "theorem_1Y_not_local_qm_input", "file": "total_energy_density_accounting_results.json", "path": ("accounting_separation", "rho_avg_is_local_quantum_input"), "expected": False, "tolerance": 0},
    {"id": "theorem_1Y_component_slot_sum_not_licensed", "file": "total_energy_density_accounting_results.json", "path": ("accounting_separation", "component_slot_sum_licensed_without_typed_measure_theorem"), "expected": False, "tolerance": 0},
    {"id": "registry_all_required_phrases", "file": "core_theorem_registry_results.json", "path": ("all_required_registry_phrases_present",), "expected": True, "tolerance": 0},
    {"id": "registry_1X", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.X", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_1Y", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.Y", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_1Z", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.Z", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_1W", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.W", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_1V", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.V", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_1U", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.U", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_1T", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "1.T", "pass"), "expected": True, "tolerance": 0},
    {"id": "registry_closed_s3_reconciliation", "file": "core_theorem_registry_results.json", "path": ("theorem_checks", "closed_s3_cosmo_reconciliation", "pass"), "expected": True, "tolerance": 0},
    {"id": "closed_s3_chain_first", "file": "core_theorem_registry_results.json", "path": ("approved_closed_s3_reduction_chain", "0"), "expected": "Theorem 1.Z", "tolerance": 0},
    {"id": "closed_s3_chain_guard", "file": "core_theorem_registry_results.json", "path": ("approved_closed_s3_reduction_chain", "2"), "expected": "Theorem 1.V", "tolerance": 0}
]


def read_path(obj: Any, path: tuple[str, ...]) -> Any:
    cur = obj
    for part in path:
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def passes(actual: Any, expected: Any, tolerance: float) -> bool:
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
        ok = passes(actual, check["expected"], check["tolerance"])
        if ok:
            pass_count += 1
            state = "PASS"
        else:
            fail_count += 1
            state = "FAIL"
        print(
            f"{state} {check['id']}: actual={actual!r} expected={check['expected']!r} "
            f"tol={check['tolerance']}"
        )
    total = pass_count + fail_count
    print(f"SUMMARY total_checks={total} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
