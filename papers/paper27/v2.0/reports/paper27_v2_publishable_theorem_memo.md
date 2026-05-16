# Paper 27 v2.0 Publishable Theorem Memo: Boundary State on the Lifted Carrier

Date: 2026-05-16

## Purpose

This memo consolidates the theorem-grade results intended for insertion into
Paper 27 v2.0 after the state-selection investigation on the lifted
scalar-bridge carrier

```text
h_vec = L^2(R,dnu) tensor H_g tensor Omega^1_coex(S^3).
```

The result is not a full state-selection theorem. The correct publication
boundary is narrower and stronger:

```text
The full ambient state on h_vec remains OPEN/PREMISE_GAP.

The residual state freedom outside the scalar bridge quotient cannot tune the
native scalar amplitude A_s, cannot be hidden as an exact-P1 background
normalization, and is either quotient-null for current scalar observables,
backreaction-constrained, gauge/null, separately imported, or a future
perturbative observable.
```

This is the theorem package that can go into Paper 27. It is designed to be
auditable inline: every load-bearing statement has a status label and a
dependency chain back to P1, P2, named standard physics, or banked framework
theorems.

## Executive Insertion Recommendation

Insert a new subsection after the Paper 27 Spatial CCR Lift / boundary-state
discussion, with a title such as:

```text
Boundary-State Residuals: Quotient Exhaustion and P1 Background Separation
```

Include three theorem blocks:

1. **Scalar-bridge quotient exhaustion**: Definitions 27.O1-27.O2, Lemma
   27.O3, Lemma 27.O4, Theorem 27.O5, Corollary 27.O6.
2. **Banked-observable classification and universal no-go**: Definitions
   27.AO1-27.AO2, Lemma 27.AO3, Lemma 27.AO4, Theorem 27.AO5, Theorem
   27.AO6, Corollary 27.AO7.
3. **P1 background/perturbation separation**: Definitions 27.P1B1-27.P1B4,
   Lemma 27.P1B5, Lemma 27.P1B6, Theorem 27.P1B7, Corollary 27.P1B8.

Add a short guardrail paragraph after the theorem blocks:

```text
The full state on h_vec is not selected in this paper. The theorem package
proves that the remaining full-carrier state freedom is not a hidden fit
parameter in the current scalar-amplitude chain. It does not prove that every
future perturbative observable on h_vec is physically null.
```

Recommended final label summary:

```text
Current scalar-bridge observable exhaustion: DERIVED/THEOREM.
Banked IO observable classification: DERIVED/THEOREM.
P1 background/perturbation separation: DERIVED/CONDITIONAL_VERIFIED.
Native A_s residual fit freedom: excluded by theorem.
Universal all-future h_vec observable exhaustion: DERIVED/NO-GO.
Full h_vec state selection: OPEN/PREMISE_GAP.
```

## Theorem Package I: Scalar-Bridge Quotient Exhaustion

### Definition 27.O1: Current Scalar-Bridge Quotient Observable

A current scalar-bridge quotient observable is any observable `O` whose
dependence on the lifted source covariance `G^(1)` enters only through the
Paper 23 scalar bridge compression

```text
C^(0) = B G^(1) B^dagger
```

and, for the scalar-amplitude slot, through the Paper 31 rank-one active-line
quotient of that compression.

Membership is intrinsic: `O` belongs to this class if replacing `G^(1)` by
another covariance with the same `B G^(1) B^dagger` leaves the definition and
numerical value of `O` unchanged.

Included examples:

- the native scalar-amplitude quotient `A_s`;
- scalar-amplitude downstream readouts using only the Paper 31 active line;
- current Paper 27 CLASS input use of the scalar amplitude as a frozen scalar
  source amplitude;
- any scalar-bridge observable whose source side is exactly
  `B G^(1) B^dagger`.

Excluded examples:

- a future observable that reads a higher coexact shell directly;
- tensor-sector observables whose carrier is transverse-traceless rather than
  `h_vec`;
- vector, polarization, or non-Gaussian observables with direct residual-shell
  sensitivity;
- any observable whose definition contains an additional functional of
  `G^(1)` not factored through `B G^(1) B^dagger`.

Chain:

```text
Definition 27.O1
<- Paper 23 Theorem 23.3 (No-Doubling covariance form)
<- Paper 27 v2.0 Theorem 27.1 / Spatial CCR Lift
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- P1 (observable universe inside a Schwarzschild black hole)
<- P2 (physics inside equals physics outside)
```

