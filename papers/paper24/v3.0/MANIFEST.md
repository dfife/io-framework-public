# Paper 24 v3.0 Bundle Manifest

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
- `scripts/04_r4_firas_kappa_audit.py`
  - R4/FIRAS kappa-style audit for Paper 24 v3.0 script impact, label
    discipline, abbreviations, and IO slang.
- `scripts/05_validate_expected_outputs.py`
  - Fast validation of frozen outputs.
- `scripts/06_combined_uncertainty_propagation.py`
  - PRyMordial-free Monte Carlo propagation of combined `Q_GS` and Henderson
    `B(E2)` uncertainty through the branch-sum formula.

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
  - Output of the Paper 24 v3.0 Henderson excited-state import recomputation.
- `results/r4_firas_kappa_audit_results.json`
  - R4/FIRAS audit result showing no R4 damage to the active BBN scorecard.
- `results/combined_uncertainty_propagation_results.json`
  - Frozen `N = 100000` Monte Carlo propagation of the combined imported
    nuclear-input uncertainty band.

## Reports

- `reports/final_excited_branch_report.txt`
  - Human-readable final excited-branch scorecard report.
- `reports/excited_state_import_recomputation_memo.md`
  - Henderson import recomputation memo.
- `reports/qtrans_ex_formula_documentation_memo.md`
  - Audit formula for `B(E2 down) -> Q_trans,ex,imp`.
- `reports/paper24_v30_r4_firas_kappa_audit_report.md`
  - Kappa-style R4/FIRAS audit report and manuscript hygiene flags.
- `reports/combined_uncertainty_propagation_memo.md`
  - Human-readable summary and manuscript handoff text for §15 item 6 closure.

## Excluded

- PRyMordial source code.
- Private class-automation database.
- Exploratory GSM/AZURE2 class-search scripts.
- Scratch PDFs or locally downloaded source copies.
- Failed-route memos not used by Paper 24 v3.0.
