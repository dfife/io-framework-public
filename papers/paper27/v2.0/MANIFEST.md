# Manifest

## Root Files

- `README.md` - bundle overview, claim boundary, and quickstart.
- `MANIFEST.md` - this file inventory.
- `VERSION.md` - version metadata and R4/FIRAS boundary.
- `CITATION.cff` - citation metadata.
- `LICENSE` - bundle license.
- `CONSTRUCTION_SUMMARY.md` - script-by-script construction summary.
- `INVENTORY_REPORT.md` - source artifact inventory and exclusions.
- `SHA256SUMS.txt` - SHA256 checksums for bundle files.

## Environment

- `environment/requirements.txt` - Python dependency statement.
- `environment/python_version.txt` - Python version requirement.
- `environment/apt_packages.txt` - system package statement.
- `environment/environment_seed.md` - random seed statement.
- `environment/external_dependencies.md` - external theorem/data dependency
  statement.

## Data

- `data/imported_constants.json` - frozen framework constants and Paper 27
  v2.0 values.
- `data/external_data_sources.md` - external data and licensing statement.

## Scripts

- `scripts/_common.py` - shared helpers.
- `scripts/01_c1a_cross_term_vanishing.py` - C1a representation mismatch.
- `scripts/02_spatial_ccr_lift.py` - spatial CCR carrier facts.
- `scripts/03_residual_cone_and_closed_geometry.py` - rank-one quotient and
  closed-geometry exponents.
- `scripts/04_backreaction_passivity.py` - passivity/backreaction residual
  ledger.
- `scripts/05_bridge_rigidity_observable_exhaustion.py` - bridge-readable
  covariance and observable-exhaustion ledger.
- `scripts/06_visibility_and_inheritance.py` - visibility-slot equality.
- `scripts/07_kappa_r4_audit_summary.py` - R4/kappa audit JSON.
- `scripts/08_validate_expected_outputs.py` - validation entry point.
- `scripts/README.md` - script descriptions.

## Results

- `results/c1a_cross_term_vanishing_results.json`
- `results/spatial_ccr_lift_results.json`
- `results/residual_cone_and_closed_geometry_results.json`
- `results/backreaction_passivity_results.json`
- `results/bridge_rigidity_observable_exhaustion_results.json`
- `results/visibility_and_inheritance_results.json`
- `results/kappa_r4_audit_summary_results.json`

## Reports

- `reports/paper27_kappa_audit_report.md`
- `reports/paper27_kappa_audit_results.json`
- `reports/paper27_v2_publishable_theorem_memo.md`
- `reports/paper27_v2_publishable_theorem_memo_results.json`
- `reports/paper27_v2_section9_boundary_state_on_lifted_carrier.md`
- `reports/paper27_v2_section9_boundary_state_on_lifted_carrier_results.json`
- `reports/paper27_v2_residual_state_freedom_classification.md`
- `reports/paper27_v2_residual_state_freedom_classification_results.json`
- `reports/paper27_v2_closed_geometry_residual_reduction.md`
- `reports/paper27_v2_closed_geometry_residual_reduction_results.json`
- `reports/paper27_v2_backreaction_passivity_residual_reduction.md`
- `reports/paper27_v2_backreaction_passivity_residual_reduction_results.json`
- `reports/paper27_v2_joint_observable_exhaustion_attempt.md`
- `reports/paper27_v2_joint_observable_exhaustion_attempt_results.json`
- `reports/paper27_v2_admissible_observable_classification_attempt.md`
- `reports/paper27_v2_admissible_observable_classification_attempt_results.json`
- `reports/paper27_v2_p1_background_perturbation_residual_classification.md`
- `reports/paper27_v2_p1_background_perturbation_residual_classification_results.json`
- `reports/paper27_spatial_ccr_lift_theorem_memo.md`
- `reports/paper27_theorem_sequences_spatial_ccr_c1a.md`

## External Dataset Checksums

No external observational datasets are redistributed in this bundle.
