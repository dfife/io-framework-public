#!/usr/bin/env python3
"""Emit the public Paper 26 v2.0 kappa-audit summary.

The full audit is shipped in `reports/paper26_kappa_audit_report.md`. This
script makes its headline verdict machine-readable for validation and records
the R4/FIRAS boundary: the observed CMB temperature is not counted as an
independent IO prediction.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "kappa_audit_summary_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    result = {
        "paper": "Paper 26 v2.0",
        "audit": "kappa_style_field_redefinition",
        "hidden_continuous_parameter_found": False,
        "visible_conditionals": data["visible_conditionals"],
        "closed_conditional_verified": data["closed_conditional_verified"],
        "core_verdict": "no hidden continuous fitted parameter found; A_s remains conditional on C1+C2c, visibility remains conditional on AV1, and C3 is narrowed/closed by Theorem 26.C3 for the reduced centered Gaussian source-covariance class",
        "R4_FIRAS": data["framework_constants"]["R4_FIRAS"],
        "CMB_temperature_status": data["framework_constants"]["CMB_temperature_status"],
        "hygiene_finding": data["cmb_baryon_diagnostic"]["manuscript_hygiene_note"],
        "bridge_variable_hygiene": "Step 382 is aligned to the body theorem in the v2.0 draft, but Step 383 still carries older Levi-Civita-only language and should be reconciled with Theorem 26.2.",
        "must_not_say": [
            "Paper 26 proves all CMB inputs theorem-grade.",
            "Paper 26 independently predicts the observed CMB temperature.",
            "tau_eff_IO is identical to astrophysical tau_reio.",
            "high-l TT reionization-shape insensitivity closes low-l EE.",
            "Theorem 26.C3 closes arbitrary CMB transfer, ionization history, or low-l EE.",
            "the chi2=7714 row is the current bundled reproducible CLASS row without qualification."
        ]
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
