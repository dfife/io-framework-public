# Calculator Phase 5 Scoped Closed-scalar Pipeline Theorem Memo

Date: 2026-04-15

## Executive result

The calculator now carries a scoped closed-`S^3` scalar perturbation pipeline
from the active scalar source block to explicit transfer packets and
shell-summed angular spectra.

Status:

- carrier laws, metric formulas, projector formulas, and LOS formulas:
  `derived / scoped as maps`
- full composed end-to-end closed-scalar pipeline:
  `conditional / scoped`

The composed status is conditional because the Stage-2 dynamic-history segment
is supplied by the inherited-FULL exact-history builder under Premise 2.

## The theorem chain

### 1. Closed `S^3` scalar carrier

The spatial carrier is fixed on the discrete closed-shell ladder with

- `lambda_n - 3 = (n-1)(n+3)`
- `k_n^2 = n(n+2) / R_curv^2`
- `q_n^2 = (n+1)^2 / R_curv^2`
- physical scalar support `n >= 2`
- angular support `ell < nu = q / sqrt(K)`

Status:

- `derived / scoped`

### 2. Active scalar source block

The source-side field block is fixed by

- `T_field = exp[-(K_g tensor log(r_s Lambda_DtN^coex)) / (2x)]`
- `P_src = B_+ o U_coex o T_field`
- `C_N^src = A_s W_N`

Status:

- `derived / scoped`

### 3. Source-to-initial-condition bridge

The active scalar-source bridge carries the shell covariance and the leading
closed-shell adiabatic seed.

Status:

- `derived / scoped`

### 4. Exact Stage-2 history segment

The calculator now exports the exact sampled Stage-2 state

- `Y_rec = (x_e, T_m, D_-(q;z), L_-(z))`

through a standalone inherited-FULL builder on the active IO local background.

Status:

- `conditional / scoped`

Why conditional:

- it uses inherited FULL atomic and radiative-transfer physics under Premise 2
- it is not yet a universal IO-native Stage-2 renormalization theorem

### 5. Coupled Thomson-history tuple

The admissible acoustic carrier uses the full coupled tuple

- `(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)`

with

- `tau_c = 1 / thomson_drag_rate`
- `dtau_c = - d(thomson_drag_rate) tau_c^2`

Status:

- `derived / scoped`

### 6. Einstein-side metric-state builder

Once the explicit total scalar stress summary is supplied, the Newtonian and
synchronous metric states are fixed algebraically on the closed shell.

Status:

- `derived / scoped as maps`

### 7. Local scalar acoustic generator

With the sampled Stage-2 state, Thomson tuple, and metric quartet supplied,
the local photon-baryon scalar hierarchy map is fixed on one physical closed
shell.

Status:

- `derived / scoped as maps`

Important boundary:

- the local primitive loading `R(z)` is not a silent one-slot collapse of the
  hierarchy-wide perturbation `R` slot

### 8. Hierarchy-to-transfer projector

Given an explicit scalar source history, the transparent scalar source laws,
closed radial chain, and LOS integration map produce explicit `Delta_l^X(q)`
packets.

Status:

- `derived / scoped as maps`

### 9. Shell power and LOS assembly

The shell covariance and `C_l` assembly are explicit once shell weights and
transfer packets are supplied.

Status:

- `derived / scoped`

## Exact status boundary

What is closed:

- a scoped typed scalar pipeline exists from source shell to transfer packets
  and shell-summed spectra
- there is no longer a missing connector class in the perturbation center

What is not closed:

- a universal IO-native Stage-2 renormalization theorem
- a theorem-grade hierarchy-wide one-slot collapse on `R`
- a universal automatic TT/TE/EE solver for arbitrary branches or sectors

## No-`R`-collapse rule

The pipeline publication keeps the following statement explicit:

- no silent one-slot collapse on the hierarchy-wide perturbation `R` slot is
  licensed anywhere in the composed pipeline

That rule is carried in the theorem dictionary itself, not only in lab notes.

## Verification

Verification at publication time:

- `python -m pytest tests -q` -> `85 passed`
- `python build_bundle.py` completed cleanly

The public theorem surface is prerendered, so these status labels appear in the
HTML source directly.
