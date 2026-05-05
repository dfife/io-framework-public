# Paper 17 v1.5 Construction Summary

## Script-to-Claim Mapping

- `01_gauge_payload_determinant.py` verifies the gauge-side determinant chain:
  `Q = 1 + gamma_BI^2`, `a = dim(S2)/2 = 1`, and
  `K_gauge = ln(Q)`. This supports the gauge-payload side of Theorem 17.1 and
  the Step 40 `a != R4` clarification.
- `02_firas_fixed_r4.py` reproduces Theorem 17.2's numerical normalization:
  `R4_FIRAS = ln(T_FIRAS/T_IO)/(K_gauge ln x) = 1.0031014644105183`.
- `03_readout_uniqueness_check.py` verifies the nonzero-slope monotonicity
  argument that makes the FIRAS solution unique.
- `04_modular_projection_surrogate.py` reproduces the finite-dimensional
  direct-integral identity used as a numerical surrogate for the modular
  projection theorem.
- `05_foundation_closure_toy_model.py` reproduces a finite-dimensional KMS/GNS
  toy check for the A-vacuum foundation package.
- `06_framework_constructible_uniqueness_summary.py` validates the frozen
  enumeration summary: 5545 raw FIRAS-band algebraic hits, but seven published
  structural aliases all collapse to `K_gauge`.
- `07_r4_no_go_registry.py` records the killed routes showing that R4 is not
  internally forced by the current modular-projection stack.
- `08_kappa_audit_summary.py` reduces the kappa-audit report to a machine
  summary.
- `09_validate_expected_outputs.py` reruns the public scripts and checks the
  active v1.5 values.

## Gaps Not Filled by This Bundle

- The bundle does not derive R4=1 from operator algebra alone. Paper 17 v1.5
  explicitly says that route remains open.
- The bundle does not extend the theorem from the reduced thermal-plus-gauge
  sector to the full unreduced horizon algebra.
- The bundle does not redistribute FIRAS data files; the manuscript value is
  cited and used as the empirical datum.
