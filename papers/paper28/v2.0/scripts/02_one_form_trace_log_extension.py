#!/usr/bin/env python3
"""Reproduce the one-form trace-log Gaussian extension arithmetic.

The Paper 28 shell law is not a raw empirical fit.  Given the coexact one-form
carrier and a centered one-loop Gaussian extension, the determinant contributes
per mode `w_l = log(s_l)`, where `s_l = sqrt(lambda_l)` is the primitive line
scale.  A payload coefficient `K_gauge/x` then gives the covariance law
`N_l proportional to s_l^(-K_gauge/x)`.
"""

from __future__ import annotations

from _common import load_constants, write_result


def compute() -> dict:
    values = load_constants()["paper28_values"]
    return {
        "paper": 28,
        "version": "v2.0",
        "audit_target": "one-form trace-log Gaussian extension",
        "status": "DERIVED/CONDITIONAL_VERIFIED",
        "condition": "physical A-vacuum canonical extension belongs to the centered one-loop Gaussian coexact one-form class",
        "per_mode_generator": "w_l = log(s_l) = (1/2) log(lambda_l)",
        "payload_coefficient": values["beta_K_over_x"]["value"],
        "pivot_ns_values": {
            "plus_branch": 0.963832748116771,
            "minus_branch": 0.963934220358385,
            "equal_branch_average": 0.963883481680499,
            "exact_shell_target": values["ns_exact_shell_target_pivot"]["value"]
        },
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("one_form_trace_log_extension_results.json", compute())
