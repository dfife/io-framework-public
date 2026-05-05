#!/usr/bin/env python3
"""Reproduce the TT branch and Channel Floor theorem arithmetic.

Paper 22 adds the transverse-traceless symmetric rank-2 tensor branch that
the de Rham complex does not contain. This script computes the low TT mode
table and the diagonal SU(2) channel-floor law J_min = s for the principal
transverse spin-s branch on S^3.

Run from the bundle root:

    python3 scripts/02_tt_channel_floor.py

Output:

    results/tt_channel_floor_results.json
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = BUNDLE_ROOT / "results" / "tt_channel_floor_results.json"


def half_integer_label(twice_j: int) -> str:
    return str(twice_j // 2) if twice_j % 2 == 0 else f"{twice_j}/2"


def rep_label(left_twice: int, right_twice: int) -> str:
    return f"({half_integer_label(left_twice)}, {half_integer_label(right_twice)})"


def tt_mode(n: int) -> dict[str, object]:
    """Return unit-radius TT mode data for level n >= 2."""
    if n < 2:
        raise ValueError("TT principal branch starts at n=2")
    return {
        "n": n,
        "multiplicity": 2 * (n - 1) * (n + 3),
        "rough_laplacian_eigenvalue_unit_radius": n * (n + 2) - 2,
        "lichnerowicz_eigenvalue_unit_radius": n * (n + 2) + 4,
        "so4_rep": [rep_label(n + 2, n - 2), rep_label(n - 2, n + 2)],
        "diagonal_su2_range": f"J={2}..{n}",
    }


def channel_floor(s: int, n: int) -> dict[str, object]:
    """Compute the diagonal SU(2) floor for the principal transverse spin-s branch."""
    if n < s:
        raise ValueError("principal branch requires n >= s")
    left_twice = n + s
    right_twice = n - s
    return {
        "s": s,
        "n": n,
        "so4_rep": [rep_label(left_twice, right_twice), rep_label(right_twice, left_twice)],
        "J_min": abs(left_twice - right_twice) // 2,
        "J_max": (left_twice + right_twice) // 2,
        "diagonal_su2_range": f"J={s}..{n}",
    }


def main() -> None:
    tt_table = [tt_mode(n) for n in range(2, 7)]
    floors = [channel_floor(s, max(s, 3)) for s in range(0, 4)]
    result = {
        "script": Path(__file__).name,
        "claim_support": [
            "Theorem 22.3 TT Branch Theorem",
            "Theorem 22.4 Channel Floor Theorem"
        ],
        "status": "DERIVED/THEOREM for the principal transverse branch",
        "tt_low_mode_table_unit_radius": tt_table,
        "lowest_TT_block": {
            "n": 2,
            "multiplicity": tt_table[0]["multiplicity"],
            "rough_laplacian_eigenvalue_unit_radius": tt_table[0]["rough_laplacian_eigenvalue_unit_radius"],
            "lichnerowicz_eigenvalue_unit_radius": tt_table[0]["lichnerowicz_eigenvalue_unit_radius"],
            "representation": "(2,0) plus (0,2)",
            "interpretation": "10-dimensional lowest TT block used by the TBS denominator"
        },
        "channel_floor_examples": floors,
        "selection_rule": {
            "J0": "scalar only",
            "J1": "scalar plus vector",
            "J2": "scalar plus vector plus TT tensor",
            "boundary": "The clean J_min=s theorem applies to principal transverse branches, not derivative descendants."
        },
        "checks": {
            "mult_TT_n2_is_10": tt_table[0]["multiplicity"] == 10,
            "tt_rough_n2_is_6": tt_table[0]["rough_laplacian_eigenvalue_unit_radius"] == 6,
            "tt_lichnerowicz_n2_is_12": tt_table[0]["lichnerowicz_eigenvalue_unit_radius"] == 12,
            "floor_s2_is_2": channel_floor(2, 2)["J_min"] == 2
        }
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
