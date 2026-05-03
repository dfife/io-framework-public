#!/usr/bin/env python3
"""Paper 35 v1.1 script 06: JWST formation-time table.

Purpose:
    Reproduce the high-redshift age comparison table for the IO bare master
    clock and the Planck/LambdaCDM comparator.

Inputs:
    data/imported_constants.json

Outputs:
    results/jwst_formation_time_table_results.json

Claim boundary:
    DERIVED/SCOPED timing relief. This does not prove full galaxy-formation
    closure or make any listed galaxy literally impossible in LCDM.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"
SECONDS_PER_GYR = 365.25 * 24.0 * 3600.0 * 1.0e9
MPC_M = 3.0856775814913673e22


def omega_r_from_tcmb_neff(*, T_cmb: float, N_eff: float, H0: float) -> float:
    h = H0 / 100.0
    omega_gamma_h2 = 2.4728e-5 * (T_cmb / 2.7255) ** 4
    omega_r_h2 = omega_gamma_h2 * (1.0 + 0.22710731766 * N_eff)
    return omega_r_h2 / (h * h)


def fixed_simpson(f, a: float, b: float, n: int = 20000) -> float:
    """Deterministic Simpson integration.

    The original lab script used scipy.integrate.quad. The public bundle keeps
    the validation path dependency-free, so a high-resolution fixed Simpson
    rule is used instead. At n=20000 the JWST age table is stable well below
    manuscript precision.
    """
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    odd = 0.0
    even = 0.0
    for i in range(1, n):
        if i % 2:
            odd += f(a + i * h)
        else:
            even += f(a + i * h)
    return h * (total + 4.0 * odd + 2.0 * even) / 3.0


def age_gyr(z: float, bg: dict[str, float], omega_r: float, omega_lambda_override: float | None = None) -> float:
    a_max = 1.0 / (1.0 + z)
    h0_si = bg["H0"] * 1000.0 / MPC_M
    omega_lambda = bg["Omega_lambda"] if omega_lambda_override is None else omega_lambda_override

    def integrand(a: float) -> float:
        if a == 0.0:
            return 0.0
        e2 = omega_r / a**4 + bg["Omega_m"] / a**3 + bg["Omega_k"] / a**2 + omega_lambda
        return 1.0 / (a * h0_si * math.sqrt(e2))

    return fixed_simpson(integrand, 0.0, a_max) / SECONDS_PER_GYR


def classify_clock_only(window_myr: float, build_time_myr: float) -> str:
    return "not impossible from clock time alone" if build_time_myr <= window_myr else "clock-pressure remains"


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    bgs = constants["jwst_backgrounds"]
    bare = bgs["io_bare_master_clock"]
    lcdm = bgs["lcdm_comparator"]
    onset = bgs["star_formation_onset_Gyr"]

    omega_r_bare = omega_r_from_tcmb_neff(T_cmb=bare["T_cmb"], N_eff=bare["N_eff"], H0=bare["H0"])
    omega_r_lcdm = omega_r_from_tcmb_neff(T_cmb=lcdm["T_cmb"], N_eff=lcdm["N_eff"], H0=lcdm["H0"])
    omega_lambda_lcdm = 1.0 - lcdm["Omega_m"] - omega_r_lcdm

    grid = []
    for z in [10.0, 12.0, 14.0, 16.0]:
        t_io = age_gyr(z, bare, omega_r_bare)
        t_lcdm = age_gyr(z, lcdm, omega_r_lcdm, omega_lambda_lcdm)
        grid.append(
            {
                "z": z,
                "t_io_gyr": t_io,
                "t_lcdm_gyr": t_lcdm,
                "delta_myr": (t_io - t_lcdm) * 1.0e3,
                "ratio": t_io / t_lcdm,
                "formation_window_io_myr_after_100myr": max(t_io - onset, 0.0) * 1.0e3,
                "formation_window_lcdm_myr_after_100myr": max(t_lcdm - onset, 0.0) * 1.0e3,
            }
        )

    objects = []
    for obj in constants["jwst_objects"]:
        t_io = age_gyr(obj["z"], bare, omega_r_bare)
        t_lcdm = age_gyr(obj["z"], lcdm, omega_r_lcdm, omega_lambda_lcdm)
        mstar = 10.0 ** obj["log10_mstar"]
        build_time_myr = mstar / obj["sfr_msun_per_year"] / 1.0e6
        window_io = max(t_io - onset, 0.0) * 1.0e3
        window_lcdm = max(t_lcdm - onset, 0.0) * 1.0e3
        objects.append(
            {
                **obj,
                "t_io_gyr": t_io,
                "t_lcdm_gyr": t_lcdm,
                "delta_myr": (t_io - t_lcdm) * 1.0e3,
                "window_io_myr_after_100myr": window_io,
                "window_lcdm_myr_after_100myr": window_lcdm,
                "build_time_at_published_sfr_myr": build_time_myr,
                "lcdm_clock_only_classification": classify_clock_only(window_lcdm, build_time_myr),
                "io_clock_only_classification": classify_clock_only(window_io, build_time_myr),
            }
        )

    payload = {
        "script": "06_jwst_formation_time_table.py",
        "status": "verified",
        "claim_boundary": "DERIVED/SCOPED timing relief, not full galaxy-formation closure",
        "grid": grid,
        "objects": objects,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "jwst_formation_time_table_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"rows": len(grid), "objects": len(objects), "z10_ratio": grid[0]["ratio"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
