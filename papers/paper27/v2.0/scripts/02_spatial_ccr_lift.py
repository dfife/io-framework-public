#!/usr/bin/env python3
"""Reproduce Theorem 27.1: Spatial canonical-commutation-relation lift.

The theorem identifies the scalar-bridge perturbation carrier

    h_vec = L2(R, dnu) x H_g x Omega1_coex(S3).

The checks here are structural: the closed `S^3` spatial slice has no harmonic
one-forms, so the live vector branch is coexact; the channel floor selects the
lowest vector shell.  The script freezes those inputs and their status labels
for bundle validation.
"""

from __future__ import annotations

from _common import write_result


def compute() -> dict:
    first_betti_number_s3 = 0
    lowest_coexact_vector_shell = 1
    harmonic_one_form_dimension = first_betti_number_s3
    coexact_branch_available = harmonic_one_form_dimension == 0

    return {
        "paper": 27,
        "version": "v2.0",
        "audit_target": "Theorem 27.1 Spatial CCR Lift",
        "status": "DERIVED/THEOREM",
        "carrier": "L2(R,dnu) tensor H_g tensor Omega1_coex(S3)",
        "topology_check": {
            "manifold": "S3",
            "first_betti_number": first_betti_number_s3,
            "harmonic_one_form_dimension": harmonic_one_form_dimension,
            "coexact_branch_available": coexact_branch_available,
            "lowest_coexact_vector_shell": lowest_coexact_vector_shell,
        },
        "chain": [
            "P1: closed K=+1 interior spatial slice",
            "Hodge decomposition on compact S3",
            "Paper 22 v2.0 Channel Floor Theorem",
            "Paper 27 v2.0 Theorem 27.1",
        ],
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("spatial_ccr_lift_results.json", compute())
