# Calculator Phase 4 Source/Readout Foundation Audit

Date: 2026-04-14

## Question

Before public release, the Phase 4 source/readout modules were audited against
the same theorem-grade standard used in earlier calculator phases:

1. every formula must trace to a theorem in the paper stack or to Premise 1/2
2. every open seam must be an explicit interface that raises if invoked
3. no implementation choice may masquerade as a physical law
4. nothing may silently fall back to CLASS defaults

The four audited modules were:

- `source_block.py`
- `closed_shell_power.py`
- `los_transfer.py`
- `readout_functionals.py`

## Executive Result

1. `derived / scoped`: the four-module Phase 4 source/readout foundation is
   theorem-grade at its stated scope.
2. `verified`: the public release slice reproduces the local audit tests.
3. `derived / scoped`: the release does not hide the remaining solver debt. The
   exact Stage-2 operator, the final typed source/acoustic operator, the exact
   LOS projector, and the `A_peak -> theta_peak` identification all remain
   explicit open seams.
4. `verified`: no blocking boundary leak was found in the audit.

## Module-Level Audit

### 1. `source_block.py`

Status: `derived / scoped`

Closed source-side formulas carried directly:

- `sigma_ell = (ell+1) / r_s`
- `Y_ell = log(ell+1) = log(r_s Lambda_DtN^coex)`
- `T_field = exp[-(K_g tensor log(r_s Lambda_DtN^coex)) / (2x)]`
- `R_cov = T_field^* T_field`
- `P_src = B_+ o U_coex o T_field`
- `W_N = (N / N_p)^(-K_gauge / x)`
- `A_s = (25/9) [gamma^2 / (1 + gamma^2)] [1 / sqrt(2)] [exp(4 pi sqrt(2)) - 1]^-1`

Audit result:

- the module stays strictly on the active scalar-source sector closed by the
  Paper 32 modular-DtN theorem.
- there is no hidden source-to-phase identification or perturbation closure.
- the fixed pivot shell only instantiates the carried active-sector
  normalization `N_p`; it does not alter the source law itself.

### 2. `closed_shell_power.py`

Status: `derived / scoped`

Exact closed-`S^3` shell formulas carried directly:

- shell degeneracy: `D_n = (n+1)^2`
- shell variance prefactor: `((n+1)^2 / (2 pi^2 R^3))`
- shell variables:
  `q_n = (n+1)/R`,
  `k_scalar = sqrt(n(n+2))/R`,
  `k_MS = sqrt((n-1)(n+3))/R`
- dimensionless prefactors:
  `Delta_q^2`,
  `Delta_scalar^2`,
  `Delta_MS^2`

Audit result:

- the observer-side shell covariance and exact prefactors match the Paper 28
  closed-geometry definitions.
- the module does not import the flat `k^3` law as a primitive.
- the physical source-side shell covariance remains out of scope and explicit.

### 3. `los_transfer.py`

Status: `derived / scoped`

Closed LOS carrier content:

- closed support rule `ell < nu = q / sqrt(K)`
- explicit `Delta_l^X(q)` transfer packets on that support
- explicit shell-weighted `C_l` assembly from supplied packets

Audit result:

- the module refuses to project from hierarchy history to transfer packets
  without an exact theorem-grade LOS operator.
- there is no fallback to flat interpolation or a CLASS default transfer kernel.
- `C_l` assembly is allowed only from explicitly supplied transfer packets and
  explicitly supplied shell weights; the assembly layer does not pretend those
  packets were derived by the module itself.

### 4. `readout_functionals.py`

Status: `derived / scoped`

Readout-side content:

- explicit null-family field
  `omega_hat(eta) = (ev_eta tensor C_n) P_src(Phi)`
- explicit estimator-class evaluation
  `E_rs = integral c_s(eta) R_hist^ac(omega_hat(eta)) d eta`
- discrete peak functional on supplied `C_l`

Audit result:

- the module preserves the Paper 37 separation between the background acoustic
  ratio and the physical peak-position readout.
- it may read an `A_peak`-type functional from supplied `C_l`, but it raises on
  the still-open identification `A_peak -> theta_peak`.
- there is no backdoor path from a peak or background ratio to a theorem-grade
  numeric acoustic angle.

## Open Boundaries

This release intentionally does not close:

- the exact Stage-2 dynamic-network operator
- the final typed source/acoustic operator on the closed `S^3` hierarchy
- the exact LOS projector `y^(md,ic,q)(tau) -> Delta_l^X(q)`
- the exact readout identification `A_peak -> theta_peak`

These remain theorem boundaries, not missing convenience features.

## Verification

Public release-slice verification command:

```bash
cd releases/calculator_phase4_source_readout_foundation
PYTHONPATH=src python -m pytest tests -q
```

Expected result at release time:

```text
16 passed
```

Local calculator verification before publication:

- `python -m pytest tests/test_source_block.py -q` -> `4 passed`
- `python -m pytest tests/test_closed_shell_power.py -q` -> `4 passed`
- `python -m pytest tests/test_los_transfer.py -q` -> `4 passed`
- `python -m pytest tests/test_readout_functionals.py -q` -> `4 passed`
- `python -m pytest tests/test_source_block.py tests/test_closed_shell_power.py tests/test_los_transfer.py tests/test_readout_functionals.py tests/test_provenance.py -q` -> `25 passed`
- `python -m pytest tests -q` -> `60 passed`

## Claim Boundary

This publication is a theorem-grade source/readout-foundation release, not a
full IO-native `C_ell` solver release.
