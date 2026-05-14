#!/usr/bin/env python3
"""Emit the public summary of the Paper 25 v2.0 kappa-style audit.

The full v2.0 audit report is in
`reports/paper25_v20_r4_kappa_audit_report.md`. This script produces a compact
JSON summary used by the one-command validator.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = BUNDLE_ROOT / "results" / "kappa_audit_summary_results.json"


def main() -> None:
    result = {
        "paper": "Paper 25 v2.0",
        "audit": "kappa_style_field_redefinition",
        "hidden_continuous_parameter_found": False,
        "visible_conditionals": ["H1", "H2", "H3"],
        "core_verdict": "survives audit with visible H1-H3 conditional verification and no unlabelled fitted scalar",
        "R4_FIRAS": 1.0031014644,
        "R4_damage_verdict": "No active Paper 25 script uses R4. Inherited appendix/master-reference CMB prediction wording is stale manuscript hygiene and should not be treated as active Paper 25 evidence.",
        "classifications": {
            "bilinearity_theorem": "DERIVED/THEOREM inside CCR/KMS package",
            "V_prime_exclusion": "DERIVED/THEOREM under centered two-time rate formulation",
            "V_double_prime_exclusion": "DERIVED/CONDITIONAL_VERIFIED on H1 via 25.12",
            "R_gamma_equals_1": "DERIVED/CONDITIONAL_VERIFIED on H1 and H2",
            "epsilon_w_Kgauge_L1": "DERIVED/CONDITIONAL_VERIFIED on H1-H3 plus upstream L_1",
            "bbn_scorecard": "VERIFIED computational support"
        },
        "label_drift_flags": [
            "Paper 25 v2.0 manuscript still contains CONDITIONAL/THEOREM and bare DERIVED status lines; these should migrate to canonical Claims Discipline labels before publication.",
            "Appendix master-reference entries still include retired independent CMB-temperature prediction wording and a Paper 17 R4 premise reference."
        ],
        "must_not_say": [
            "Paper 25 unconditionally proves weak-sector closure outside H1-H3.",
            "The BBN chi2 proves the theorem.",
            "Paper 25 independently predicts the CMB temperature.",
            "The V' branch is excluded only because its numerical chi2 is bad."
        ]
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
