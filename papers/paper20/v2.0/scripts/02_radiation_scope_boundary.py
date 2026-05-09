#!/usr/bin/env python3
"""
Print the Paper 20 v2.0 radiation scope-boundary theorem support.

Theorem 20.3 is a reduced-core no-go: the reduced bosonic photon sector plus
central gauge data cannot determine the effective number of relativistic
species. This script exposes the missing carrier and the late-time sensitivity
check recorded in the frozen result.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "radiation_scope_boundary_results.json").read_text(encoding="utf-8"))
    print(data["theorem"])
    print(f"status: {data['status']}")
    print("reduced stack:", data["reduced_stack"]["algebra"])
    print("absent sectors:", ", ".join(data["reduced_stack"]["sectors_absent"]))
    print(f"Delta H0 max over N_eff scan = {data['late_time_sensitivity']['Delta_H0_max_km_s_Mpc']} km/s/Mpc")
    for item in data["no_go_arguments"]:
        print(f"- {item}")


if __name__ == "__main__":
    main()
