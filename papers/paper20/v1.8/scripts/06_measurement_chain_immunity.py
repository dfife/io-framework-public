#!/usr/bin/env python3
"""
Print the Paper 20 BBN measurement-chain immunity audit.

This audit checks whether late-time observer-side geometric Jacobians can rescue
the BBN abundance tensions by acting differently on D/H, Y_p, and Li/H
measurement pipelines. The result is negative: the measured quantities are
dimensionless ratios, so common geometric factors cancel at leading order.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "bbn_measurement_chain_results.json").read_text(encoding="utf-8"))
    print("Paper 20 BBN measurement-chain audit")
    for name, row in data["measurement_chains"].items():
        print(
            f"{name}: common_factor_cancels={row['common_factor_cancels']}, "
            f"needed_factor={row['needed_measurement_factor']:.12f}"
        )
    print(data["verdict"]["summary"])


if __name__ == "__main__":
    main()
