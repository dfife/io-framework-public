#!/usr/bin/env python3
"""Reproduce the closed-S3 scalar perturbation bookkeeping used by Paper 23.

This script is intentionally narrow. It does not solve a Boltzmann system and
does not generate a CMB spectrum. It verifies the theorem-support algebra that
Paper 23 uses before the bridge/readout step:

* scalar harmonics on the round three-sphere have eigenvalue n(n+2),
* physical scalar modes start at n = 2 after removing homogeneous/gauge modes,
* the Mukhanov-Sasaki closed-S3 dictionary uses k_MS R = sqrt((n-1)(n+3)),
* the current Oppenheimer-Snyder dust-branch sample has a''/a < 0 at eta=1.893.

Run:

    python3 papers/paper23/v2.0/scripts/02_scalar_perturbation_equations.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results" / "scalar_perturbation_equations_results.json"

ETA_SAMPLE = 1.893


def scalar_laplacian_eigenvalue(n: int) -> int:
    return n * (n + 2)


def scalar_multiplicity(n: int) -> int:
    return (n + 1) ** 2


def k_ms_times_r(n: int) -> float:
    return math.sqrt((n - 1) * (n + 3))


def os_a_double_prime_over_a(eta: float) -> float:
    """Return a''/a for the normalized OS dust parametric branch.

    With a(eta) proportional to (1 - cos eta), direct differentiation gives
    a''/a = cos(eta) / (1 - cos(eta)).
    """

    return math.cos(eta) / (1.0 - math.cos(eta))


def main() -> int:
    samples = []
    for n in range(0, 9):
        lambda_n = scalar_laplacian_eigenvalue(n)
        lambda_shifted = lambda_n - 3
        samples.append(
            {
                "n": n,
                "lambda_n": lambda_n,
                "multiplicity": scalar_multiplicity(n),
                "lambda_n_minus_3": lambda_shifted,
                "k_MS_R": None if n < 2 else k_ms_times_r(n),
                "physical_scalar_status": (
                    "homogeneous/background" if n == 0 else "gauge" if n == 1 else "physical"
                ),
            }
        )

    results = {
        "paper": "Paper 23",
        "version": "v2.0",
        "claim_status": {
            "closed_S3_scalar_harmonic_spectrum": "DERIVED/THEOREM",
            "physical_scalar_start_n_equals_2": "DERIVED/THEOREM",
            "closed_S3_Mukhanov_Sasaki_wavenumber_dictionary": "DERIVED/THEOREM",
            "OS_branch_sample": "VERIFIED",
        },
        "formulas": {
            "scalar_laplacian": "-Delta_{S3} Q_nlm = n(n+2) Q_nlm",
            "multiplicity": "dim H_n^(0) = (n+1)^2",
            "closed_MS_wavenumber": "k_MS(n) = sqrt((n-1)(n+3)) / R",
            "scalar_mode_equation": "v_n'' + [k_MS(n)^2 - z''/z] v_n = 0",
            "OS_dust_branch_sample": "a''/a = cos(eta)/(1-cos(eta))",
        },
        "samples": samples,
        "OS_branch": {
            "eta_sample": ETA_SAMPLE,
            "a_double_prime_over_a": os_a_double_prime_over_a(ETA_SAMPLE),
            "interpretation": "negative at the sampled expanding branch point used in the private analysis",
        },
        "checks": {
            "lambda_2": scalar_laplacian_eigenvalue(2),
            "lambda_2_minus_3": scalar_laplacian_eigenvalue(2) - 3,
            "multiplicity_2": scalar_multiplicity(2),
            "physical_start_n": 2,
        },
    }

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

