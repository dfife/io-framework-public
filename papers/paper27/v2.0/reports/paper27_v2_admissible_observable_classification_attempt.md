# Paper 27 v2.0 Admissible Observable Classification Attempt

Date: 2026-05-16

## Question

Can we prove the remaining theorem needed after the joint-observable exhaustion
attempt?

Target theorem:

```text
Every IO-admissible physical observable on h_vec either:
  (a) factors through the Paper 23 scalar bridge quotient,
  (b) belongs to a separate carrier sector,
  (c) is stress-energy/backreaction-forbidden by P1,
  (d) is gauge/null,
  or (e) is an imported exterior observable with a separately fixed state.
```

If true, the residual shell-tail freedom on `h_vec` would be physically null
for all IO-admissible observables, not only for the current scalar-bridge
quotient class.

## Executive Verdict

The universal admissible-observable classification theorem does **not** close.

The obstruction is not abstract algebra. It is standard physics:

```text
If h_vec is a physical coexact connection/vector perturbation sector, then
standard exterior/interior physics admits quadratic energy, flux, stress, and
shell-power observables built from that sector. These observables do not have
to factor through the Paper 23 scalar bridge quotient B G B^dagger.
```

Therefore the proposed classification is false unless "IO-admissible" is
defined so narrowly that it excludes legitimate stress-energy or field-strength
observables. That would be a new scope restriction, not a theorem from P1+P2.

What does close:

```text
Theorem 27.AO5:
Current scalar-bridge and currently banked IO observables are exhausted by the
known quotient/carrier classes.
```

What does not close:

```text
Theorem 27.AO6:
Universal admissible-observable exhaustion over all physically valid future
observables on h_vec.
```

Status summary:

- current realized/banked observable classification: `DERIVED/THEOREM`;
- native `A_s` residual-fit exclusion: `DERIVED/THEOREM`;
- universal all-admissible-observable classification: `DERIVED/NO-GO`;
- full `h_vec` state selection: `OPEN/PREMISE_GAP`.

## Definition 27.AO1: Banked IO Observable on `h_vec`

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
4. a separate carrier class such as transverse-traceless tensor perturbations
   or weak two-time bridge-rate observables, as established in Papers 24 and 25.

Chain:

```text
Definition 27.AO1
<- Paper 23 Theorem 23.3
<- Paper 27 Spatial CCR Lift Theorem
<- Paper 31 rank-one active-line scalar-amplitude quotient
<- Paper 24 Theorem 24.G1 transverse-traceless observable-class closure
<- Paper 25 Theorem 25.13 weak observable-class closure
<- P1
<- P2
```

Status: `DERIVED/THEOREM` as a definition of current banked scope.

## Definition 27.AO2: Broad P2-Admissible Future Observable on `h_vec`

A broad P2-admissible future observable on `h_vec` is a gauge-invariant or
gauge-fixed-then-quotient-invariant observable constructible from standard
exterior/interior physics on the physical coexact connection/vector
perturbation sector, compatible with P1 background constraints.

Examples include:

- shell energy;
- shell power;
- stress-energy;
- flux;
- polarization or vector diagnostics;
- higher-point functions;
- non-Gaussian diagnostics;
- any imported exterior observable with a standard field-strength or
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

## Lemma 27.AO3: Banked Observables Factor Through Known Quotients or Separate Carriers

Every currently banked IO observable that reads `h_vec` either factors through
the Paper 23 scalar bridge quotient, through the Paper 31 rank-one active-line
quotient, or belongs to a separate established carrier class.

### Proof

The Paper 23 scalar-source covariance mechanism is explicitly

```text
C^(0) = B G^(1) B^dagger.
```

Paper 31 narrows the scalar-amplitude source state to a rank-one active-line
quotient of this compression.

Paper 24's lithium channel is transverse-traceless, not a direct `h_vec`
residual-shell observable. Its closure is scoped to the Paper 24
transverse-traceless observable class.

Paper 25's weak observable class is a centered two-time KMS correlator on the
weak bridge canonical-commutation-relation algebra under its own H1-H3 package.
It is not a free higher-shell diagnostic on the Paper 27 residual cone.

Paper 27's CLASS confrontation uses the scalar source amplitude and related
parameters as frozen inputs; it does not add a new functional of the full
`G^(1)`.

Therefore every currently banked observable is covered by known quotient or
separate-carrier classes.

Chain:

