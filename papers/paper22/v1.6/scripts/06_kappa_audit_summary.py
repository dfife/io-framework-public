#!/usr/bin/env python3
"""Emit a machine-readable summary of the Paper 22 kappa-style audit.

The full audit report is shipped under reports/. This script creates a compact
JSON digest for validation tooling and for readers who want to inspect the
field-redefinition verdict without parsing the whole report.

Run from the bundle root:

    python3 scripts/06_kappa_audit_summary.py

Output:

    results/kappa_audit_summary_results.json
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = BUNDLE_ROOT / "results" / "kappa_audit_summary_results.json"


def main() -> None:
    result = {
        "script": Path(__file__).name,
        "audit": "Paper 22 v1.6 paper-level kappa-style structural audit",
        "verdict": "no unlabelled continuous fitted kappa parameter found",
        "not_upgraded": "The audit does not upgrade Theorem 22.23 or 22.25 to unconditional theorem status.",
        "visible_conditional_fields": [
            {
                "field": "GMP",
                "classification": "NEW PREMISE / CONDITIONAL",
                "promotion_path": "equivariant bridge uniqueness theorem"
            },
            {
                "field": "TBS / TT modular budget saturation",
                "classification": "PREMISE / CONDITIONAL",
                "promotion_path": "modular intertwining theorem, modular Gauss law, or modular-energy transport theorem"
            },
            {
                "field": "WMR(H1-H3)",
                "classification": "DERIVED/CONDITIONAL on H1-H3",
                "promotion_path": "physical selection of the Paper 25 two-time KMS/CCR bridge observable"
            },
            {
                "field": "rate-dressing orientation sign",
                "classification": "DISCRETE ORIENTATION CONVENTION",
                "promotion_path": "explicit positivity/suppression orientation theorem"
            }
        ],
        "derived_core": [
            "round-S3 Hodge spectrum",
            "Peter-Weyl bridge",
            "TT branch multiplicities",
            "Channel Floor Theorem J_min=s",
            "homogeneous gauge placement in coexact vector channel",
            "stress scalarization and injection no-gos",
            "TT linear volume no-go",
            "compact-support theta suppression bound"
        ],
        "conditional_core": [
            "zero-parameter amplitude construction",
            "Li-7 out-of-sample consistency inherited from Theorem 22.23",
            "formal bridge operator P_resp^(bridge)"
        ],
        "claim_boundary": [
            "Do not say Paper 22 unconditionally derives K_gauge * L1.",
            "Do not say Paper 22 unconditionally derives (K_mean/10) * L2.",
            "Do not say the BBN scorecard proves TBS.",
            "Do not cite the old YPBBN scorecard as active.",
            "Do not present F_abs as an active expansion-rate energy-density correction."
        ],
        "reports": [
            "reports/paper22_kappa_audit_report.md",
            "reports/paper22_kappa_audit_results.json",
            "reports/paper22_theorem_22_23_kappa_audit_report.md",
            "reports/paper22_theorem_22_23_kappa_audit_results.json"
        ],
        "checks": {
            "hidden_continuous_parameter_found": False,
            "GMP_visible": True,
            "TBS_visible": True,
            "WMR_H1_H3_visible": True
        }
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
