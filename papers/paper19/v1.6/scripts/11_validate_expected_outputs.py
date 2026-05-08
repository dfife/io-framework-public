#!/usr/bin/env python3
"""
Validate the frozen Paper 19 v1.6 reproducibility outputs.

This is the referee quickstart. It performs standard-library checks against
the JSON artifacts included in the bundle and exits nonzero on any mismatch.
It does not require CAMB, CLASS, PRyMordial, or external observational data.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


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

    bridge = load("bridge_theorems_results.json")
    check_float(
        "omega_b_alpha_3_over_2",
        float(bridge["resulting_branch"]["omega_b_alpha_3_over_2"]),
        0.017053042566348755,
        1e-16,
        failures,
    )

    bdp = load("bdp_domain_no_go_results.json")
    check_bool(
        "bdp_old_low_below_observer_endpoint",
        bool(bdp["no_go_checks"]["old_low_below_observer_endpoint"]),
        True,
        failures,
    )

    boss = load("boss_fullshape_baryon_audit_results.json")
    scenarios = {row["name"]: row for row in boss["scenarios"]}
    check_float(
        "boss_decoupled_geometric_baryon_chi2",
        scenarios["decoupled_geometric_baryon"]["chi2"],
        82.40891206029595,
        1e-9,
        failures,
    )
    check_float(
        "boss_lcdm_reference_chi2",
        scenarios["planck_reference"]["chi2"],
        70.32360985979422,
        1e-9,
        failures,
    )

    score = load("corrected_scorecard_results.json")
    check_float(
        "scorecard_alpha_3_over_2_boss_chi2",
        score["branches"]["alpha_3_over_2"]["boss_fullshape_chi2"],
        73.03360608958111,
        1e-9,
        failures,
    )
    check_float(
        "scorecard_z_eq",
        score["equality_redshift"]["z_eq_alpha_3_over_2"],
        2823.879425051597,
        1e-9,
        failures,
    )
    check_float(
        "scorecard_T_FIRAS",
        score["inputs"]["T0_IO"],
        2.7255,
        1e-12,
        failures,
    )

    bbn = load("bbn_scorecard_results.json")
    check_float(
        "bbn_D_over_H",
        bbn["prymordial"]["large_network_exact"]["D/H"],
        2.5233039701421276e-05,
        1e-16,
        failures,
    )
    check_float(
        "bbn_Y_p",
        bbn["prymordial"]["large_network_exact"]["Y_p"],
        0.24779423821196234,
        1e-14,
        failures,
    )
    d_sigma = bbn["comparisons"]["vs_observed_conventions_v1_sigma"]["D/H_sigma"]
    y_sigma = bbn["comparisons"]["vs_observed_conventions_v1_sigma"]["Y_p_sigma"]
    check_float("bbn_chi2_D_plus_Y", d_sigma * d_sigma + y_sigma * y_sigma, 0.5031639343080561, 1e-12, failures)

    r4 = load("r4_impact_audit_results.json")
    check_float("R4_FIRAS", r4["r4_repair"]["R4_FIRAS"], 1.0031014644, 1e-12, failures)

    audit = load("kappa_audit_summary_results.json")
    check_bool(
        "no_hidden_baryon_scalarization_parameter",
        bool(audit["hidden_continuous_parameter_found_in_baryon_scalarization"]),
        False,
        failures,
    )

    total = 12
    passed = total - len(failures)
    print(f"SUMMARY total_checks={total} pass_count={passed} fail_count={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
