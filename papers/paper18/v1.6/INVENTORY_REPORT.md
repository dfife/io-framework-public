# Paper 18 v1.6 Inventory Report

## Source Scripts Reviewed

All scripts in `/opt/cosmology-lab/results/paper18/` were reviewed.

R4-bearing scripts were patched and rerun:

- `paper18_bogoliubov_coefficients_checks.py`
- `paper18_modular_bogoliubov_upgrade_checks.py`
- `paper18_legacy_observables_recalculation_checks.py`
- `paper18_jwst_age_recalculation_checks.py`
- `paper18_matter_power_shape_test.py`
- `paper18_zeq_kruskal_audit_checks.py`

R4-independent scripts were internally documented and rerun or copied with no
thermal-readout changes:

- `paper18_cmp_theorem_checks.py`
- `paper18_bdp_theorem_checks.py`
- `paper18_bdp_gap_closure_checks.py`
- `paper18_bdp_epoch_independence_audit_checks.py`
- `paper18_v_alpha_theorem_checks.py`
- `paper18_neff_delta_theorem_checks.py`
- `paper18_curvature_implementation_resolution_checks.py`
- `paper18_structural_attacks_audit_checks.py`

## Gaps or Deferred Items

No live scripted Paper 18 theorem was found without a script.

Two scripts require external datasets and compiled cosmology codes for a fresh
full rerun:

- `08_legacy_observables_recalculation.py`: DESI DR1 Gaussian BAO files and CLASS.
- `10_matter_power_shape_test.py`: BOSS DR12 full-shape archive and CAMB.

Their frozen JSON outputs are included and validated by value. The scripts are
provided for reviewers who want to repeat the external reruns after obtaining
the datasets.

## Manuscript Impact for v1.6

The v1.6 manuscript should remove the independent CMB-temperature prediction
claim from Paper 18. The correct active statement is that Paper 18 inherits
Paper 17 v1.5's FIRAS-fixed observer readout normalization and uses it in the
Bogoliubov spectrum support calculation.
