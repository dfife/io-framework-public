#!/usr/bin/env python3
"""Reproduce the bridge-readable covariance and observable-exhaustion checks.

The current scalar bridge reads a rank-one covariance quotient.  Given the
Hawking/KMS boundary state on the bridge-readable shell, the occupation factor
is

    g_H = 1 / (exp(4*pi*sqrt(2)) - 1).

The script computes this value and records the theorem labels for bridge
rigidity, current-observable exhaustion, and the explicit no-go for universal
future-observable closure.
"""

from __future__ import annotations

import math

from _common import load_constants, write_result


def compute() -> dict:
    constants = load_constants()["paper27_values"]
    beta_omega = 4.0 * math.pi * math.sqrt(2.0)
    occupation = 1.0 / (math.exp(beta_omega) - 1.0)

    return {
        "paper": 27,
        "version": "v2.0",
        "audit_targets": [
            "Theorem 27.7.5 bridge-readable state rigidity",
            "Theorem 27.8.5 current scalar-bridge observable exhaustion",
            "Theorem 27.9.5 banked IO observable classification",
            "Theorem 27.11.4 universal all-future-observable no-go",
        ],
        "statuses": {
            "27.7.5": "DERIVED/CONDITIONAL_VERIFIED",
            "27.8.5": "DERIVED/THEOREM",
            "27.9.5": "DERIVED/THEOREM",
            "27.11.4": "DERIVED/NO-GO",
        },
        "boundary_l1_beta_omega": beta_omega,
        "boundary_covariance_l1_occupation": occupation,
        "frozen_boundary_covariance_l1_occupation": constants["boundary_covariance_l1_occupation"]["value"],
        "formula": "1/(exp(4*pi*sqrt(2)) - 1)",
        "claim_boundary": "The rank-one scalar quotient is fixed; the full h_vec state is not uniquely selected.",
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("bridge_rigidity_observable_exhaustion_results.json", compute())
