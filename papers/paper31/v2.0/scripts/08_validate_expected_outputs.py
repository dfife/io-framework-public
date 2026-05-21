#!/usr/bin/env python3
"""Validate frozen Paper 31 v2.0 reproducibility outputs.

This validator intentionally checks archived JSON outputs rather than rerunning
CLASS/PlanckLite. The heavy scripts are included for provenance and extended
reruns, while this entry point verifies that the public bundle contains the
expected v2.0 numerical state.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def load_json(name: str) -> Any:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def lookup(obj: Any, path: str) -> Any:
    cur = obj
    for part in path.split("."):
        if "[" in part and part.endswith("]"):
            key, index = part[:-1].split("[", 1)
            cur = cur[key][int(index)]
        else:
            cur = cur[part]
    return cur


def assert_close(label: str, actual: float, expected: float, tol: float = 1e-10) -> None:
    if not math.isclose(float(actual), float(expected), rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_equal(label: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> None:
    checks = 0

    numeric_checks = [
        (
            "N_eff spectral Delta",
            "paper31_neff_delta_spectral_weight_results.json",
            "inputs.Delta",
            5.624216852624105,
        ),
        (
            "N_eff standard equivalent if total g equals Delta",
            "paper31_neff_delta_spectral_weight_results.json",
            "normalization_boundary.standard_Neff_equivalent_if_total_g_equals_Delta",
            7.979084271625898,
        ),
        (
            "half-order Weyl refit chi2",
            "paper31_planck_weyl_halforder_refit_results.json",
            "best_fit.chi2",
            2832.405044412244,
        ),
        (
            "half-order Weyl refit tau",
            "paper31_planck_weyl_halforder_refit_results.json",
            "best_fit.tau",
            0.0021,
        ),
        (
            "half-order Weyl refit theta",
            "paper31_planck_weyl_halforder_refit_results.json",
            "best_fit.100theta_s",
            1.048176079405297,
        ),
        (
            "exact curved Weyl refit chi2",
            "paper31_planck_weyl_exact_curved_refit_results.json",
            "best_fit.chi2",
            2832.381617929708,
        ),
        (
            "exact curved Weyl refit theta",
            "paper31_planck_weyl_exact_curved_refit_results.json",
            "best_fit.100theta_s",
            1.0481760968191347,
        ),
        (
            "free tilt refit tilt",
            "paper31_planck_weyl_tilt_refit_results.json",
            "best_fit.lcmb_tilt",
            -0.4625,
        ),
        (
            "free tilt refit chi2",
            "paper31_planck_weyl_tilt_refit_results.json",
            "best_fit.chi2",
            2827.1964128641075,
        ),
        (
            "practical structured CMB chi2",
            "paper31_practical_io_cl_confrontation_results.json",
            "cases.io_conditional_structured.analysis.chi2_total",
            2135.7229871928344,
        ),
        (
            "practical backbone-control CMB chi2",
            "paper31_practical_io_cl_confrontation_results.json",
            "cases.io_backbone_control.analysis.chi2_total",
            3445.2838615131695,
        ),
        (
            "Planck LCDM reference CMB chi2",
            "paper31_practical_io_cl_confrontation_results.json",
            "cases.lcdm_planck_reference.analysis.chi2_total",
            619.3141066733623,
        ),
        (
            "fixed-CDM baryon-slot top chi2",
            "paper31_practical_io_baryon_slot_audit_fixed_cdm.json",
            "rows[0].chi2",
            1924.535754993541,
        ),
        (
            "fixed-CDM baryon-slot sanity chi2",
            "paper31_practical_io_baryon_slot_audit_fixed_cdm.json",
            "sanity.one_number_struct.chi2",
            2135.7229871928344,
        ),
        (
            "variable-CDM baryon-slot top chi2",
            "paper31_practical_io_baryon_slot_audit_variable_cdm.json",
            "rows[0].chi2",
            1938.7531781396067,
        ),
        (
            "Ly-alpha BAO raw ruler",
            "paper31_lya_bao_end_to_end_inheritance_theorem_results.json",
            "raw_ruler_Mpc",
            143.06250283686956,
        ),
        (
            "Ly-alpha imported isotropic shift",
            "paper31_lya_bao_end_to_end_inheritance_theorem_results.json",
            "best_imported_shift_case.alpha_iso",
            0.9905,
        ),
        (
            "E_G projected Schur sigma8",
            "paper31_seam3_eg_pipeline_results.json",
            "cases.projected_schur_active.sigma8",
            0.9486404440522879,
        ),
        (
            "background baryon structured baseline chi2",
            "paper31_background_baryon_slot_resolution_audit_results.json",
            "one_number_structured_baseline.result.chi2",
            2135.7229871928344,
        ),
        (
            "recombination transport z=1100 R_rec",
            "paper31_recombination_clock_transport_check_results.json",
            "transport_rows[4].R_rec",
            1.727401580832834,
        ),
        (
            "Schur audit standard N_eff chi2",
            "paper31_schur_neff_necessity_audit_results.json",
            "class_standard_vs_delta.standard_3p044.chi2",
            232.84201634033693,
        ),
    ]

    for label, filename, path, expected in numeric_checks:
        assert_close(label, lookup(load_json(filename), path), expected)
        checks += 1

    equality_checks = [
        (
            "N_eff Delta status",
            "paper31_neff_delta_spectral_weight_results.json",
            "claim_status.io_boundary_weight_equals_Delta",
            "derived_from_Paper15_Paper18_object_type",
        ),
        (
            "half-order Weyl valid flag",
            "paper31_planck_weyl_halforder_refit_results.json",
            "best_fit.valid",
            True,
        ),
        (
            "exact curved Weyl valid flag",
            "paper31_planck_weyl_exact_curved_refit_results.json",
            "best_fit.valid",
            True,
        ),
        (
            "Ly-alpha end-to-end closure flag",
            "paper31_lya_bao_end_to_end_inheritance_theorem_results.json",
            "conditional_end_to_end_closure.best_published_redshift_space_shift_closes_current_desi_precision",
            True,
        ),
    ]

    for label, filename, path, expected in equality_checks:
        assert_equal(label, lookup(load_json(filename), path), expected)
        checks += 1

    print(f"Paper 31 v2.0 validation passed: {checks}/{checks} checks")


if __name__ == "__main__":
    main()
