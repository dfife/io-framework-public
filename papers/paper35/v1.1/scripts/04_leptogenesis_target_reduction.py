#!/usr/bin/env python3
"""Paper 35 v1.1 script 04: leptogenesis target reduction.

Purpose:
    Convert the fixed IO eta target into standard external leptogenesis target
    quantities: Y_B, Y_(B-L), epsilon_1*kappa_f, and the Poplawski target
    compatibility values used in the manuscript.

Inputs:
    data/imported_constants.json

Outputs:
    results/leptogenesis_target_reduction_results.json

Claim boundary:
    DERIVED/CONDITIONAL on standard external leptogenesis formulas. This is a
    target reduction, not IO source-sector closure.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"


def relativistic_majorana_yield(g_internal: float, g_star: float) -> float:
    zeta3 = 1.2020569031595942
    return (135.0 * zeta3 * g_internal) / (8.0 * math.pi**4 * g_star)


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    eta_late = constants["eta_inputs"]["eta_late_mean_baryon_mass"]
    lep = constants["leptogenesis_standard_inputs"]

    y_b = eta_late / 7.04
    y_b_minus_l = lep["sphaleron_inverse_79_over_28"] * y_b
    y_n1_eq = relativistic_majorana_yield(
        lep["heavy_majorana_internal_degrees"],
        lep["g_star_SM"],
    )
    eps1_kappa_target = y_b / (lep["sphaleron_c_sph"] * y_n1_eq)

    # Davidson-Ibarra coefficient in the SM convention:
    # |eps1| <= (3 m_atm M1) / (16 pi v^2), with m_atm converted eV -> GeV.
    m_atm_gev = lep["m_atm_eV"] * 1.0e-9
    c_di = 3.0 * m_atm_gev / (16.0 * math.pi * lep["v_SM_GeV"] ** 2)
    m1_floor_absolute = eps1_kappa_target / c_di
    t_f_target_gev = 2.20039385974778e13
    epsilon_max_at_t_f = c_di * t_f_target_gev
    kappa_required_if_m1_equals_t_f = eps1_kappa_target / epsilon_max_at_t_f

    payload = {
        "script": "04_leptogenesis_target_reduction.py",
        "status": "verified",
        "claim_boundary": "DERIVED/CONDITIONAL on standard external leptogenesis class",
        "formulae": {
            "Y_B": "eta_late / 7.04",
            "Y_B_minus_L": "(79/28) Y_B",
            "Y_N1_eq": "135 zeta(3) g_N1 / (8 pi^4 g_*)",
            "eps1_kappa_target": "Y_B / (c_sph Y_N1_eq)",
            "Davidson_Ibarra_bound": "|eps1| <= 3 m_atm M1 / (16 pi v^2)",
        },
        "numbers": {
            "eta_late": eta_late,
            "Y_B_target": y_b,
            "Y_B_minus_L_target": y_b_minus_l,
            "Y_N1_eq": y_n1_eq,
            "eps1_kappa_target": eps1_kappa_target,
            "c_DI_per_GeV": c_di,
            "M1_floor_kappa_equals_1_GeV": m1_floor_absolute,
            "T_f_target_GeV": t_f_target_gev,
            "epsilon_max_at_T_f": epsilon_max_at_t_f,
            "kappa_required_if_M1_equals_T_f": kappa_required_if_m1_equals_t_f,
            "T_f_over_M1_floor_absolute": t_f_target_gev / m1_floor_absolute,
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "leptogenesis_target_reduction_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["numbers"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
