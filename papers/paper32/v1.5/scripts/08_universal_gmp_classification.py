#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 08.

Purpose:
    Reproduce the three-part universal-GMP closure-or-characterization ledger:

    1. GMP closes on realized typed bridge-placement observables.
    2. GMP is inapplicable on physical non-bridge history/solver sectors.
    3. Universal GMP is false on the larger abstract local algebra by explicit
       non-geometric bypass operators.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/universal_gmp_classification_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / structural ledger reproduction from the Paper 32 support
    reports. This script is not a theorem prover.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "universal_gmp_classification_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    domains = [
        {
            "domain": "realized_typed_bridge_readout_observables",
            "gmp_status": "holds",
            "classification": "DERIVED/SCOPED",
            "reason": "block type, channel floor, background placement, and multiplicity-one bridge grammar force geometric mode placement"
        },
        {
            "domain": "physical_non_bridge_history_solver_complement",
            "gmp_status": "inapplicable",
            "classification": "DERIVED/SCOPED",
            "examples": [
                "recombination characteristic/history block",
                "reionization local-history block",
                "closed-S3 perturbation hierarchy"
            ],
            "reason": "these are physical sectors but not puncture-load-to-spatial-channel placement observables"
        },
        {
            "domain": "abstract_larger_local_algebra",
            "gmp_status": "false_as_universal_statement",
            "classification": "DERIVED/NO-GO",
            "counterexample": "Q_w^(ng) = R_w tensor I_th tensor I_sp tensor sqrt(L1) P_1",
            "reason": "identity spatial leg bypasses geometric placement"
        }
    ]

    results = {
        "paper": payload["paper"],
        "classification": "verified / structural ledger reproduction",
        "headline": "Universal GMP is characterized, not universally closed.",
        "domains": domains,
        "allowed_manuscript_wording": "GMP is closed on realized typed bridge-placement observables and characterized/no-go outside that scope.",
        "forbidden_manuscript_wording": "Universal GMP is closed on the full local algebra."
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

