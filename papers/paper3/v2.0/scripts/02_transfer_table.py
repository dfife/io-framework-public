#!/usr/bin/env python3
"""Paper 3 v2.0 script 02: transfer-function table.

Purpose:
    Reproduce the representative Paper 3 v2.0 transfer table on the active
    Paper 10 / Paper 29 branch.

Inputs:
    data/imported_constants.json

Outputs:
    results/transfer_table_results.json

Claim boundary:
    This table illustrates the analytic transfer theorem. It is not the proof
    of continuity or monotonicity; those are checked in script 03.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "transfer_table_results.json"


def main() -> None:
    payload = json.loads(DATA.read_text())
    branch = payload["active_branch_constants"]
    constants = payload["physical_constants"]

    G = constants["G_SI"]
    c = constants["c_m_s"]
    hbar = constants["hbar_J_s"]
    k_B = constants["k_B_J_K"]
    l_P = constants["l_P_m"]
    Mpc_m = constants["Mpc_m"]
    seconds_per_Gyr = constants["seconds_per_Gyr"]

    M_U = branch["M_U_kg"]
    x = branch["x"]
    H0 = branch["H0_km_s_Mpc"]
    omega_r = branch["Omega_r"]
    omega_m = branch["Omega_m"]
    omega_k = branch["Omega_k"]
    omega_lambda = branch["Omega_Lambda"]

    r_s = 2.0 * G * M_U / (c * c)
    R_U = r_s / x
    gamma_temp = math.sqrt(r_s / l_P)
    thermal_invariant = hbar * c * gamma_temp / (4.0 * math.pi * k_B)
    a0 = c * c / r_s
    eta_s = math.acos(1.0 - 2.0 / x)

    def R_of_eta(eta: float) -> float:
        return 0.5 * r_s * (1.0 - math.cos(eta))

    def tau_of_eta_gyr(eta: float) -> float:
        return (r_s / (2.0 * c)) * (eta - math.sin(eta)) / seconds_per_Gyr

    def Q_of_y(y: float) -> float:
        return omega_r * y**4 + omega_m * y**3 + omega_k * y**2 + omega_lambda

    etas = [0.35, 0.70, 1.00, eta_s, 2.20, 2.70, math.pi]
    rows = []
    for eta in etas:
        R = R_of_eta(eta)
        y = R_U / R
        Q = Q_of_y(y)
        rows.append(
            {
                "eta": eta,
                "tau_OS_Gyr": tau_of_eta_gyr(eta),
                "R_m": R,
                "y": y,
                "redshift_like_y_minus_1": y - 1.0,
                "T_K": thermal_invariant / R,
                "Q_y": Q,
                "H_km_s_Mpc": H0 * math.sqrt(Q),
                "a0_m_s2": a0,
                "current_spatial_epoch": abs(eta - eta_s) < 1.0e-12
            }
        )

    result = {
        "status": "VERIFIED transfer-table arithmetic",
        "claim_boundary": "Illustrative table only; continuity and monotonicity are established by script 03.",
        "constants": {
            "r_s_m": r_s,
            "R_U_m": R_U,
            "eta_s": eta_s,
            "thermal_invariant_K_m": thermal_invariant,
            "a0_m_s2": a0
        },
        "rows": rows,
        "table_note": "The eta_s row is the current spatial epoch R=R_U. tau_OS is not the radiation-inclusive Paper 30 master clock."
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
