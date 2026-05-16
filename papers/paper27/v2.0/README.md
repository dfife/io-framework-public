# Paper 27 v2.0 Reproducibility Bundle

Paper 27 v2.0, **Theorem-Grade Closures for the Scalar-Bridge Perturbation
Sector**, updates Paper 27 away from the retired CLASS/Planck-confrontation
branch and into a structural theorem paper. The live claims concern the lifted
scalar-bridge carrier, C1a cross-term vanishing, the rank-one scalar quotient,
residual state freedom on the full carrier, bridge-readable covariance, and the
boundary where full state selection remains open.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper27/v2.0
python3 scripts/08_validate_expected_outputs.py
```

Expected final line:

```text
PASS Paper 27 v2.0 validation: total checks=10, pass count=10, fail count=0
```

## What This Bundle Reproduces

- The `SU(2)` representation mismatch behind C1a cross-term vanishing.
- The closed-`S^3` coexact carrier facts behind the spatial CCR lift.
- The rank-one scalar quotient and residual state-freedom boundary.
- The closed-geometry exponent checks `4*pi*sqrt(2)` and `8*pi`.
- The bridge-readable Hawking/KMS covariance factor
  `1/(exp(4*pi*sqrt(2)) - 1)`.
- The visibility-slot inheritance `omega_b,vis = omega_b,eff = 0.02910`.
- The kappa-style R4 audit disposition and exclusion of retired
  CMB-temperature scripts.

## Claim Boundary

Paper 27 v2.0 does not claim an independent CMB-temperature prediction. The
framework value `R4_FIRAS = 1.0031014644` is recorded as an imported boundary
constant from Paper 17 v1.5, but no active Paper 27 script uses `R4 = 1`.

The full state on `h_vec` remains `OPEN/PREMISE_GAP`. The current scalar
observables are protected by the rank-one quotient and observable-exhaustion
theorems; the residual full-carrier state freedom is not a hidden scalar
amplitude fit.

## Detailed Reproduction

Run individual scripts from the bundle root:

```bash
python3 scripts/01_c1a_cross_term_vanishing.py
python3 scripts/02_spatial_ccr_lift.py
python3 scripts/03_residual_cone_and_closed_geometry.py
python3 scripts/04_backreaction_passivity.py
python3 scripts/05_bridge_rigidity_observable_exhaustion.py
python3 scripts/06_visibility_and_inheritance.py
python3 scripts/07_kappa_r4_audit_summary.py
python3 scripts/08_validate_expected_outputs.py
```

Each script writes one JSON result to `results/`.

## Dependencies

Only Python 3.11+ and the standard library are required.

## Citation

If using this bundle, cite the Paper 27 v2.0 Zenodo record and the GitHub
release tag `paper27-v2.0`.
