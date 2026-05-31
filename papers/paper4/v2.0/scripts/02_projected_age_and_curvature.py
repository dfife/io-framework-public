#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "imported_constants.json").read_text())
SEC_PER_GYR = DATA["external_constants"]["seconds_per_Gyr"]
MPC = DATA["external_constants"]["Mpc_m"]


def h0_inv_gyr(h0_km_s_mpc: float) -> float:
    return (h0_km_s_mpc * 1000.0 / MPC) * SEC_PER_GYR


def age_gyr(z: float, *, h0: float, omega_m: float, omega_k: float, omega_r: float, omega_lambda: float) -> float:
    # t(a) = H0^-1 int_0^a da / sqrt(Omega_r + Omega_m a + Omega_k a^2 + Omega_Lambda a^4)
    a_max = 1.0 / (1.0 + z)

    def f(a: float) -> float:
        return a / math.sqrt(omega_r + omega_m * a + omega_k * a * a + omega_lambda * a**4)

    def simpson(a: float, b: float) -> float:
        c = 0.5 * (a + b)
        return (b - a) * (f(a) + 4.0 * f(c) + f(b)) / 6.0

    def adaptive(a: float, b: float, eps: float, whole: float, depth: int) -> float:
        c = 0.5 * (a + b)
        left = simpson(a, c)
        right = simpson(c, b)
        if depth <= 0 or abs(left + right - whole) <= 15.0 * eps:
            return left + right + (left + right - whole) / 15.0
        return adaptive(a, c, 0.5 * eps, left, depth - 1) + adaptive(c, b, 0.5 * eps, right, depth - 1)

    whole = simpson(0.0, a_max)
    return adaptive(0.0, a_max, 1e-13, whole, 50) / h0_inv_gyr(h0)


def main() -> None:
    active = DATA["active_branch"]
    lcdm = DATA["lcdm_comparator"]
    rows = []
    for z in (6, 10, 14, 20):
        t_io = age_gyr(
            z,
            h0=active["H0_km_s_Mpc"],
            omega_m=active["Omega_m"],
            omega_k=active["Omega_k"],
            omega_r=active["Omega_r"],
            omega_lambda=active["Omega_Lambda"]
        )
        t_lcdm = age_gyr(
            z,
            h0=lcdm["H0_km_s_Mpc"],
            omega_m=lcdm["Omega_m"],
            omega_k=lcdm["Omega_k"],
            omega_r=lcdm["Omega_r"],
            omega_lambda=lcdm["Omega_Lambda"]
        )
        rows.append({
            "z": z,
            "t_IO_projected_Gyr": t_io,
            "t_LCDM_Gyr": t_lcdm,
            "ratio_IO_over_LCDM": t_io / t_lcdm,
            "difference_IO_minus_LCDM_Myr": 1000.0 * (t_io - t_lcdm),
            "percent_difference": 100.0 * (t_io / t_lcdm - 1.0)
        })

    omega_k = active["Omega_k"]
    omega_lambda = active["Omega_Lambda"]
    old_apparent_w0 = -1.0 + (2.0 / 3.0) * omega_k / (omega_k + omega_lambda)

    result = {
        "paper": "Paper 4",
        "version": "v2.0",
        "status": {
            "projected_age_table": "DERIVED/CONDITIONAL_VERIFIED on active branch constants",
            "old_curvature_diagnostic": "DERIVED but superseded as presentation by Paper 35",
            "paper35_flat_cpl_reinterpretation": "VERIFIED inherited from Paper 35"
        },
        "projected_optical_age_rows": rows,
        "old_curvature_diagnostic": {
            "formula": "w0_apparent = -1 + (2/3) Omega_k/(Omega_k + Omega_Lambda)",
            "w0_apparent": old_apparent_w0,
            "presentation_boundary": "Diagnostic only; Paper 35 flat-CPL reinterpretation is the active presentation."
        },
        "paper35_flat_cpl_reinterpretation": {
            "w": -1.0,
            "w0": -1.030263043675755,
            "wa": -0.1115075206254369,
            "chi2_to_io_synthetic": 0.8578882977742515,
            "source": "/opt/cosmology-lab/results/paper35/paper35_desi_dark_energy_investigation_results.json"
        }
    }
    out = ROOT / "results" / "projected_age_and_curvature_results.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()
