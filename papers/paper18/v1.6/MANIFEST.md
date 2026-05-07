# Paper 18 v1.6 Bundle Manifest

Classification: `verified / public-reproducibility-support / R4-FIRAS repaired`

File-level SHA256 checksums are recorded in `SHA256SUMS.txt`.

## Top-Level Documentation

- `README.md`: overview, quickstart, claim discipline, and citation block.
- `VERSION.md`: version metadata and release policy.
- `CITATION.cff`: machine-readable citation metadata.
- `CONSTRUCTION_SUMMARY.md`: script-by-script construction summary.
- `INVENTORY_REPORT.md`: source-script inventory and deferred external rerun notes.
- `MANIFEST.md`: this file.
- `SHA256SUMS.txt`: checksum ledger.
- `LICENSE`: reuse and external-data boundary.

## Environment

- `environment/requirements.txt`: Python package versions observed for full reruns.
- `environment/python_version.txt`: Python version.
- `environment/apt_packages.txt`: system package notes.
- `environment/environment_seed.md`: randomness statement.
- `environment/external_dependencies.md`: external dependency notes.

## Data

- `data/imported_constants.json`: framework constants, R4/FIRAS values, conditional branch inputs, and external dependency pointers.
- `data/external_data_sources.md`: non-redistribution policy and fetch/placement instructions.

## Scripts

- `scripts/01_cmp_theorem.py`
- `scripts/02_bdp_theorem.py`
- `scripts/03_bdp_gap_closure.py`
- `scripts/04_v_alpha_uniqueness.py`
- `scripts/05_neff_entropy_rank.py`
- `scripts/06_bogoliubov_coefficients.py`
- `scripts/07_modular_bogoliubov_upgrade.py`
- `scripts/08_legacy_observables_recalculation.py`
- `scripts/09_jwst_age_recalculation.py`
- `scripts/10_matter_power_shape_test.py`
- `scripts/11_zeq_kruskal_audit.py`
- `scripts/12_curvature_implementation_resolution.py`
- `scripts/13_bdp_epoch_independence_audit.py`
- `scripts/14_structural_attacks_audit.py`
- `scripts/15_r4_impact_audit.py`
- `scripts/16_kappa_audit_summary.py`
- `scripts/17_validate_expected_outputs.py`
- `scripts/README.md`

## Results

The `results/` directory contains frozen JSON outputs for every numbered script
and the v1.6 R4/kappa audit.

## Reports

The `reports/` directory contains the original Paper 18 support reports plus:

- `paper18_v16_r4_kappa_audit_report.md`
- `paper18_v16_r4_kappa_audit_results.json`
- `paper18_v16_r4_impact_audit_results.json`

## Validation

Run:

```bash
python3 scripts/17_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=30 pass_count=30 fail_count=0
```
