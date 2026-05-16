#!/usr/bin/env python3
"""Reproduce Theorem 27.3 visibility-slot inheritance.

Paper 27 v2.0 inherits the visibility baryon slot from the effective baryon
value used in the scalar bridge chain:

    omega_b,vis = omega_b,eff = 0.02910.

This script records that equality, the status labels for inherited H2/H3
closures, and the explicit boundary that AV1 and full state selection are not
silently promoted.
"""

from __future__ import annotations

from _common import load_constants, write_result


def compute() -> dict:
    values = load_constants()["paper27_values"]
    omega_b_eff = values["omega_b_visibility"]["value"]

    return {
        "paper": 27,
        "version": "v2.0",
        "audit_targets": [
            "Theorem 27.3 AV1 visibility-slot inheritance",
            "H2 spatial CCR lift inheritance",
            "H3 quadratic thermal covariance inheritance",
        ],
        "statuses": {
            "Theorem 27.3": "DERIVED/THEOREM",
            "H2": "DERIVED/THEOREM via Paper 27 v2.0 Theorem 27.1",
            "H3": "DERIVED/THEOREM via Paper 25 v2.0 Theorems 25.9-25.11",
        },
        "omega_b_visibility": omega_b_eff,
        "omega_b_effective": omega_b_eff,
        "formula": "omega_b,vis = omega_b,eff",
        "AV1_promoted": False,
        "full_h_vec_state_selected": False,
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("visibility_and_inheritance_results.json", compute())
