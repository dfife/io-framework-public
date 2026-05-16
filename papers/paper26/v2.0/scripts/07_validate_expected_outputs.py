#!/usr/bin/env python3
"""Validate every frozen Paper 26 v2.0 bundle output.

This is the one-command public validator. It reruns the numbered scripts,
loads the generated JSON files, and checks the active Paper 26 values against
explicit tolerances. It exits with status 0 only if every check passes.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "01_scalar_amplitude_chain.py",
    "02_tensor_conditionals.py",
    "03_cmb_baryon_class_diagnostic.py",
    "04_tau_eff_and_damping.py",
    "05_reionization_shape_tt_check.py",
    "06_kappa_audit_summary.py",
    "c2c_analysis/01_c2c_as_forward_check.py"
]


def load_json(name: str) -> Any:
    return json.loads((BUNDLE_ROOT / "results" / name).read_text(encoding="utf-8"))


def close(actual: float, expected: float, tol: float) -> bool:
    return abs(actual - expected) <= tol


def record(checks: list[tuple[str, bool, str]], name: str, passed: bool, detail: str = "") -> None:
    checks.append((name, passed, detail))
    print(f"{'PASS' if passed else 'FAIL'} {name}{(' ' + detail) if detail else ''}")


def main() -> int:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(BUNDLE_ROOT / "scripts" / script)], check=True)

    checks: list[tuple[str, bool, str]] = []
    scalar = load_json("scalar_amplitude_chain_results.json")
    tensor = load_json("tensor_conditionals_results.json")
    baryon = load_json("cmb_baryon_class_diagnostic_results.json")
    tau = load_json("tau_eff_and_damping_results.json")
    reio = load_json("reionization_shape_tt_check_results.json")
    audit = load_json("kappa_audit_summary_results.json")
    c2c = json.loads(
        (BUNDLE_ROOT / "results" / "c2c_analysis" / "c2c_as_forward_check_results.json").read_text(
            encoding="utf-8"
        )
    )

    record(checks, "A_s", close(scalar["A_s"], 2.0072459972737347e-09, 1.0e-21))
    record(checks, "beta_omega", close(scalar["factors"]["beta_omega_S2_l1"], 17.771531752633464, 1.0e-14))
    record(checks, "g_H", close(scalar["factors"]["g_H_S2_l1"], 1.9139114172056972e-08, 1.0e-20))
    record(checks, "extrinsic_fraction", close(scalar["factors"]["extrinsic_fraction"], 0.053394468273923946, 1.0e-15))
    record(checks, "A_s_sigma_delta", close(scalar["sigma_delta_vs_Planck"], -3.09180009087551, 1.0e-12))
    record(checks, "tensor_r_min", close(tensor["quoted_range"]["r_min"], 0.0004493164700207459, 1.0e-18))
    record(checks, "tensor_r_max", close(tensor["quoted_range"]["r_max"], 0.000635429445700943, 1.0e-18))
    record(checks, "omega_b_eff", close(baryon["baryon_values"]["omega_b_eff"], 0.0291, 1.0e-15))
    record(checks, "onefluid_chi2", close(baryon["diagnostic_rows"]["onefluid_eff"]["chi2_TT_highl"], 2281.086162276891, 1.0e-12))
    record(checks, "typed_native_chi2", close(baryon["diagnostic_rows"]["typed_native_geomchem_effacoustic"]["chi2_TT_highl"], 8133.4934835173035, 1.0e-9))
    record(checks, "typed_native_delta_chi2", close(baryon["diagnostic_rows"]["typed_native_geomchem_effacoustic"]["delta_chi2_TT_highl_vs_onefluid"], 5852.407321240413, 1.0e-9))
    record(checks, "tau_eff", close(tau["tau_eff_IO"], 0.02743640887145733, 1.0e-15))
    record(checks, "damping_factor", close(tau["damping_factor_exp_minus_K_gauge"], 0.9466055317260761, 1.0e-15))
    record(checks, "A_eff", close(tau["A_eff"], 1.9000701645543414e-09, 1.0e-21))
    record(checks, "reio_delta_chi2", close(reio["max_delta_chi2_TT_highl"], 0.3706526281876412, 1.0e-12))
    record(checks, "reio_less_than_0p4", reio["passes_less_than_0p4_claim"] is True)
    record(checks, "kappa_no_hidden_parameter", audit["hidden_continuous_parameter_found"] is False)
    record(checks, "visible_conditionals_count", len(audit["visible_conditionals"]) == 3)
    record(checks, "C3_closed_present", "C3" in audit["closed_conditional_verified"])
    record(checks, "R4_FIRAS_metadata", close(audit["R4_FIRAS"], 1.0031014644, 1.0e-12))
    record(checks, "c2c_forward_A_s", close(c2c["paper26_body_formula_terms"]["A_s"], 2.0072459972737347e-09, 1.0e-21))
    record(checks, "c2c_squared_guard", c2c["appendix_formula_guard"]["matches_body_A_s"] is False)

    pass_count = sum(1 for _, passed, _ in checks if passed)
    fail_count = len(checks) - pass_count
    print(f"SUMMARY total_checks={len(checks)} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
