#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "imported_constants.json").read_text())
C = DATA["external_constants"]["c_m_s"]
G = DATA["external_constants"]["G_m3_kg_s2"]
HBAR = DATA["external_constants"]["hbar_J_s"]
KB = DATA["external_constants"]["k_B_J_K"]
LP = DATA["external_constants"]["l_P_m"]
M_U = DATA["framework_inputs"]["M_U_kg"]
GAMMA_BI = DATA["framework_inputs"]["gamma_BI"]
X = DATA["framework_inputs"]["x"]
RHO_OBS = DATA["framework_inputs"]["observed_rho_Lambda_kg_m3"]
MOND_A0 = DATA["framework_inputs"]["observed_mond_a0_m_s2"]
MPC = DATA["external_constants"]["Mpc_m"]


def main() -> None:
    rs = 2.0 * G * M_U / C**2
    r_u = rs / X
    gamma_geom = math.sqrt(rs / LP)
    t_hawking = HBAR * C / (4.0 * math.pi * KB * rs)
    thermal_invariant = HBAR * C * gamma_geom / (4.0 * math.pi * KB)
    t_io = thermal_invariant / r_u
    a0 = C**2 / rs
    rho_torsion_at_rs = 9.0 * math.pi * C**2 / (32.0 * G * rs**2 * (1.0 + GAMMA_BI**2))
    rho_torsion_eff = rho_torsion_at_rs * X**2

    h0 = DATA["active_branch"]["H0_km_s_Mpc"] * 1000.0 / MPC
    rho_crit = 3.0 * h0**2 / (8.0 * math.pi * G)
    rho_active = DATA["active_branch"]["Omega_Lambda"] * rho_crit

    # Paper 2 v2.0 reports this reverse-bridge value from equating its two
    # Lambda routes. It is recorded as an inherited bridge result because the
    # Paper 2 route uses its own rounded interior-Friedmann convention.
    gamma_bridge_paper2_v20 = 0.240

    result = {
        "paper": "Paper 4",
        "version": "v2.0",
        "status": {
            "horizon_constants": "DERIVED",
            "torsion_dark_energy_density": "DERIVED",
            "active_observer_dark_energy_density": "DERIVED/CONDITIONAL_VERIFIED",
            "gamma_bridge": "DERIVED/CONDITIONAL_VERIFIED inherited from Paper 2 v2.0"
        },
        "inputs": {
            "M_U_kg": M_U,
            "gamma_BI": GAMMA_BI,
            "x": X,
            "observed_rho_Lambda_kg_m3": RHO_OBS,
            "observed_mond_a0_m_s2": MOND_A0
        },
        "derived": {
            "r_s_m": rs,
            "R_U_m": r_u,
            "gamma_geom_sqrt_rs_over_lP": gamma_geom,
            "T_Hawking_K": t_hawking,
            "thermal_invariant_K_m": thermal_invariant,
            "T_IO_at_R_U_K": t_io,
            "amplification_factor_TIO_over_TH": t_io / t_hawking,
            "a0_m_s2": a0,
            "a0_percent_offset_vs_1p2e_minus10": 100.0 * (a0 / MOND_A0 - 1.0),
            "rho_Lambda_torsion_at_rs_kg_m3": rho_torsion_at_rs,
            "rho_Lambda_torsion_eff_kg_m3": rho_torsion_eff,
            "rho_Lambda_torsion_eff_percent_offset_vs_observed": 100.0 * (rho_torsion_eff / RHO_OBS - 1.0),
            "rho_crit_active_kg_m3": rho_crit,
            "rho_Lambda_active_observer_kg_m3": rho_active,
            "rho_Lambda_active_percent_offset_vs_observed": 100.0 * (rho_active / RHO_OBS - 1.0),
            "gamma_BI_recovered_paper2_v20": gamma_bridge_paper2_v20,
            "gamma_BI_recovered_percent_offset_vs_0p2375": 100.0 * (gamma_bridge_paper2_v20 / GAMMA_BI - 1.0)
        },
        "claim_boundary": {
            "dark_energy_density": "Paper 1 torsion route is support/readout geometry; active observer branch density is Omega_Lambda rho_crit. Paper 35 maps the support law to observer-frame w=-1 on the active branch.",
            "gamma_bridge": "Paper 4 cites the Paper 2 v2.0 reverse-bridge number. It is not refit on the active Paper 29 density tuple."
        }
    }
    out = ROOT / "results" / "horizon_connections_results.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()
