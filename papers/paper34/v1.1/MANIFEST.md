# Paper 34 v1.1 Bundle Manifest

## Documentation

- `README.md`: run instructions, scope, headline values, and claim boundary.
- `VERSION.md`: version lock and update policy.
- `CITATION.cff`: citation metadata for this support bundle.
- `MANIFEST.md`: this file.

## Environment

- `environment/requirements.txt`: Python dependency note.
- `environment/external_dependencies.md`: external data and non-vendoring note.

## Scripts

- `scripts/README.md`
  - Script inventory, run order, dependencies, outputs, and claim boundaries.
- `scripts/01_compute_hext_grid.py`
  - Computes the full `(alpha,n)` grid.
  - Rewrites `results/hext_grid_results.json`.
- `scripts/02_compare_to_published_measurements.py`
  - Computes the six-method published-measurement comparison scorecard.
  - Rewrites `results/published_measurements_comparison_results.json`.
- `scripts/03_run_anti_fit_check.py`
  - Computes the anti-fit backstop table and payload-rival diagnostics.
  - Rewrites `results/anti_fit_check_results.json`.
- `scripts/04_validate_expected_outputs.py`
  - Fast validation of frozen outputs.

## Data

- `data/imported_constants.json`
  - Framework constants, admissible grid values, and imported published H0
    comparison values with source links.

## Results

- `results/hext_grid_results.json`
  - Output of the full H_ext grid computation.
- `results/published_measurements_comparison_results.json`
  - Output of the six-method comparison script.
- `results/anti_fit_check_results.json`
  - Output of the anti-fit check script.

## Reports

- `reports/paper34_hext_alpha_n_kappa_audit_report.md`
  - Formal kappa-style structural audit of the H_ext formula and assignments.
- `reports/paper34_hext_alpha_n_kappa_audit_results.json`
  - Machine-readable kappa-audit results.

## Excluded

- Private research-lab route-search scripts.
- Killed-route scans and scratch memos.
- Manuscript drafts and local Zenodo upload state.
- Any non-public automation database.
