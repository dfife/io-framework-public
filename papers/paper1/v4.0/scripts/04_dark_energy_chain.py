#!/usr/bin/env python3
"""Paper 1 v4.0 script 04: dark-energy chain.

Purpose:
    Recompute the Paper 1 torsion/effective dark-energy density formula from
    the stated v4.0 constants and compare it to the manuscript-quoted legacy
    values.

Inputs:
    data/imported_constants.json
    results/foundation_constants_results.json

Outputs:
    results/dark_energy_chain_results.json

Claim boundary:
    Verified arithmetic and audit finding. The current stated constants do not
    reproduce the manuscript's quoted rho_Lambda values exactly; this script
    makes that mismatch explicit.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
FOUNDATION = BUNDLE_ROOT / "results" / "foundation_constants_results.json"
RESULTS = BUNDLE_ROOT / "results"


def rel(a: float, b: float) -> float:
    return (a - b) / b


def main() -> None:
    constants = json.loads(DATA.read_text())
    foundation = json.loads(FOUNDATION.read_text())
    phys = constants["physical_constants"]
    inp = constants["paper1_inputs"]
    quoted = constants["manuscript_quoted_values"]

    c = phys["c_m_s"]
    G = phys["G_m3_kg_s2"]
    gamma_bi = inp["gamma_BI"]
    rho_obs = inp["rho_Lambda_observed_kg_m3"]
    r_s = foundation["headline"]["r_s_m"]
    x = foundation["headline"]["x"]

    Q = 1.0 + gamma_bi**2
    rho_torsion = 9.0 * math.pi * c**2 / (32.0 * G * r_s**2 * Q)
    rho_eff = rho_torsion * x**2
    Lambda_torsion = 9.0 * math.pi**2 / (4.0 * r_s**2 * Q)

    manuscript_rho_torsion = quoted["rho_Lambda_torsion_kg_m3"]
    manuscript_rho_eff = quoted["rho_Lambda_eff_kg_m3"]

    output = {
        "script": "04_dark_energy_chain.py",
        "headline": {
            "rho_Lambda_torsion_kg_m3": rho_torsion,
            "rho_Lambda_eff_kg_m3": rho_eff,
            "Lambda_torsion_m_minus2": Lambda_torsion,
            "rho_Lambda_observed_kg_m3": rho_obs,
            "formula_vs_observed_relative": rel(rho_eff, rho_obs),
            "formula_vs_observed_percent": 100.0 * rel(rho_eff, rho_obs)
        },
        "manuscript_quoted_legacy_values": {
            "rho_Lambda_torsion_kg_m3": manuscript_rho_torsion,
            "rho_Lambda_eff_kg_m3": manuscript_rho_eff,
            "quoted_vs_observed_relative": rel(manuscript_rho_eff, rho_obs),
            "quoted_vs_observed_percent": 100.0 * rel(manuscript_rho_eff, rho_obs)
        },
        "audit_finding": {
            "formula_reproduces_manuscript_dark_energy_values": False,
            "rho_torsion_formula_minus_manuscript_relative": rel(rho_torsion, manuscript_rho_torsion),
            "rho_eff_formula_minus_manuscript_relative": rel(rho_eff, manuscript_rho_eff),
            "rho_eff_formula_minus_manuscript_percent": 100.0 * rel(rho_eff, manuscript_rho_eff),
            "interpretation": "With the v4.0 stated constants M_U=4.50e53 kg and R_U=4.40e26 m, the formula gives rho_eff=5.8176e-27 kg/m^3, not the manuscript-quoted 6.05e-27 kg/m^3."
        }
    }

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "dark_energy_chain_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output["headline"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

