#!/usr/bin/env python3
"""
Print the Paper 20 v1.6/v1.7 corrected BBN wrapper scorecard.

This script documents the wrapper correction inherited by v1.8:

- helium uses PRyMordial YPCMB / PRyMresults()[3], not YPBBN / index 4;
- observational denominators follow IO Framework Conventions;
- weak and nuclear amplitudes inherit the modern Paper 22 / Paper 24 values.

PRyMordial is not redistributed in this public repository. The frozen JSON is
the public artifact; full reruns require a separate PRyMordial checkout.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "bbn_wrapper_scorecard_results.json").read_text(encoding="utf-8"))
    row = data["side_by_side"]["Paper20_vNext_PathC_corrected"]
    print("Paper 20 corrected BBN wrapper row")
    print(f"D/H      = {row['D/H']:.15e} ({row['D/H_sigma']:+.6f} sigma)")
    print(f"Y_p      = {row['Y_p']:.15f} ({row['Y_p_sigma']:+.6f} sigma)")
    print(f"Li7/H    = {row['Li7/H']:.15e} ({row['Li7/H_sigma']:+.6f} sigma)")
    print(f"chi2(D/H + Y_p) = {row['chi2_DH_plus_Yp']:.12f}")
    print(f"helium output component = {row['Y_p_output_component']}")


if __name__ == "__main__":
    main()
