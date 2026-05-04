#!/usr/bin/env python3
"""Paper 21 v1.7 reproducibility script 04.

Purpose:
    Record and validate the Paper 21 PRyMordial wrapper convention: helium is
    read as YPCMB / PRyMresults()[3], while YPBBN / PRyMresults()[4] is retained
    only as an audit field.

Manuscript role:
    Supports the v1.5/v1.6 wrapper-correction scorecard and the v1.7 Code and
    Data Availability update.

Inputs:
    data/imported_constants.json.

Outputs:
    results/prymordial_wrapper_conventions_results.json

External dependencies:
    Python standard library only. PRyMordial itself is a separate external
    repository and is not redistributed in this bundle.

Claim boundary:
    This script validates the wrapper convention and observational denominators;
    it does not rerun the PRyMordial ODE network.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "prymordial_wrapper_conventions_results.json"


def main() -> int:
    constants = json.loads(DATA.read_text())
    score = constants["paper21_corrected_scorecard"]
    obs = constants["observational_conventions"]
    payload = {
        "claim": "Paper 21 corrected PRyMordial wrapper convention",
        "status": "verified / wrapper convention",
        "helium_observational_output": {
            "component": "YPCMB",
            "PRyMresults_index": 3,
            "value": score["Y_p"]
        },
        "helium_audit_only_output": {
            "component": "YPBBN",
            "PRyMresults_index": 4,
            "value": score["Y_p_BBN_audit_only"],
            "use": "audit only; not compared to observational Y_p compilations"
        },
        "observational_denominators": obs,
        "external_dependency": {
            "PRyMordial": "not redistributed; this public bundle validates the wrapper convention and frozen outputs"
        },
        "claim_boundary": "Wrapper-convention artifact, not a new BBN network implementation."
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "output": str(OUT), "helium_index": 3}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
