#!/usr/bin/env python3
"""
Reproduce the Paper 20 v2.0 acoustic theorem arithmetic.

The load-bearing algebraic factor is

    J_theta = x^(-1/2) * sqrt(1 + gamma_BI^2)

The manuscript rounds the predicted acoustic angle to 0.599 degrees. The frozen
JSON also records the two exact rows behind the percent/sigma wording so a
reviewer can see the small reporting ambiguity explicitly.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "acoustic_theorems_results.json").read_text(encoding="utf-8"))
    t20_2 = data["theorems"]["20.2"]
    x = 1.51899
    gamma = 0.2375
    j_theta = x ** (-0.5) * math.sqrt(1.0 + gamma * gamma)

    print("Paper 20 v2.0 acoustic theorem check")
    print(f"J_theta recomputed = {j_theta:.16f}")
    print(f"J_theta frozen     = {t20_2['J_theta']:.16f}")
    print(f"theta* rounded manuscript value = {t20_2['theta_star_pred_deg_manuscript_rounded']} deg")
    for name, row in data["exact_rows"].items():
        print(f"{name}: theta={row['theta_obs_deg']:.15f} deg, residual={row['residual_percent']:.6f}%, sigma={row['sigma_offset']:.6f}")


if __name__ == "__main__":
    main()
