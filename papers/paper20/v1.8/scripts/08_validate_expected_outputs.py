#!/usr/bin/env python3
"""
Validate the frozen Paper 20 v1.8 reproducibility outputs.

This is the referee quickstart. It uses only Python standard-library modules
and the JSON files included in the bundle. It does not require PRyMordial,
CLASS, CAMB, scipy, numpy, pandas, or external observational datasets.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"
DATA = BUNDLE_ROOT / "data"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check_float(label: str, value: float, expected: float, tol: float, failures: list[str]) -> None:
    delta = abs(value - expected)
    if delta <= tol:
        print(f"PASS {label}: value={value} expected={expected} delta={delta}")
    else:
        msg = f"FAIL {label}: value={value} expected={expected} delta={delta} tol={tol}"
        print(msg)
        failures.append(msg)


def check_bool(label: str, value: bool, expected: bool, failures: list[str]) -> None:
    if value is expected:
        print(f"PASS {label}: value={value}")
    else:
        msg = f"FAIL {label}: value={value} expected={expected}"
        print(msg)
        failures.append(msg)


def main() -> int:
    failures: list[str] = []

    constants = load_json(DATA / "imported_constants.json")["framework_constants"]
    check_float("R4_FIRAS", constants["R4_FIRAS"], 1.0031014644, 1e-12, failures)
    check_float("T_FIRAS_K", constants["T_FIRAS_K"], 2.7255, 1e-12, failures)

    score = load_json(RESULTS / "filtered_scorecard_results.json")
    temp = score["scoreable_channels"]["temperature"]
    check_float("temperature_T_obs", temp["observer_side_thermal_datum"]["T_obs_K"], 2.7255, 1e-12, failures)
    check_bool("temperature_not_independent_prediction", temp["counts_as_independent_cmb_prediction"], False, failures)

    bbn = load_json(RESULTS / "bbn_wrapper_scorecard_results.json")["side_by_side"]["Paper20_vNext_PathC_corrected"]
    check_float("bbn_D_over_H", bbn["D/H"], 2.510410594954571e-05, 1e-16, failures)
    check_float("bbn_D_sigma", bbn["D/H_sigma"], -0.5529801681809717, 1e-12, failures)
    check_float("bbn_Y_p", bbn["Y_p"], 0.24781814417284279, 1e-14, failures)
    check_float("bbn_Y_sigma", bbn["Y_p_sigma"], 0.7045360432106975, 1e-12, failures)
    check_float("bbn_chi2_D_plus_Y", bbn["chi2_DH_plus_Yp"], 0.8021581025844415, 1e-12, failures)

    acoustic = load_json(RESULTS / "acoustic_phase_precision_results.json")
    check_float("J_theta", acoustic["inputs"]["J_theta_derived"], 0.8339461798286282, 1e-15, failures)

    lam = load_json(RESULTS / "torsion_lambda_branch_results.json")["branch"]
    check_float("torsion_lambda_H0_obs", lam["H0_obs"], 61.05967054543954, 1e-10, failures)
    check_float("torsion_lambda_age_obs", lam["age_obs_Gyr"], 15.063539536645377, 1e-10, failures)

    audit = load_json(RESULTS / "kappa_audit_results.json")
    check_bool("hidden_continuous_parameter_found", audit["hidden_continuous_parameter_found"], False, failures)
    check_bool(
        "independent_cmb_temperature_prediction_retired",
        audit["independent_cmb_temperature_prediction_retired"],
        True,
        failures,
    )

    total = 14
    passed = total - len(failures)
    print(f"SUMMARY total_checks={total} pass_count={passed} fail_count={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
