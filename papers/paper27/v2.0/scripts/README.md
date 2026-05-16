# Script Inventory

Run the validation entry point:

```bash
python3 scripts/08_validate_expected_outputs.py
```

The scripts are intentionally small and documented. Paper 27 v2.0 is a
structural theorem paper; the live bundle reproduces theorem-support
arithmetic and machine-readable labels, not the retired CLASS confrontation
branch.

- `01_c1a_cross_term_vanishing.py` records the `SU(2)` representation mismatch
  that forces the C1a cross term to vanish.
- `02_spatial_ccr_lift.py` records the `S^3` Hodge/coexact carrier facts used
  by the spatial canonical-commutation-relation lift.
- `03_residual_cone_and_closed_geometry.py` records the rank-one quotient,
  residual state freedom, and closed-geometry exponent checks.
- `04_backreaction_passivity.py` records the backreaction/passivity residual
  reduction ledger.
- `05_bridge_rigidity_observable_exhaustion.py` computes the bridge-readable
  Hawking/KMS covariance factor `1/(exp(4*pi*sqrt(2)) - 1)`.
- `06_visibility_and_inheritance.py` records visibility-slot inheritance
  `omega_b,vis = omega_b,eff = 0.02910`.
- `07_kappa_r4_audit_summary.py` records the R4 and hidden-parameter audit
  disposition.
- `08_validate_expected_outputs.py` reruns all prior scripts and checks the
  frozen outputs.
