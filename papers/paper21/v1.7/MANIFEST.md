# Paper 21 v1.7 Bundle Manifest

Classification: `verified / public-reproducibility-support`

This manifest inventories the Paper 21 v1.7 reproducibility bundle. SHA256
checksums for payload files are recorded in `SHA256SUMS.txt`.

## Top-Level Documentation

- `README.md`: overview, quickstart, detailed reproduction, discipline
  statement, and citation block.
- `VERSION.md`: version metadata and immutable release policy.
- `CITATION.cff`: machine-readable citation metadata.
- `LICENSE`: bundle license note pointing to repository-level license files.
- `CONSTRUCTION_SUMMARY.md`: script-by-script construction summary.
- `INVENTORY_REPORT.md`: inclusion/exclusion rationale.
- `SHA256SUMS.txt`: checksum ledger for payload files.

## Environment

- `environment/requirements.txt`: pip dependency statement.
- `environment/python_version.txt`: Python version used.
- `environment/apt_packages.txt`: system package notes.
- `environment/environment_seed.md`: randomness/seed statement.
- `environment/external_dependencies.md`: PRyMordial and conventions notes.

## Data

- `data/imported_constants.json`: framework constants, puncture-load expected
  values, observational denominators, and frozen corrected BBN support values.
- `data/external_data_sources.md`: non-redistribution and external dependency
  policy.

## Scripts

- `scripts/01_derive_L1_puncture_load.py`
- `scripts/02_derive_L2_puncture_load.py`
- `scripts/03_compute_ac1_closure.py`
- `scripts/04_prymordial_wrapper_conventions.py`
- `scripts/05_generate_bbn_scorecard.py`
- `scripts/06_operator_algebra_live_theorem_artifacts.py`
- `scripts/07_validate_expected_outputs.py`
- `scripts/README.md`

## Results

- `results/L1_puncture_load_results.json`
- `results/L2_puncture_load_results.json`
- `results/ac1_closure_results.json`
- `results/prymordial_wrapper_conventions_results.json`
- `results/bbn_scorecard_results.json`
- `results/operator_algebra_live_theorem_artifacts_results.json`

## Reports

- `reports/paper21_kappa_audit_report.md`
- `reports/paper21_kappa_audit_results.json`
- `reports/paper21_reproducibility_script_manifest.md`

## Excluded

The private Paper 21 folder contains additional historical `P_resp` route
rerunners. They are excluded from this public bundle by PI instruction: no-go
demonstrations stay in the manuscript and audit reports; the bundle does not
rerun dead routes to prove they are still dead.

## External Data Policy

No external observational dataset is redistributed. PRyMordial is not bundled.
The public scripts validate frozen Paper 21 correction-audit outputs, wrapper
convention, denominators, and theorem-support arithmetic.
