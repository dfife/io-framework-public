#!/usr/bin/env python3
"""
Print Theorems 20.RAD1, 20.RAD2, and 20.RAD3 from frozen output.

These are the live v2.0 radiation-algebra surfaces: one admissible construction,
one consistency construction, and one bulk-vacuum no-go.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "radiation_algebra_theorems_results.json").read_text(encoding="utf-8"))
    print("Paper 20 v2.0 radiation algebra theorem summary")
    for key, row in data["theorems"].items():
        print(f"{key}: {row['name']} [{row['status']}]")
        print(f"  boundary: {row['boundary']}")
    print(f"rho_fermion/rho_gamma pre-decoupling = {data['theorems']['20.RAD2']['rho_fermion_over_rho_gamma_pre_decoupling']}")
    print(f"bulk-vacuum w = {data['theorems']['20.RAD3']['w_vacuum']}")


if __name__ == "__main__":
    main()
