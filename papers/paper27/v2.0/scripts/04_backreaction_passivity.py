#!/usr/bin/env python3
"""Freeze the backreaction/passivity reduction ledger.

This script is not a numerical optimizer.  It records the theorem-grade
classification that positive residual states on the full carrier are reduced
by closed-geometry backreaction and passivity constraints, while still not
being uniquely selected as a full `h_vec` state.
"""

from __future__ import annotations

from _common import write_result


def compute() -> dict:
    return {
        "paper": 27,
        "version": "v2.0",
        "audit_target": "Theorem 27.6.15 backreaction-passivity residual reduction",
        "status": "DERIVED/CONDITIONAL_VERIFIED",
        "standard_physics_inputs": [
            "Pusz-Woronowicz passivity",
            "KMS equilibrium-state structure",
            "standard stress-energy backreaction constraint",
        ],
        "excluded_classes": [
            "negative-energy residuals violating the closed-geometry backreaction sign condition",
            "non-passive residuals that fail equilibrium admissibility",
        ],
        "surviving_classes": [
            "positive passive residual states invisible to the current scalar quotient"
        ],
        "hidden_scalar_amplitude_fit": False,
        "full_state_selected": False,
        "scope": "Restriction theorem, not full state-selection closure.",
    }


if __name__ == "__main__":
    write_result("backreaction_passivity_results.json", compute())
