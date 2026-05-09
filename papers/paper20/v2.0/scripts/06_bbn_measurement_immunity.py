#!/usr/bin/env python3
"""
Print the Big Bang nucleosynthesis measurement-immunity no-go.

Paper 20 v2.0 keeps the claim that late-time observer-side geometric Jacobians
cannot rescue D/H, Y_p, or Li7/H by acting on the measurement pipelines. The
reason is simple: the measured quantities are dimensionless abundance ratios,
so same-channel geometric factors cancel.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "bbn_measurement_immunity_results.json").read_text(encoding="utf-8"))
    print(data["claim"])
    for name, row in data["measurement_chains"].items():
        print(f"{name}: class={row['geometric_class']}, cancels={row['common_factor_cancels']}, needed_factor={row['needed_measurement_factor']:.12f}")
    print(data["verdict"])


if __name__ == "__main__":
    main()
