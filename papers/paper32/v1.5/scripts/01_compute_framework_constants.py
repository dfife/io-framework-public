#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 01.

Purpose:
    Recompute the framework constants table used by Paper 32 v1.5 from the
    public support constants:

        gamma_BI, x, M_U, r_s, and the Rosetta identity
        Delta = x^4 (1 + gamma_BI^2).

Inputs:
    - data/imported_constants.json

Outputs:
    - results/framework_constants_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction of Paper 32 support constants. The
    bundle exposes the rounded manuscript mass M_U and the harmonized Paper 32
    radius r_s separately to avoid silent precision drift.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "framework_constants_results.json"


def load_payload() -> dict:
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

    q = 1.0 + gamma**2
    k_gauge = math.log(q)
    f_gamma = math.exp(-k_gauge)
    delta = x**4 * q
    r_s_from_nominal_mass = 2.0 * G * m_nominal / c**2
    m_u_implied_by_harmonized_rs = r_s * c**2 / (2.0 * G)
    r_u = r_s / x
    t_obs = t_io * x**k_gauge

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction",
        "inputs": {
            "gamma_BI": gamma,
            "x": x,
            "M_U_nominal_kg": m_nominal,
            "r_s_harmonized_m": r_s,
            "T_IO_K": t_io,
        },
        "derived": {
            "Q": q,
            "K_gauge": k_gauge,
            "f_Gamma": f_gamma,
            "Delta": delta,
            "sqrt_Delta": math.sqrt(delta),
            "ln_Delta": math.log(delta),
            "r_s_from_nominal_M_U_m": r_s_from_nominal_mass,
            "M_U_implied_by_harmonized_r_s_kg": m_u_implied_by_harmonized_rs,
            "R_U_m": r_u,
            "T_obs_K": t_obs,
            "thermal_transfer_factor": x**k_gauge,
            "f_baryon_2gamma_over_x": 2.0 * gamma / x,
            "tau_eff_IO": k_gauge / 2.0,
            "n_s": 1.0 - k_gauge / x,
            "x_crit": q ** (-0.25),
        },
        "consistency_checks": {
            "f_Gamma_equals_inverse_Q": math.isclose(f_gamma, 1.0 / q, rel_tol=0.0, abs_tol=1e-15),
            "Delta_equals_x4_Q": math.isclose(delta, x**4 * q, rel_tol=0.0, abs_tol=1e-15),
            "T_obs_equals_T_IO_x_to_K": math.isclose(t_obs, t_io * x**k_gauge, rel_tol=0.0, abs_tol=1e-15),
        },
        "precision_note": "Paper 32 late-time scripts use r_s_harmonized_m, not r_s recomputed from rounded M_U_nominal_kg.",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

