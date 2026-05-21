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
        (
            "canonical active-branch x",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "active_branch_constants.x",
            1.5189873277742727,
        ),
        (
            "canonical active-branch H0",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "active_branch_constants.H0",
            67.57585653582628,
        ),
        (
            "canonical active-branch Omega_m",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "active_branch_constants.Omega_m",
            0.34868395067621694,
        ),
        (
            "canonical active-branch Omega_k",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "active_branch_constants.Omega_k",
            -0.04579112576013168,
        ),
        (
            "canonical active-branch Omega_lambda",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "active_branch_constants.Omega_lambda",
            0.69701575761593,
        ),
        (
            "galaxy BAO geometric pre-drag sound horizon",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "galaxy_bao_closure.r_d_geometric_pre_drag_mpc",
            144.01351425392883,
        ),
        (
            "galaxy BAO DESI DR2 target ruler",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "galaxy_bao_closure.desi_dr2_galaxy_block_target_mpc",
            147.08990960071066,
        ),
        (
            "galaxy BAO post-readout residual percent",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "galaxy_bao_closure.post_readout_residual_percent",
            0.8758010484411605,
        ),
        (
            "galaxy BAO raw-ruler residual percent",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "galaxy_bao_closure.raw_ruler_residual_percent",
            2.091506722067466,
        ),
        (
            "canonical Weyl-response S8",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.S8_weyl",
            0.8338721696752849,
        ),
        (
            "canonical E_G alpha_phi best",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.E_G_alpha_phi_best",
            2.005,
        ),
        (
            "canonical E_G alpha_phi 1sigma lower",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.E_G_alpha_phi_1sigma_lower",
            1.785,
        ),
        (
            "canonical E_G alpha_phi 1sigma upper",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.E_G_alpha_phi_1sigma_upper",
            2.247,
        ),
        (
            "canonical E_G chi2 best",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.E_G_chi2_best",
            5.817022925773303,
        ),
        (
            "joint S8 plus E_G chi2 with slip",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.joint_chi2_with_slip_alpha2_old_As",
            5.854740682707307,
        ),
        (
            "joint S8 plus E_G no-slip chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "weak_lensing_and_E_G.joint_chi2_no_slip",
            125.49981098047948,
        ),
        (
            "native A_s",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "native_amplitude_and_tau.A_s_native",
            2.0072459972737347e-09,
        ),
        (
            "native A_eff",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "native_amplitude_and_tau.A_eff_backbone_control",
            1.9000701645543414e-09,
        ),
        (
            "native tau K_gauge over two",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "native_amplitude_and_tau.tau_cov",
            0.02743640887145733,
        ),
        (
            "R-leg kill baseline chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "r_leg_kill_chi2.baseline_metric_weyl",
            2834.716042331566,
        ),
        (
            "R-leg kill r_eff chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "r_leg_kill_chi2.r_eff",
            4206.728413458745,
        ),
        (
            "R-leg kill r_geom chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "r_leg_kill_chi2.r_geom",
            20683.683798095575,
        ),
        (
            "R-leg kill r_cluster chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "r_leg_kill_chi2.r_cluster",
            69000.51334374436,
        ),
        (
            "source-route onefluid control chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.onefluid_control",
            2834.7160423315654,
        ),
        (
            "source-route native zero-borrow chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.native_zero_borrow",
            3845.667111463328,
        ),
        (
            "source-route typed geom opacity geom chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.typed_geom_eff_eff_opacity_geom",
            6173.882076495199,
        ),
        (
            "source-route typed geom opacity eff chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.typed_geom_eff_eff_opacity_eff",
            5589.192222486751,
        ),
        (
            "source-route constant local visibility geom chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.typed_geom_eff_eff_opacity_geom_uniform_local",
            255291.47176950224,
        ),
        (
            "source-route constant local visibility eff chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.typed_geom_eff_eff_opacity_eff_uniform_local",
            265476.88246172864,
        ),
        (
            "source-route channel split eff-pol chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.onefluid_control_sw_geom_dop_eff_pol_eff",
            23085.10814147827,
        ),
        (
            "source-route channel split pol-one chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.onefluid_control_sw_geom_dop_eff_pol_one",
            22691.63076592728,
        ),
        (
            "source-route channel split SW-only chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "source_route_exclusions.onefluid_control_sw_geom_only",
            29917.864260910013,
        ),
        (
            "transfer-function complement best checked delta chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "transfer_function_complement.best_checked_case_delta_chi2_vs_baseline",
            -594.9887407270012,
        ),
        (
            "transfer-function visibility-only delta chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "transfer_function_complement.visibility_only_delta_chi2_vs_baseline",
            1147.96745294116,
        ),
        (
            "archived Paper 29 chronometer plus DESI chi2",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "chronometer_plus_desi_crosspaper.archived_combined_chi2",
            42.48,
        ),
        (
            "archived Paper 29 chronometer plus DESI LCDM comparator",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "chronometer_plus_desi_crosspaper.lcdm_comparator_chi2_claim",
            44.80,
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
        (
            "chronometer plus DESI active-branch reproducer boundary",
            "paper31_v2_0_manuscript_reconciliation_results.json",
            "chronometer_plus_desi_crosspaper.status",
            "archived legacy-context value only; the available source JSON labels 42.48 under paper29_dead_schur_claims, so this bundle does not upgrade it to an active-branch reproducer.",
        ),
    ]

    for label, filename, path, expected in equality_checks:
        assert_equal(label, lookup(load_json(filename), path), expected)
        checks += 1

    print(f"Paper 31 v2.0 validation passed: {checks}/{checks} checks")


if __name__ == "__main__":
    main()
