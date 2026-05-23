# Paper 35 v2.0 Bundle Manifest

Classification: `verified / public-reproducibility-support / R4-FIRAS repaired / DESI same-data diagnostics extended`

This manifest inventories the Paper 35 v2.0 reproducibility bundle. File-level
SHA256 checksums are recorded in `SHA256SUMS.txt`, generated after all payload
files are finalized.

## Top-Level Documentation

- `README.md`: overview, quickstart, discipline statement, and citation block.
- `VERSION.md`: version metadata and immutable release policy.
- `CITATION.cff`: machine-readable citation metadata.
- `CONSTRUCTION_SUMMARY.md`: script-by-script construction summary.
- `MANIFEST.md`: this file.
- `SHA256SUMS.txt`: checksum ledger for bundle payload files.

## Environment

- `environment/requirements.txt`: pip dependency statement.
- `environment/python_version.txt`: Python version used.
- `environment/apt_packages.txt`: system package notes.
- `environment/environment_seed.md`: randomness/seed statement.
- `environment/external_dependencies.md`: external dependency notes.

## Data

- `data/imported_constants.json`: framework constants, FIRAS-fixed R4, standard constants, source values, and external checksums.
- `data/theorem_registry.json`: machine-readable 48-surface registry.
- `data/external_data_sources.md`: non-redistribution and external data source policy.
- `data/bibliography.md`: source pointers used by scripts and reports.

## Scripts

- `scripts/01_eta_derivation_chain.py`
- `scripts/02_temperature_assignment.py`
- `scripts/03_chiral_source_diagnostic.py`
- `scripts/04_leptogenesis_target_reduction.py`
- `scripts/05_baryogenesis_registry_summary.py`
- `scripts/06_jwst_formation_time_table.py`
- `scripts/07_desi_confrontation.py`
- `scripts/08_dark_matter_null_forecast.py`
- `scripts/09_r4_firas_impact_audit.py`
- `scripts/10_validate_expected_outputs.py`
- `scripts/README.md`

## Results

- `results/baryogenesis_registry_summary_results.json`
- `results/chiral_source_diagnostic_results.json`
- `results/dark_matter_null_forecast_results.json`
- `results/desi_confrontation_results.json`
- `results/eta_derivation_chain_results.json`
- `results/jwst_formation_time_table_results.json`
- `results/leptogenesis_target_reduction_results.json`
- `results/r4_firas_impact_audit_results.json`
- `results/temperature_assignment_results.json`

## Reports

- `reports/paper35_v12_r4_firas_kappa_audit_report.md`
- `reports/paper35_v12_r4_firas_kappa_audit_results.json`
- `reports/paper35_kappa_audit_report.md`
- `reports/paper35_kappa_audit_results.json`
- `reports/paper35_v2_desi_rca_report.md`
- `reports/paper35_v2_desi_full_rca_report.md`
- `reports/paper35_layer2_lya_shift_import_evidence_memo.md`
- `reports/paper35_conditional_verified_audit_results.md`
- `reports/paper35_conditional_verified_audit_results.json`
- `reports/theorem_registry/`: 48 theorem-surface report/result pairs plus index.

## External Data Policy

No external observational dataset is redistributed. DESI files are fetched at
runtime and checksummed. JWST, Planck, LZ, XENONnT, and PandaX-4T material is
cited, not bundled.

## Validation

Run from this directory:

```bash
python3 scripts/10_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=58 pass_count=58 fail_count=0
```
