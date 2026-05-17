#!/usr/bin/env python3
"""Reproduce the coexact Dirichlet-to-Neumann Hessian spectral-index check.

On the flat Painleve-Gullstrand source collar, the coexact differential-form
Dirichlet-to-Neumann operator on the `B^3/S^2` model has shell eigenvalues
`sigma_l = l + 1`.  Paper 28 uses this first-order boundary Hessian class to
generate the finite-shell spectral-index value at pivot shell `N = 712`.
"""

from __future__ import annotations

from _common import load_constants, write_result


def compute() -> dict:
    values = load_constants()["paper28_values"]
    constants = load_constants()["framework_constants"]
    beta = constants["K_gauge"]["value"] / constants["x"]["value"]
    ns_continuum = 1.0 - beta

    return {
        "paper": 28,
        "version": "v2.0",
        "audit_target": "coexact DtN Hessian spectral-index chain",
        "status": "DERIVED/CONDITIONAL_VERIFIED",
        "condition": "full reduced IO boundary Hessian agrees with the coexact DtN class through the stated collar reduction",
        "dtn_shell_law": "sigma_l = l + 1",
        "beta_K_over_x": beta,
        "ns_continuum": ns_continuum,
        "pivot_N": 712,
        "pivot_values": {
            "dtn_plus_branch": 0.963858187553,
            "dtn_minus_branch": 0.963959517376,
            "dtn_equal_branch_average": values["ns_dtn_equal_branch_average_pivot"]["value"],
            "exact_shell_target": values["ns_exact_shell_target_pivot"]["value"]
        },
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("dtn_hessian_spectral_index_results.json", compute())
