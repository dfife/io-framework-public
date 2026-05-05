#!/usr/bin/env python3
"""Reproduce Paper 22 spatial Hodge complex support tables.

This script is part of the Paper 22 v1.6 public reproducibility bundle.
It computes the low-mode Hodge spectra on the round 3-sphere, the
Peter-Weyl representation labels used in the puncture-to-spatial bridge,
and the current-epoch framework constants imported by Paper 22.

The script is intentionally self-contained and uses only the Python standard
library. It does not rerun private exploratory searches. Its role is to give
a referee a compact, auditable version of the formulas behind Theorems 22.1
and 22.2 and the Peter-Weyl bridge statements carried by the manuscript.

Run from the bundle root:

    python3 scripts/01_spatial_hodge_complex.py

Output:

    results/spatial_hodge_complex_results.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
CONSTANTS_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT_PATH = BUNDLE_ROOT / "results" / "spatial_hodge_complex_results.json"


def half_integer_label(twice_j: int) -> str:
    """Return a compact label for a half-integer SU(2) spin."""
    return str(twice_j // 2) if twice_j % 2 == 0 else f"{twice_j}/2"


def rep_label(left_twice: int, right_twice: int) -> str:
    """Format the SU(2)_L x SU(2)_R representation label."""
    return f"({half_integer_label(left_twice)}, {half_integer_label(right_twice)})"


def hodge_mode_tables(max_n: int = 4) -> dict[str, list[dict[str, object]]]:
    """Compute unit-radius Hodge eigenvalue/multiplicity tables."""
    scalar = []
    exact_1 = []
    coexact_1 = []
    exact_2 = []
    coexact_2 = []
    three_forms = []
    for n in range(0, max_n + 1):
        scalar.append(
            {
                "n": n,
                "eigenvalue_unit_radius": n * (n + 2),
                "multiplicity": (n + 1) ** 2,
                "so4_rep": rep_label(n, n),
                "diag_su2_range": f"J=0..{n}",
            }
        )
        three_forms.append(
            {
                "n": n,
                "eigenvalue_unit_radius": n * (n + 2),
                "multiplicity": (n + 1) ** 2,
                "origin": "Hodge dual of scalar mode",
            }
        )
        if n >= 1:
            exact_1.append(
                {
                    "n": n,
                    "eigenvalue_unit_radius": n * (n + 2),
                    "multiplicity": (n + 1) ** 2,
                    "origin": "d applied to scalar mode",
                    "so4_rep": rep_label(n, n),
                }
            )
            coexact_1.append(
                {
                    "n": n,
                    "eigenvalue_unit_radius": (n + 1) ** 2,
                    "multiplicity": 2 * n * (n + 2),
                    "so4_rep": [rep_label(n + 1, n - 1), rep_label(n - 1, n + 1)],
                    "diag_su2_range": f"J=1..{n}",
                }
            )
            exact_2.append(
                {
                    "n": n,
                    "eigenvalue_unit_radius": (n + 1) ** 2,
                    "multiplicity": 2 * n * (n + 2),
                    "origin": "d applied to coexact 1-form mode",
                }
            )
            coexact_2.append(
                {
                    "n": n,
                    "eigenvalue_unit_radius": n * (n + 2),
                    "multiplicity": (n + 1) ** 2,
                    "origin": "Hodge dual of exact 1-form mode",
                }
            )
    return {
        "scalar_0_forms": scalar,
        "exact_1_forms": exact_1,
        "coexact_1_forms": coexact_1,
        "exact_2_forms": exact_2,
        "coexact_2_forms": coexact_2,
        "three_forms": three_forms,
    }


def main() -> None:
    constants = json.loads(CONSTANTS_PATH.read_text(encoding="utf-8"))
    fw = constants["framework_constants"]
    computed_r_u = 0.5 * fw["r_s_m"] * (1.0 - math.cos(fw["eta_s"]))
    computed_x = fw["r_s_m"] / computed_r_u
    computed_delta = computed_x**4 * (1.0 + fw["gamma_BI"] ** 2)
    result = {
        "script": Path(__file__).name,
        "claim_support": [
            "Theorem 22.1 Spatial Closure Theorem",
            "Theorem 22.2 Hodge Spectrum Theorem",
            "Peter-Weyl bridge on S^3 ~= SU(2)"
        ],
        "status": "DERIVED/THEOREM within the round-S3 OS spatial slice",
        "framework_constant_recompute": {
            "R_U_m": computed_r_u,
            "x": computed_x,
            "Delta": computed_delta,
            "K_gauge": math.log(1.0 + fw["gamma_BI"] ** 2),
            "K_total": math.log(computed_delta)
        },
        "hodge_complex": {
            "complex": "Omega^0(S^3) -> Omega^1(S^3) -> Omega^2(S^3) -> Omega^3(S^3)",
            "cohomology": {"H0": "R", "H1": "0", "H2": "0", "H3": "R"},
            "hodge_star": "*^2 = 1 on all form degrees in dimension 3",
            "radius_scaling": "all listed unit-radius eigenvalues scale as a(eta)^(-2)"
        },
        "unit_radius_mode_tables": hodge_mode_tables(),
        "peter_weyl_summary": {
            "scalar_branch": "L^2(S^3) = direct_sum_{n>=0} V_{n/2} tensor V_{n/2}^*",
            "coexact_vector_branch": "direct_sum_{n>=1} [(V_{(n+1)/2},V_{(n-1)/2}) plus parity conjugate]",
            "diagonal_su2_boundary": "scalar/exact branch contains J=0; coexact vector branch starts at J=1"
        },
        "checks": {
            "R_U_matches_import": abs(computed_r_u - fw["R_U_m"]) < 1.0e12,
            "x_matches_import": abs(computed_x - fw["x"]) < 1.0e-12,
            "delta_matches_import": abs(computed_delta - fw["Delta"]) < 1.0e-10,
            "coexact_vector_n1_multiplicity": 2 * 1 * (1 + 2)
        }
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
