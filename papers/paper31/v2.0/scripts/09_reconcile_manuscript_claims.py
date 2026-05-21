#!/usr/bin/env python3
"""Build the Paper 31 v2.0 manuscript-claim reconciliation summary.

This script is intentionally lightweight: it collects the archived canonical
Paper 31 result files that close the pre-Zenodo audit gaps and emits one
machine-readable summary plus a short report. Heavy CLASS/PlanckLite reruns are
kept in their original scripts; this reconciler validates that the public
bundle exposes the manuscript-level values at canonical precision.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
REPORTS = ROOT / "reports"
DATA = ROOT / "data"

OUT_JSON = RESULTS / "paper31_v2_0_manuscript_reconciliation_results.json"
OUT_REPORT = REPORTS / "paper31_v2_0_manuscript_reconciliation_report.md"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    full = load_json(RESULTS / "paper31_full_recompute_legacy_branch_results.json")
    joint = load_json(RESULTS / "paper31_seam3_joint_alpha_as_fit_results.json")
    acoustic = load_json(RESULTS / "paper31_cmb_acoustic_operator_family_theorem_results.json")
    optical = load_json(RESULTS / "paper31_cmb_optical_history_complement_theorem_results.json")
    nogo = load_json(RESULTS / "paper31_cmb_source_operator_nogo_results.json")
    practical = load_json(RESULTS / "paper31_practical_io_cl_confrontation_results.json")

    paper29_path = DATA / "upstream_paper29" / "paper29_iid_branch_chi2_recompute_results.json"
    paper29 = load_json(paper29_path) if paper29_path.exists() else {}
    legacy_chi2 = (
        paper29.get("legacy_comparison", {})
        .get("paper29_dead_schur_claims", {})
    )

    active = full["active_parameters"]
    bao = full["bao_galaxy_block"]
    rd = full["geometric_pre_drag_ruler"]["r_d_mpc"]
    galaxy_target = bao["galaxy_target_mpc"]

    s8_eg = full["sigma8_s8_eg"]
    eg_all = s8_eg["E_G_group_fits"]["all"]
    package = joint["package_comparison"]

    r_leg = acoustic["branches"]["control"]
    optical_named = optical["named_points"]
    source_cases = nogo["cases"]

    reconciliation = {
        "metadata": {
            "paper": 31,
            "version": "v2.0",
            "purpose": "pre-Zenodo manuscript/bundle numerical reconciliation",
            "canonical_precision_note": (
                "Canonical active-branch constants are taken from "
                "paper31_full_recompute_legacy_branch_results.json; x is "
                "1.5189873277742727, displayed in the manuscript as 1.51899."
            ),
        },
        "active_branch_constants": active,
        "galaxy_bao_closure": {
            "r_d_geometric_pre_drag_mpc": rd,
            "desi_dr2_galaxy_block_target_mpc": galaxy_target,
            "post_readout_effective_ruler_proxy_mpc": bao["effective_ruler_proxy_mpc"],
            "post_readout_residual_fraction": bao["residual_fraction_vs_target"],
            "post_readout_residual_percent": bao["residual_percent_vs_target"],
            "raw_ruler_residual_fraction": (galaxy_target - rd) / galaxy_target,
            "raw_ruler_residual_percent": 100.0 * (galaxy_target - rd) / galaxy_target,
        },
        "weak_lensing_and_E_G": {
            "Sigma_IO": s8_eg["Sigma_IO"],
            "S8_weyl": s8_eg["S8_weyl"],
            "S8_clustering": s8_eg["sigma8_clustering"],
            "E_G_alpha_phi_best": eg_all["alpha_best"],
            "E_G_alpha_phi_1sigma_lower": eg_all["alpha_1sigma_lo"],
            "E_G_alpha_phi_1sigma_upper": eg_all["alpha_1sigma_hi"],
            "E_G_chi2_best": eg_all["chi2_best"],
            "joint_chi2_with_slip_alpha2_old_As": package["alpha2_old_As"]["chi2_total"],
            "joint_chi2_no_slip": package["active_no_slip"]["chi2_total"],
            "joint_chi2_with_slip_label": (
                "alpha_phi=2 with original Paper 26 A_s package; this is the "
                "manuscript's 5.85 rounded comparison against no-slip."
            ),
        },
        "native_amplitude_and_tau": {
            "A_s_native": practical["constants"]["A_s_native"],
            "A_eff_backbone_control": practical["cases"]["io_backbone_control"]["analysis"]["A_eff_proxy"],
            "tau_cov": full["tau_reconciliation"]["tau_cov"],
            "tau_cov_formula": "K_gauge / 2",
        },
        "cmb_weyl_kernel": full["cmb_weyl_halforder_kernel"],
        "r_leg_kill_chi2": {
            "baseline_metric_weyl": r_leg["baseline"]["chi2"],
            "r_eff": r_leg["physical_points"]["r_eff"]["chi2"],
            "r_geom": r_leg["physical_points"]["r_geom"]["chi2"],
            "r_cluster": r_leg["physical_points"]["r_cluster"]["chi2"],
        },
        "source_route_exclusions": {
            key: value["result"]["chi2_TTTEEE_lowTT"]
            for key, value in source_cases.items()
        },
        "transfer_function_complement": {
            "baseline_chi2": optical["baseline"]["chi2"],
            "best_checked_case": "theorem_candidate_common_fGamma2",
            "best_checked_case_chi2": optical_named["theorem_candidate_common_fGamma2"]["chi2"],
            "best_checked_case_delta_chi2_vs_baseline": optical_named[
                "theorem_candidate_common_fGamma2"
            ]["delta_chi2_vs_baseline"],
            "visibility_only_delta_chi2_vs_baseline": optical_named[
                "theorem_candidate_visibility_only_fGamma2"
            ]["delta_chi2_vs_baseline"],
        },
        "chronometer_plus_desi_crosspaper": {
            "source_file": str(paper29_path.relative_to(ROOT)) if paper29_path.exists() else None,
            "archived_combined_chi2": legacy_chi2.get("combined_chi2"),
            "archived_cc_chi2": legacy_chi2.get("cc_chi2"),
            "archived_bao_chi2": legacy_chi2.get("bao_chi2"),
            "lcdm_comparator_chi2_claim": 44.80,
            "status": (
                "archived legacy-context value only; the available source JSON labels "
                "42.48 under paper29_dead_schur_claims, so this bundle does not "
                "upgrade it to an active-branch reproducer."
            ),
        },
    }

    OUT_JSON.write_text(json.dumps(reconciliation, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Paper 31 v2.0 Manuscript Reconciliation",
        "",
        "Canonical active-branch constants are read from "
        "`paper31_full_recompute_legacy_branch_results.json`.",
        "",
        "## Resolved Values",
        "",
        f"- `x = {active['x']}` (`1.51899` manuscript display).",
        f"- `r_d = {rd:.12f} Mpc`; DESI galaxy-block target "
        f"`{galaxy_target:.12f} Mpc`; post-readout residual "
        f"`{bao['residual_percent_vs_target']:.6f}%`; raw-ruler residual "
        f"`{100.0 * (galaxy_target - rd) / galaxy_target:.6f}%`.",
        f"- `S8_weyl = {s8_eg['S8_weyl']:.12f}`.",
        f"- `E_G alpha_phi = {eg_all['alpha_best']:.3f}` with 1 sigma "
        f"`[{eg_all['alpha_1sigma_lo']:.3f}, {eg_all['alpha_1sigma_hi']:.3f}]`; "
        f"`chi2_best = {eg_all['chi2_best']:.12f}`.",
        f"- Joint `S8 + E_G` with slip, alpha=2, original Paper 26 A_s: "
        f"`chi2 = {package['alpha2_old_As']['chi2_total']:.12f}`.",
        f"- Joint no-slip baseline: `chi2 = {package['active_no_slip']['chi2_total']:.12f}`.",
        f"- `A_s = {practical['constants']['A_s_native']:.16e}`; "
        f"`A_eff = {practical['cases']['io_backbone_control']['analysis']['A_eff_proxy']:.16e}`; "
        f"`tau = {full['tau_reconciliation']['tau_cov']:.12f}`.",
        "",
        "## Audit Boundary",
        "",
        "The cosmic-chronometer + DESI `42.48` value is archived here from the "
        "public Paper 29 cross-paper data, but that source labels it as "
        "`paper29_dead_schur_claims`. It is therefore exposed for manuscript "
        "traceability, not promoted by this bundle as an active-branch reproducer.",
    ]
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
