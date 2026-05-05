#!/usr/bin/env python3
"""Emit the public summary of the Paper 25 kappa-style audit.

The full audit report is in `reports/paper25_kappa_audit_report.md`. This
script produces a compact JSON summary used by the one-command validator.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = BUNDLE_ROOT / "results" / "kappa_audit_summary_results.json"


def main() -> None:
    result = {
        "paper": "Paper 25 v1.3",
        "audit": "kappa_style_field_redefinition",
        "hidden_continuous_parameter_found": False,
        "visible_conditionals": ["H1", "H2", "H3"],
        "core_verdict": "survives audit with visible conditional premises and no unlabelled fitted scalar",
        "classifications": {
            "bilinearity_theorem": "DERIVED/THEOREM inside CCR/KMS package",
            "V_prime_exclusion": "DERIVED/THEOREM under centered two-time rate formulation",
            "V_double_prime_exclusion": "CONDITIONAL/THEOREM on H1",
            "R_gamma_equals_1": "DERIVED on constructed extension; CONDITIONAL on H1",
            "epsilon_w_Kgauge_L1": "DERIVED/CONDITIONAL on H1-H3 plus upstream L_1",
            "bbn_scorecard": "VERIFIED computational support"
        },
        "must_not_say": [
            "Paper 25 unconditionally proves weak-sector closure outside H1-H3.",
            "The BBN chi2 proves the theorem.",
            "The private kinetic-runner Li-7 row is the active Paper 25 lithium scorecard.",
            "The V' branch is excluded only because its numerical chi2 is bad."
        ]
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