Status: `DERIVED/THEOREM` as a definition of the current observable class.

### Definition 27.O2: Scalar-Bridge Residual

A scalar-bridge residual covariance increment is a positive or signed
Hadamard-regular covariance difference `DeltaG` on the gauge/null-reduced
source carrier satisfying

```text
B DeltaG B^dagger = 0.
```

When positivity is imposed, this is the residual cone from Theorem 27.R5. When
signed replacement states are considered, this is the bridge-null Hadamard
smoothing residual difference.

Chain:

```text
Definition 27.O2
<- Definition 27.O1
<- Theorem 27.R5 (infinite residual state freedom after fixed scalar quotient)
<- Paper 23 Theorem 23.3
<- standard positive-cone and covariance-difference structure for quasifree
   CCR states
<- P2
```

Status: `DERIVED/THEOREM`.

### Lemma 27.O3: Bridge-Null Residuals Are Invisible to Scalar-Bridge Quotient Observables

Let `O` be a current scalar-bridge quotient observable. Let `G_1` and `G_2` be
two admissible source covariances such that

```text
B G_1 B^dagger = B G_2 B^dagger.
```

Then

```text
O(G_1) = O(G_2).
```

In particular, if `G_2 = G_1 + DeltaG` and

```text
B DeltaG B^dagger = 0,
```

then `DeltaG` is invisible to `O`.

Proof. By Definition 27.O1, `O` depends on `G^(1)` only through the compressed
covariance `B G^(1) B^dagger`, and for the scalar amplitude through the
rank-one quotient of that compressed covariance. If two covariances have the
same compression, the input datum seen by `O` is identical. Therefore the
observable value is identical.

For `G_2 = G_1 + DeltaG`, linearity gives

```text
B G_2 B^dagger
= B(G_1 + DeltaG)B^dagger
= B G_1 B^dagger + B DeltaG B^dagger
= B G_1 B^dagger.
```

Thus every bridge-null residual is invisible to every observable in the class.

Chain:

```text
Lemma 27.O3
<- Definition 27.O1
<- Definition 27.O2
<- linearity of B G B^dagger
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- P2
```

Status: `DERIVED/THEOREM`.

### Lemma 27.O4: Current Paper 27 Source-Side Scalar Inputs Belong to the Class

The current Paper 27 scalar-source inputs that depend on the lifted carrier
belong to Definition 27.O1. These include the native scalar-amplitude quotient
and any downstream CLASS use of that scalar amplitude as a frozen scalar-source
input.

Proof. Paper 27's source-side scalar input inherits the Paper 26/Paper 31
scalar-amplitude chain. That chain uses the Paper 23 No-Doubling form

```text
C^(0) = B G^(1) B^dagger
```

and the Paper 31 rank-one active-line quotient for the scalar amplitude. It
does not contain an additional functional that directly reads residual coexact
shell tails. The CLASS confrontation in Paper 27 uses the resulting scalar
amplitude and spectral parameters as numerical inputs; it does not add a new
source-side functional of the full covariance `G^(1)`.

Therefore the current Paper 27 scalar-source use of `h_vec` belongs to the
current scalar-bridge quotient observable class.

Chain:

```text
Lemma 27.O4
<- Definition 27.O1
<- Paper 23 Theorem 23.3
<- Paper 27 v2.0 Theorem 27.1 / Spatial CCR Lift
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- Paper 27 verified CLASS input inventory
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` on the current Paper 27 source-input
inventory.

### Theorem 27.O5: Current Scalar-Bridge Observable Exhaustion

For the current scalar-bridge quotient observable class, residual shell-tail
freedom on `h_vec` is physically null. Equivalently, for every observable `O`
in Definition 27.O1 and every residual `DeltaG` in Definition 27.O2,

```text
O(G + DeltaG) = O(G)
```

whenever both sides are admissible.

Proof. By Definition 27.O1, every observable in the class depends on `G^(1)`
only through `B G^(1) B^dagger` and possibly the Paper 31 rank-one quotient of
that compressed covariance. By Definition 27.O2, a residual satisfies
`B DeltaG B^dagger = 0`. Lemma 27.O3 then gives invariance of every observable
in the class under addition of the residual. Lemma 27.O4 verifies that the
current Paper 27 scalar-source inputs belong to this class.

Thus the residual shell-tail freedom is null for the current scalar-bridge
quotient observables.

Chain:

