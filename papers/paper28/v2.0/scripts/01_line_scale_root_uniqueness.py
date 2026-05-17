#!/usr/bin/env python3
"""Reproduce the primitive line-scale root uniqueness result.

For a non-IO reader: the question is whether the coexact one-form carrier uses
the Laplacian scale `Delta` or the line scale `sqrt(Delta)`.  A one-form line
transport generator must scale with inverse length, while the Laplacian scales
with inverse length squared.  Therefore `(Delta)^q` has the correct line
dimension only for `q = 1/2`.
"""

from __future__ import annotations

from _common import load_constants, write_result


def compute() -> dict:
    constants = load_constants()["framework_constants"]
    q_line = 0.5
    k_gauge = constants["K_gauge"]["value"]
    x = constants["x"]["value"]
    beta = k_gauge / x

    return {
        "paper": 28,
        "version": "v2.0",
        "audit_target": "primitive line-scale root uniqueness",
        "status": "DERIVED/THEOREM",
        "formula": "Delta_1^q has line-transport dimension only when 2q = 1",
        "q_line": q_line,
        "K_gauge_over_x": beta,
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("line_scale_root_uniqueness_results.json", compute())
