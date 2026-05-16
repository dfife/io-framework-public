#!/usr/bin/env python3
"""Reproduce the Paper 26 v2.0 CMB baryon-class diagnostic ledger.

Paper 26 distinguishes three upstream baryon values and tests whether the
late-time clustering value is authorized in CMB perturbation slots. The public
script does not rerun CLASS or distribute Planck likelihood data. It emits the
frozen audited CLASS diagnostic rows and their deltas so reviewers can check
the manuscript's numerical support surface without needing restricted external
data.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "cmb_baryon_class_diagnostic_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    c = data["framework_constants"]
    diag = data["cmb_baryon_diagnostic"]

    result = {
        "paper": "Paper 26 v2.0",
        "baryon_values": {
            "omega_b_geom": c["omega_b_geom"],
            "omega_b_eff": c["omega_b_eff"],
            "omega_b_clustering": c["omega_b_clustering"]
        },
        "diagnostic_rows": {
            "onefluid_eff": {
                "chi2_TT_highl": diag["onefluid_eff_chi2_TT_highl"],
                "100theta_s": diag["onefluid_eff_100theta_s"]
            },
            "typed_native_geomchem_effacoustic": {
                "chi2_TT_highl": diag["typed_native_chi2_TT_highl"],
                "100theta_s": diag["typed_native_100theta_s"],
                "delta_chi2_TT_highl_vs_onefluid": diag["typed_native_delta_chi2_TT_highl"]
            }
        },
        "legacy_text_note": {
            "manuscript_v1_1_legacy_clustering_claim": diag["manuscript_v1_1_legacy_clustering_claim"],
            "hygiene_note": diag["manuscript_hygiene_note"]
        },
        "claim_boundary": "The no-authorization statement is theorem-backed; chi-square values are verified CLASS diagnostics.",
        "conditionals": diag["conditionals"]
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
