#!/usr/bin/env python3
"""Reproduce the residual-cone and closed-geometry arithmetic.

Sections 5 and 6 of Paper 27 v2.0 separate the rank-one quotient seen by the
current scalar bridge from the residual state cone on the full lifted carrier.
The residual freedom remains open on the full carrier, but it is not a hidden
fit parameter for the active scalar amplitude because the quotient is rank one.
"""

from __future__ import annotations

import math

from _common import load_constants, write_result


def compute() -> dict:
    constants = load_constants()["paper27_values"]
    beta_l1 = 4.0 * math.pi * math.sqrt(2.0)
    beta_s3_n1 = 8.0 * math.pi

    return {
        "paper": 27,
        "version": "v2.0",
        "audit_targets": [
            "Theorem 27.5.8 scalar-quotient residual freedom",
            "Theorem 27.6.6 closed-geometry residual reduction",
            "Theorem 27.6.7 exact-P1 backreaction boundary",
        ],
        "statuses": {
            "27.5.8": "DERIVED/THEOREM",
            "27.6.6": "DERIVED/THEOREM",
            "27.6.7": "DERIVED/THEOREM",
        },
        "rank_one_quotient_dimension": 1,
        "full_carrier_residual_state_freedom": "infinite-dimensional",
        "residual_is_hidden_scalar_amplitude_fit": False,
        "closed_geometry_exponents": {
            "boundary_l1_beta_omega": beta_l1,
            "boundary_l1_formula": "4*pi*sqrt(2)",
            "s3_n1_reference_exponent": beta_s3_n1,
            "s3_n1_formula": "8*pi",
            "frozen_boundary_l1_beta_omega": constants["hawking_boundary_beta_omega_l1"]["value"],
            "frozen_s3_n1_reference_exponent": constants["closed_geometry_n1_reference_exponent"]["value"],
        },
        "scope": "Current scalar bridge quotient only; full h_vec state selection remains OPEN/PREMISE_GAP.",
    }


if __name__ == "__main__":
    write_result("residual_cone_and_closed_geometry_results.json", compute())