```text
Lemma 27.AO3
<- Definition 27.AO1
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line quotient
<- Paper 24 Theorem 24.G1
<- Paper 25 Theorem 25.13
<- Paper 27 verified CLASS input inventory
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.AO4: Broad P2-Admissible Observables Can Separate Residual Shell Tails

There exist broad P2-admissible future observables on `h_vec` that can separate
residual shell-tail covariance differences.

### Proof

Let `P_n` be a coexact shell projector on the gauge/null-reduced
`Omega^1_coex(S^3)` sector, with `n` outside the rank-one scalar-amplitude
quotient. For a covariance `G`, define a shell-power or shell-energy
functional

```text
O_n(G) = Tr(P_n H_n^{1/2} G H_n^{1/2} P_n)
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
<- Theorem 27.G7 (infinite residual shell-tail family)
<- standard operator algebra separation by shell projectors
<- standard stress-energy / field-strength observables for vector fields
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem 27.AO5: Banked IO Observable Classification Closure

For currently banked IO observables involving `h_vec`, all residual shell-tail
freedom is either:

1. killed by the Paper 23/Paper 31 scalar bridge quotient;
2. outside the observable's carrier class;
3. excluded as positive-energy background freedom by P1 backreaction
   compatibility;
4. or not part of the current banked observable.

Therefore residual shell-tail freedom is not a hidden parameter for any
currently banked IO result.

### Proof

By Lemma 27.AO3, current banked observables factor through known quotients or
separate carriers. For scalar-bridge quotient observables, Theorem 27.O5 proves
bridge-null residuals are invisible. For the scalar amplitude specifically,
Corollary 27.O6 excludes residual fit freedom. For positive-energy background
additions, Theorem 27.B8 excludes them from exact-P1 background admissibility.
For separate carrier classes, residuals on `h_vec` are not part of the
observable definition.

Thus all currently banked observables are classified.

Chain:

```text
Theorem 27.AO5
<- Lemma 27.AO3
<- Theorem 27.O5
<- Corollary 27.O6
<- Theorem 27.B8
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one active-line quotient
<- Paper 24 Theorem 24.G1
<- Paper 25 Theorem 25.13
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem 27.AO6: Universal Admissible-Observable Classification No-Go

The proposed universal theorem

```text
Every IO-admissible physical observable on h_vec either factors through the
Paper 23 scalar bridge quotient, belongs to a separate carrier sector, is
stress-energy/backreaction-forbidden by P1, is gauge/null, or is an imported
exterior observable with a separately fixed state
```

does not follow from P1, P2, standard exterior physics, or the current IO
carrier architecture.

More strongly, the theorem is false under the broad P2-admissible future
observable definition 27.AO2.

### Proof

Lemma 27.AO4 constructs broad P2-admissible observables that directly read
higher coexact shell covariance. These observables are:

- not scalar-bridge quotient observables, because they do not factor through
  `B G B^dagger`;
- not separate carrier observables, because they act on `h_vec` itself;
- not gauge/null by construction after the gauge/null quotient;
- not automatically P1-forbidden, because a measurement/diagnostic of
  perturbation shell power is not the same as adding that perturbation as a new
  exact background state;
- not imported exterior observables with separately fixed state unless an
  additional state-selection theorem is supplied.

Therefore the proposed exhaustive classification misses a legitimate class:

```text
h_vec-internal higher-shell diagnostics.
```

One could forbid this class by definition, but that would narrow
"IO-admissible" rather than derive the classification from P1+P2.

Chain:

```text
Theorem 27.AO6
<- Lemma 27.AO4
<- Theorem 27.G7
<- standard vector-field shell energy/stress observables
<- standard operator algebra separation
<- P1
<- P2
```

Status: `DERIVED/NO-GO`.

## Corollary 27.AO7: What Would Be Needed to Close the Universal Version

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
   quotient algebra generated by the current scalar bridge, TT, weak, and
   imported exterior classes.

Each option is a real additional theorem or a deliberate scope definition. None
is currently forced by P1+P2 alone.

Chain:

```text
Corollary 27.AO7
<- Theorem 27.AO6
<- Theorem 27.X2
<- Theorem 27.O7
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Final Boundary

Can I do the admissible-observable classification theorem?

Answer:

```text
Yes for current/banked IO observables.
No for universal all-admissible future observables.
```

Final status:

```text
Banked IO observable classification:
    DERIVED/THEOREM.

Native A_s residual fit freedom:
    excluded.

Universal admissible-observable classification:
    DERIVED/NO-GO.

Full h_vec state selection:
    OPEN/PREMISE_GAP.
```

The decisive obstruction is the legitimate broad P2-admissible class of
`h_vec`-internal higher-shell diagnostics.

