#!/usr/bin/env python3
"""Reproduce the homogeneous OS JWST formation-clock map.

The active theorem-grade clock result is not an observational fit.  In the
homogeneous Oppenheimer-Snyder interior, local structure formation follows the
proper time on comoving matter worldlines.  For radial null propagation to the
observer epoch `a(eta_s)=r_s/x`, the background event map is

    u(z) = 1/[x(1+z)]
    tau(z) = (r_s/(2c)) [acos(1 - 2u) - 2 sqrt(u(1-u))].
"""

from __future__ import annotations

import math

from _common import load_constants, write_result


SECONDS_PER_GYR = 365.25 * 24.0 * 3600.0 * 1.0e9


def tau_gyr(z: float, x: float, r_s_m: float, c_m_s: float) -> float:
    u = 1.0 / (x * (1.0 + z))
    return (r_s_m / (2.0 * c_m_s) / SECONDS_PER_GYR) * (
        math.acos(1.0 - 2.0 * u) - 2.0 * math.sqrt(u * (1.0 - u))
    )


def compute() -> dict:
    constants = load_constants()["framework_constants"]
    x = constants["x"]["value"]
    r_s_m = constants["r_s_m"]["value"]
    c_m_s = constants["c_m_s"]["value"]
    redshifts = [10, 12, 14, 17, 20]
    rows = [{"z": z, "t_form_gyr": tau_gyr(z, x, r_s_m, c_m_s)} for z in redshifts]

    return {
        "paper": 28,
        "version": "v2.0",
        "audit_target": "homogeneous OS JWST formation-clock map",
        "status": "DERIVED/THEOREM on the homogeneous OS background",
        "formula": "tau(z) = (r_s/(2c))[acos(1 - 2/[x(1+z)]) - 2 sqrt(u(1-u))]",
        "inputs": {"x": x, "r_s_m": r_s_m, "c_m_s": c_m_s},
        "rows": rows,
        "scope": "Peculiar velocities, local potentials, and nonlinear structure are perturbative corrections around this background theorem.",
        "hidden_fitted_parameter": False,
    }


if __name__ == "__main__":
    write_result("jwst_clock_map_results.json", compute())
