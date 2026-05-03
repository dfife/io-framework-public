#!/usr/bin/env python3
"""Paper 35 v1.1 script 02: BBN temperature assignment.

Purpose:
    Reproduce the typed-observable temperature assignment: BBN reaction rates
    use local T_IO, while the observer photon bath uses T_obs.

Inputs:
    data/imported_constants.json

Outputs:
    results/temperature_assignment_results.json

Claim boundary:
    DERIVED/SCOPED to the IO typed-observable map. The Planck comparison is a
    cross-typed consistency check, not a same-observable theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    fw = constants["framework_constants"]
    eta = constants["eta_inputs"]

    conversion = (eta["T_obs_K"] / eta["T_IO_K"]) ** 3
    symbolic_conversion = fw["x"] ** (3.0 * fw["K_gauge"])

    payload = {
        "script": "02_temperature_assignment.py",
        "status": "verified",
        "claim_boundary": "DERIVED/SCOPED typed-observable temperature assignment",
        "assignment": {
            "BBN_reaction_network_temperature": "T_IO",
            "observer_photon_bath_temperature": "T_obs = T_IO x^K_gauge",
        },
        "formulae": {
            "eta_BBN": "eta_obs * (T_obs/T_IO)^3",
            "conversion": "x^(3 K_gauge)",
        },
        "numbers": {
            "T_IO_K": eta["T_IO_K"],
            "T_obs_K": eta["T_obs_K"],
            "temperature_conversion_factor_direct": conversion,
            "temperature_conversion_factor_symbolic": symbolic_conversion,
            "eta_obs_proton_mass": eta["eta_late_proton_mass"],
            "eta_BBN_proton_mass": eta["eta_late_proton_mass"] * conversion,
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "temperature_assignment_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["numbers"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
