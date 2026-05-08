#!/usr/bin/env python3
"""
Summarize the Paper 20 v1.8 kappa-style hidden-parameter audit.

The audit replaces each load-bearing scalar or structural assignment by a free
field and asks whether the value is forced, imported, reconstructed, fitted, or
an open premise gap. This script prints the machine-readable audit verdict.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "kappa_audit_results.json").read_text(encoding="utf-8"))
    print("Paper 20 v1.8 kappa audit")
    print(f"hidden continuous parameter found: {data['hidden_continuous_parameter_found']}")
    print(f"independent CMB-temperature prediction retired: {data['independent_cmb_temperature_prediction_retired']}")
    for row in data["candidate_fields"]:
        print(f"{row['field']}: {row['classification']}")


if __name__ == "__main__":
    main()
