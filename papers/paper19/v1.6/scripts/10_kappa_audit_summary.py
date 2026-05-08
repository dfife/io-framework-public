#!/usr/bin/env python3
"""
Generate a machine-readable summary of the Paper 19 v1.6 kappa audit.

This script preserves the audit verdict in a compact JSON file for validators
and reviewers. The full reasoning is in
``reports/paper19_v16_r4_kappa_audit_report.md``.

Output:
    ../results/kappa_audit_summary_results.json
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT = BUNDLE_ROOT / "results" / "kappa_audit_summary_results.json"


def main() -> None:
    payload = {
        "paper": "Paper 19",
        "version": "v1.6",
        "hidden_continuous_parameter_found_in_baryon_scalarization": False,
        "r4_status": "IMPORTED/EMPIRICAL FIRAS-fixed readout normalization inherited from Paper 17 v1.5",
        "cmb_prediction_status": "retired",
        "alpha_3_over_2_status": "DERIVED/CONDITIONAL_VERIFIED if v1.6 states the proper-time comoving-dust metric-measure premise chain",
        "age_closed_N_mode_status": "OPEN/PREMISE_GAP unless theorem-fixed elsewhere",
        "noncanonical_labels_found": True,
        "abbreviation_slang_flags_found": True,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
