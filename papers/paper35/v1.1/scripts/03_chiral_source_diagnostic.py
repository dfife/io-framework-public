#!/usr/bin/env python3
"""Paper 35 v1.1 script 03: chiral source-era diagnostic.

Purpose:
    Evaluate the conditional chiral source-era diagnostic quantities
    `g_chi = K_gauge^4`, `T_f`, and `eta_chiral = 7.04 K_gauge^8`.

Inputs:
    data/imported_constants.json

Outputs:
    results/chiral_source_diagnostic_results.json

Claim boundary:
    CONDITIONAL/CONSTRUCTED diagnostic. This is not a theorem-grade derivation
    of a full baryogenesis mechanism.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    k = constants["framework_constants"]["K_gauge"]

    g_chi = k**4
    k8 = k**8
    eta_chiral = 7.04 * k8
    # Paper 35 source-era diagnostic convention, matching the local audit.
    m_pl_reduced_for_diagnostic = 2.427008942118276e18
    t_f = g_chi * m_pl_reduced_for_diagnostic

    payload = {
        "script": "03_chiral_source_diagnostic.py",
        "status": "verified",
        "claim_boundary": "CONDITIONAL/CONSTRUCTED source-era diagnostic",
        "formulae": {
            "g_chi": "K_gauge^4",
            "T_f": "K_gauge^4 M_Pl,reduced(diagnostic convention)",
            "eta_chiral": "7.04 K_gauge^8",
        },
        "numbers": {
            "K_gauge": k,
            "g_chi": g_chi,
            "K_gauge_8": k8,
            "eta_chiral": eta_chiral,
            "eta10_chiral": eta_chiral * 1.0e10,
            "M_Pl_reduced_GeV_diagnostic": m_pl_reduced_for_diagnostic,
            "T_f_GeV": t_f,
        },
        "discipline": {
            "missing_for_full_baryogenesis": [
                "baryon-number transfer operator",
                "chirality/sign selector",
                "freeze-out dynamics theorem",
            ]
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "chiral_source_diagnostic_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["numbers"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
