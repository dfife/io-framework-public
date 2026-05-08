#!/usr/bin/env python3
"""
Summarize the Paper 20 radiation-sector theorem audit.

The radiation-sector scripts test whether the reduced observer algebra derives
the effective radiation species count internally. The active conclusion is a
no-go for internal N_eff derivation from the reduced stack, plus compatibility
constructions for standard radiation physics.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "radiation_three_theorems_results.json").read_text(encoding="utf-8"))
    print("Paper 20 radiation-sector theorem summary")
    for key, status in data["claim_discipline"].items():
        print(f"{key}: {status}")
    print(f"N_eff_SM = {data['inputs']['N_eff_SM']}")
    print(f"delta_N_eff_required = {data['inputs']['delta_N_eff_required']}")
    print(data["verdict"]["summary"])


if __name__ == "__main__":
    main()
