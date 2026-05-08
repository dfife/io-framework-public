#!/usr/bin/env python3
"""
Reproduce the Paper 20 acoustic phase-calibration arithmetic from frozen output.

This script is intentionally lightweight. The heavyweight CLASS computation that
produced `acoustic_phase_precision_results.json` is not rerun here because it
requires a local CLASS installation and cosmology data plumbing. Instead, this
script verifies the load-bearing algebraic factor

    J_theta = x^(-1/2) * sqrt(1 + gamma_BI^2)

and prints the frozen acoustic precision cases used for the Paper 20 audit.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "acoustic_phase_precision_results.json").read_text(encoding="utf-8"))
    inputs = data["inputs"]
    x = 1.51899
    gamma = 0.2375
    j_theta = x ** (-0.5) * math.sqrt(1.0 + gamma * gamma)

    print("Paper 20 acoustic phase-calibration check")
    print(f"J_theta recomputed = {j_theta:.15f}")
    print(f"J_theta frozen     = {inputs['J_theta_derived']:.15f}")
    for name, row in data["cases"].items():
        print(
            f"{name}: theta_obs={row['theta_obs_deg']:.12f} deg, "
            f"sigma={row['sigma_offset']:.6f}, z_star={row['z_star']:.6f}"
        )


if __name__ == "__main__":
    main()
