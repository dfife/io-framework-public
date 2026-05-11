#!/usr/bin/env python3
"""Reproduce the Paper 23 tensor-support bookkeeping.

Paper 23's tensor sector is not the scalar spectral-index headline result. This
script records the tensor harmonic arithmetic and the scope boundary:

* transverse-traceless tensor harmonics on S3 start at n = 2,
* the lowest TT block has multiplicity 10,
* the tensor evolution equation uses the closed-S3 shifted spectrum,
* the tensor tilt claim remains premise-dependent/open unless a gamma-neutrality
  theorem is supplied elsewhere.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results" / "tensor_perturbations_results.json"


def tt_multiplicity(n: int) -> int:
    return 2 * (n - 1) * (n + 3)


def rough_tt_laplacian(n: int) -> int:
    return n * (n + 2) - 2


def lichnerowicz_tt_eigenvalue(n: int) -> int:
    return n * (n + 2) + 4


def tensor_jacobian(n: int) -> float:
    return (n + 1) / (n + 2)


def main() -> int:
    samples = {
        str(n): {
            "n": n,
            "multiplicity": tt_multiplicity(n),
            "rough_laplacian_eigenvalue_unit_radius": rough_tt_laplacian(n),
            "lichnerowicz_eigenvalue_unit_radius": lichnerowicz_tt_eigenvalue(n),
            "d_ln_k_d_ln_n_continuum_proxy": tensor_jacobian(n),
        }
        for n in [2, 3, 4, 10, 30, 100]
    }

    results = {
        "paper": "Paper 23",
        "version": "v2.0",
        "claim_status": {
            "TT_spectrum_bookkeeping": "DERIVED/THEOREM",
            "lowest_TT_block": "DERIVED/THEOREM",
            "tensor_evolution_equation": "DERIVED/THEOREM within closed-FRW perturbation theory",
            "tensor_tilt_n_t_equals_0": "OPEN/PREMISE_GAP unless gamma-neutrality chain is supplied",
        },
        "formulas": {
            "TT_multiplicity": "mult_TT(n) = 2(n-1)(n+3), n >= 2",
            "rough_laplacian": "lambda_TT^rough(n) = n(n+2)-2",
            "lichnerowicz": "lambda_TT^L(n) = n(n+2)+4",
            "mode_equation": "u_n'' + [n(n+2) - a''/a] u_n = 0 in the reduced tensor bookkeeping",
        },
        "samples": samples,
        "checks": {
            "lowest_n": 2,
            "mult_TT_n2": tt_multiplicity(2),
            "rough_laplacian_n2": rough_tt_laplacian(2),
            "lichnerowicz_n2": lichnerowicz_tt_eigenvalue(2),
            "tensor_jacobian_n30": tensor_jacobian(30),
        },
    }

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

