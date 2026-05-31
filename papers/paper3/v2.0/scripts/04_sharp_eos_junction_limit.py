#!/usr/bin/env python3
"""Paper 3 v2.0 script 04: sharp-EOS junction limit.

Purpose:
    Record the limiting Israel-Darmois/Raychaudhuri arithmetic for the
    continuous mixed-fluid Paper 5 interior.

Inputs:
    data/imported_constants.json

Outputs:
    results/sharp_eos_junction_limit_results.json

Claim boundary:
    This is a limiting theorem for the sharp equation-of-state transition. The
    active physical early-time model is the continuous mixed-fluid interior.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "sharp_eos_junction_limit_results.json"


def main() -> None:
    payload = json.loads(DATA.read_text())
    w_radiation = 1.0 / 3.0
    w_dust = 0.0
    acceleration_ratio = (1.0 + 3.0 * w_radiation) / (1.0 + 3.0 * w_dust)

    result = {
        "status": "DERIVED/CONDITIONAL_VERIFIED",
        "verdict": "SURVIVES as a sharp-EOS limiting statement of the Paper 5 continuous mixed-fluid interior",
        "claim_boundary": "The old discrete Vaidya-to-OS phase is not the active physical model. The clean Israel-Darmois statement survives only as the sharp-transition limit.",
        "matching_conditions": {
            "metric_continuity": "continuous induced metric follows from continuous scale factor a",
            "extrinsic_curvature_continuity": "continuous extrinsic curvature follows from continuous first derivative adot, not from continuous acceleration addot",
            "surface_layer": "no surface layer in the limiting statement when a and adot are continuous"
        },
        "raychaudhuri_limit": {
            "equation": "addot/a = -(4 pi G/3) rho (1 + 3w)",
            "w_radiation": w_radiation,
            "w_dust": w_dust,
            "fixed_quantities": ["a", "rho"],
            "acceleration_magnitude_ratio_radiation_to_dust": acceleration_ratio
        },
        "p1_p2_chain": payload["p1_p2_chain"]
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
