# Construction Summary

## Scripts

- `01_acoustic_phase_precision.py`
  - Input: `results/acoustic_phase_precision_results.json`
  - Verifies: `J_theta = 0.8339461798286282` and acoustic precision cases.
  - External dependencies: none for frozen-output path.

- `02_bbn_wrapper_scorecard.py`
  - Input: `results/bbn_wrapper_scorecard_results.json`
  - Verifies: YPCMB corrected BBN row and `chi2(D/H + Y_p)`.
  - External dependencies: PRyMordial for full rerun, not needed for frozen path.

- `03_r4_impact_audit.py`
  - Input: `data/imported_constants.json`
  - Verifies: old R4=1 factor, FIRAS-fixed R4 factor, and CMB-prediction
    retirement boundary.

- `04_torsion_lambda_branch.py`
  - Input: `results/torsion_lambda_branch_results.json`
  - Verifies: torsion-Lambda branch values.

- `05_radiation_theorems_summary.py`
  - Input: `results/radiation_three_theorems_results.json`
  - Verifies: radiation-sector theorem/no-go classifications.

- `06_measurement_chain_immunity.py`
  - Input: `results/bbn_measurement_chain_results.json`
  - Verifies: abundance-ratio measurement-chain cancellation result.

- `07_kappa_audit_summary.py`
  - Input: `results/kappa_audit_results.json`
  - Verifies: hidden-parameter audit verdict.

- `08_validate_expected_outputs.py`
  - Inputs: all frozen JSON outputs needed for headline checks.
  - Expected: `SUMMARY total_checks=14 pass_count=14 fail_count=0`.

## Deferred / Not Redistributed

Raw external datasets and third-party cosmology engines are not redistributed.
The bundle records frozen outputs and dependency instructions for heavyweight
reruns.