```text
Theorem 27.O5
<- Definition 27.O1
<- Definition 27.O2
<- Lemma 27.O3
<- Lemma 27.O4
<- Theorem 27.R5
<- Theorem 27.B8 (backreaction-passivity residual reduction)
<- Paper 23 Theorem 23.3
<- Paper 27 v2.0 Theorem 27.1 / Spatial CCR Lift
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- P1
<- P2
```

Status: `DERIVED/THEOREM` for the current scalar-bridge quotient observable
class.

### Corollary 27.O6: No Hidden Native `A_s` Fit Parameter

Residual shell-tail freedom on `h_vec` is not a hidden fit parameter for native
`A_s`.

Proof. Native `A_s` belongs to the Paper 31 rank-one scalar-amplitude
quotient. By Theorem 27.O5, bridge-null residuals cannot change any observable
in that class. Therefore they cannot tune native `A_s`. This conclusion is
independent of whether the full ambient state on `h_vec` is selected.

Chain:

```text
Corollary 27.O6
<- Theorem 27.O5
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- Corollary 27.R6 (residual freedom is not a hidden A_s parameter)
<- Corollary 27.B9 (positive residuals are not hidden scalar-amplitude fits)
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem Package II: Banked Observable Classification and Universal No-Go

### Definition 27.AO1: Banked IO Observable on `h_vec`

A banked IO observable on `h_vec` is an observable whose construction is
explicitly present in the current Paper 23-Paper 31 chain and whose dependence
on the lifted one-particle covariance is one of:

1. scalar-bridge quotient dependence through

   ```text
   C^(0) = B G^(1) B^dagger;
   ```

2. the Paper 31 rank-one scalar-amplitude active-line quotient;
3. observer-side readout use of the scalar amplitude as an already-frozen
   source parameter;
4. a separate carrier class, such as the Paper 24 transverse-traceless
   observable class or the Paper 25 weak two-time bridge-rate observable class.

Chain:

```text
Definition 27.AO1
<- Paper 23 Theorem 23.3
<- Paper 27 v2.0 Theorem 27.1 / Spatial CCR Lift
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- Paper 24 v3.0 transverse-traceless observable-class closure
<- Paper 25 v2.0 Theorem 25.13 weak observable-class closure
<- P1
<- P2
```

Status: `DERIVED/THEOREM` as a definition of current banked scope.

### Definition 27.AO2: Broad P2-Admissible Future Observable on `h_vec`

A broad P2-admissible future observable on `h_vec` is a gauge-invariant or
gauge-fixed-then-quotient-invariant observable constructible from standard
exterior/interior physics on the physical coexact connection/vector
perturbation sector, compatible with P1 background constraints.

Examples include shell energy, shell power, stress-energy, flux, polarization
or vector diagnostics, higher-point functions, non-Gaussian diagnostics, and
any imported exterior observable with a standard field-strength or
stress-tensor interpretation.

This definition is intentionally broader than Definition 27.AO1. It is the
class a hostile referee can reasonably invoke under P2 if `h_vec` is physical.

Chain:

```text
Definition 27.AO2
<- P2 exterior physics admissibility
<- standard gauge/vector field observables on curved spacetime
<- standard stress-energy and field-strength observables
<- P1 background compatibility
```

Status: `DERIVED/CONDITIONAL_VERIFIED` as a broad admissibility definition
under P1+P2.

### Lemma 27.AO3: Banked Observables Factor Through Known Quotients or Separate Carriers

Every currently banked IO observable that reads `h_vec` either factors through
the Paper 23 scalar bridge quotient, through the Paper 31 rank-one active-line
quotient, or belongs to a separate established carrier class.

Proof. The Paper 23 scalar-source covariance mechanism is explicitly

```text
C^(0) = B G^(1) B^dagger.
```

Paper 31 narrows the scalar-amplitude source state to a rank-one active-line
quotient of this compression. Paper 24's lithium channel is
transverse-traceless, not a direct `h_vec` residual-shell observable. Paper
25's weak observable class is a centered two-time KMS correlator on the weak
bridge canonical-commutation-relation algebra under its own H1-H3 package; it
is not a free higher-shell diagnostic on the Paper 27 residual cone. Paper 27's
CLASS confrontation uses the scalar source amplitude and related parameters as
frozen inputs; it does not add a new functional of the full `G^(1)`.

Therefore every currently banked observable is covered by known quotient or
separate-carrier classes.

Chain:

```text
Lemma 27.AO3
<- Definition 27.AO1
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- Paper 24 v3.0 transverse-traceless observable-class closure
<- Paper 25 v2.0 Theorem 25.13
<- Paper 27 verified CLASS input inventory
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

