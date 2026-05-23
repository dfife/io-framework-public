# Paper 1 v4.0 Bundle Manifest

Classification: `verified / public-reproducibility-support / foundational-arithmetic`

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
  manuscript-quoted values, and inherited cross-paper source pointers.

## Scripts

- `scripts/01_foundation_constants.py`
- `scripts/02_temperature_chain.py`
- `scripts/03_spectral_theorem_flags.py`
- `scripts/04_dark_energy_chain.py`
- `scripts/05_cross_paper_consistency.py`
- `scripts/06_validate_expected_outputs.py`
- `scripts/README.md`

## Results

- `results/foundation_constants_results.json`
- `results/temperature_chain_results.json`
- `results/spectral_theorem_flags_results.json`
- `results/dark_energy_chain_results.json`
- `results/cross_paper_consistency_results.json`

## Reports

- `reports/paper1_v4_0_reproducibility_reconstruction_report.md`

## Validation

Run from this directory:

```bash
python3 scripts/06_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=24 pass_count=24 fail_count=0
```
