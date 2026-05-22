#!/usr/bin/env python3
"""
Paper 32 v2.0 reproducibility script 01.

Purpose:
    Recompute the framework constants table used by Paper 32 v2.0 from the
    public support constants:

        gamma_BI, x, M_U, r_s, the Rosetta identity
        Delta = x^4 (1 + gamma_BI^2), and the Paper 17 v1.5
        FIRAS-fixed optical readout normalization R4.

    The v2.0 repair is explicit: the observed CMB temperature is not treated
    as an independent IO prediction.  The active observer-side temperature is
    the unique FIRAS-normalized value in the readout family

        T_obs(R4) = T_IO * x^(R4 * K_gauge).

    The old R4=1 value is retained only as a historical diagnostic so a reader
    can see exactly what changed.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/framework_constants_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction of Paper 32 support constants and the
    Paper 17 v1.5 R4/FIRAS repair.  This script does not claim an independent
    CMB-temperature prediction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "framework_constants_results.json"


def load_payload() -> dict:
    """Load the public constants and provenance ledger for this bundle."""
    return json.loads(DATA_PATH.read_text())


def main() -> int:
    payload = load_payload()
    constants = payload["framework_constants"]
    physical = payload["physical_constants"]

    c = physical["c_m_s"]
    G = physical["G_m3_kg_s2"]
    gamma = constants["gamma_BI"]
    x = constants["x"]
    m_nominal = constants["M_U_nominal_kg"]
    r_s = constants["r_s_harmonized_m"]
    t_io = constants["T_IO_K"]
    t_firas = constants["T_FIRAS_K"]
    sigma_t_firas = constants["sigma_T_FIRAS_K"]
    r4_firas = constants["R4_FIRAS"]

    q = 1.0 + gamma**2
    k_gauge = math.log(q)
    f_gamma = math.exp(-k_gauge)
    delta = x**4 * q
    ln_x = math.log(x)
    r_s_from_nominal_mass = 2.0 * G * m_nominal / c**2
    m_u_implied_by_harmonized_rs = r_s * c**2 / (2.0 * G)
    r_u = r_s / x

    # Historical unit-normalization value from v1.5.  This is no longer an
    # active prediction of the observed CMB temperature.
    thermal_transfer_unit_r4 = x**k_gauge
    t_obs_unit_r4 = t_io * thermal_transfer_unit_r4

    # Active v2.0 readout: FIRAS fixes R4 once; downstream scripts may not
    # retune this normalization against any other observable.
    thermal_transfer_firas = x ** (r4_firas * k_gauge)
    t_obs_firas_fixed = t_io * thermal_transfer_firas
    r4_from_firas = math.log(t_firas / t_io) / (k_gauge * ln_x)
    sigma_r4_firas_only = (sigma_t_firas / t_firas) / (k_gauge * ln_x)

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction / R4-FIRAS repaired",
        "inputs": {
            "gamma_BI": gamma,
            "x": x,
            "M_U_nominal_kg": m_nominal,
            "r_s_harmonized_m": r_s,
            "T_IO_K": t_io,
            "T_FIRAS_K": t_firas,
            "sigma_T_FIRAS_K": sigma_t_firas,
            "R4_FIRAS_input": r4_firas,
        },
        "derived": {
            "Q": q,
            "K_gauge": k_gauge,
            "ln_x": ln_x,
            "K_gauge_ln_x": k_gauge * ln_x,
            "f_Gamma": f_gamma,
            "Delta": delta,
            "sqrt_Delta": math.sqrt(delta),
            "ln_Delta": math.log(delta),
            "r_s_from_nominal_M_U_m": r_s_from_nominal_mass,
            "M_U_implied_by_harmonized_r_s_kg": m_u_implied_by_harmonized_rs,
            "R_U_m": r_u,
            "R4_FIRAS": r4_from_firas,
            "sigma_R4_FIRAS_only": sigma_r4_firas_only,
            "effective_sigma_R4_K_gauge": r4_from_firas * k_gauge,
            "T_obs_FIRAS_fixed_K": t_obs_firas_fixed,
            "thermal_transfer_factor_FIRAS_fixed": thermal_transfer_firas,
            "T_obs_R4_equals_1_K": t_obs_unit_r4,
            "thermal_transfer_factor_R4_equals_1": thermal_transfer_unit_r4,
            "T_obs_R4_equals_1_minus_FIRAS_K": t_obs_unit_r4 - t_firas,
            "T_obs_R4_equals_1_minus_FIRAS_sigma": (t_obs_unit_r4 - t_firas) / sigma_t_firas,
            "f_baryon_2gamma_over_x": 2.0 * gamma / x,
            "tau_eff_IO": k_gauge / 2.0,
            "n_s": 1.0 - k_gauge / x,
            "x_crit": q ** (-0.25),
        },
        "consistency_checks": {
            "f_Gamma_equals_inverse_Q": math.isclose(f_gamma, 1.0 / q, rel_tol=0.0, abs_tol=1e-15),
            "Delta_equals_x4_Q": math.isclose(delta, x**4 * q, rel_tol=0.0, abs_tol=1e-15),
            "R4_input_matches_FIRAS_inversion": math.isclose(r4_firas, r4_from_firas, rel_tol=0.0, abs_tol=1e-15),
            "T_obs_FIRAS_fixed_equals_T_FIRAS": math.isclose(t_obs_firas_fixed, t_firas, rel_tol=0.0, abs_tol=1e-15),
        },
        "claim_boundary": {
            "observed_CMB_temperature_status": "FIRAS-fixed empirical readout, not independent IO prediction",
            "R4_status": "unique algebraic normalization given FIRAS empirical thermal datum",
            "R4_downstream_rule": "R4_FIRAS is fixed once and may not be retuned against downstream observables.",
            "R4_equals_1_status": "historical diagnostic only",
        },
        "precision_note": "Paper 32 late-time scripts use r_s_harmonized_m, not r_s recomputed from rounded M_U_nominal_kg.",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
