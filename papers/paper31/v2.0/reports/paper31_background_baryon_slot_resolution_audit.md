# Paper 31: Background Baryon Slot Resolution Audit

Date: 2026-04-04

## Question

Cosmo's ruling is:

1. the background Friedmann equation carries only total projected Schur matter
   `omega_m = 0.15939026836`,
2. the split into `omega_b + omega_cdm` at background level is only CLASS
   bookkeeping,
3. typed baryons should enter only where the framework assigns them at
   thermodynamics / perturbation level.

This audit therefore tests exactly one practical implementation on the active
Schur branch:

- background bookkeeping split:
  `omega_b,bookkeeping = omega_b,struct = 0.02594110201749857`
- background CDM bookkeeping:
  `omega_cdm = omega_m - omega_b,bookkeeping = 0.13344916634250142`
- chemistry slot:
  `omega_b,geom = 0.02108`
- acoustic slot:
  `omega_b,eff = 0.0291`
- clustering/background bookkeeping slot in current fork:
  `omega_b,clustering = omega_b,struct`

No slot scan was performed.

## Branch Verification

`derived`:
the active Schur practical branch uses

- `H0 = 68.91`
- `Omega_k = -0.005613722564239`

The older `H0 = 67.58`, `Omega_k = -0.006` package is the retired mixed branch,
not the live Schur branch.

## Fixed IO Constants

- `x = 1.519`
- `gamma = 0.2375`
- `f_Gamma = 0.946605531726076`
- `K_gauge = 0.05487281774291466`
- `J_Phi = 0.8113740489243784`
- `eta_IO = 0.6227480978487567`
- `A_s = 2.0072459972737347e-09`

## Practical Cases

### One-number structured Schur baseline

This is the existing practical structured branch:

- `omega_b = omega_b,struct`
- `omega_cdm = omega_m - omega_b,struct`

Result:

- `chi2_TTTEEE+lowTT = 2135.722987`
- `100theta_s = 1.056106033`

### Framework background-slot resolution case

This is the direct non-scanned implementation of Cosmo's ruling in the current
fork:

- `omega_b_geom = 0.02108`
- `omega_b_eff = 0.0291`
- `omega_b_clustering = omega_b,struct = 0.02594110201749857`
- `omega_cdm = 0.13344916634250142`

Result:

- `chi2_TTTEEE+lowTT = 7966.229457`
- `100theta_s = 1.039361162`

Difference relative to the one-number practical structured baseline:

- `Delta chi2 = 5830.506469`

## Executive Result

`verified`:
the current fork does not yield a competitive practical calculator when the
background baryon slot is treated as neutral bookkeeping and the typed baryons
are inserted directly as

- chemistry -> `omega_b,geom`
- acoustic loading -> `omega_b,eff`
- background bookkeeping -> `omega_b,struct`

on the active Schur branch.

The direct current-fork result is

\[
\chi^2 = 7966.229457,
\]

which is dramatically worse than the one-number practical structured branch.

`derived / diagnostic`:
this means the remaining calculator problem is not just the old mixed-background
mistake. Even after enforcing

- active Schur `H0`
- no typed background baryon slot
- fixed total `omega_m`

the present explicit typed-baryon wiring in the patched CLASS fork is still not
a faithful practical realization of the Paper 31 baryon map.

## Boundary

This audit does **not** promote any new best-fit branch.
It is a fixed, framework-implied confrontation only.

The result should be read as evidence that the current explicit slot insertion
layer is still wrong or incomplete, not as evidence against the background-slot
ruling itself.
