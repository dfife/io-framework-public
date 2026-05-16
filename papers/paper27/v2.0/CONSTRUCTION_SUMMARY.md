# Construction Summary

## Script Outputs

- `01_c1a_cross_term_vanishing.py`
  - Input: `SU(2)` spin labels for scalar singlet and coexact vector branch.
  - Output: `results/c1a_cross_term_vanishing_results.json`.
  - Verifies: cross-term Hom dimension is zero.

- `02_spatial_ccr_lift.py`
  - Input: closed `S^3` Hodge/coexact structure.
  - Output: `results/spatial_ccr_lift_results.json`.
  - Verifies: spatial CCR carrier and coexact vector shell facts.

- `03_residual_cone_and_closed_geometry.py`
  - Input: rank-one quotient and closed-geometry exponent formulas.
  - Output: `results/residual_cone_and_closed_geometry_results.json`.
  - Verifies: rank-one quotient, residual-state boundary, `4*pi*sqrt(2)`,
    and `8*pi`.

- `04_backreaction_passivity.py`
  - Input: passivity/KMS/backreaction theorem package.
  - Output: `results/backreaction_passivity_results.json`.
  - Verifies: residual restriction but not full state selection.

- `05_bridge_rigidity_observable_exhaustion.py`
  - Input: Hawking/KMS boundary shell formula.
  - Output: `results/bridge_rigidity_observable_exhaustion_results.json`.
  - Verifies: `1/(exp(4*pi*sqrt(2)) - 1)`.

- `06_visibility_and_inheritance.py`
  - Input: visibility-slot equality.
  - Output: `results/visibility_and_inheritance_results.json`.
  - Verifies: `omega_b,vis = omega_b,eff = 0.02910`.

- `07_kappa_r4_audit_summary.py`
  - Input: R4/FIRAS repair boundary and audit findings.
  - Output: `results/kappa_r4_audit_summary_results.json`.
  - Verifies: no active `R4 = 1` use and no active independent
    CMB-temperature prediction.

- `08_validate_expected_outputs.py`
  - Input: scripts 01-07 and frozen expected values.
  - Output: pass/fail terminal report.
  - Verifies: every frozen output matches expected values.

## Exclusions

Retired Paper 27 CLASS/Planck-confrontation scripts are not included because
Paper 27 v2.0 supersedes that branch. The audit report names the excluded
scripts that contain old CMB-temperature-era constants.
