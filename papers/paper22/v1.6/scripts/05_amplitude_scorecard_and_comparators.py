#!/usr/bin/env python3
"""Reproduce Paper 22 amplitude, scorecard, and comparator arithmetic.

This is the public audit entry point for Theorems 22.23 and 22.24. It does
not redistribute or rerun PRyMordial. Instead it recomputes the algebraic
amplitudes from the framework constants, records the corrected YPCMB wrapper
row frozen during the v1.4/v1.5 sweep, and verifies the chi-square and
Li-7 benchmark arithmetic quoted in Paper 22 v1.5.

Run from the bundle root:

    python3 scripts/05_amplitude_scorecard_and_comparators.py

Output:

    results/amplitude_scorecard_and_comparators_results.json
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
CONSTANTS_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT_PATH = BUNDLE_ROOT / "results" / "amplitude_scorecard_and_comparators_results.json"


def chi2(*sigmas: float) -> float:
    return sum(s * s for s in sigmas)


def main() -> None:
    constants = json.loads(CONSTANTS_PATH.read_text(encoding="utf-8"))
    fw = constants["framework_constants"]
    loads = constants["puncture_loads"]
    amp = constants["amplitude_construction"]
    score = constants["corrected_bbn_scorecard"]
    li7 = constants["li7_uniform_benchmark"]
    comp = constants["two_parameter_comparator"]
    epsilon_w = fw["K_gauge"] * loads["L_1"]
    epsilon_n = (fw["K_mean"] / constants["spatial_channel_constants"]["mult_TT_n2"]) * loads["L_2"]
    active_chi2 = chi2(score["D_over_H_sigma"], score["Y_p_sigma"])
    comparator_chi2 = chi2(comp["D_over_H_sigma"], comp["Y_p_sigma"])
    li7_fraction = score["Li7_over_H"] / li7["uniform_DeltaNeff_Fabs_Li7_over_H"] - 1.0
    result = {
        "script": Path(__file__).name,
        "claim_support": [
            "Theorem 22.23 Zero-Parameter Amplitude Construction",
            "Theorem 22.24 Li-7 Out-of-Sample Consistency",
            "v1.4/v1.5 YPCMB scorecard correction"
        ],
        "status": amp["status"],
        "amplitudes": {
            "epsilon_w": epsilon_w,
            "epsilon_w_formula": amp["epsilon_w_formula"],
            "epsilon_n": epsilon_n,
            "epsilon_n_formula": amp["epsilon_n_formula"],
            "claim_boundary": "zero fitted observational parameters inside the stated premise package; not an unconditional derivation of GMP/TBS."
        },
        "corrected_scorecard": {
            "Y_p": score["Y_p"],
            "Y_p_CMB": score["Y_p_CMB"],
            "Y_p_BBN_audit_only": score["Y_p_BBN_audit_only"],
            "Y_p_output_component": score["Y_p_output_component"],
            "Y_p_sigma": score["Y_p_sigma"],
            "D_over_H": score["D_over_H"],
            "D_over_H_sigma": score["D_over_H_sigma"],
            "Li7_over_H": score["Li7_over_H"],
            "Li7_over_H_sigma": score["Li7_over_H_sigma"],
            "He3_over_H": score["He3_over_H"],
            "chi2_DH_plus_Yp": active_chi2
        },
        "two_parameter_comparator": {
            "eps_freeze": comp["eps_freeze"],
            "eps_nucleo": comp["eps_nucleo"],
            "D_over_H_sigma": comp["D_over_H_sigma"],
            "Y_p_sigma": comp["Y_p_sigma"],
            "chi2_DH_plus_Yp": comparator_chi2,
            "zero_parameter_margin": comparator_chi2 - active_chi2
        },
        "li7_uniform_benchmark": {
            "uniform_DeltaNeff_Fabs_Li7_over_H": li7["uniform_DeltaNeff_Fabs_Li7_over_H"],
            "uniform_DeltaNeff_Fabs_Li7_sigma": li7["uniform_DeltaNeff_Fabs_Li7_sigma"],
            "zero_parameter_minus_uniform_fraction": li7_fraction,
            "absolute_fractional_difference": abs(li7_fraction),
            "percent_difference": 100.0 * li7_fraction,
            "claim_boundary": "Li-7 was not used in calibration; this is internal consistency with the old uniform benchmark, not a lithium solution."
        },
        "checks": {
            "epsilon_w_matches_frozen": abs(epsilon_w - amp["epsilon_w"]) < 1.0e-15,
            "epsilon_n_matches_frozen": abs(epsilon_n - amp["epsilon_n"]) < 1.0e-15,
            "chi2_matches_frozen": abs(active_chi2 - score["chi2_DH_plus_Yp"]) < 1.0e-15,
            "comparator_chi2_matches_frozen": abs(comparator_chi2 - comp["chi2_DH_plus_Yp"]) < 1.0e-15,
            "li7_fraction_matches_frozen": abs(li7_fraction - li7["zero_parameter_minus_uniform_fraction"]) < 1.0e-15
        }
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
