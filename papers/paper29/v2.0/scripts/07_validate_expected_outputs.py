#!/usr/bin/env python3
"""Single-entry validation for the Paper 29 v2.0 frozen JSON outputs."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def get(payload: dict, dotted: str):
    obj = payload
    for part in dotted.split("."):
        obj = obj[part]
    return obj


CHECKS = [
    ("bao_kernel_coefficients_results.json", "inputs.K_gauge", 0.05487281774291466, 1e-12, "K_gauge"),
    ("bao_kernel_coefficients_results.json", "derived.eta", 0.036124605346983495, 1e-12, "eta"),
    ("bao_kernel_coefficients_results.json", "derived.f_perp", 1.036785027400527, 1e-12, "f_perp"),
    ("bao_kernel_coefficients_results.json", "derived.f_parallel", 1.0182264126413767, 1e-12, "f_parallel"),
    ("sound_speed_baryon_selector_results.json", "derived.paper29_banked_r_d_Mpc", 144.01351425392883, 1e-10, "r_d"),
    ("desi_chronometer_confrontation_results.json", "derived.cc_chi2_banked", 14.701523963980787, 1e-12, "CC chi2"),
    ("desi_chronometer_confrontation_results.json", "derived.bao_chi2", 27.735229301342457, 1e-9, "BAO chi2"),
    ("desi_chronometer_confrontation_results.json", "derived.combined_chi2", 42.43675326532325, 1e-9, "combined chi2"),
    ("reionization_prediction_results.json", "derived.transported_z_50pct", 10.185954753995242, 1e-9, "z_50_IO"),
    ("reionization_prediction_results.json", "derived.tau_IO_transported", 0.07373089905293533, 1e-9, "tau_IO"),
    ("21cm_prediction_results.json", "derived.io_observer_brightness_diagnostic.z_dec", 123.67217038722819, 1e-9, "z_dec"),
    ("21cm_prediction_results.json", "derived.io_observer_brightness_diagnostic.y21_reduced", -5.926231688179344, 1e-9, "y21"),
    ("21cm_prediction_results.json", "derived.io_observer_brightness_diagnostic.T21_mK", -190.78729466061188, 1e-9, "T21"),
    ("cmb_inventory_results.json", "imported_or_inherited.N_eff", 3.044, 1e-12, "N_eff"),
    ("cmb_inventory_results.json", "imported_or_inherited.Omega_k_IO", -0.04579112576013168, 1e-12, "Omega_k"),
    ("omega_m_3x2pt_results.json", "derived.Omega_m_IO", 0.34868395067621694, 1e-12, "Omega_m_IO"),
    ("fsigma8_rsd_results.json", "derived.fsigma8_z_1p2", 0.4695277101511699, 1e-12, "f_sigma8_z_1p2"),
    ("w0wa_results.json", "derived.cpl_residual_norm", 0.0, 1e-12, "w0wa_CPL_residual"),
]


def main() -> int:
    total = passed = failed = 0
    failures: list[str] = []
    for filename, path, expected, tol, label in CHECKS:
        total += 1
        payload = json.loads((RESULTS / filename).read_text(encoding="utf-8"))
        actual = float(get(payload, path))
        delta = actual - expected
        ok = math.isfinite(actual) and abs(delta) <= tol
        if ok:
            passed += 1
            print(f"PASS {label}: actual={actual:.15g} expected={expected:.15g} delta={delta:.3g}")
        else:
            failed += 1
            msg = f"FAIL {label}: actual={actual:.15g} expected={expected:.15g} delta={delta:.3g} tol={tol}"
            failures.append(msg)
            print(msg)
    print(f"Paper 29 v2.0 validation summary: total checks={total}, pass count={passed}, fail count={failed}")
    if failures:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
