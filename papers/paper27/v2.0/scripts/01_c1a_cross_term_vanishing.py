#!/usr/bin/env python3
"""Reproduce Theorem 27.2: C1a cross-term vanishing.

Paper 27 v2.0 separates the scalar branch from the rank-one spin source.  The
load-bearing algebraic fact is that an `SU(2)`-equivariant cross-map from the
scalar singlet block to the vector/coexact branch has zero invariant dimension.

For a non-IO reader: this is the elementary compact-representation statement
that inequivalent irreducible `SU(2)` representations have no nonzero
intertwiner.  The script records the spin labels and the resulting zero
dimension rather than pretending that a numerical simulation is needed.
"""

from __future__ import annotations

from _common import write_result


def compute() -> dict:
    scalar_spin = 0
    coexact_vector_spin = 1
    invariant_hom_dimension = 1 if scalar_spin == coexact_vector_spin else 0

    return {
        "paper": 27,
        "version": "v2.0",
        "audit_target": "Theorem 27.2 C1a cross-term vanishing",
        "status": "DERIVED/THEOREM",
        "representation_check": {
            "source_block": "scalar singlet",
            "source_spin": scalar_spin,
            "target_block": "S3 coexact vector shell",
            "target_spin": coexact_vector_spin,
            "invariant_hom_dimension": invariant_hom_dimension,
            "selection_rule": "Hom_SU2(V_0, V_1) = 0",
        },
        "claim": "The cross covariance term vanishes by SU(2) representation mismatch.",
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("c1a_cross_term_vanishing_results.json", compute())
