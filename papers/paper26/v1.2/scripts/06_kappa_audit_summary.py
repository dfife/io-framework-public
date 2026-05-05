#!/usr/bin/env python3
"""Emit the public Paper 26 kappa-audit summary.

The full audit is shipped in `reports/paper26_kappa_audit_report.md`. This
script makes its headline verdict machine-readable for validation.
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
        "paper": "Paper 26 v1.2",
        "audit": "kappa_style_field_redefinition",
        "hidden_continuous_parameter_found": False,
        "visible_conditionals": data["visible_conditionals"],
        "core_verdict": "no hidden continuous fitted parameter found; headline values remain conditional on C1, C2c, AV1, and C3",
        "hygiene_finding": data["cmb_baryon_diagnostic"]["manuscript_hygiene_note"],
        "bridge_variable_hygiene": "Active body text uses gamma delta K bridge with delta Gamma killed; inherited step text contains older delta Gamma phrasing and should be clarified in v1.2.",
        "must_not_say": [
            "Paper 26 proves all CMB inputs theorem-grade.",
            "tau_eff_IO is identical to astrophysical tau_reio.",
            "high-l TT reionization-shape insensitivity closes low-l EE.",
            "the v1.1 legacy chi2=7714 row is the current bundled reproducible CLASS row without qualification."
        ]
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