### Lemma 27.AO4: Broad P2-Admissible Observables Can Separate Residual Shell Tails

There exist broad P2-admissible future observables on `h_vec` that can
separate residual shell-tail covariance differences.

Proof. Let `P_n` be a coexact shell projector on the gauge/null-reduced
`Omega^1_coex(S^3)` sector, with `n` outside the rank-one scalar-amplitude
quotient. For a covariance `G`, define a shell-power or shell-energy
functional

```text
O_n(G) = Tr(P_n H_n^(1/2) G H_n^(1/2) P_n),
```

or, in the simplest shell-power form,

```text
O_n(G) = Tr(P_n G P_n).
```

If `DeltaG` is a residual shell-tail covariance with support in shell `n`, then

```text
B DeltaG B^dagger = 0
```

can hold while

```text
O_n(G + DeltaG) - O_n(G) = Tr(P_n DeltaG P_n) != 0.
```

Such an observable is not an abstract bypass in the Paper 24 sense. If `h_vec`
is a physical coexact connection/vector perturbation sector, shell energy,
stress-energy, and field-strength power are standard physical observables.
P2 cannot exclude them merely because they do not factor through the scalar
bridge quotient.

P1 can exclude positive residual additions from the exact background state by
backreaction compatibility, but it cannot prove that no measurement or
perturbative diagnostic can ever read the shell. A perturbation observable and
a background-state admissibility condition are different claims.

Chain:

```text
Lemma 27.AO4
<- Definition 27.AO2
<- coexact shell projectors on Omega^1_coex(S^3)
<- Theorem 27.R5 (infinite residual shell-tail family)
<- standard operator algebra separation by shell projectors
<- standard stress-energy / field-strength observables for vector fields
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

### Theorem 27.AO5: Banked IO Observable Classification Closure

For currently banked IO observables involving `h_vec`, all residual shell-tail
freedom is either:

1. killed by the Paper 23/Paper 31 scalar bridge quotient;
2. outside the observable's carrier class;
3. excluded as positive-energy background freedom by P1 backreaction
   compatibility;
4. or not part of the current banked observable.

Therefore residual shell-tail freedom is not a hidden parameter for any
currently banked IO result.

Proof. By Lemma 27.AO3, current banked observables factor through known
quotients or separate carriers. For scalar-bridge quotient observables, Theorem
27.O5 proves bridge-null residuals are invisible. For the scalar amplitude
specifically, Corollary 27.O6 excludes residual fit freedom. For
positive-energy background additions, Theorem 27.B8 excludes them from
exact-P1 background admissibility. For separate carrier classes, residuals on
`h_vec` are not part of the observable definition.

Thus all currently banked observables are classified.

Chain:

```text
Theorem 27.AO5
<- Lemma 27.AO3
<- Theorem 27.O5
<- Corollary 27.O6
<- Theorem 27.B8
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line scalar-amplitude quotient theorem
<- Paper 24 v3.0 transverse-traceless observable-class closure
<- Paper 25 v2.0 Theorem 25.13
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

### Theorem 27.AO6: Universal Admissible-Observable Classification No-Go

The proposed universal theorem

```text
Every IO-admissible physical observable on h_vec either factors through the
Paper 23 scalar bridge quotient, belongs to a separate carrier sector, is
stress-energy/backreaction-forbidden by P1, is gauge/null, or is an imported
exterior observable with a separately fixed state
```

does not follow from P1, P2, standard exterior physics, or the current IO
carrier architecture. More strongly, the theorem is false under the broad
P2-admissible future-observable definition 27.AO2.

Proof. Lemma 27.AO4 constructs broad P2-admissible observables that directly
read higher coexact shell covariance. These observables are:

- not scalar-bridge quotient observables, because they do not factor through
  `B G B^dagger`;
- not separate carrier observables, because they act on `h_vec` itself;
- not gauge/null by construction after the gauge/null quotient;
- not automatically P1-forbidden, because a measurement or diagnostic of
  perturbation shell power is not the same as adding that perturbation as a new
  exact background state;
- not imported exterior observables with separately fixed state unless an
  additional state-selection theorem is supplied.

Therefore the proposed exhaustive classification misses a legitimate class:

```text
h_vec-internal higher-shell diagnostics.
```

One could forbid this class by definition, but that would narrow
`IO-admissible` rather than derive the classification from P1+P2.

Chain:

