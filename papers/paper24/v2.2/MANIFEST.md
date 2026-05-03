# Paper 24 v2.2 Bundle Manifest

## Documentation

- `README.md`: run instructions, scope, headline values, and claim boundary.
- `VERSION.md`: version lock and update policy.
- `CITATION.cff`: citation metadata for this support bundle.
- `MANIFEST.md`: this file.

## Environment

- `environment/requirements.txt`: Python packages used by the public scripts.
- `environment/external_dependencies.md`: PRyMordial and external convention
  notes.

## Scripts

- `scripts/01_compute_qtrans_carrier.py`
  - Public, self-contained carrier audit.
  - Rewrites `results/qtrans_carrier_results.json`.
- `scripts/README.md`
  - Script inventory, run order, dependencies, outputs, and claim boundaries.
- `scripts/02_recompute_excited_state_import.py`
  - Recomputes Henderson import cases and writes
    `results/excited_state_import_recomputation_results.json`.
  - Full execution imports the PRyMordial scorecard script.
- `scripts/03_run_final_bbn_scorecard.py`
  - PRyMordial-dependent full scorecard script.
  - Rewrites `results/final_excited_branch_results.json` and
    `results/final_excited_branch_report.txt`.
- `scripts/04_validate_expected_outputs.py`
  - Fast validation of frozen outputs.

## Data

- `data/imported_constants.json`: compact table of constants and imported
  source values used by the bundle.
- `data/README.md`: data-source and non-vendoring notes.

## Results

- `results/qtrans_carrier_results.json`
  - Output of the final-state quadrupole carrier audit.
- `results/final_excited_branch_results.json`
  - Output of the final excited-branch kernel and PRyMordial scorecard.
- `results/excited_state_import_recomputation_results.json`
  - Output of the Paper 24 v2.2 Henderson excited-state import recomputation.

## Reports

- `reports/final_excited_branch_report.txt`
  - Human-readable final excited-branch scorecard report.
- `reports/excited_state_import_recomputation_memo.md`
  - Henderson import recomputation memo.
- `reports/qtrans_ex_formula_documentation_memo.md`
  - Audit formula for `B(E2 down) -> Q_trans,ex,imp`.

## Excluded

- PRyMordial source code.
- Private class-automation database.
- Exploratory GSM/AZURE2 class-search scripts.
- Scratch PDFs or locally downloaded source copies.
- Failed-route memos not used by Paper 24 v2.2.
