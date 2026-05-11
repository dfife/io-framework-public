# Paper 23 v2.0 Bundle Construction Summary

## Bundle Scope

The bundle includes only scripts that reproduce live Paper 23 v2.0 numbers or
live theorem-support surfaces. Historical exploratory scripts and dead routes
remain in the private lab tree and are not rerun as bundle artifacts.

## Script Inventory

- `01_r4_firas_dependency_audit.py`
  - Inputs: frozen framework constants, `R4_FIRAS`.
  - Outputs: `results/r4_firas_dependency_audit_results.json`.
  - Verifies: R4/FIRAS repair boundary; Paper 23 active spectral index is not R4-dependent.

- `02_scalar_perturbation_equations.py`
  - Inputs: closed-S3 scalar harmonic formulas and OS sample branch.
  - Outputs: `results/scalar_perturbation_equations_results.json`.
  - Verifies: scalar spectrum, physical start at `n=2`, and `k_MS` dictionary.

- `03_bridge_operator_and_uniqueness.py`
  - Inputs: Paper 23 bridge theorem statements.
  - Outputs: `results/bridge_operator_and_uniqueness_results.json`.
  - Verifies: trace bridge, epsilon-f proportionality, branch multiplicity, and tensor uniqueness boundary.

- `04_white_baseline_and_hopf_selection.py`
  - Inputs: isotropic S2 baseline and Hopf-selection formulas.
  - Outputs: `results/white_baseline_and_hopf_selection_results.json`.
  - Verifies: `C_l = 4 pi/N`, `N_eff/N = 0.7696`, and `n = 2 ell` selection.

- `05_no_doubling_and_spectral_index.py`
  - Inputs: `gamma_BI`, `x`, Planck comparison value.
  - Outputs: `results/no_doubling_and_spectral_index_results.json`.
  - Verifies: `n_s = 0.9638756437486053`, no-doubling rejection, finite-shell correction, and pivot-shell mapping.

- `06_tensor_perturbations.py`
  - Inputs: closed-S3 tensor harmonic formulas.
  - Outputs: `results/tensor_perturbations_results.json`.
  - Verifies: TT multiplicities, eigenvalue bookkeeping, and tensor scope boundary.

- `07_kappa_audit_summary.py`
  - Inputs: audit findings.
  - Outputs: `results/kappa_audit_summary_results.json`.
  - Verifies: no hidden continuous fitted parameter; R4 not active; open premise surfaces visible.

- `08_validate_expected_outputs.py`
  - Inputs: scripts 1-7.
  - Outputs: terminal PASS/FAIL summary.
  - Verifies: all frozen outputs match expected values.

## Gaps and Deferred Items

- The v2.0 manuscript should remove stale independent CMB-temperature prediction wording.
- The v2.0 manuscript should replace stale inherited Paper 22 scorecard rows with Paper 22 v2.0 values or remove them if not live.
- The v2.0 manuscript should migrate noncanonical labels to the current public claim-discipline convention.
- Tensor `n_t = 0`, the Primordial Scalar Readout Principle, the Boundary Covariance Exponent, and the spatial canonical-commutation-relation lift remain premise-gap surfaces unless v2.0 supplies direct chains to Premise 1, Premise 2, or frozen imported physics.

