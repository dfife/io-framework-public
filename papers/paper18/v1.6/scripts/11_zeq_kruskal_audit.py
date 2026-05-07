"""Audit Paper 18 equality-redshift and Kruskal comparisons after R4 repair.

The equality-redshift diagnostic belongs to the conditional `N_eff = Delta`
branch that Paper 18 itself withdraws as a Friedmann-radiation identification.
For v1.6, the observer-side thermal input is no longer the implicit `R4 = 1`
value `2.7253 K`; it is the Paper 17 v1.5 FIRAS-fixed readout.
"""

import json
import math
from pathlib import Path


def main() -> None:
    gamma_bi = 0.2375
    x_r4_source = 1.519
    k_gauge = math.log(1.0 + gamma_bi**2)
    r4_firas = 1.0031014644
    t_io_bulk = 2.6635
    t_firas = 2.7255

    h0 = 68.91
    omega_m = 0.335
    t0 = t_io_bulk * (x_r4_source ** (r4_firas * k_gauge))
    n_eff = 5.62421685262410640625

    h = h0 / 100.0
    omega_gamma_h2 = 2.4728e-5 * (t0 / 2.7255) ** 4
    omega_r_h2 = omega_gamma_h2 * (1.0 + 0.22710731766 * n_eff)
    omega_r = omega_r_h2 / (h * h)
    z_eq = omega_m / omega_r - 1.0

    legacy_z_eq = 1758.0

    kruskal_factor = 2.0 / math.sqrt(math.e)
    legacy_f_opt = 1.205
    active_frame_split = math.log(n_eff) * 1.519 / (8.0 * 0.2375)

    payload = {
        "active_branch_inputs": {
            "H0": h0,
            "Omega_m": omega_m,
            "T0": t0,
            "T_FIRAS": t_firas,
            "T0_minus_FIRAS": t0 - t_firas,
            "R4_FIRAS": r4_firas,
            "thermal_status": "FIRAS-fixed observer readout; not an independent CMB-temperature prediction.",
            "N_eff": n_eff,
        },
        "derived_radiation_sector": {
            "h": h,
            "omega_gamma_h2": omega_gamma_h2,
            "omega_r_h2": omega_r_h2,
            "Omega_r": omega_r,
        },
        "equality_redshift": {
            "z_eq_active": z_eq,
            "z_eq_legacy_paper3": legacy_z_eq,
            "delta_z_eq": z_eq - legacy_z_eq,
            "ratio_active_to_legacy": z_eq / legacy_z_eq,
        },
        "kruskal_bbn_comparison": {
            "kruskal_factor_2_over_sqrt_e": kruskal_factor,
            "legacy_F_opt": legacy_f_opt,
            "percent_diff_vs_legacy_F_opt": 100.0 * (kruskal_factor - legacy_f_opt) / legacy_f_opt,
            "active_BDP_frame_split_F": active_frame_split,
            "percent_diff_vs_active_BDP_F": 100.0 * (kruskal_factor - active_frame_split) / active_frame_split,
        },
    }

    out = Path(__file__).resolve().parents[1] / "results" / "paper18_zeq_kruskal_audit_checks.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
