# Scripts

The numbered scripts are designed for readers who are not already familiar with
the Interior Observer notation.

- `01_acoustic_phase_precision.py`: verifies the acoustic phase-calibration
  factor and prints the frozen acoustic cases.
- `02_bbn_wrapper_scorecard.py`: prints the YPCMB-corrected BBN scorecard.
- `03_r4_impact_audit.py`: recomputes the R4/FIRAS readout arithmetic.
- `04_torsion_lambda_branch.py`: prints the torsion-Lambda branch values.
- `05_radiation_theorems_summary.py`: summarizes radiation-sector theorem
  status.
- `06_measurement_chain_immunity.py`: summarizes the abundance-ratio
  measurement-chain audit.
- `07_kappa_audit_summary.py`: prints the hidden-parameter audit verdict.
- `08_validate_expected_outputs.py`: standard-library frozen-output validator.

Scripts 01-07 are explanatory and read frozen JSON outputs. The validator is
the main reviewer entry point and exits nonzero on any mismatch.
