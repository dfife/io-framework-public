#!/usr/bin/env python3
"""Paper 1 v4.0 script 02: temperature chain.

Purpose:
    Recompute the Paper 1 local Hawking-temperature chain, including the
    geometric boost factor and the Planck-temperature identity.

Inputs:
    data/imported_constants.json
    results/foundation_constants_results.json

Outputs:
    results/temperature_chain_results.json

Claim boundary:
    Paper 1 local thermal-scale arithmetic only. The FIRAS-observed
    observer-side temperature is archived as an empirical readout datum, not
    an independent Paper 1 prediction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
FOUNDATION = BUNDLE_ROOT / "results" / "foundation_constants_results.json"
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    constants = json.loads(DATA.read_text())
    foundation = json.loads(FOUNDATION.read_text())
    phys = constants["physical_constants"]
    inp = constants["paper1_inputs"]

    c = phys["c_m_s"]
    hbar = phys["hbar_J_s"]
    k_B = phys["k_B_J_K"]
    T_P = phys["planck_temperature_K"]
    M_U = inp["M_U_kg"]
    T_FIRAS = inp["T_FIRAS_K"]

    r_s = foundation["headline"]["r_s_m"]
    R_U = inp["R_U_m"]
    gamma_geometric = foundation["headline"]["gamma_geometric"]
    x = foundation["headline"]["x"]

    T_Hawking = hbar * c / (4.0 * math.pi * k_B * r_s)
    T_IO = hbar * c * gamma_geometric / (4.0 * math.pi * k_B * R_U)
    T_planck_identity = math.sqrt(T_Hawking * T_P) * r_s / (2.0 * math.sqrt(math.pi) * R_U)
    T_local = T_Hawking * x

    # Invert the Paper 1 temperature formula to show the mass consistency
    # implied by the manuscript's rounded constants.
    G = phys["G_m3_kg_s2"]
    l_p = phys["planck_length_m"]
    coefficient = hbar * c / (4.0 * math.pi * k_B * R_U * math.sqrt(l_p))
    r_s_from_T = (T_IO / coefficient) ** 2
    M_U_from_T = r_s_from_T * c**2 / (2.0 * G)
    mass_relative_error = (M_U_from_T - M_U) / M_U
    FIRAS_readout_ratio = T_FIRAS / T_IO

    output = {
        "script": "02_temperature_chain.py",
        "headline": {
            "T_Hawking_K": T_Hawking,
            "T_IO_K": T_IO,
            "T_planck_identity_K": T_planck_identity,
            "T_local_K": T_local,
            "FIRAS_readout_ratio": FIRAS_readout_ratio,
            "M_U_from_T_IO_kg": M_U_from_T,
            "mass_relative_error": mass_relative_error
        },
        "claim_boundary": {
            "T_IO_status": "local Paper 1 formula arithmetic",
            "T_FIRAS_status": "IMPORTED/EMPIRICAL observer-side readout datum inherited through Paper 17 v1.5",
            "independent_CMB_temperature_prediction": False
        },
        "manuscript_comparison": {
            "T_Hawking_rounds_to_2p73e_minus31": round(T_Hawking / 1e-31, 2) == 2.73,
            "T_IO_rounds_to_2p6635": round(T_IO, 4) == 2.6632,
            "T_local_rounds_to_4p14e_minus31": round(T_local / 1e-31, 2) == 4.14
        }
    }

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "temperature_chain_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output["headline"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
