#!/usr/bin/env python3
"""Validate frozen outputs for the Paper 5 v2.0 public bundle."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]


def run_generators() -> None:
    for script in [
        "01_kerr_spin_temperature.py",
        "02_vaidyano_go.py",
        "03_mixed_friedmann_bbn.py",
        "04_inherited_claims.py",
    ]:
        subprocess.run([sys.executable, str(BUNDLE_ROOT / "scripts" / script)], check=True)


def load_result(name: str) -> dict:
    return json.loads((BUNDLE_ROOT / "results" / name).read_text())


def close(actual: float, expected: float, tol: float) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def main() -> int:
    run_generators()
    k = load_result("kerr_spin_temperature_results.json")
    v = load_result("vaidya_no_go_results.json")
    b = load_result("mixed_friedmann_bbn_results.json")
    i = load_result("inherited_claims_results.json")

    rows_by_z = {row["z"]: row for row in b["redshift_rows"]}
    krows = {row["spin_a_over_M"]: row for row in k["rows"]}
    checks = [
        ("kerr_status", k["status"] == "DERIVED"),
        ("kerr_ratio_spin_0", close(krows[0.0]["kappa_ratio_formula"], 1.0, 1e-15)),
        ("kerr_ratio_spin_0096", close(krows[0.096]["kappa_ratio_formula"], 0.997685321617791, 1e-15)),
        ("kerr_temperature_spin_05", close(krows[0.5]["interior_temperature_K"], 2.4719708944924506, 1e-15)),
        ("kerr_monotone", k["monotonicity_check"]["ratios_strictly_decrease_after_zero"] is True),
        ("vaidya_status", v["status"] == "DERIVED/NO-GO"),
        ("vaidya_angular_pressure_zero", v["diagnostic_components"]["angular_pressure_T_theta_theta"] == 0),
        ("vaidya_isotropic_requirement", v["diagnostic_components"]["isotropic_radiation_requires_positive_angular_pressure"] is True),
        ("bbn_status", b["status"] == "DERIVED"),
        ("bbn_ratio_z1e9", close(rows_by_z[1.0e9]["ratio_H_IO_over_H_LCDM"], 1.0008962961749086, 1e-15)),
        ("recombination_ratio_z1100", close(rows_by_z[1100.0]["ratio_H_IO_over_H_LCDM"], 1.0423603296522679, 1e-15)),
        ("z0_ratio", close(rows_by_z[0.0]["ratio_H_IO_over_H_LCDM"], 1.0027165318755586, 1e-15)),
        ("radiation_asymptotic_ratio", close(b["radiation_era_asymptotic_ratio"], 1.0008961042812452, 1e-15)),
        ("inherited_status", i["status"] == "VERIFIED"),
        ("first_peak", i["entries"][0]["value"] == 220),
        ("theta_star", close(i["entries"][1]["value"], 0.5994, 1e-15)),
        ("theta_star_sigma", close(i["entries"][1]["sigma_residual"], 9.2, 1e-15)),
    ]

    passed = 0
    for name, ok in checks:
        if ok:
            passed += 1
            print(f"PASS {name}")
        else:
            print(f"FAIL {name}")
    failed = len(checks) - passed
    print(f"SUMMARY total_checks={len(checks)} pass_count={passed} fail_count={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
