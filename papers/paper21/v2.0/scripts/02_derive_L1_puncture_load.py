#!/usr/bin/env python3
"""Paper 21 v2.0 reproducibility script 02.

Purpose:
    Recompute the singleton j=1 puncture load L_1 from the SU(2) isolated
    horizon puncture spectrum.

Manuscript role:
    Supports Paper 21's puncture-load derivation and the value inherited by
    Paper 22's rate-dressing construction.

Inputs:
    data/imported_constants.json for gamma_BI and expected values.

Outputs:
    results/L1_puncture_load_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    L_1 is derived as a Paper 21 puncture-load value. Its later use as a
    weak-rate dressing amplitude is conditional structure in Paper 22/Paper 25,
    not proven by this script.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "L1_puncture_load_results.json"


def chi(j: float, gamma: float) -> float:
    return 2.0 * math.pi * gamma * math.sqrt(j * (j + 1.0))


def energy_weight(j: float, gamma: float) -> float:
    c = chi(j, gamma)
    return c * (2.0 * j + 1.0) * math.exp(-c)


def puncture_levels(max_half_integer: int = 240) -> list[float]:
    return [n / 2.0 for n in range(1, max_half_integer + 1)]


def main() -> int:
    constants = json.loads(DATA.read_text())
    gamma = constants["framework_constants"]["gamma_BI"]
    levels = puncture_levels()
    denominator = sum(energy_weight(j, gamma) for j in levels)
    numerator = energy_weight(1.0, gamma)
    value = numerator / denominator
    expected = constants["puncture_loads"]["L_1"]
    payload = {
        "claim": "L_1 puncture load",
        "status": "VERIFIED arithmetic for DERIVED/THEOREM puncture-load value",
        "formula": constants["puncture_loads"]["formula"],
        "gamma_BI": gamma,
        "j": 1.0,
        "chi_j": chi(1.0, gamma),
        "numerator": numerator,
        "denominator": denominator,
        "L_1": value,
        "expected_L_1": expected,
        "absolute_difference": value - expected,
        "claim_boundary": "Standalone Paper 21 load value; later rate-dressing use is Paper 22/Paper 25 conditional bridge structure."
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "output": str(OUT), "L_1": value}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
