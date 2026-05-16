# Paper 27 v2.0 P1 Background/Perturbation Residual Classification

Date: 2026-05-16

## Question

Can P1 protect the framework from the residual `h_vec` state freedom without
selecting the full ambient state?

Specifically: can P1 force higher-shell residual diagnostics to be either
future perturbative observables, backreaction-constrained deformations, gauge
nulls, or separately fixed exterior imports, rather than hidden background
normalization parameters?

## Executive Verdict

Yes.

P1 does not select the full state on `h_vec`, but it does supply a strong
background/perturbation separation theorem:

```text
The exact IO background is the Schwarzschild/OS support geometry plus the
banked Hawking-compatible boundary sector. Any nonzero h_vec-internal
higher-shell residual diagnostic is not a background normalization freedom. It
is either a perturbative observable, a backreaction-constrained deformation, a
gauge/null direction, or a separately fixed exterior import.
```

This is enough to protect the zero-fitted-parameter status of current scalar
observables:

- current scalar-amplitude observables factor through the Paper 23/Paper 31
  scalar bridge quotient;
- residual shell tails cannot tune native `A_s`;
- future higher-shell diagnostics may exist, but they become falsifiable
  perturbation-sector observables, not hidden knobs.

Status:

```text
DERIVED/CONDITIONAL_VERIFIED
```

Scope:

```text
P1-fixed exact background plus perturbative h_vec sector.
```

## Definition 27.P1B1: Exact P1 Background Sector

The exact P1 background sector is the background structure fixed before
perturbative source covariance is considered:

1. the Schwarzschild horizon radius and mass parameter;
2. the closed `K=+1` OS interior support geometry;
3. the round horizon symmetry;
4. the banked Hawking-compatible boundary thermal datum used by the active
   scalar-amplitude quotient;
5. the framework constants already fixed independently of residual `h_vec`
   shell-tail choices.

The exact background sector does not include arbitrary additional coexact
shell power on `h_vec`.

Chain:

```text
Definition 27.P1B1
<- P1 (observable universe inside a Schwarzschild black hole)
<- standard Schwarzschild horizon geometry
<- closed OS interior geometry
<- Hawking boundary thermality for the active quotient
<- Paper 31 rank-one scalar-amplitude quotient closure
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Definition 27.P1B2: `h_vec` Perturbation Sector

The `h_vec` perturbation sector is the gauge/null-reduced coexact
one-particle carrier

```text
h_vec = L^2(R,dnu) tensor H_g tensor Omega^1_coex(S^3)
```

used by the Paper 23 scalar bridge and upgraded by the Paper 27 Spatial CCR
Lift Theorem.

Its rank-one scalar-amplitude quotient is fixed by Paper 31. Its residual
shell-tail directions are perturbative directions unless separately proved to
belong to the exact background.

Chain:

```text
Definition 27.P1B2
<- Paper 27 Spatial CCR Lift Theorem
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line quotient closure
<- Theorem 27.G6
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Definition 27.P1B3: Background-Normalization Freedom

A background-normalization freedom is a variable that can be changed while
leaving the exact P1 background interpretation intact and while changing a
current cosmological prediction.

If a quantity changes the Schwarzschild/OS background stress-energy, horizon
flux, mass parameter, or round-horizon symmetry, it is not a background
normalization freedom. It is a perturbation or a different background.

Chain:

```text
Definition 27.P1B3
<- Definition 27.P1B1
<- semiclassical Einstein equation compatibility
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Definition 27.P1B4: Higher-Shell Residual Diagnostic

A higher-shell residual diagnostic is an observable or diagnostic functional
on `h_vec` that reads covariance content outside the rank-one scalar-amplitude
quotient, for example

```text
O_n(G) = Tr(P_n G P_n)
```

where `P_n` projects onto a coexact shell outside the active quotient.

Chain:

```text
Definition 27.P1B4
<- Theorem 27.AO4
<- coexact shell projectors on Omega^1_coex(S^3)
<- Theorem 27.G7
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.P1B5: Higher-Shell Residuals Are Not Exact-Background Normalizations

A nonzero higher-shell residual diagnostic on `h_vec` is not a background
normalization freedom of the exact P1 sector.

### Proof

By Definition 27.P1B1, the exact background sector is fixed by the
Schwarzschild/OS geometry and the banked Hawking-compatible active quotient.
By Definition 27.P1B3, a background-normalization freedom must be changeable
without changing the exact background interpretation.

A nonzero higher-shell residual diagnostic has one of four statuses:

1. it carries stress-energy, flux, shell power, or anisotropic stress, in which
   case Theorem 27.B8 classifies it as a backreaction-constrained deformation
   rather than a hidden background freedom;
2. it is bridge-null for the current scalar-amplitude quotient, in which case
   Theorem 27.O5 and Corollary 27.O6 show it cannot change native `A_s`;
3. it is gauge/null, in which case it is not physical;
4. it is an exterior imported sector with a separately fixed state.

In none of these cases is it a tunable background-normalization parameter for
current scalar observables.

Chain:

