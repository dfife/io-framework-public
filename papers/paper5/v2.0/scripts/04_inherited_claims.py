#!/usr/bin/env python3
"""Freeze the Paper 5 v2.0 inherited-claim ledger entries."""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]


def load_constants() -> dict:
    return json.loads((BUNDLE_ROOT / "data" / "imported_constants.json").read_text())


def main() -> None:
    constants = load_constants()
    inherited = constants["inherited_claims"]
    payload = {
        "status": "VERIFIED",
        "claim_boundary": (
            "These are dependency pointers for Paper 5 v2.0. Their theorem or "
            "conditional-verification status is owned by the cited source papers."
        ),
        "active_branch_constants_source": "Papers 10 and 29",
        "entries": [
            {
                "quantity": "first_peak_ell1",
                "value": inherited["paper12_first_peak_ell1"],
                "status": "DERIVED/CONDITIONAL_VERIFIED",
                "source": "Paper 12"
            },
            {
                "quantity": "theta_star_deg",
                "value": inherited["paper20_theta_star_deg"],
                "sigma_residual": inherited["paper20_theta_star_sigma_residual"],
                "status": "DERIVED/CONDITIONAL_VERIFIED",
                "source": "Paper 20 v2.0"
            },
            {
                "quantity": "light_element_scorecard_interpretation",
                "value": inherited["paper22_24_bbn_interpretation"],
                "status": "DERIVED/CONDITIONAL_VERIFIED",
                "source": "Papers 22 and 24"
            }
        ]
    }
    out = BUNDLE_ROOT / "results" / "inherited_claims_results.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()