```text
Theorem 27.AO6
<- Lemma 27.AO4
<- Theorem 27.R5
<- standard vector-field shell energy/stress observables
<- standard operator algebra separation
<- P1
<- P2
```

Status: `DERIVED/NO-GO`.

### Corollary 27.AO7: What Would Be Needed to Close the Universal Version

Universal admissible-observable classification can close only if a new theorem
proves one of the following:

1. `h_vec` is not a physical observable carrier beyond the scalar bridge
   quotient;
2. every higher-shell diagnostic on `h_vec` is stress-energy/backreaction
   forbidden even as a perturbative observable, not merely as background-state
   freedom;
3. every P2-admissible higher-shell observable has a separately fixed exterior
   state and cannot carry free residual covariance;
4. the framework's physical-observable algebra is explicitly defined as the
   quotient algebra generated by the current scalar bridge, transverse-
   traceless, weak, and imported exterior classes.

Each option is a real additional theorem or a deliberate scope definition.
None is currently forced by P1+P2 alone.

Chain:

```text
Corollary 27.AO7
<- Theorem 27.AO6
<- Theorem 27.X2 (full state selection requires generator-transfer or
   observable-exhaustion closure)
<- Theorem 27.O7 (universal all-future-observable exhaustion no-go)
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem Package III: P1 Background/Perturbation Separation

### Definition 27.P1B1: Exact P1 Background Sector

The exact P1 background sector is the background structure fixed before
perturbative source covariance is considered:

1. the Schwarzschild horizon radius and mass parameter;
2. the closed `K=+1` Oppenheimer-Snyder interior support geometry;
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
<- closed Oppenheimer-Snyder interior geometry
<- Hawking boundary thermality for the active quotient
<- Paper 31 rank-one scalar-amplitude quotient closure
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

### Definition 27.P1B2: `h_vec` Perturbation Sector

The `h_vec` perturbation sector is the gauge/null-reduced coexact one-particle
carrier

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
<- Paper 27 v2.0 Theorem 27.1 / Spatial CCR Lift
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line scalar-amplitude quotient closure
<- Theorem 27.R5
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

### Definition 27.P1B3: Background-Normalization Freedom

A background-normalization freedom is a variable that can be changed while
leaving the exact P1 background interpretation intact and while changing a
current cosmological prediction.

If a quantity changes the Schwarzschild/Oppenheimer-Snyder background
stress-energy, horizon flux, mass parameter, or round-horizon symmetry, it is
not a background normalization freedom. It is a perturbation or a different
background.

Chain:

```text
Definition 27.P1B3
<- Definition 27.P1B1
<- semiclassical Einstein equation compatibility
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

### Definition 27.P1B4: Higher-Shell Residual Diagnostic

A higher-shell residual diagnostic is an observable or diagnostic functional
on `h_vec` that reads covariance content outside the rank-one scalar-amplitude
quotient, for example

```text
O_n(G) = Tr(P_n G P_n),
```

where `P_n` projects onto a coexact shell outside the active quotient.

Chain:

