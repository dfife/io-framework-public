#!/usr/bin/env python3
"""
Recompute the R4/FIRAS readout arithmetic inherited by Paper 20 v2.0.

Paper 20 v2.0 does not treat the observed cosmic microwave background
temperature as an independent prediction. Paper 17 v1.5 supplies the readout
family

    T_obs(R4) = T_IO * x^(R4*K_gauge)

and FIRAS fixes R4 once. This script prints the frozen values and recomputes
the two readout factors from the included constants.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "r4_firas_readout_results.json").read_text(encoding="utf-8"))
    inputs = data["inputs"]
    x = inputs["x"]
    k_gauge = inputs["K_gauge"]
    r4 = inputs["R4_FIRAS"]
    t_io = inputs["T_IO_K"]

    old_factor = x**k_gauge
    fixed_factor = x ** (r4 * k_gauge)

    print("Paper 20 v2.0 R4/FIRAS readout audit")
    print(f"old R4=1 factor     = {old_factor:.15f}")
    print(f"fixed R4 factor     = {fixed_factor:.15f}")
    print(f"T_IO * fixed factor = {t_io * fixed_factor:.12f} K")
    print(f"counts as independent CMB-temperature prediction = {data['status']['independent_cmb_temperature_prediction']}")


if __name__ == "__main__":
    main()
