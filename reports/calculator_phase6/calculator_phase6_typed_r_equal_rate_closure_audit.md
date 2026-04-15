# Calculator Phase 6 Typed R Equal-rate Closure Audit

Date: 2026-04-15

## Question

Before publication, the typed-`R` closure was audited against Cosmo's accepted
scope:

1. the theorem node wording must state the accepted equal-rate scoped branch
2. the site-specific typed composites must be supported by a named uniqueness
   theorem
3. the live Thomson tuple must be shown to come from the typed split history
   path rather than one undifferentiated opacity

## Executive result

The audit passed.

- the theorem dictionary now states the accepted equal-rate scoped branch
  `thomson_hierarchy_rate = thomson_drag_rate`
- the theorem node `Full Typed R Hierarchy Operator Theorem` now carries that
  accepted branch wording directly
- the theorem node `Typed R Site-uniqueness Theorem` now carries the same
  accepted branch wording directly
- the theorem node `Typed Split Thomson-history Realization Theorem` now states
  that the live tuple is the accepted equal-rate scoped conformal tuple
- the companion reports package the full operator theorem, the uniqueness
  theorem, the implementation audit, and the complete theorem chain memo

## Published theorem objects

The released theorem package is:

- `Full Typed R Hierarchy Operator Theorem`
- `Typed R Site-uniqueness Theorem`
- `Typed Split Thomson-history Realization Theorem`

The carried equal-rate branch is:

- `thomson_hierarchy_rate = thomson_drag_rate`

The carried site map is:

- `Gamma_gammab = thomson_drag_rate`
- `Gamma_bgamma = R_local,geom thomson_drag_rate`
- `c_bgamma^2 = 1 / [3 (1 + R_local,geom)]`
- `M_bgamma = 1 + R_local,geom`
- `L_odd/even = R_local,geom / (1 + R_local,geom)`
- `D_heat = R_local,geom^2 / [6 (1+R_local,geom)^2 thomson_drag_rate]`
- `D_visc = 16 / [90 (1+R_local,geom) thomson_hierarchy_rate]`

## Implementation path

The published implementation path is explicitly:

- `kappa'_loc(z) = a n_e(z) sigma_T`
- observer-side packet `(d tau_obs / dz, tau_obs, g_obs)`
- conformal equal-rate tuple
  `thomson_drag_rate = |(d tau_obs / dz) / (dC / dz)|`
  and
  `thomson_hierarchy_rate = thomson_drag_rate`

So the live tuple is not built from a single flattened opacity scalar.

## Verification

Local calculator verification before publication:

- `PYTHONPATH=src python -m pytest tests/test_provenance.py tests/test_typed_r_operator.py tests/test_thomson_history_contract.py -q`
  -> `17 passed`
- `PYTHONPATH=src python -m pytest tests -q`
  -> `101 passed`
- `python build_bundle.py`
  -> regenerated the public theorem surface bundle

## Claim boundary

This publication closes the equal-rate scoped typed-`R` branch only.

It does not claim:

- a theorem-grade nontrivial split
  `thomson_hierarchy_rate != thomson_drag_rate`
- full physical TT-spectrum validation
- any one-slot collapse of the full observed odd/even readout hierarchy
