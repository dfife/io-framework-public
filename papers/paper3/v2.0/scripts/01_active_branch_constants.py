#!/usr/bin/env python3
"""Paper 3 v2.0 script 01: active branch constants.

Purpose:
    Recompute constants used by the Paper 3 v2.0 input-structure and
    transfer-function discussion.

Inputs:
    data/imported_constants.json

Outputs:
    results/active_branch_constants_results.json

Claim boundary:
    Arithmetic reproduction only. This script does not independently validate
    the upstream Paper 10 / Paper 29 active-branch derivation.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "active_branch_constants_results.json"


def main() -> None:
    payload = json.loads(DATA.read_text())
    branch = payload["active_branch_constants"]
    constants = payload["physical_constants"]

    G = constants["G_SI"]
    c = constants["c_m_s"]
    hbar = constants["hbar_J_s"]
    k_B = constants["k_B_J_K"]
    l_P = constants["l_P_m"]
    M_U = branch["M_U_kg"]
    x = branch["x"]
    omega_m = branch["Omega_m"]
    omega_r = branch["Omega_r"]

    r_s = 2.0 * G * M_U / (c * c)
    R_U = r_s / x
    gamma_temp = math.sqrt(r_s / l_P)
    thermal_invariant = hbar * c * gamma_temp / (4.0 * math.pi * k_B)
    T_at_R_U = thermal_invariant / R_U
    a0 = c * c / r_s
    z_eq = omega_m / omega_r - 1.0

    result = {
        "status": "VERIFIED arithmetic for Paper 3 v2.0 constants",
        "claim_boundary": payload["claim_boundary"],
        "headline": {
            "r_s_m": r_s,
            "R_U_m": R_U,
            "gamma_temp": gamma_temp,
            "thermal_invariant_K_m": thermal_invariant,
            "T_at_R_U_K": T_at_R_U,
            "a0_m_s2": a0,
            "z_eq_active_branch": z_eq
        },
        "formulae": payload["formulae"],
        "active_branch_constants": branch,
        "note": "z_eq is archived here as a rehomed Paper 30 active-branch value, not as an active Paper 3 claim."
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
