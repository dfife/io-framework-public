# Paper 27 v2.0 Kappa-Style Audit and R4 Damage Report

## Executive Verdict

No hidden fitted parameter was found in the active Paper 27 v2.0 theorem chain
or in the v2.0 bundle scripts.

The active v2.0 manuscript no longer uses the retired fully IO-native CLASS
Planck-confrontation branch as a live result. The live result is the theorem
stack around the lifted scalar-bridge carrier, the rank-one quotient seen by
current scalar observables, residual-state freedom on the full carrier, and
the explicit no-go boundary for universal future-observable closure.

R4 damage is contained: no active v2.0 bundle script uses `R4 = 1`, and Paper
27 v2.0 does not claim an independent CMB-temperature prediction. The bundle
imports `R4_FIRAS = 1.0031014644` only as a framework-boundary constant from
Paper 17 v1.5.

## R4 Review

### Active Bundle Scripts

The active bundle scripts do not use R4 in any live computation. The value
`R4_FIRAS = 1.0031014644` is recorded in `data/imported_constants.json` and in
`scripts/07_kappa_r4_audit_summary.py` for audit continuity.

### Retired Paper 27 Scripts Excluded From v2.0 Bundle

The following local historical scripts/results in `results/paper27/` contain
old CMB-temperature or Planck-confrontation constants and are excluded from
the Paper 27 v2.0 public bundle:

- `paper27_full_io_native_planck_tt_confrontation.py`
- `paper27_io_geometry_floor_scan.py`
- `paper27_theta_s_constrained_geometry_floor_scan.py`
- `paper27_baryon_diagnostics.py`
- `paper27_c3_candidate_discriminator_scan.py`
- `paper27_trgb_jwst_scope.py`

These scripts belong to retired or diagnostic branches. Rewriting them into
the active bundle would incorrectly resurrect content the v2.0 manuscript
explicitly supersedes.

### Manuscript Hygiene Finding

The v2.0 draft contains historical appendix/version-history language from
older CMB-temperature and FIRAS-inversion branches. That language should remain
clearly historical if retained. It must not be read as an active Paper 27 v2.0
CMB-temperature prediction.

Recommendation: if the appendix is not intended to preserve historical audit
records, remove or annotate the old CMB-prediction/FIRAS-inversion material so
the active claim boundary is unambiguous.

## Hidden-Parameter Walkthrough

### Gamma_BI

`gamma_BI = 0.2375` is imported as the framework Barbero-Immirzi value. Paper
27 does not fit it to scalar amplitude, Planck spectra, visibility, or any
other Paper 27 observable.

Verdict: `IMPORTED/EMPIRICAL`, no hidden fit in Paper 27.

### C1a Cross-Term Vanishing

The C1a result is forced by an `SU(2)` representation mismatch: the scalar
singlet block and the coexact vector branch have no nonzero equivariant
intertwiner.

Verdict: `DERIVED/THEOREM`.

### Spatial CCR Lift

The carrier

```text
h_vec = L2(R,dnu) tensor H_g tensor Omega1_coex(S3)
```

uses the closed `S^3` spatial slice, Hodge decomposition, and the lowest
coexact vector shell. The result does not introduce a tunable carrier
dimension or adjustable representation choice.

Verdict: `DERIVED/THEOREM`.

### Rank-One Scalar Quotient

The scalar bridge reads a rank-one quotient of the full lifted carrier. The
full carrier still has residual state freedom, but that residual does not
enter the current scalar quotient and cannot tune the active scalar amplitude.

Verdict: scalar quotient closure `DERIVED/THEOREM`; full carrier state
selection remains `OPEN/PREMISE_GAP`.

### Backreaction and Passivity

Backreaction and passivity reduce the allowed residual state class but do not
select a unique full state on `h_vec`.

Verdict: `DERIVED/CONDITIONAL_VERIFIED` restriction; not a hidden fit.

### Bridge-Readable Hawking/KMS Covariance

The active bridge-readable covariance factor is

```text
1/(exp(4*pi*sqrt(2)) - 1) = 1.9139114172056972e-08
```

on the rank-one bridge-readable shell. This value is computed directly by the
bundle validator.

Verdict: bridge-readable shell fixed; full state not globally selected.

### Visibility-Slot Inheritance

Paper 27 v2.0 records

```text
omega_b,vis = omega_b,eff = 0.02910
```

as inherited visibility-slot equality. It does not fit the visibility value in
Paper 27.

Verdict: `DERIVED/THEOREM` for the slot inheritance statement; no new fitted
visibility parameter.

## Claim-Label Audit

Active theorem labels in the v2.0 theorem package match the current public
Claims Discipline taxonomy:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `OPEN/PREMISE_GAP`
- `SUPERSEDED`

Historical version-history text contains retired labels or internal workflow
language, including:

- `DERIVED/SCOPED`
- `SEMICLASSICAL PRINCIPLE`
- `CONDITIONAL/THEOREM`
- `KILLED` or dead-route language

Recommendation: leave these only if clearly marked as historical. Do not use
them in active theorem statements.

## Abbreviations and IO-Internal Terms Flagged

The v2.0 draft should define or replace the following for non-IO readers,
especially outside the appendix:

- `IO`
- `CMB`
- `CCR`
- `KMS`
- `TT`
- `QFT`
- `SU(2)`
- `LQG`
- `BDP`
- `GTTP`
- `GMP`
- `TBSb`
- `WMR`
- `AV1`
- `H2`, `H3`
- `C1a`, `C2c`, `C2q`, `C3`
- `OS`
- `ADM`
- `CLASS`
- `PRyMordial`

Terms that read as IO-internal slang and should be defined or replaced:

- `bridge-readable`
- `state-selection debt`
- `banked`
- `slot`
- `payload`
- `horizon-first`
- `IO-native`
- `dead route`
- `killed`
- `A-vacuum`
- `scalar bridge`

## Final Audit Classification

Paper 27 v2.0 is reproducible as a theorem-support bundle with no active R4
damage and no hidden fitted parameter found.

The important surviving open boundary is explicit: the full state on `h_vec`
is not uniquely selected by Paper 27 v2.0. The active scalar observables are
protected by the rank-one quotient and the observable-exhaustion results.
