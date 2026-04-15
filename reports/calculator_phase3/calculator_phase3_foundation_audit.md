# Calculator Phase 3 Foundation Audit

Date: 2026-04-14

## Question

Before public release, the Phase 3 perturbation-foundation modules were audited
against the theorem-grade standard used in the calculator:

1. every formula must trace to a theorem in the paper stack or to Premise 1/2
2. every open seam must be an explicit interface that raises if invoked
3. no implementation choice may masquerade as a physical law
4. nothing may be silently borrowed from CLASS defaults

The four audited modules were:

- `s3_modes.py`
- `perturbation_types.py`
- `scalar_hierarchy.py`
- `thomson_history_contract.py`

## Executive Result

1. `derived / scoped`: the four-module Phase 3 foundation is theorem-grade at
   its stated scope.
2. `verified`: the public release slice reproduces the local audit tests.
3. `derived / scoped`: the release does not contain a hidden perturbation
   closure. The exact Stage-2 operator, the typed source/acoustic operator, and
   the tuple-level Thomson operator all remain explicit open seams.
4. `verified`: one real boundary gap was found and fixed before release:
   `perturbation_types.py` now preserves the published clustering slot
   `omega_b,clustering`, and it exposes the exact Stage-2 dynamic-network seam
   as its own raising interface.

## Module-Level Audit

### 1. `s3_modes.py`

Status: `derived / scoped`

Published content carried directly:

- scalar ladder: `lambda_n = n(n+2)/a^2`
- scalar shifted operator: `lambda_n - 3 = (n-1)(n+3)/a^2`
- scalar multiplicity: `(n+1)^2`
- vector eigenvalue: `(n+1)^2/a^2`
- vector multiplicity: `2n(n+2)`
- tensor rough-Laplacian eigenvalue: `(n(n+2)-2)/a^2`
- tensor Lichnerowicz eigenvalue: `(n(n+2)+4)/a^2`
- tensor multiplicity: `2(n-1)(n+3)`
- closed transfer mapping: `q^2 = k^2 + K(1+m)`
- closed support rule: `ell < nu = q / sqrt(K)`

Audit result:

- `J` floors and diagonal-spin ranges are carrier data from the Paper 22 bridge,
  not implementation heuristics.
- the scalar `n = 0` and `n = 1` shells remain visible as `background` and
  `gauge`; they are not silently dropped.
- the convenience parameter `radius=1.0` is only a unit normalization. All
  formulas keep the explicit `1/a^2` scaling.

### 2. `perturbation_types.py`

Status: `derived / scoped`

Published content carried directly:

- solver tuple label: `S_IO`
- closed shell map: `q^2 = k^2 + K(1+m)`
- source block: `P_src = B_+ o U_coex o T_field`
- Stage-2 state: `Y_rec = (x_e, T_m, D_-(q;z), L_-(z))`
- thermodynamic field list:
  `(x_e, dot{kappa}, exp(-kappa), g, dg, ddg, kappa_b)`

Baryon architecture:

- chemistry: `omega_b,geom`
- primitive local opacity: `omega_b,geom`
- reduced visibility/readout: `omega_b,eff`
- clustering slot: `omega_b,clustering`
- hierarchy-wide `R`: open
- scalar metric source: open

Audit result:

- the module now preserves the published three-slot baryon architecture exactly.
- the exact Stage-2 dynamic-network operator is an explicit seam with a raising
  placeholder.
- the typed source/acoustic operator is an explicit seam with a raising
  placeholder.
- no hidden fallback to one-slot baryon loading or a CLASS-style post-solve
  patch exists in this layer.

### 3. `scalar_hierarchy.py`

Status: `derived / scoped`

Published content carried directly:

- physical scalar shells begin at `n >= 2`
- the shell carrier uses `lambda_n - 3 = (n-1)(n+3)`
- scalar hyperspherical support is `ell = 0,1,...,n`

Audit result:

- the hierarchy carrier refuses `n = 0,1`, so background/gauge shells are not
  silently promoted into physical evolution.
- the step request includes the typed perturbation carrier and the coupled
  Thomson-history contract.
- direct evolution without an exact operator raises immediately.

### 4. `thomson_history_contract.py`

Status: `derived / scoped`

Published content carried directly:

- required tuple:
  `(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)`
- definitions:
  `tau_c = 1 / thomson_drag_rate`
  `dtau_c = - d(thomson_drag_rate) * tau_c^2`

Audit result:

- the tuple matches the Paper 37 carrier exactly.
- `tau_c` and `dtau_c` are derived transparently from supplied drag-rate data.
- the tuple-level operator remains explicit and raising.
- the module does not borrow a CLASS tight-coupling closure or LOS shortcut.

## Open Boundaries

This release intentionally does not close:

- the exact Stage-2 dynamic-network operator
- the final typed source/acoustic operator on the closed `S^3` hierarchy
- the exact IO-native operator on the coupled Thomson-history tuple

Those are theorem boundaries, not missing code convenience features.

## Verification

Public release-slice verification command:

```bash
cd releases/calculator_phase3_foundation
PYTHONPATH=src python -m pytest tests -q
```

Expected result at release time:

```text
17 passed
```

Local calculator verification before publication:

- `python -m pytest tests/test_s3_modes.py -q` -> `6 passed`
- `python -m pytest tests/test_perturbation_types.py -q` -> `4 passed`
- `python -m pytest tests/test_scalar_hierarchy.py tests/test_thomson_history_contract.py -q` -> `7 passed`
- `python -m pytest tests/test_s3_modes.py tests/test_perturbation_types.py tests/test_scalar_hierarchy.py tests/test_thomson_history_contract.py tests/test_provenance.py -q` -> `26 passed`
- `python -m pytest tests -q` -> `44 passed`

## Claim Boundary

This publication is a theorem-grade perturbation-foundation release, not a full
IO-native CMB solver release.
