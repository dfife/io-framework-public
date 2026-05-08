#!/usr/bin/env python3
"""
Recompute the R4/FIRAS readout arithmetic used in the Paper 20 v1.8 audit.

Paper 20 no longer treats the observed CMB temperature as an independent
prediction. Paper 17 v1.5 supplies the readout family

    T_obs(R4) = T_IO * x^(R4*K_gauge)

and FIRAS fixes R4 once. This script recomputes the old R4=1 factor and the
FIRAS-fixed factor so a reviewer can see the numerical change directly.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"


def main() -> None:
    constants = json.loads((DATA / "imported_constants.json").read_text(encoding="utf-8"))
    c = constants["framework_constants"]
    x = c["x"]
    k_gauge = c["K_gauge"]
    r4 = c["R4_FIRAS"]
    t_io = c["T_IO_K"]
    t_firas = c["T_FIRAS_K"]

    old_factor = x**k_gauge
    fixed_factor = x ** (r4 * k_gauge)
    print("Paper 20 R4/FIRAS readout audit")
    print(f"old R4=1 factor        = {old_factor:.15f}")
    print(f"FIRAS-fixed R4         = {r4:.13f}")
    print(f"FIRAS-fixed factor     = {fixed_factor:.15f}")
    print(f"T_IO * fixed factor    = {t_io * fixed_factor:.12f} K")
    print(f"FIRAS datum            = {t_firas:.12f} K")
    print("Counts as independent CMB prediction: False")


if __name__ == "__main__":
    main()
