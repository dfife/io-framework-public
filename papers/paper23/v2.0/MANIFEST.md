# Paper 23 v2.0 Manifest

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

- `scripts/01_r4_firas_dependency_audit.py` - records the Paper 17 v1.5 FIRAS-fixed R4 convention and confirms Paper 23's active spectral-index result is not R4-dependent.
- `scripts/02_scalar_perturbation_equations.py` - reproduces closed-S3 scalar harmonic, physical-mode, and Mukhanov-Sasaki bookkeeping.
- `scripts/03_bridge_operator_and_uniqueness.py` - reproduces scalar bridge operator support, branch rules, and uniqueness/proportionality checks.
- `scripts/04_white_baseline_and_hopf_selection.py` - reproduces white boundary baseline and Hopf-selection bookkeeping.
- `scripts/05_no_doubling_and_spectral_index.py` - reproduces No-Doubling theorem arithmetic, finite-shell correction, and scalar spectral-index numerical result.
- `scripts/06_tensor_perturbations.py` - reproduces tensor harmonic bookkeeping and tensor-sector scope boundary.
- `scripts/07_kappa_audit_summary.py` - emits a compact audit verdict JSON.
- `scripts/08_validate_expected_outputs.py` - reruns all scripts and validates expected outputs.

## Data

- `data/imported_constants.json` - framework constants, R4/FIRAS readout metadata, Planck spectral-index comparison values, current Paper 22 inherited values, and audit status.
- `data/external_data_sources.md` - source and licensing notes for external references.

## Environment

- `environment/requirements.txt` - Python dependency notes.
- `environment/python_version.txt` - Python version used.
- `environment/apt_packages.txt` - system package notes.
- `environment/environment_seed.md` - random-seed notes.
- `environment/external_dependencies.md` - external dependency notes.

## Results

- `results/r4_firas_dependency_audit_results.json`
- `results/scalar_perturbation_equations_results.json`
- `results/bridge_operator_and_uniqueness_results.json`
- `results/white_baseline_and_hopf_selection_results.json`
- `results/no_doubling_and_spectral_index_results.json`
- `results/tensor_perturbations_results.json`
- `results/kappa_audit_summary_results.json`

## Reports

- `reports/paper23_v20_r4_kappa_audit_report.md`
- `reports/paper23_v20_r4_kappa_audit_results.json`
- `reports/paper23_scalar_perturbations_report.txt`
- `reports/paper23_bridge_uniqueness_report.txt`
- `reports/paper23_boundary_initial_conditions_report.txt`
- `reports/paper23_two_closing_lemmas_report.txt`
- `reports/paper23_tensor_perturbations_report.txt`

