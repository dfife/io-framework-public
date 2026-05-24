#!/usr/bin/env python3
"""Paper 1 v4.1 script 07: total-energy / density-accounting separation.

Purpose:
    Reproduce the arithmetic surface for Theorem 1.Y. The theorem separates
    the exterior Schwarzschild mass charge E_total = M_U c^2 from the
    bookkeeping average density rho_avg(R) = M_U/(2*pi^2*R^3).

Inputs:
    data/imported_constants.json

Outputs:
    results/total_energy_density_accounting_results.json

Claim boundary:
    This script does not construct a component density budget. It records the
    theorem's accounting separation and the no-common-measure guard.
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
    M_U = inp["M_U_kg"]
    R_U = inp["R_U_m"]

    v_s3 = 2.0 * math.pi**2 * R_U**3
    e_total = M_U * c**2
    rho_avg = M_U / v_s3

    output = {
        "script": "07_total_energy_density_accounting.py",
        "status_label": "DERIVED/THEOREM within the Paper 1 P1/P2 Schwarzschild-interior mass-accounting and closed-S^3 geometry setting",
        "inputs": {
            "M_U_kg": M_U,
            "R_U_m": R_U,
            "c_m_s": c,
        },
        "headline": {
            "E_total_J": e_total,
            "V_S3_R_U_m3": v_s3,
            "rho_avg_at_R_U_kg_m3": rho_avg,
        },
        "accounting_separation": {
            "E_total_role": "exterior Schwarzschild mass charge, treated as the global/quasi-local mass-energy parameter of the matched IO geometry",
            "rho_avg_role": "bookkeeping definition on a specified closed slice",
            "rho_avg_is_component_budget": False,
            "rho_avg_is_local_quantum_input": False,
            "rho_avg_is_local_stress_energy_component": False,
            "component_slot_sum_licensed_without_typed_measure_theorem": False,
        },
    }

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "total_energy_density_accounting_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output["headline"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
