# Paper 22 v2.0 Manifest

## Top-Level Files

- `README.md` - overview, quickstart, claim boundary, and citation note.
- `MANIFEST.md` - this file inventory.
- `VERSION.md` - bundle version metadata.
- `CITATION.cff` - machine-readable citation metadata.
- `LICENSE` - bundle license note matching the repository-level license state.
- `SHA256SUMS.txt` - SHA256 checksums for bundle files, generated after validation.
- `CONSTRUCTION_SUMMARY.md` - construction and scope summary.
- `INVENTORY_REPORT.md` - script inventory and deferred item report.

## Scripts

- `scripts/01_r4_firas_dependency_audit.py` - verifies the Paper 17 v1.5 FIRAS-fixed R4 convention and confirms Paper 22's active BBN scorecard is not R4-dependent.
- `scripts/02_spatial_hodge_complex.py` - reproduces Hodge spectra, Peter-Weyl bridge data, and framework constants.
- `scripts/03_tt_channel_floor.py` - reproduces transverse-traceless branch multiplicities and channel-floor arithmetic.
- `scripts/04_gauge_placement_and_channel_architecture.py` - reproduces homogeneous gauge placement and channel architecture checks.
- `scripts/05_no_go_and_rate_paradigm_ledger.py` - reproduces live no-go and rate-paradigm ledger values.
- `scripts/06_amplitude_scorecard_and_comparators.py` - reproduces Theorem 22.23/22.24 amplitude, scorecard, comparator, and Li-7 consistency arithmetic.
- `scripts/07_kappa_audit_summary.py` - emits a compact audit verdict JSON.
- `scripts/08_validate_expected_outputs.py` - reruns all scripts and validates expected outputs.
- `scripts/README.md` - script-level usage notes.

## Data

- `data/imported_constants.json` - framework constants, R4/FIRAS readout metadata, observational denominators, corrected BBN row, and frozen audit values.
- `data/external_data_sources.md` - source and licensing notes for external data/code.

## Environment

- `environment/requirements.txt` - Python dependency notes.
- `environment/python_version.txt` - Python version used.
- `environment/apt_packages.txt` - system package notes.
- `environment/environment_seed.md` - random-seed notes.
- `environment/external_dependencies.md` - external dependency notes.

## Results

- `results/r4_firas_dependency_audit_results.json`
- `results/spatial_hodge_complex_results.json`
- `results/tt_channel_floor_results.json`
- `results/gauge_placement_and_channel_architecture_results.json`
- `results/no_go_and_rate_paradigm_ledger_results.json`
- `results/amplitude_scorecard_and_comparators_results.json`
- `results/kappa_audit_summary_results.json`

## Reports

- `reports/paper22_v20_r4_kappa_audit_report.md`
- `reports/paper22_v20_r4_kappa_audit_results.json`
- `reports/paper22_kappa_audit_report.md`
- `reports/paper22_kappa_audit_results.json`
- `reports/paper22_theorem_22_23_kappa_audit_report.md`
- `reports/paper22_theorem_22_23_kappa_audit_results.json`
- `reports/paper22_v14_ypbbn_to_ypcmb_correction_memo.md`
- `reports/paper22_v14_ypbbn_to_ypcmb_correction_results.json`
