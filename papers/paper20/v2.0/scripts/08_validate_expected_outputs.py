#!/usr/bin/env python3
"""
Validate the frozen Paper 20 v2.0 reproducibility outputs.

This is the referee quickstart. It uses only Python standard-library modules
and the JSON files included in the bundle. It does not require PRyMordial,
CLASS, CAMB, scipy, numpy, pandas, or external observational datasets.
"""

from __future__ import annotations

import json
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

    r4 = load_json(RESULTS / "r4_firas_readout_results.json")
    check_bool("independent_cmb_temperature_prediction", r4["status"]["independent_cmb_temperature_prediction"], False, failures)
    check_float("firas_fixed_T_obs_K", r4["computed"]["firas_fixed_T_obs_K"], 2.725499012374763, 1e-12, failures)

    scope = load_json(RESULTS / "radiation_scope_boundary_results.json")
    check_float("Delta_H0_max", scope["late_time_sensitivity"]["Delta_H0_max_km_s_Mpc"], 0.013, 1e-15, failures)

    acoustic = load_json(RESULTS / "acoustic_theorems_results.json")
    check_float("J_r_geom", acoustic["theorems"]["20.1"]["J_r_geom"], 1.2324731234392092, 1e-15, failures)
    check_float("J_theta", acoustic["theorems"]["20.2"]["J_theta"], 0.8339461798286282, 1e-15, failures)
    check_float("theta_rounded", acoustic["theorems"]["20.2"]["theta_star_pred_deg_manuscript_rounded"], 0.599, 1e-15, failures)
    check_float("theta_legacy_percent", acoustic["exact_rows"]["legacy_exact_row"]["residual_percent"], 0.42942114370226664, 1e-12, failures)
    check_float("theta_current_sigma", acoustic["exact_rows"]["current_bipartite_rounded_row"]["sigma_offset"], 9.205378456904015, 1e-12, failures)

    bbn = load_json(RESULTS / "bbn_wrapper_scorecard_results.json")["scorecard"]
    check_float("bbn_D_over_H", bbn["D_over_H"], 2.510410594954571e-05, 1e-16, failures)
    check_float("bbn_D_sigma", bbn["D_over_H_sigma"], -0.5529801681809717, 1e-12, failures)
    check_float("bbn_Y_p", bbn["Y_p"], 0.24781814417284279, 1e-14, failures)
    check_float("bbn_Y_sigma", bbn["Y_p_sigma"], 0.7045360432106975, 1e-12, failures)
    check_float("bbn_chi2_D_plus_Y", bbn["chi2_D_over_H_plus_Y_p"], 0.8021581025844415, 1e-12, failures)

    neff = load_json(RESULTS / "neff_import_kinetic_results.json")["computed"]
    check_float("N_eff_output", neff["N_eff_output"], 3.044388520277016, 1e-15, failures)
    check_float("delta_N_eff_kinetic", neff["delta_N_eff_kinetic"], 0.044388520277015786, 1e-15, failures)
    check_float("Neff_TIO_minus_TOBS", neff["Neff_output_difference_TIO_minus_TOBS"], 0.0, 1e-15, failures)

    rad = load_json(RESULTS / "radiation_algebra_theorems_results.json")
    check_float("rho_fermion_over_rho_gamma", rad["theorems"]["20.RAD2"]["rho_fermion_over_rho_gamma_pre_decoupling"], 4.375, 1e-15, failures)
    check_float("bulk_vacuum_w", rad["theorems"]["20.RAD3"]["w_vacuum"], 1.6666666666666667, 1e-15, failures)

    audit = load_json(RESULTS / "kappa_audit_results.json")
    check_bool("hidden_continuous_parameter_found", audit["hidden_continuous_parameter_found"], False, failures)
    check_bool("removed_v18_sections_excluded", audit["removed_v18_sections_excluded"], True, failures)

    total = 22
    passed = total - len(failures)
    print(f"SUMMARY total_checks={total} pass_count={passed} fail_count={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
