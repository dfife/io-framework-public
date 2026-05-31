# Paper 3 v2.0 Bundle Manifest

Classification: `verified / public-reproducibility-support / input-structure-arithmetic-plus-theorem-surface`

## Top-Level Documentation

- `README.md`: overview, quickstart, discipline statement, and citation.
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

- `data/imported_constants.json`: physical constants, active-branch constants,
  formulae, claim boundaries, and source pointers.

## Scripts

- `scripts/01_active_branch_constants.py`
- `scripts/02_transfer_table.py`
- `scripts/03_radicand_positivity_and_monotonicity.py`
- `scripts/04_sharp_eos_junction_limit.py`
- `scripts/05_validate_expected_outputs.py`
- `scripts/README.md`

## Results

- `results/active_branch_constants_results.json`
- `results/transfer_table_results.json`
- `results/radicand_positivity_monotonicity_results.json`
- `results/sharp_eos_junction_limit_results.json`

## Reports

- `reports/paper3_v2_0_continuity_monotonicity_theorem_memo.md`
- `reports/paper3_v2_0_sharp_eos_junction_limit_theorem_memo.md`

## Validation

Run from this directory:

```bash
python3 scripts/05_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=24 pass_count=24 fail_count=0
```
