#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 04.

Purpose:
    Reproduce the Paper 32 late-time hidden-support timescales:

        Delta tau_clamp_to_crunch = pi r_s / (2c) ~= 111 Gyr
        Delta tau_cycle = 2 * Delta tau_clamp_to_crunch ~= 222 Gyr.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/recollapse_cycle_timescales_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / arithmetic reproduction. The one-way recollapse time is derived
    on the local support IVP. The full cycle is conditional on symmetric
    Paper 1/Poplawski bounce attachment.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "recollapse_cycle_timescales_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    c = payload["physical_constants"]["c_m_s"]
    gyr_s = payload["physical_constants"]["gyr_s"]
    r_s = payload["framework_constants"]["r_s_harmonized_m"]
    R_bounce = payload["late_time_inputs"]["R_bounce_m"]

    clamp_to_crunch_s = math.pi * r_s / (2.0 * c)
    clamp_to_crunch_gyr = clamp_to_crunch_s / gyr_s
    cycle_gyr = 2.0 * clamp_to_crunch_gyr

    # Near R=0, remaining OS time scales as (2/3c) R^(3/2)/sqrt(r_s).
    bounce_to_zero_s = (2.0 / (3.0 * c)) * (R_bounce ** 1.5) / math.sqrt(r_s)

    milestones = []
    for fraction in [0.5, 0.25, 0.10, 0.01]:
        theta = math.acos(2.0 * fraction - 1.0)
        tau_gyr = (r_s / (2.0 * c)) * (theta + math.sin(theta)) / gyr_s
        milestones.append({"R_over_r_s": fraction, "Delta_tau_Gyr": tau_gyr})

    results = {
        "paper": payload["paper"],
        "classification": "verified / arithmetic reproduction",
        "equations": {
            "R_theta": "R(theta) = (r_s/2)(1 + cos(theta))",
            "tau_theta": "Delta tau(theta) = (r_s/2c)(theta + sin(theta))",
            "crunch_time": "Delta tau(pi) = pi r_s/(2c)",
            "cycle_time": "2*pi r_s/(2c), conditional on symmetric bounce attachment"
        },
        "inputs": {
            "c_m_s": c,
            "r_s_m": r_s,
            "R_bounce_m": R_bounce
        },
        "results": {
            "clamp_to_crunch_s": clamp_to_crunch_s,
            "clamp_to_crunch_Gyr": clamp_to_crunch_gyr,
            "cycle_Gyr": cycle_gyr,
            "R_bounce_over_r_s": R_bounce / r_s,
            "bounce_to_zero_remaining_s": bounce_to_zero_s
        },
        "milestones": milestones,
        "conditional_dependencies": [
            "Paper 1/Poplawski torsion bounce attachment on the collapsing branch",
            "time-reversal symmetric re-expansion branch for the local cycle"
        ]
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

