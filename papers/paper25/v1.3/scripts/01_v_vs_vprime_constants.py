#!/usr/bin/env python3
"""Recompute the Paper 25 V-versus-V' constants.

This script is intentionally small and explicit. It gives reviewers the
numerical spine of the Paper 25 weak-sector identity problem without requiring
private lab code:

    gamma_BI -> Q = 1 + gamma_BI^2
             -> K_gauge = log(Q)
             -> V' = 2 gamma_BI
             -> V'' = 2 Q

It also recomputes the weak amplitudes used in Paper 25:

    old linear branch:      epsilon_w = K_gauge * sqrt(L_1)
    active quadratic branch: epsilon_w = K_gauge * L_1
    V' comparator branch:    epsilon_w = V' * sqrt(L_1)

Run from the bundle root:

    python3 scripts/01_v_vs_vprime_constants.py

or from the repository root:

    python3 papers/paper25/v1.3/scripts/01_v_vs_vprime_constants.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "v_vs_vprime_constants_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    constants = data["framework_constants"]

    gamma = constants["gamma_BI"]
    l1 = constants["L1"]
    sqrt_l1 = math.sqrt(l1)
    l2 = constants["L2"]
    k_mean = constants["K_mean_aligned"]

    q = 1.0 + gamma * gamma
    k_gauge = math.log(q)
    v_prime = 2.0 * gamma
    v_double_prime = 2.0 * q
    epsilon_w_quadratic = k_gauge * l1
    epsilon_w_linear = k_gauge * sqrt_l1
    epsilon_w_vprime = v_prime * sqrt_l1
    epsilon_n = (k_mean / 10.0) * l2

    result = {
        "paper": "Paper 25 v1.3",
        "purpose": "recompute V, V', V'', and weak-amplitude branches",
        "constants": {
            "gamma_BI": gamma,
            "Q": q,
            "K_gauge": k_gauge,
            "V_prime": v_prime,
            "V_double_prime": v_double_prime,
            "L1": l1,
            "sqrt_L1": sqrt_l1,
            "L2": l2,
            "K_mean_aligned": k_mean
        },
        "amplitudes": {
            "epsilon_w_quadratic_Kgauge_L1": epsilon_w_quadratic,
            "epsilon_w_linear_Kgauge_sqrtL1": epsilon_w_linear,
            "epsilon_w_vprime_sqrtL1": epsilon_w_vprime,
            "epsilon_n_Kmean_over_10_L2": epsilon_n
        },
        "ratios": {
            "V_prime_over_K_gauge": v_prime / k_gauge,
            "linear_over_quadratic_weak_amplitude": epsilon_w_linear / epsilon_w_quadratic,
            "vprime_over_quadratic_weak_amplitude": epsilon_w_vprime / epsilon_w_quadratic
        },
        "claim_boundary": "K_gauge is the finite modular payload; Paper 25 tests whether the weak rate reads K_gauge or V'."
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
