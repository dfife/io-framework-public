# Manifest

## Root Files

- `README.md` - bundle overview and quickstart.
- `MANIFEST.md` - file inventory.
- `VERSION.md` - version and constants snapshot.
- `CITATION.cff` - citation metadata.
- `LICENSE` - MIT license.
- `CONSTRUCTION_SUMMARY.md` - script/input/output summary.
- `INVENTORY_REPORT.md` - inclusion/exclusion decisions.
- `SHA256SUMS.txt` - file checksums generated at bundle build time.

## Environment

- `environment/requirements.txt`
- `environment/external_dependencies.md`

## Data

- `data/upstream_paper29/*.json` - frozen Paper 29 v2.0 upstream outputs.
- `data/legacy_context/*.json` - frozen legacy-context outputs used only for comparison columns.
- `data/external_cache/` - runtime cache for public fetched observational files; not required to be prepopulated.

## Scripts

- `scripts/01_full_twenty_test_recompute.py`
- `scripts/02_validate_expected_outputs.py`

## Results

- `results/full_twenty_test_recompute_results.json`
- `results/validation_results.json`

## Reports

- `reports/full_twenty_test_recompute_report.md`
- `reports/k_style_audit_and_r4_report.md`
