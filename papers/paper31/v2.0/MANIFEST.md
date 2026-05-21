# Manifest

## Scripts

- `paper31_neff_delta_spectral_weight_derivation.py` — compact thermal
  spectral-weight audit.
- `paper31_planck_weyl_halforder_refit.py` — PlanckLite refit with the
  half-order Weyl kernel.
- `paper31_planck_weyl_exact_curved_refit.py` — PlanckLite refit with the exact
  curved Weyl-kernel implementation.
- `paper31_planck_weyl_tilt_scan.py` and
  `paper31_planck_weyl_tilt_refit.py` — free-tilt surrogate checks.
- `paper31_practical_io_cl_confrontation.py` — practical CMB confrontation
  branch.
- `paper31_practical_io_baryon_slot_audit.py` — baryon-slot audit.
- `paper31_lya_bao_end_to_end_inheritance_theorem.py` — Ly-alpha BAO
  inheritance check.
- `paper31_seam3_eg_pipeline.py` — E_G and lensing pipeline check.
- `paper31_background_baryon_slot_resolution_audit.py` — background baryon-slot
  resolution audit.
- `paper31_recombination_clock_transport_check.py` — recombination-clock
  transport check.
- `paper31_schur_neff_necessity_audit.py` — Schur-branch N_eff audit.
- `paper31_full_recompute_legacy_branch.py` — canonical active-branch
  reconciliation source for galaxy BAO, S8, E_G, tau, and Weyl-kernel values.
- `paper31_seam3_joint_alpha_as_fit.py` — archived joint S8 + E_G package
  comparison, including the no-slip baseline.
- `paper31_cmb_acoustic_operator_family_theorem.py` — R-leg kill and acoustic
  operator-family audit.
- `paper31_cmb_optical_history_complement_theorem.py` — optical-history
  complement and transfer-function delta-chi2 audit.
- `paper31_cmb_source_operator_nogo.py` — source-route exclusion audit.
- `09_reconcile_manuscript_claims.py` — public manuscript-claim reconciliation
  summary used by the expanded validator.
- `08_validate_expected_outputs.py` — public frozen-output validator.

## Results

The `results/` directory contains the frozen JSON/CSV outputs used by the
validator and the CMB residual CSV products. The reconciliation entry point is
`results/paper31_v2_0_manuscript_reconciliation_results.json`.

## Data

The `data/upstream_paper29/` directory contains the public Paper 29 cross-paper
context files used only to expose the chronometer + DESI `chi2 = 42.48` claim
boundary. The source labels that value as legacy Schur-context material; it is
not treated as an active-branch reproducer by this bundle.

## Reports

The `reports/` directory contains the corresponding run reports and theorem or
audit memos that document the chain boundaries for the archived computations.

## Figures

The `figures/` directory contains the archived practical CMB residual plot.
