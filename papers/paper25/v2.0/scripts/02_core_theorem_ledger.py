#!/usr/bin/env python3
"""Emit the Paper 25 v2.0 live theorem and premise ledger.

The manuscript contains many historical dead routes. The public bundle keeps a
compact ledger of the live theorem-support surface: H1-H3, the central
Theorems 25.1-25.13, the channel-budget equation, the weak-observable-class
geometric-mediation closure, and the 29 killed-route count. This script does
not prove those theorems; it makes the status labels and conditional
dependencies machine-readable for review using the canonical public Claims
Discipline labels.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "core_theorem_ledger_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    premises = data["premises"]

    theorem_ledger = [
        {"id": "25.1", "name": "Centrality Neutralization", "status": "DERIVED/THEOREM"},
        {"id": "25.2", "name": "Scalarization Preserves V-Type", "status": "DERIVED/CONDITIONAL_VERIFIED"},
        {"id": "25.3", "name": "K_geom is gamma-independent", "status": "DERIVED/THEOREM"},
        {"id": "25.4", "name": "j=1 transport is gamma-blind", "status": "DERIVED/THEOREM"},
        {"id": "25.5", "name": "Reaction and CAR legs gauge-trivial", "status": "DERIVED"},
        {"id": "25.6", "name": "gamma-localization to Z_g", "status": "DERIVED/THEOREM"},
        {"id": "25.7", "name": "TT multiplicity factor 10", "status": "DERIVED/THEOREM"},
        {"id": "25.8", "name": "Channel-carrier localization", "status": "DERIVED/THEOREM"},
        {"id": "25.9", "name": "Bilinearity of the Bridge Correlator", "status": "DERIVED/THEOREM"},
        {"id": "25.10", "name": "Structural Exclusion of V'", "status": "DERIVED/THEOREM"},
        {"id": "25.11", "name": "Structural Exclusion of V''", "status": "DERIVED/CONDITIONAL_VERIFIED on H1 via 25.12"},
        {"id": "25.12", "name": "R(gamma)=1 on constructed extension", "status": "DERIVED/CONDITIONAL_VERIFIED on H1 and H2"},
        {"id": "25.13", "name": "Geometric-Mediation Closure for the Weak Observable Class", "status": "DERIVED/CONDITIONAL_VERIFIED on H1-H3"}
    ]

    result = {
        "paper": "Paper 25 v2.0",
        "premises": premises,
        "theorems": theorem_ledger,
        "channel_budget_equation": {
            "formula": "epsilon_w/L_1 + K_geom = 10*epsilon_n/L_2 = <K>",
            "status": "DERIVED/CONDITIONAL_VERIFIED on channel-to-payload assignment; weak modular readout resolved by Paper 25 inside H1-H3"
        },
        "closed_open_problem": {
            "id": "WMR",
            "statement": "weak rate reads V = K_gauge, not V'",
            "status": "closed inside H1-H3 as DERIVED/CONDITIONAL_VERIFIED"
        },
        "killed_route_count": 29,
        "claim_boundary": "This ledger preserves labels; it does not upgrade conditional results to unconditional theorems."
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