```text
Definition 27.P1B4
<- Theorem 27.AO4
<- coexact shell projectors on Omega^1_coex(S^3)
<- Theorem 27.R5
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

### Lemma 27.P1B5: Higher-Shell Residuals Are Not Exact-Background Normalizations

A nonzero higher-shell residual diagnostic on `h_vec` is not a background
normalization freedom of the exact P1 sector.

Proof. By Definition 27.P1B1, the exact background sector is fixed by the
Schwarzschild/Oppenheimer-Snyder geometry and the banked Hawking-compatible
active quotient. By Definition 27.P1B3, a background-normalization freedom must
be changeable without changing the exact background interpretation.

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

### Lemma 27.P1B6: Higher-Shell Diagnostics Are Future Perturbative Observables If Physical

If a higher-shell residual diagnostic is physical and not gauge/null or
backreaction-forbidden, then it is a perturbative observable of the `h_vec`
sector, not a hidden parameter in the current scalar-amplitude chain.

Proof. By Definition 27.P1B2, residual shell-tail directions lie in the
perturbative `h_vec` sector outside the rank-one scalar-amplitude quotient. By
Theorem 27.AO4, broad P2-admissible diagnostics can in principle read those
directions. If such a diagnostic is physical, it must be treated as an
observable with its own prediction or measurement, not as a silently adjustable
parameter in the background. If it were silently adjustable while changing
current scalar predictions, it would contradict Theorem 27.O5 for scalar-bridge
quotient observables. If it changes stress-energy or flux, Theorem 27.B8 makes
it a backreaction-constrained perturbation.

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

### Theorem 27.P1B7: P1 Background/Perturbation Separation for `h_vec`

Under P1 and P2, residual higher-shell freedom on `h_vec` cannot be used as a
hidden background normalization parameter for current IO scalar observables.

Every higher-shell residual diagnostic is classified as exactly one of:

1. **Scalar-quotient null:** killed by the Paper 23/Paper 31 scalar bridge
   quotient for current scalar observables;
2. **Perturbative observable:** a future diagnostic with its own measurable
   content;
3. **Backreaction-constrained deformation:** a stress-energy, flux, or
   symmetry deformation of the exact P1 background;
4. **Gauge/null:** removed by the gauge/null quotient;
5. **External imported sector:** governed by a separately fixed exterior state
   or imported physics input.

Proof. Let `DeltaG` be a residual shell-tail direction on `h_vec`.

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
<- Paper 31 rank-one active-line scalar-amplitude quotient closure
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

### Corollary 27.P1B8: Full State Selection Remains Open but Non-Damaging for Current Scalar Predictions

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
<- Theorem 27.E7 (no full exterior-generator embedding from P1+P2 alone)
<- Theorem 27.X2 (full state selection requires generator-transfer or
   observable-exhaustion closure)
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Guardrail No-Go Results to Mention, Not Overuse

These results are important for preventing overclaiming. They do not need to be
expanded in the main body unless the paper has room, but their conclusions
should be reflected in the prose.

### Theorem 27.E7: No Full Exterior-Generator Embedding from P1+P2 Alone

External Hartle-Hawking/Hawking state-selection theorems select a state on an
exterior field algebra once that algebra and Schwarzschild Killing dynamics are
fixed. They do not prove that `CCR(h_vec)` is an invariant subalgebra of the
exterior algebra with the same one-particle generator.

Missing theorem:

```text
CCR(h_vec) subset A_ext,
alpha_t(CCR(h_vec)) subset CCR(h_vec),
H_hvec = iota^* H_ext iota.
```

Status: `DERIVED/NO-GO` as a full closure route from P1+P2 alone.

### Theorem 27.X1: Natural Interior Coexact Dynamics Does Not Equal the Active Hawking Quotient

On the source-free coexact vector branch of the closed `S^3` interior, standard
conformally invariant vector-field dynamics fixes the natural generator

```text
H_S3 = (hbar c / r_s) sqrt(Delta_coex,S3).
```

For the lowest `S^3` coexact shell, this gives

```text
beta_H hbar omega_S3 = 8 pi.
```

The active scalar-amplitude quotient instead uses the reduced horizon `S^2`
coexact exponent

```text
beta_H hbar omega_S2 = 4 pi sqrt(2).
```

Since `8 pi != 4 pi sqrt(2)`, the natural full `S^3` generator cannot be
silently substituted for the active `S^2` Hawking quotient generator.

Status: `DERIVED/THEOREM` for the natural interior generator; `DERIVED/NO-GO`
as a direct full-state closure route.

### Theorem 27.X2: Full State Selection Requires One of Two Nontrivial Closures

The full state on `h_vec` can be closed only by proving at least one of:

1. **Generator-transfer closure:**

   ```text
   H_hvec = U^* H_S2,Hawking U
   ```

   on all physically relevant bridge shells, with the active `S^2` Hawking
   quotient preserved.

2. **Observable-exhaustion closure:**

   ```text
   all residual directions outside the rank-one quotient are gauge/null or
   physically unobservable by every IO observable.
   ```

Current work closes observable exhaustion only for current scalar-bridge
quotient observables and current banked IO observables. It does not close the
universal all-future observable version.

Status: `DERIVED/NO-GO` for full closure without one of the two named future
theorems.

## Recommended Manuscript Wording

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

## Final Verdict

Proof package complete for Paper 27 insertion.

Closed for Paper 27:

```text
Current scalar-bridge observable exhaustion:
    DERIVED/THEOREM.

Banked IO observable classification:
    DERIVED/THEOREM.

P1 background/perturbation separation:
    DERIVED/CONDITIONAL_VERIFIED.

Native A_s residual fit freedom:
    excluded by theorem.
```

Not closed:

```text
Full h_vec state selection:
    OPEN/PREMISE_GAP.

Universal all-future h_vec observable exhaustion:
    DERIVED/NO-GO from current inputs.
```

Ready for Cosmo verification.
