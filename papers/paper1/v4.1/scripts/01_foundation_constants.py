#!/usr/bin/env python3
"""Paper 1 v4.0 script 01: foundational constants.

Purpose:
    Recompute the Schwarzschild radius, line-scale ratio, gauge factor,
    spatial decoupling factor, and related constants used locally in Paper 1.

Inputs:
    data/imported_constants.json

Outputs:
    results/foundation_constants_results.json

Claim boundary:
    Verified arithmetic from stated constants only. This script does not
    validate later-paper theorem claims.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    constants = json.loads(DATA.read_text())
    phys = constants["physical_constants"]
    inp = constants["paper1_inputs"]

    c = phys["c_m_s"]
    G = phys["G_m3_kg_s2"]
    l_p = phys["planck_length_m"]
    M_U = inp["M_U_kg"]
    R_U = inp["R_U_m"]
    gamma_bi = inp["gamma_BI"]

    r_s = 2.0 * G * M_U / c**2
    x = r_s / R_U
    gamma_geometric = math.sqrt(r_s / l_p)
    Q = 1.0 + gamma_bi**2
    K_gauge = math.log(Q)
    Delta = x**4 * Q
    K_mean = math.log(Delta)
    x_crit = Q ** (-0.25)
    kretschmann_horizon = 12.0 / r_s**4

    output = {
        "script": "01_foundation_constants.py",
        "inputs": {
            "M_U_kg": M_U,
            "R_U_m": R_U,
            "gamma_BI": gamma_bi,
            "G_m3_kg_s2": G,
            "c_m_s": c,
            "planck_length_m": l_p
        },
        "headline": {
            "r_s_m": r_s,
            "x": x,
            "gamma_geometric": gamma_geometric,
            "Q": Q,
            "K_gauge": K_gauge,
            "Delta": Delta,
            "K_mean": K_mean,
            "x_crit": x_crit,
            "kretschmann_horizon_m_minus4": kretschmann_horizon
        },
        "manuscript_comparison": {
            "r_s_rounds_to_6p685e26": round(r_s / 1e26, 3) == 6.684,
            "x_rounds_to_1p519": round(x, 3) == 1.519,
            "gamma_rounds_to_6p431e30": round(gamma_geometric / 1e30, 3) == 6.431,
            "Delta_rounds_to_5p6240": round(Delta, 4) == 5.6240,
            "K_gauge_rounds_to_0p0549": round(K_gauge, 4) == 0.0549,
            "x_crit_rounds_to_0p9864": round(x_crit, 4) == 0.9864
        }
    }

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "foundation_constants_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output["headline"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

