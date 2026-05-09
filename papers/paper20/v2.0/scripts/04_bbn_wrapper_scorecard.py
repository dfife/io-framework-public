#!/usr/bin/env python3
"""
Print the corrected Paper 20 v2.0 Big Bang nucleosynthesis comparison row.

The public bundle does not redistribute PRyMordial. This frozen row records the
already-audited wrapper correction: helium is read from YPCMB / PRyMresults()[3],
not YPBBN / index 4, and amplitudes are aligned to Paper 22 v1.5/v1.6.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "bbn_wrapper_scorecard_results.json").read_text(encoding="utf-8"))
    row = data["scorecard"]
    print("Paper 20 v2.0 corrected BBN comparison row")
    print(f"D/H      = {row['D_over_H']:.15e} ({row['D_over_H_sigma']:+.6f} sigma)")
    print(f"Y_p      = {row['Y_p']:.15f} ({row['Y_p_sigma']:+.6f} sigma)")
    print(f"Li7/H    = {row['Li7_over_H']:.15e} ({row['Li7_over_H_sigma']:+.6f} sigma)")
    print(f"chi2(D/H + Y_p) = {row['chi2_D_over_H_plus_Y_p']:.12f}")


if __name__ == "__main__":
    main()
