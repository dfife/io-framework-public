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
- `08_validate_expected_outputs.py` — public frozen-output validator.

## Results

The `results/` directory contains the frozen JSON/CSV outputs used by the
validator and the CMB residual CSV products.

## Reports

The `reports/` directory contains the corresponding run reports and theorem or
audit memos that document the chain boundaries for the archived computations.

## Figures

The `figures/` directory contains the archived practical CMB residual plot.
