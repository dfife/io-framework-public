# Paper 1 v4.1 Bundle Manifest

Classification: `verified / public-reproducibility-support / foundational-arithmetic-plus-core-registry`

## Top-Level Documentation

- `README.md`: overview, quickstart, audit boundary, and citation.
- `MANIFEST.md`: this file.
- `VERSION.md`: version metadata and release policy.
- `CITATION.cff`: machine-readable citation metadata.
- `SHA256SUMS.txt`: file checksum ledger.
- `SHA256SUMS_RELEASE.txt`: release tarball checksum.

## Environment

- `environment/requirements.txt`: Python dependency statement.
- `environment/external_dependencies.md`: external dependency notes.
- `environment/environment_seed.md`: randomness statement.
- `environment/python_version.txt`: Python compatibility note.

## Data

- `data/imported_constants.json`: physical constants, Paper 1 inputs, formulae,
  manuscript-quoted values, inherited cross-paper source pointers, and v4.1
  registry notes.

## Scripts

- `scripts/01_foundation_constants.py`
- `scripts/02_temperature_chain.py`
- `scripts/03_spectral_theorem_flags.py`
- `scripts/04_dark_energy_chain.py`
- `scripts/05_cross_paper_consistency.py`
- `scripts/06_validate_expected_outputs.py`
- `scripts/07_total_energy_density_accounting.py`
- `scripts/08_core_theorem_registry.py`
- `scripts/README.md`

## Results

- `results/foundation_constants_results.json`
- `results/temperature_chain_results.json`
- `results/spectral_theorem_flags_results.json`
- `results/dark_energy_chain_results.json`
- `results/cross_paper_consistency_results.json`
- `results/total_energy_density_accounting_results.json`
- `results/core_theorem_registry_results.json`

## Reports

- `reports/paper1_v4_0_reproducibility_reconstruction_report.md`
- `reports/paper1_v4_0_finite_horizon_readable_quotient_theorem_memo.md`
- `reports/paper1_v4_1_theorem_1Y_registry_memo.md`
- `reports/paper1_v4_1_core_inheritance_theorems_memo.md`
- `reports/paper1_v4_1_closed_s3_reduction_cosmo_reconciliation.md`
- `reports/paper1_v4_1_schwarzschild_mass_measure_theorem_memo.md`
- `reports/paper1_total_energy_prompt_response_for_claude.md`
- `reports/rovelli_vidotto_2024_planck_stars_source_ingestion_memo.md`

## Validation

Run from this directory:

```bash
python3 scripts/06_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=41 pass_count=41 fail_count=0
```
