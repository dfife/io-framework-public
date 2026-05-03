#!/usr/bin/env python3
"""Paper 35 v1.1 script 05: baryogenesis registry summary.

Purpose:
    Summarize the 48 theorem-surface registry entries and preserve the
    distinction between CLEAN and CONDITIONAL_VERIFIED surfaces.

Inputs:
    data/theorem_registry.json

Outputs:
    results/baryogenesis_registry_summary_results.json

Claim boundary:
    Registry/audit support. Conditional surfaces are audit-trail and
    scope-tracking artifacts, not unconditional theorem closure.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"


def main() -> int:
    registry = json.loads((DATA / "theorem_registry.json").read_text())
    entries = registry["entries"]
    by_status = Counter(entry["status_label"] for entry in entries)
    by_category = Counter(entry["category"] for entry in entries)
    conditional = [
        {
            "sequence": entry["sequence"],
            "theorem_surface_name": entry["theorem_surface_name"],
            "admissions": entry["admitted_premises_external_classes_or_framework_slices"],
            "promotion_path_to_clean": entry["promotion_path_to_clean"],
            "audit_reference": entry["audit_reference"],
        }
        for entry in entries
        if entry["status_label"] == "CONDITIONAL_VERIFIED"
    ]

    payload = {
        "script": "05_baryogenesis_registry_summary.py",
        "status": "verified",
        "claim_boundary": "registry summary; conditional surfaces are not unconditional theorem closure",
        "summary": {
            "total": len(entries),
            "clean": by_status["CLEAN"],
            "conditional_verified": by_status["CONDITIONAL_VERIFIED"],
            "needs_review": by_status["NEEDS_REVIEW"],
            "circular": by_status["CIRCULAR"],
        },
        "by_category": dict(sorted(by_category.items())),
        "conditional_verified_entries": conditional,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "baryogenesis_registry_summary_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
