#!/usr/bin/env python3
"""Paper 35 v1.1 script 09: validate expected outputs.

Purpose:
    Referee entry point. Validate every frozen JSON in `results/` and compare
    the manuscript-facing values against explicit tolerances.

Inputs:
    results/*.json

Outputs:
    PASS/FAIL lines for every check plus a final summary line. Exit code 0 is
    returned only when all checks pass.

Claim boundary:
    Bundle validation only. Passing this script verifies reproducibility of the
    shipped numerical artifacts; it does not upgrade conditional theorem
    surfaces to unconditional proof.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


CHECKS: list[dict[str, Any]] = [
    {
        "id": "eta_late_mean_baryon_mass",
        "file": "eta_derivation_chain_results.json",
        "path": ("headline", "eta_late_mean_baryon_mass"),
        "expected": 5.748778515173695e-10,
        "tolerance": 1e-22,
        "claim_type": "framework-specific eta arithmetic",
    },
    {
        "id": "eta_late_proton_mass",
        "file": "eta_derivation_chain_results.json",
        "path": ("headline", "eta_late_proton_mass"),
        "expected": 5.74179586430453e-10,
        "tolerance": 1e-22,
        "claim_type": "framework-specific eta arithmetic",
    },
    {
        "id": "f_b_ledger",
        "file": "eta_derivation_chain_results.json",
        "path": ("framework_values", "f_b"),
        "expected": 0.3127083362150814,
        "tolerance": 1e-15,
        "claim_type": "exact framework constant combination",
    },
    {
        "id": "temperature_conversion",
        "file": "temperature_assignment_results.json",
        "path": ("numbers", "temperature_conversion_factor_direct"),
        "expected": 1.071240943860573,
        "tolerance": 1e-15,
        "claim_type": "exact framework temperature conversion",
    },
    {
        "id": "eta_bbn_proton_mass",
        "file": "temperature_assignment_results.json",
        "path": ("numbers", "eta_BBN_proton_mass"),
        "expected": 6.150846821132321e-10,
        "tolerance": 1e-22,
        "claim_type": "framework-specific eta arithmetic",
    },
    {
        "id": "g_chi",
        "file": "chiral_source_diagnostic_results.json",
        "path": ("numbers", "g_chi"),
        "expected": 9.066278337760437e-06,
        "tolerance": 1e-18,
        "claim_type": "exact framework constant power",
    },
    {
        "id": "eta_chiral",
        "file": "chiral_source_diagnostic_results.json",
        "path": ("numbers", "eta_chiral"),
        "expected": 5.786697164001189e-10,
        "tolerance": 1e-22,
        "claim_type": "conditional diagnostic arithmetic",
    },
    {
        "id": "T_f_target",
        "file": "chiral_source_diagnostic_results.json",
        "path": ("numbers", "T_f_GeV"),
        "expected": 22003938597477.8,
        "tolerance": 1e-3,
        "claim_type": "conditional diagnostic scale",
    },
    {
        "id": "Y_B_target",
        "file": "leptogenesis_target_reduction_results.json",
        "path": ("numbers", "Y_B_target"),
        "expected": 8.165878572689907e-11,
        "tolerance": 1e-23,
        "claim_type": "standard-literature reduction arithmetic",
    },
    {
        "id": "eps1_kappa_target",
        "file": "leptogenesis_target_reduction_results.json",
        "path": ("numbers", "eps1_kappa_target"),
        "expected": 5.905280726708112e-08,
        "tolerance": 1e-20,
        "claim_type": "standard-literature reduction arithmetic",
    },
    {
        "id": "registry_total",
        "file": "baryogenesis_registry_summary_results.json",
        "path": ("summary", "total"),
        "expected": 48,
        "tolerance": 0,
        "claim_type": "exact registry count",
    },
    {
        "id": "registry_clean",
        "file": "baryogenesis_registry_summary_results.json",
        "path": ("summary", "clean"),
        "expected": 15,
        "tolerance": 0,
        "claim_type": "exact registry count",
    },
    {
        "id": "registry_conditional_verified",
        "file": "baryogenesis_registry_summary_results.json",
        "path": ("summary", "conditional_verified"),
        "expected": 33,
        "tolerance": 0,
        "claim_type": "exact registry count",
    },
    {
        "id": "jwst_z10_ratio",
        "file": "jwst_formation_time_table_results.json",
        "path": ("grid", 0, "ratio"),
        "expected": 1.478575721721601,
        "tolerance": 1e-9,
        "claim_type": "deterministic numerical integral",
    },
    {
        "id": "jwst_jades_z14_delta_myr",
        "file": "jwst_formation_time_table_results.json",
        "path": ("objects", 0, "delta_myr"),
        "expected": 135.78694162866518,
        "tolerance": 1e-6,
        "claim_type": "deterministic numerical integral",
    },
    {
        "id": "desi_active_chi2",
        "file": "desi_confrontation_results.json",
        "path": ("raw_gccomb", "active_branch_chi2"),
        "expected": 69.48480893315653,
        "tolerance": 1e-9,
        "claim_type": "fixed DESI covariance chi2",
    },
    {
        "id": "desi_flat_cpl_w0",
        "file": "desi_confrontation_results.json",
        "path": ("flat_cpl_reinterpretation_fixed_point", "w0"),
        "expected": -1.030263043675755,
        "tolerance": 1e-15,
        "claim_type": "fixed flat-CPL reinterpretation point",
    },
    {
        "id": "desi_flat_cpl_wa",
        "file": "desi_confrontation_results.json",
        "path": ("flat_cpl_reinterpretation_fixed_point", "wa"),
        "expected": -0.1115075206254369,
        "tolerance": 1e-15,
        "claim_type": "fixed flat-CPL reinterpretation point",
    },
    {
        "id": "dark_sector_f_b",
        "file": "dark_matter_null_forecast_results.json",
        "path": ("framework_ledger", "f_b"),
        "expected": 0.3127083362150814,
        "tolerance": 1e-15,
        "claim_type": "exact framework constant combination",
    },
    {
        "id": "LZ_limit",
        "file": "dark_matter_null_forecast_results.json",
        "path": ("experimental_limit_checks", "LZ_2024", "limit_cm2"),
        "expected": 2.2e-48,
        "tolerance": 0.0,
        "claim_type": "manuscript-cited external value",
    },
    {
        "id": "XENONnT_limit",
        "file": "dark_matter_null_forecast_results.json",
        "path": ("experimental_limit_checks", "XENONnT", "limit_cm2"),
        "expected": 2.58e-47,
        "tolerance": 0.0,
        "claim_type": "manuscript-cited external value",
    },
    {
        "id": "PandaX4T_limit",
        "file": "dark_matter_null_forecast_results.json",
        "path": ("experimental_limit_checks", "PandaX4T", "limit_cm2"),
        "expected": 1.6e-47,
        "tolerance": 0.0,
        "claim_type": "manuscript-cited external value",
    },
]


def descend(payload: Any, path: tuple[Any, ...]) -> Any:
    cur = payload
    for key in path:
        cur = cur[key]
    return cur


def is_close(actual: Any, expected: Any, tolerance: float) -> tuple[bool, float | None]:
    if isinstance(expected, bool):
        return actual is expected, None
    if isinstance(expected, str):
        return actual == expected, None
    if isinstance(expected, int) and tolerance == 0:
        return actual == expected, None
    delta = abs(float(actual) - float(expected))
    return delta <= tolerance, delta


def main() -> int:
    result_files = sorted(RESULTS.glob("*.json"))
    parse_failures = []
    payloads = {}
    for path in result_files:
        try:
            payloads[path.name] = json.loads(path.read_text())
            print(f"PASS parse {path.name}")
        except Exception as exc:
            parse_failures.append({"file": path.name, "error": str(exc)})
            print(f"FAIL parse {path.name}: {exc}")

    failures = []
    pass_count = len(result_files) - len(parse_failures)
    total_checks = len(result_files)

    for check in CHECKS:
        total_checks += 1
        payload = payloads.get(check["file"])
        if payload is None:
            failures.append({"id": check["id"], "reason": "missing or unparsable JSON", "file": check["file"]})
            print(f"FAIL {check['id']}: missing or unparsable {check['file']}")
            continue
        actual = descend(payload, check["path"])
        ok, delta = is_close(actual, check["expected"], check["tolerance"])
        if ok:
            pass_count += 1
            if delta is None:
                print(f"PASS {check['id']}: actual={actual!r}")
            else:
                print(f"PASS {check['id']}: actual={actual:.17g} expected={check['expected']:.17g} delta={delta:.3g} tol={check['tolerance']}")
        else:
            failure = {
                "id": check["id"],
                "file": check["file"],
                "path": list(check["path"]),
                "actual": actual,
                "expected": check["expected"],
                "tolerance": check["tolerance"],
                "delta": delta,
                "claim_type": check["claim_type"],
            }
            failures.append(failure)
            print(
                f"FAIL {check['id']}: actual={actual!r} expected={check['expected']!r} "
                f"delta={delta!r} tol={check['tolerance']}"
            )

    failures.extend(parse_failures)
    fail_count = len(failures)
    print(f"SUMMARY total_checks={total_checks} pass_count={pass_count} fail_count={fail_count}")
    if failures:
        print(json.dumps({"state": "failed", "failures": failures}, indent=2, sort_keys=True))
        return 1
    print(json.dumps({"state": "passed", "total_checks": total_checks, "pass_count": pass_count, "fail_count": 0}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
