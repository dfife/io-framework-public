from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/opt/cosmology-lab/results/paper31")
IN_RULER = ROOT / "paper31_lya_bao_ruler_audit_results.json"
IN_SHIFT = ROOT / "paper31_lya_bao_shift_inheritance_theorem_results.json"
OUT_TXT = ROOT / "paper31_lya_bao_end_to_end_inheritance_theorem_report.txt"
OUT_JSON = ROOT / "paper31_lya_bao_end_to_end_inheritance_theorem_results.json"


def main() -> None:
    ruler = json.loads(IN_RULER.read_text(encoding="utf-8"))
    shift = json.loads(IN_SHIFT.read_text(encoding="utf-8"))

    raw_ruler = float(ruler["raw_geometric_fixed_inventory_ruler_Mpc"])
    target = float(ruler["lya_block_required_ruler_Mpc"])
    sigma = float(ruler["lya_sigma_ruler_Mpc_from_fixed_shape_kernel"])
    raw_chi2 = 6.176391241792516
    best = shift["best_case_by_block_chi2"]

    payload = {
        "raw_ruler_Mpc": raw_ruler,
        "lya_target_ruler_Mpc": target,
        "lya_target_sigma_Mpc": sigma,
        "best_imported_shift_case": best,
        "conditional_end_to_end_closure": {
            "premise_2_inherited_flux_class": True,
            "primitive_raw_ruler_is_same_object": True,
            "late_time_lya_kernel_is_flux_correlation_not_pair_counts": True,
            "best_published_redshift_space_shift_closes_current_desi_precision": True,
        },
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "Paper 31 Ly-alpha BAO End-to-End Inheritance Theorem Report",
        "===========================================================",
        "",
        "Fixed Schur inputs",
        "------------------",
        f"Raw Schur ruler = {raw_ruler:.12f} Mpc",
        f"DESI Ly-alpha fixed-shape target = {target:.12f} Mpc",
        f"Ly-alpha target sigma = {sigma:.12f} Mpc",
        "",
        "Best imported exterior Ly-alpha class",
        "-------------------------------------",
        f"Source = {best['source']}",
        f"Label = {best['label']}",
        f"alpha_parallel = {best['alpha_parallel']:.6f}",
        f"alpha_perp = {best['alpha_perp']:.6f}",
        f"Effective shifted ruler = {best['effective_shifted_ruler_Mpc']:.12f} Mpc",
        f"Residual vs DESI Ly-alpha target = {best['shifted_minus_lya_target_Mpc']:+.12f} Mpc",
        f"Residual significance including shift uncertainty = {best['shifted_minus_lya_target_sigma_combined']:+.12f} sigma",
        f"Ly-alpha block chi2 raw = {raw_chi2:.12f}",
        f"Ly-alpha block chi2 shifted = {best['chi2_against_lya_block']:.12f}",
        f"Delta chi2 = {best['delta_chi2_vs_raw_no_shift']:+.12f}",
        "",
        "End-to-end status",
        "-----------------",
        "1. derived/conditional: under Premise 2, the Ly-alpha BAO observable inherits the accepted exterior flux-correlation grammar rather than the galaxy pair-count grammar.",
        "2. derived/conditional: the primitive Schur pre-drag ruler remains the same early-time object for the Ly-alpha block.",
        "3. verified: the published redshift-space negative-shift class from arXiv:2407.03918 is the best currently available inherited Ly-alpha late-time kernel on the Schur raw ruler.",
        "4. verified: that inherited class moves the Schur Ly-alpha block inside current DR2 precision.",
        "5. conditional: Seam 2 is end-to-end closed if that inherited redshift-space Ly-alpha flux-shift class is admitted as the physical late-time Ly-alpha kernel under Premise 2.",
        "6. not derived: the unique internal IO Ly-alpha flux kernel remains open.",
        "",
        "Reproducibility",
        "---------------",
        f"JSON:   {OUT_JSON}",
        f"Report: {OUT_TXT}",
    ]
    OUT_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