```text
Lemma 27.P1B5
<- Definition 27.P1B1
<- Definition 27.P1B3
<- Definition 27.P1B4
<- Theorem 27.B8
<- Theorem 27.O5
<- Corollary 27.O6
<- Theorem 27.AO4
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Lemma 27.P1B6: Higher-Shell Diagnostics Are Future Perturbative Observables If Physical

If a higher-shell residual diagnostic is physical and not gauge/null or
backreaction-forbidden, then it is a perturbative observable of the `h_vec`
sector, not a hidden parameter in the current scalar-amplitude chain.

### Proof

By Definition 27.P1B2, residual shell-tail directions lie in the perturbative
`h_vec` sector outside the rank-one scalar-amplitude quotient. By Theorem
27.AO4, broad P2-admissible diagnostics can in principle read those directions.
If such a diagnostic is physical, it must be treated as an observable with its
own prediction or measurement, not as a silently adjustable parameter in the
background. If it were silently adjustable while changing current scalar
predictions, it would contradict Theorem 27.O5 for scalar-bridge quotient
observables. If it changes stress-energy or flux, Theorem 27.B8 makes it a
backreaction-constrained perturbation.

Therefore a surviving higher-shell diagnostic is a future perturbative
observable.

Chain:

```text
Lemma 27.P1B6
<- Definition 27.P1B2
<- Definition 27.P1B4
<- Theorem 27.AO4
<- Theorem 27.O5
<- Theorem 27.B8
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Theorem 27.P1B7: P1 Background/Perturbation Separation for `h_vec`

Under P1 and P2, residual higher-shell freedom on `h_vec` cannot be used as a
hidden background normalization parameter for current IO scalar observables.

Every higher-shell residual diagnostic is classified as exactly one of:

1. **Scalar-quotient null:** killed by the Paper 23/Paper 31 scalar bridge
   quotient for current scalar observables;
2. **Perturbative observable:** a future diagnostic with its own measurable
   content;
3. **Backreaction-constrained deformation:** a stress-energy/flux/symmetry
   deformation of the exact P1 background;
4. **Gauge/null:** removed by the gauge/null quotient;
5. **External imported sector:** governed by a separately fixed exterior state
   or imported physics input.

### Proof

Let `DeltaG` be a residual shell-tail direction on `h_vec`.

If it is bridge-null for the current scalar-amplitude quotient, Theorem 27.O5
and Corollary 27.O6 show it cannot tune current scalar observables.

If it carries positive background energy, horizon flux, or anisotropic
stress-energy, Theorem 27.B8 classifies it as incompatible with the exact P1
background unless treated as a perturbation/backreaction sector.

If it is gauge/null, it is removed by the quotient defining the physical
carrier.

If it is an imported exterior sector, P2 requires the exterior state or
observable law to be fixed by the imported physics rather than tuned inside IO.

If none of those apply and the diagnostic is physical, Lemma 27.P1B6 classifies
it as a future perturbative observable. It may be measurable or falsifying, but
it is not a hidden background normalization freedom.

The listed cases therefore exhaust the physical statuses of residual
higher-shell diagnostics relative to the exact P1 background.

Chain:

```text
Theorem 27.P1B7
<- Definition 27.P1B1
<- Definition 27.P1B2
<- Definition 27.P1B3
<- Definition 27.P1B4
<- Lemma 27.P1B5
<- Lemma 27.P1B6
<- Theorem 27.O5
<- Corollary 27.O6
<- Theorem 27.B8
<- Theorem 27.AO5
<- Theorem 27.AO6
<- Paper 31 rank-one active-line quotient closure
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Corollary 27.P1B8: Full State Selection Remains Open but Non-Damaging for Current Scalar Predictions

The full ambient state on `h_vec` remains `OPEN/PREMISE_GAP`.

However, that open status does not create a hidden fitted parameter in current
scalar predictions, because residual higher-shell freedom is not a background
normalization freedom and cannot tune the current scalar-bridge quotient.

Chain:

```text
Corollary 27.P1B8
<- Theorem 27.P1B7
<- Theorem 27.O5
<- Corollary 27.O6
<- Theorem 27.E7
<- Theorem 27.X2
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Paper 27 Wording Recommendation

Use this wording:

```text
The full state on h_vec is not selected in this paper. This is not a hidden
normalization freedom for the scalar amplitude. P1 separates exact-background
data from perturbative carrier data: residual higher-shell covariance either is
null under the scalar bridge quotient, is constrained by backreaction, is
gauge/null, is separately fixed by imported exterior physics, or becomes a
future perturbative observable. It is not adjustable inside the current scalar
prediction chain.
```

Do not say:

```text
P1 selects the full h_vec state.
```

Do not say:

```text
Higher-shell h_vec observables are unphysical.
```

The correct claim is:

```text
Higher-shell h_vec observables, if physical, are future perturbative
observables rather than hidden background parameters.
```

## Final Boundary

After this theorem package:

```text
Current scalar-bridge observable exhaustion:
    DERIVED/THEOREM.

Banked IO observable classification:
    DERIVED/THEOREM.

P1 background/perturbation separation:
    DERIVED/CONDITIONAL_VERIFIED.

Native A_s residual fit freedom:
    excluded.

Full h_vec state selection:
    OPEN/PREMISE_GAP.
```

