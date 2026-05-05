# Paper 26 v1.2 Bundle Manifest

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

- `data/imported_constants.json`: framework constants, conditional premises,
  scalar-amplitude factors, tensor branch numbers, tau/damping values, CMB
  baryon diagnostics, and reionization-shape diagnostics.
- `data/external_data_sources.md`: external-data and CLASS/Planck
  redistribution boundary.

## Environment

- `environment/requirements.txt`: Python dependency note.
- `environment/python_version.txt`: recommended Python version.
- `environment/apt_packages.txt`: system-package note.
- `environment/environment_seed.md`: random-seed note.
- `environment/external_dependencies.md`: dependency boundary note.

## Scripts

- `scripts/01_scalar_amplitude_chain.py`
- `scripts/02_tensor_conditionals.py`
- `scripts/03_cmb_baryon_class_diagnostic.py`
- `scripts/04_tau_eff_and_damping.py`
- `scripts/05_reionization_shape_tt_check.py`
- `scripts/06_kappa_audit_summary.py`
- `scripts/07_validate_expected_outputs.py`
- `scripts/README.md`

## Results

- `results/scalar_amplitude_chain_results.json`
- `results/tensor_conditionals_results.json`
- `results/cmb_baryon_class_diagnostic_results.json`
- `results/tau_eff_and_damping_results.json`
- `results/reionization_shape_tt_check_results.json`
- `results/kappa_audit_summary_results.json`

## Reports

- `reports/paper26_kappa_audit_report.md`
- `reports/paper26_kappa_audit_results.json`
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
python3 papers/paper26/v1.2/scripts/07_validate_expected_outputs.py
```

Expected summary:

```text
SUMMARY total_checks=18 pass_count=18 fail_count=0
```
