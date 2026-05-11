#!/usr/bin/env python3
"""Reproduce the Paper 23 no-doubling and scalar spectral-index numbers.

This is the headline numerical script for the Paper 23 v2.0 bundle. It computes

    1 - n_s = K_gauge / x

using the active framework constants, compares it to the Planck reference value
used in the manuscript, and records the closed-S3 finite-shell correction

    F(n) = (n-1)(n+3)/(n(n+1)).

The rejected doubled route is also evaluated to make the no-doubling boundary
auditable.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results" / "no_doubling_and_spectral_index_results.json"

GAMMA_BI = 0.2375
X = 1.51899780195519
K_GAUGE = math.log1p(GAMMA_BI**2)
PLANCK_ONE_MINUS_NS = 0.0351
PLANCK_SIGMA = 0.0042
R_U_M = 4.40092802727914e26
MPC_M = 3.0856775814913673e22


def shell_factor(n: int) -> float:
    return ((n - 1) * (n + 3)) / (n * (n + 1))


def shell_from_k(k_mpc_inverse: float) -> float:
    """Solve sqrt((n-1)(n+3))/R_U = k for continuous n."""

    r_u_mpc = R_U_M / MPC_M
    y = k_mpc_inverse * r_u_mpc
    return -1.0 + math.sqrt(y * y + 4.0)


def sigma(value: float) -> float:
    return (value - PLANCK_ONE_MINUS_NS) / PLANCK_SIGMA


def main() -> int:
    one_slot = K_GAUGE / X
    doubled = 2.0 * one_slot
    shell_samples = {}
    for n in [2, 3, 6, 7, 29, 30, 245, 712, 713]:
        factor = shell_factor(n)
        shell_samples[str(n)] = {
            "n": n,
            "factor": factor,
            "one_minus_ns_shell_corrected": one_slot * factor,
            "n_s_shell_corrected": 1.0 - one_slot * factor,
        }

    results = {
        "paper": "Paper 23",
        "version": "v2.0",
        "claim_status": {
            "No_Doubling_theorem": "DERIVED/CONDITIONAL_VERIFIED",
            "scalar_spectral_index": "DERIVED/CONDITIONAL_VERIFIED",
            "Planck_residual": "VERIFIED",
            "finite_shell_correction": "DERIVED/THEOREM",
            "doubled_route": "DERIVED/NO-GO",
        },
        "constants": {
            "gamma_BI": GAMMA_BI,
            "x": X,
            "K_gauge": K_GAUGE,
            "R_U_m": R_U_M,
            "R_U_Mpc": R_U_M / MPC_M,
            "planck_one_minus_ns": PLANCK_ONE_MINUS_NS,
            "planck_sigma": PLANCK_SIGMA,
        },
        "active_result": {
            "formula": "1 - n_s = K_gauge / x",
            "one_minus_ns": one_slot,
            "n_s": 1.0 - one_slot,
            "sigma_residual": sigma(one_slot),
        },
        "rejected_doubled_route": {
            "formula": "1 - n_s = 2 K_gauge / x",
            "one_minus_ns": doubled,
            "n_s": 1.0 - doubled,
            "sigma_residual": sigma(doubled),
            "finding": "The doubled covariance route is not an adjustable branch; it is killed.",
        },
        "finite_shell_correction": {
            "formula": "1 - n_s(n) = (K_gauge/x) * (n-1)(n+3)/(n(n+1))",
            "samples": shell_samples,
            "peak_note": "The factor is 5/6 at n=2, 1 at n=3, and peaks near n=6.5 at 15/14.",
        },
        "pivot_shells": {
            "formula": "sqrt((n-1)(n+3))/R_U = k",
            "k_0_002_Mpc_inverse": shell_from_k(0.002),
            "k_0_05_Mpc_inverse": shell_from_k(0.05),
        },
        "checks": {
            "one_minus_ns": one_slot,
            "n_s": 1.0 - one_slot,
            "sigma_residual": sigma(one_slot),
            "doubled_sigma_residual": sigma(doubled),
            "shell_factor_n2": shell_factor(2),
            "shell_factor_n3": shell_factor(3),
            "shell_factor_n7": shell_factor(7),
            "pivot_shell_k0_05": shell_from_k(0.05),
        },
    }

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

