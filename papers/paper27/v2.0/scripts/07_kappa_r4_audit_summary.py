#!/usr/bin/env python3
"""Generate the Paper 27 v2.0 R4 and kappa-audit summary.

The script makes the audit boundary machine-readable.  It does not scan the
manuscript dynamically; the textual audit in reports/paper27_kappa_audit_report.md
contains the forensic walk-through.  This JSON gives validators the key
disposition of R4, retired CMB-temperature scripts, hidden-parameter checks,
label drift, abbreviations, and IO-internal terminology.
"""

from __future__ import annotations

from _common import load_constants, write_result


def compute() -> dict:
    constants = load_constants()["framework_constants"]
    return {
        "paper": 27,
        "version": "v2.0",
        "audit_target": "Paper 27 v2.0 kappa/R4 audit",
        "status": "VERIFIED",
        "R4_FIRAS": constants["R4_FIRAS"]["value"],
        "active_R4_use_in_bundle_scripts": False,
        "active_R4_equals_one_found": False,
        "active_independent_CMB_temperature_prediction": False,
        "retired_scripts_excluded_for_CMB_temperature_dependency": [
            "paper27_full_io_native_planck_tt_confrontation.py",
            "paper27_io_geometry_floor_scan.py",
            "paper27_theta_s_constrained_geometry_floor_scan.py",
            "paper27_baryon_diagnostics.py",
            "paper27_c3_candidate_discriminator_scan.py",
            "paper27_trgb_jwst_scope.py"
        ],
        "hidden_fitted_parameter_found": False,
        "open_premise_gaps_preserved": [
            "full h_vec state selection",
            "AV1 beyond visibility-slot inheritance"
        ],
        "noncanonical_active_labels_found": False,
        "historical_label_language_flagged": [
            "DERIVED/SCOPED in older version-history text",
            "SEMICLASSICAL PRINCIPLE in older version-history text",
            "KILLED or dead-route language in archive-style material"
        ],
        "abbreviation_and_slang_review_required": True,
        "recommendation": "Keep retired CMB-temperature scripts out of the v2.0 bundle and define or replace IO-internal abbreviations in manuscript-facing text.",
    }


if __name__ == "__main__":
    write_result("kappa_r4_audit_summary_results.json", compute())
