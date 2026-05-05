# Paper 17 v1.5 Bundle Manifest

## Top-Level Files

- `README.md`: bundle overview, quickstart, claim boundary, citation.
- `MANIFEST.md`: this inventory.
- `VERSION.md`: paper and bundle version metadata.
- `CITATION.cff`: machine-readable citation metadata.
- `LICENSE`: reuse and attribution note.
- `CONSTRUCTION_SUMMARY.md`: script-to-claim mapping.
- `INVENTORY_REPORT.md`: included/excluded artifact inventory.
- `SHA256SUMS.txt`: SHA256 checksums for bundle files.

## Data

- `data/imported_constants.json`: framework constants and FIRAS datum used by
  the scripts.
- `data/external_data_sources.md`: external-data and licensing boundary.

## Environment

- `environment/requirements.txt`: Python dependency note.
- `environment/python_version.txt`: recommended Python version.
- `environment/apt_packages.txt`: system-package note.
- `environment/environment_seed.md`: random-seed note.
- `environment/external_dependencies.md`: dependency boundary note.

## Scripts

- `scripts/01_gauge_payload_determinant.py`
- `scripts/02_firas_fixed_r4.py`
- `scripts/03_readout_uniqueness_check.py`
- `scripts/04_modular_projection_surrogate.py`
- `scripts/05_foundation_closure_toy_model.py`
- `scripts/06_framework_constructible_uniqueness_summary.py`
- `scripts/07_r4_no_go_registry.py`
- `scripts/08_kappa_audit_summary.py`
- `scripts/09_validate_expected_outputs.py`
- `scripts/README.md`

## Results

- `results/gauge_payload_determinant_results.json`
- `results/firas_fixed_r4_results.json`
- `results/readout_uniqueness_results.json`
- `results/modular_projection_surrogate_results.json`
- `results/foundation_closure_toy_model_results.json`
- `results/framework_constructible_uniqueness_results.json`
- `results/r4_no_go_registry_results.json`
- `results/kappa_audit_summary_results.json`
- `results/sigma_candidate_enumeration_summary.json`
- `results/sigma_consistency_sweep_summary.json`

## Reports

- `reports/paper17_kappa_audit_report.md`
- `reports/paper17_kappa_audit_results.json`
- `reports/paper17_r4_impossibility_theorem_report.md`
- `reports/paper17_r4_impossibility_theorem_results.json`
- `reports/paper17_r4_one_efold_normalization_audit_report.md`
- `reports/paper17_r4_one_efold_normalization_audit_results.json`
- `reports/paper17_r4_firas_uniqueness_consensus_outcome.md`
- `reports/paper17_r4_firas_uniqueness_consensus_outcome_results.json`
- `reports/paper17_vnext_r4_firas_uniqueness_blast_radius_report.md`
- `reports/paper17_vnext_r4_firas_uniqueness_blast_radius_results.json`
- `reports/paper17_modular_projection_report.txt`
- `reports/paper17_foundation_closure_report.txt`
- `reports/paper17_sigma_candidate_enumeration_report.txt`
- `reports/paper17_sigma_consistency_sweep_report.txt`

## Validation

Validator command from repository root:

```bash
python3 papers/paper17/v1.5/scripts/09_validate_expected_outputs.py
```

Expected summary:

```text
SUMMARY total_checks=24 pass_count=24 fail_count=0
```
