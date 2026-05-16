#!/usr/bin/env python3
"""Validate every frozen JSON output in the Paper 27 v2.0 bundle.

This is the referee entry point.  It reruns scripts 01-07, loads their JSON
outputs, and checks the manuscript-facing values and status labels.  Exit code
0 means all checks passed; any mismatch raises with the failing claim name.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from _common import BUNDLE_ROOT, RESULTS_DIR, assert_close


SCRIPT_DIR = Path(__file__).resolve().parent


EXPECTED_FILES = {
    "c1a": "c1a_cross_term_vanishing_results.json",
    "ccr": "spatial_ccr_lift_results.json",
    "residual": "residual_cone_and_closed_geometry_results.json",
    "passivity": "backreaction_passivity_results.json",
    "rigidity": "bridge_rigidity_observable_exhaustion_results.json",
    "visibility": "visibility_and_inheritance_results.json",
    "audit": "kappa_r4_audit_summary_results.json",
}


def run_script(script_name: str) -> None:
    path = SCRIPT_DIR / script_name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.compute()
    module.write_result(EXPECTED_FILES_FOR_SCRIPT[script_name], result)


EXPECTED_FILES_FOR_SCRIPT = {
    "01_c1a_cross_term_vanishing.py": EXPECTED_FILES["c1a"],
    "02_spatial_ccr_lift.py": EXPECTED_FILES["ccr"],
    "03_residual_cone_and_closed_geometry.py": EXPECTED_FILES["residual"],
    "04_backreaction_passivity.py": EXPECTED_FILES["passivity"],
    "05_bridge_rigidity_observable_exhaustion.py": EXPECTED_FILES["rigidity"],
    "06_visibility_and_inheritance.py": EXPECTED_FILES["visibility"],
    "07_kappa_r4_audit_summary.py": EXPECTED_FILES["audit"],
}


def load_result(key: str) -> dict:
    return json.loads((RESULTS_DIR / EXPECTED_FILES[key]).read_text(encoding="utf-8"))


def main() -> int:
    for script in EXPECTED_FILES_FOR_SCRIPT:
        run_script(script)

    checks = 0
    passed = 0

    c1a = load_result("c1a")
    checks += 1
    assert c1a["representation_check"]["invariant_hom_dimension"] == 0
    passed += 1

    ccr = load_result("ccr")
    checks += 1
    assert ccr["topology_check"]["first_betti_number"] == 0
    passed += 1

    residual = load_result("residual")
    checks += 1
    assert residual["rank_one_quotient_dimension"] == 1
    passed += 1
    checks += 1
    assert_close(
        "boundary_l1_beta_omega",
        residual["closed_geometry_exponents"]["boundary_l1_beta_omega"],
        17.771531752633464,
        1e-12,
    )
    passed += 1

    passivity = load_result("passivity")
    checks += 1
    assert passivity["full_state_selected"] is False
    passed += 1

    rigidity = load_result("rigidity")
    checks += 1
    assert_close(
        "boundary_covariance_l1_occupation",
        rigidity["boundary_covariance_l1_occupation"],
        1.9139114172056972e-08,
        1e-20,
    )
    passed += 1
    checks += 1
    assert rigidity["statuses"]["27.11.4"] == "DERIVED/NO-GO"
    passed += 1

    visibility = load_result("visibility")
    checks += 1
    assert_close("omega_b_visibility", visibility["omega_b_visibility"], 0.02910, 1e-12)
    passed += 1

    audit = load_result("audit")
    checks += 1
    assert_close("R4_FIRAS", audit["R4_FIRAS"], 1.0031014644, 1e-12)
    passed += 1
    checks += 1
    assert audit["active_independent_CMB_temperature_prediction"] is False
    passed += 1

    print(f"PASS Paper 27 v2.0 validation: total checks={checks}, pass count={passed}, fail count=0")
    print(f"Bundle root: {BUNDLE_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
