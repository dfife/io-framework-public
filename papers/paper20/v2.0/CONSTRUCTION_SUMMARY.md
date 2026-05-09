# Construction Summary

## Scripts

- `01_r4_firas_readout_audit.py`
  - Input: `results/r4_firas_readout_results.json`
  - Verifies: R4/FIRAS readout arithmetic and the non-prediction boundary for
    the observed cosmic microwave background temperature.

- `02_radiation_scope_boundary.py`
  - Input: `results/radiation_scope_boundary_results.json`
  - Verifies: Theorem 20.3 reduced-core species-count no-go summary and
    late-time insensitivity row.

- `03_acoustic_theorems.py`
  - Input: `results/acoustic_theorems_results.json`
  - Verifies: `J_theta`, rounded `theta*`, exact acoustic rows, and the twelve
    eliminated alternatives.

- `04_bbn_wrapper_scorecard.py`
  - Input: `results/bbn_wrapper_scorecard_results.json`
  - Verifies: corrected YPCMB Big Bang nucleosynthesis comparison row.

- `05_neff_import_kinetic_correction.py`
  - Input: `results/neff_import_kinetic_results.json`
  - Verifies: Standard Model `N_eff`, kinetic correction, and the statement
    that the local MeV decoupling equations are independent of the present-day
    temperature anchor.

- `06_bbn_measurement_immunity.py`
  - Input: `results/bbn_measurement_immunity_results.json`
  - Verifies: dimensionless abundance-ratio cancellation and the no-go for
    measurement-geometry rescue.

- `07_radiation_algebra_theorems.py`
  - Input: `results/radiation_algebra_theorems_results.json`
  - Verifies: Theorems 20.RAD1, 20.RAD2, and 20.RAD3.

- `08_validate_expected_outputs.py`
  - Inputs: all frozen JSON outputs needed for headline checks.
  - Expected: `SUMMARY total_checks=22 pass_count=22 fail_count=0`.

## Deferred / Not Redistributed

Raw external datasets, PRyMordial, CLASS, CAMB, and private exploratory files
are not redistributed. The v2.0 bundle records frozen outputs and enough
documented arithmetic for a reviewer to audit the manuscript-facing values.
