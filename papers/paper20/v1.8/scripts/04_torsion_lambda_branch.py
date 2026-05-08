#!/usr/bin/env python3
"""
Summarize the Paper 20 torsion-Lambda bare branch from frozen output.

This branch is algebraically specified from M_U, Oppenheimer-Snyder geometry,
Paper 1's torsion Lambda, and imported standard-model radiation. The v1.8 audit
classifies the arithmetic as theorem-grade once those inputs are granted, but
the branch-selection/observational adequacy status remains an open premise gap.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "torsion_lambda_branch_results.json").read_text(encoding="utf-8"))
    branch = data["branch"]
    firas = data["scorecard_direct"]["firas"]
    print("Paper 20 torsion-Lambda branch")
    print(f"H0_bare = {branch['H0_bare']:.12f} km/s/Mpc")
    print(f"H0_obs  = {branch['H0_obs']:.12f} km/s/Mpc")
    print(f"Omega_m = {branch['Omega_m']:.12f}")
    print(f"Omega_k = {branch['Omega_k']:.12f}")
    print(f"Omega_Lambda = {branch['Omega_lambda']:.12f}")
    print(f"age_obs = {branch['age_obs_Gyr']:.12f} Gyr")
    print(f"temperature status = {firas['status']}")


if __name__ == "__main__":
    main()
