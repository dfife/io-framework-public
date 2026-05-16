# Paper 26 v2.0 Bundle Manifest

## Top-Level Files

- `README.md`: bundle overview, quickstart, claim boundary, citation.
- `MANIFEST.md`: this inventory.
- `VERSION.md`: paper and bundle version metadata.
- `CITATION.cff`: machine-readable citation metadata.
- `LICENSE`: reuse and attribution note.
- `CONSTRUCTION_SUMMARY.md`: construction notes and script-to-claim mapping.
- `INVENTORY_REPORT.md`: inventory of included and excluded artifacts.
- `SHA256SUMS.txt`: SHA256 checksums for bundle files.

## Data

- `data/imported_constants.json`: framework constants, R4/FIRAS metadata,
  active conditionals, closed C3 metadata, scalar-amplitude factors, tensor
  branch numbers, damping values, baryon diagnostics, and reionization-shape
  diagnostics.
- `data/external_data_sources.md`: external-data and CLASS/Planck
  redistribution boundary.

## Environment

- `environment/requirements.txt`: Python dependency note.
- `environment/python_version.txt`: recommended Python version.
- `environment/apt_packages.txt`: system-package note.
- `environment/environment_seed.md`: random-seed note.
- `environment/external_dependencies.md`: dependency boundary note.

## Scripts

- `scripts/01_scalar_amplitude_chain.py`: recomputes the Paper 26 scalar
  amplitude arithmetic.
- `scripts/02_tensor_conditionals.py`: freezes the conditional tensor branch
  range and scope boundary.
- `scripts/03_cmb_baryon_class_diagnostic.py`: records the baryon-class
  diagnostic ledger and frozen CLASS-support rows.
- `scripts/04_tau_eff_and_damping.py`: verifies `tau_eff`, the damping factor,
  and the Theorem 26.C3 scope metadata.
- `scripts/05_reionization_shape_tt_check.py`: validates the high-multipole
  temperature-temperature reionization-shape diagnostic.
- `scripts/06_kappa_audit_summary.py`: emits machine-readable audit metadata.
- `scripts/c2c_analysis/01_c2c_as_forward_check.py`: checks the forward
  Hawking-state scalar-amplitude arithmetic and guards against the retired
  squared-occupation formula.
- `scripts/07_validate_expected_outputs.py`: one-command frozen-output
  validator.
- `scripts/README.md`: script-level usage notes.

## Results

- `results/scalar_amplitude_chain_results.json`
- `results/tensor_conditionals_results.json`
- `results/cmb_baryon_class_diagnostic_results.json`
- `results/tau_eff_and_damping_results.json`
- `results/reionization_shape_tt_check_results.json`
- `results/kappa_audit_summary_results.json`
- `results/c2c_analysis/c2c_as_forward_check_results.json`

## Reports

- `reports/paper26_kappa_audit_report.md`
- `reports/paper26_kappa_audit_results.json`
- `reports/paper26_v2.0_full_dependency_chains.md`
- `reports/paper26_c3_reduced_source_covariance_closure_report.md`
- `reports/paper26_c3_reduced_source_covariance_closure_results.json`
- `reports/paper26_c2c_hawking_state_closure_analysis.md`
- `reports/paper26_c2c_full_closure_attempt_report.md`
- `reports/paper26_c2c_route_exhaustion_report.md`
- `reports/paper26_C2_channel_separation_audit.md`
- `reports/paper26_carrier_lift_Ucoex_audit.md`
- `reports/paper26_thomson_kernel_identity_audit.md`
- `reports/paper26_tau_routes_A_B_C_audit.md`
- `reports/paper26_reionization_shape_elimination_audit.md`
- `reports/paper26_reionization_shape_elimination_audit_results.json`
- `reports/paper26_io_native_recombination.md`
- `reports/paper26_io_native_recombination_results.json`
- `reports/paper26_S2_tensor_ratio_audit_results.json`

## Validation

Validator command from repository root:

```bash
python3 papers/paper26/v2.0/scripts/07_validate_expected_outputs.py
```

Expected summary:

```text
SUMMARY total_checks=22 pass_count=22 fail_count=0
```
