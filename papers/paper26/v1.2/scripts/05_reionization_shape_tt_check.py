#!/usr/bin/env python3
"""Emit the Paper 26 reionization-shape high-l TT diagnostic.

The public bundle freezes the audited CLASS result: changing the reionization
shape has negligible impact on high-l TT for the tested branch, but this does
not close low-l EE polarization.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "reionization_shape_tt_check_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    reio = data["reionization_shape"]

    result = {
        "paper": "Paper 26 v1.2",
        "baseline_reio_camb_chi2_TT_highl": reio["baseline_reio_camb_chi2_TT_highl"],
        "max_shape_shift_case": reio["max_shape_sweep_case"],
        "max_shape_shift_chi2_TT_highl": reio["max_shape_shift_chi2_TT_highl"],
        "max_delta_chi2_TT_highl": reio["max_delta_chi2_TT_highl"],
        "passes_less_than_0p4_claim": reio["max_delta_chi2_TT_highl"] < 0.4,
        "low_ell_EE_caveat": reio["low_ell_EE_caveat"],
        "status": "VERIFIED computational diagnostic for high-l TT only"
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
