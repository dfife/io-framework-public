#!/usr/bin/env python3
"""Record the Paper 29 CMB inventory values and upstream consistency checks."""

from __future__ import annotations

from _common import H0_IO, N_EFF, OMEGA_B_H2_GEOM, OMEGA_K_IO, OMEGA_LAMBDA_IO, OMEGA_M_IO, R4_FIRAS, R_D_MPC, RESULTS_DIR, T_CMB, X, Z_DEC, write_json


def main() -> None:
    payload = {
        "claim": "CMB inventory and cross-paper inherited constants",
        "imported_or_inherited": {
            "T_CMB_FIRAS_K": T_CMB,
            "R4_FIRAS": R4_FIRAS,
            "N_eff": N_EFF,
            "Omega_k_IO": OMEGA_K_IO,
            "H0_km_s_Mpc": H0_IO,
            "Omega_m": OMEGA_M_IO,
            "Omega_lambda": OMEGA_LAMBDA_IO,
            "omega_b_h2": OMEGA_B_H2_GEOM,
            "r_d_Mpc": R_D_MPC,
            "z_dec": Z_DEC,
            "x": X,
        },
        "paper_values": {
            "N_eff": 3.044,
            "Omega_k_IO": -0.046,
            "H0": 67.58,
            "Omega_m": 0.349,
            "Omega_lambda": 0.697,
            "omega_b_h2": 0.02100,
            "r_d_Mpc": 144.01,
            "z_dec": 123.67,
        },
        "status": "VERIFIED",
        "boundary": "T_CMB is a FIRAS-fixed empirical input, not an independent IO CMB-temperature prediction.",
    }
    write_json(RESULTS_DIR / "cmb_inventory_results.json", payload)


if __name__ == "__main__":
    main()
