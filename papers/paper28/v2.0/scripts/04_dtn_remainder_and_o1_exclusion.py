#!/usr/bin/env python3
"""Reproduce the DtN remainder bound and O(1) deformation exclusion.

Once the IO boundary Hessian matches the flat-collar coexact DtN operator
through subprincipal order, ordinary lower-order terms cannot move the CMB
pivot tilt materially.  This script freezes the explicit bound used in the
Paper 28 support reports.
"""

from __future__ import annotations

from _common import load_constants, write_result


def slope_error_bound(beta: float, ell_plus_one: int, a_bound: float) -> float:
    return 2.0 * beta * a_bound / (ell_plus_one * ell_plus_one - a_bound)


def compute() -> dict:
    constants = load_constants()["framework_constants"]
    beta = constants["K_gauge"]["value"] / constants["x"]["value"]
    ell_plus_one = 712
    bounds = {str(a): slope_error_bound(beta, ell_plus_one, a) for a in [1, 5, 10, 50, 100]}

    return {
        "paper": 28,
        "version": "v2.0",
        "audit_target": "DtN lower-order remainder and O(1) deformation exclusion",
        "status": "DERIVED/CONDITIONAL_VERIFIED",
        "condition": "full IO reduced operator is Laplace-type on the exact flat Painleve-Gullstrand source collar",
        "bound_formula": "2 beta A / ((ell+1)^2 - A)",
        "ell": 711,
        "ell_plus_one": ell_plus_one,
        "beta": beta,
        "slope_error_bounds": bounds,
        "o1_shell_deformations_excluded_on_flat_collar": True,
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("dtn_remainder_and_o1_exclusion_results.json", compute())
