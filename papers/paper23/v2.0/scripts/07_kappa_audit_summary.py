#!/usr/bin/env python3
"""Emit the machine-readable Paper 23 v2.0 kappa-audit summary.

The full prose audit is in `reports/paper23_v20_r4_kappa_audit_report.md`.
This script freezes the audit verdict and the manuscript hygiene findings so
the validator can check them alongside the numerical theorem-support outputs.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results" / "kappa_audit_summary_results.json"


def main() -> int:
    results = {
        "paper": "Paper 23",
        "version": "v2.0",
        "verdict": {
            "hidden_continuous_fitted_parameter_found": False,
            "r4_enters_active_spectral_index": False,
            "cmb_temperature_prediction_wording_present_in_draft": True,
            "stale_paper22_values_present_in_draft": True,
            "label_migration_required": True,
        },
        "open_or_conditional_surfaces": [
            {
                "surface": "Primordial Scalar Readout Principle",
                "recommended_label": "OPEN/PREMISE_GAP",
                "promotion_path": "Provide explicit chain to Premise 1, Premise 2, or frozen imported physics.",
            },
            {
                "surface": "Boundary Covariance Exponent",
                "recommended_label": "OPEN/PREMISE_GAP",
                "promotion_path": "Provide explicit chain to Premise 1, Premise 2, or frozen imported physics.",
            },
            {
                "surface": "spatial canonical-commutation-relation lift",
                "recommended_label": "OPEN/PREMISE_GAP",
                "promotion_path": "Provide explicit chain to Premise 1, Premise 2, or frozen imported physics.",
            },
            {
                "surface": "tensor gamma-neutrality / n_t = 0",
                "recommended_label": "OPEN/PREMISE_GAP",
                "promotion_path": "Supply gamma-neutral tensor readout theorem or cite later closure.",
            },
        ],
        "noncanonical_labels_to_migrate": [
            "CONDITIONAL/THEOREM",
            "CONDITIONAL",
            "DERIVED/VERIFIED",
            "unqualified DERIVED where a canonical status is required",
        ],
        "abbreviations_to_expand": [
            "IO",
            "OS",
            "FRW",
            "CMB",
            "BBN",
            "LQG",
            "CCR",
            "KMS",
            "TT",
            "AQFT",
            "PSRP",
            "FIRAS",
            "GTTP",
            "GMP",
            "TBS",
            "WMR",
            "PRyMordial",
            "YPCMB",
            "YPBBN",
            "SU(2)",
            "SO(4)",
            "U(1)",
            "n_s",
            "n_t",
            "A_s",
        ],
        "io_slang_to_define_or_replace": [
            "bridge",
            "one-slot",
            "two-slot",
            "rung",
            "payload",
            "degree wall",
            "no-doubling",
            "live/open stack",
            "theorem-grade",
            "killed route",
            "readout",
            "Paper stack",
            "white baseline",
            "horizon puncture load",
            "spatial Hodge complex",
            "rate-dressing",
        ],
        "checks": {
            "hidden_continuous_parameter_found": False,
            "r4_active_dependency": False,
            "PSRP_visible_as_open": True,
            "boundary_covariance_visible_as_open": True,
            "CCR_lift_visible_as_open": True,
        },
    }

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

