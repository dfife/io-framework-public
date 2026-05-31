#!/usr/bin/env python3
"""Reproduce the Paper 5 v2.0 Kerr-spin temperature diagnostic."""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]


def load_constants() -> dict:
    return json.loads((BUNDLE_ROOT / "data" / "imported_constants.json").read_text())


def kerr_surface_gravity_ratio(j: float) -> float:
    """Return kappa_Kerr / kappa_Schwarzschild for dimensionless spin j=a/M."""

    if not 0.0 <= j < 1.0:
        raise ValueError("dimensionless spin j=a/M must satisfy 0 <= j < 1")
    s = math.sqrt(1.0 - j * j)
    return 2.0 * s / (1.0 + s)


def spin_for_ratio(target_ratio: float) -> float:
    """Invert 2s/(1+s)=target_ratio for j=sqrt(1-s^2)."""

    s = target_ratio / (2.0 - target_ratio)
    return math.sqrt(max(0.0, 1.0 - s * s))


def main() -> None:
    constants = load_constants()
    t0 = constants["io_foundation"]["T_IO_schwarzschild_K"]
    spins = [0.0, 0.096, 0.325, 0.5, 0.99]
    rows = []
    for j in spins:
        ratio = kerr_surface_gravity_ratio(j)
        rows.append(
            {
                "spin_a_over_M": j,
                "kappa_ratio_formula": ratio,
                "interior_temperature_K": t0 * ratio,
            }
        )

    payload = {
        "status": "DERIVED",
        "claim_boundary": (
            "Kerr spin lowers horizon surface gravity monotonically. Since the "
            "Paper 5 temperature channel is proportional to surface gravity, "
            "nonzero spin can only lower the Schwarzschild value."
        ),
        "formula": "kappa_Kerr/kappa_Schwarzschild = 2*sqrt(1-j^2)/(1+sqrt(1-j^2))",
        "T_IO_schwarzschild_K": t0,
        "rows": rows,
        "monotonicity_check": {
            "sampled_spins_increasing": spins,
            "ratios_strictly_decrease_after_zero": all(
                rows[i]["kappa_ratio_formula"] > rows[i + 1]["kappa_ratio_formula"]
                for i in range(len(rows) - 1)
            ),
        },
        "ratio_threshold_spins": {
            "one_percent_temperature_drop": spin_for_ratio(0.99),
            "two_point_five_percent_temperature_drop": spin_for_ratio(0.975),
            "five_percent_temperature_drop": spin_for_ratio(0.95),
        },
        "manuscript_note": (
            "The manuscript table rounds the spin rows for storytelling. The exact "
            "support formula is the surface-gravity ratio above."
        ),
    }
    out = BUNDLE_ROOT / "results" / "kerr_spin_temperature_results.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()
