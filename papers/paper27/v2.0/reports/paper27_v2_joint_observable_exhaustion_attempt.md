# Paper 27 v2.0 Joint-Observable Exhaustion Attempt

Date: 2026-05-16

## Question

Can the remaining residual state freedom on

```text
h_vec = L^2(R,dnu) tensor H_g tensor Omega^1_coex(S^3)
```

be eliminated without selecting the full ambient state, by proving that all
residual shell-tail directions are physically null for the IO observables that
can read `h_vec`?

This is the last viable route identified after the exterior-generator and
all-routes exhaustion passes.

## Executive Verdict

A scoped exhaustion theorem closes for the **current scalar-bridge observable
class**.

It does not close for all possible future IO observables on `h_vec`.

The correct theorem boundary is:

```text
For observables whose h_vec-dependence factors through the Paper 23 scalar
bridge compression C^(0)=B G^(1) B^dagger and the Paper 31 rank-one
scalar-amplitude quotient, every residual covariance DeltaG satisfying
B DeltaG B^dagger = 0 is physically invisible.
```

Status:

```text
DERIVED/THEOREM for the current scalar-bridge quotient observable class.
```

The universal statement

```text
all residual directions are null for every possible IO observable
```

does not close, because future tensor, vector, polarization, non-Gaussian, or
higher-shell observables could be explicitly designed to read residual coexact
shell tails. Those observables are not part of the current scalar-amplitude
quotient class.

Status:

```text
DERIVED/NO-GO as a universal all-future-observable exhaustion claim.
```

## Definition 27.O1: Current Scalar-Bridge Quotient Observable

A current scalar-bridge quotient observable is any observable `O` whose
dependence on the lifted source covariance `G^(1)` enters only through the
Paper 23 scalar bridge compression

```text
C^(0) = B G^(1) B^dagger
```

and, for the scalar-amplitude slot, through the Paper 31 rank-one active-line
quotient of that compression.

Membership is intrinsic:

`O` belongs to this class if replacing `G^(1)` by another covariance with the
same `B G^(1) B^dagger` leaves the definition and numerical value of `O`
unchanged.

Included examples:

- native scalar-amplitude quotient `A_s`;
- scalar-amplitude downstream readouts using only the Paper 31 active line;
- current Paper 27 CLASS input use of the scalar amplitude as a frozen scalar
  source amplitude;
- any scalar-bridge observable whose source side is exactly `B G^(1) B^dagger`.

Excluded examples:

- a hypothetical future observable that reads a higher coexact shell directly;
- tensor-sector observables whose carrier is TT rather than `h_vec`;
- vector/polarization/non-Gaussian observables with direct residual-shell
  sensitivity;
- any observable whose definition contains an additional functional of
  `G^(1)` not factored through `B G^(1) B^dagger`.

Chain:

```text
Definition 27.O1
<- Paper 23 Theorem 23.3 (No-Doubling covariance form)
<- Paper 27 Spatial CCR Lift Theorem
<- Paper 31 rank-one scalar-amplitude quotient theorem
<- P1
<- P2
```

Status: `DERIVED/THEOREM` as a definition of the current observable class.

## Definition 27.O2: Scalar-Bridge Residual

A scalar-bridge residual covariance increment is a positive or signed
Hadamard-regular covariance difference `DeltaG` on the gauge/null-reduced
source carrier satisfying

```text
B DeltaG B^dagger = 0.
```

When positivity is imposed, this is the residual cone from Theorem 27.R5.
When signed replacement states are considered, this is the bridge-null
Hadamard smoothing residual difference.

Chain:

```text
Definition 27.O2
<- Definition 27.O1
<- Theorem 27.R5
<- Theorem 27.G6
<- Paper 23 Theorem 23.3
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.O3: Bridge-Null Residuals Are Invisible to Scalar-Bridge Quotient Observables

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

### Proof

By Definition 27.O1, the observable `O` depends on `G^(1)` only through the
compressed covariance `B G^(1) B^dagger`, and for the scalar amplitude through
the rank-one quotient of that compressed covariance. If two covariances have
the same compression, the input datum seen by `O` is identical. Therefore the
observable value is identical.

For `G_2 = G_1 + DeltaG`, linearity gives

```text
B G_2 B^dagger
= B(G_1 + DeltaG)B^dagger
= B G_1 B^dagger + B DeltaG B^dagger
= B G_1 B^dagger.
```

So every bridge-null residual is invisible to every observable in the class.

Chain:

```text
Lemma 27.O3
<- Definition 27.O1
<- Definition 27.O2
<- linearity of B G B^dagger
<- Paper 23 Theorem 23.3
<- Paper 31 rank-one quotient theorem
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.O4: Current Paper 27 Source-Side Scalar Inputs Belong to the Class

The current Paper 27 scalar-source inputs that depend on the lifted carrier
belong to Definition 27.O1.

These include the native scalar-amplitude quotient and any downstream CLASS
use of that scalar amplitude as a frozen scalar-source input.

### Proof

Paper 27's source-side scalar input inherits the Paper 26/Paper 31 scalar
amplitude chain. That chain uses the Paper 23 No-Doubling form

```text
C^(0) = B G^(1) B^dagger
```

and the Paper 31 rank-one active-line quotient for the scalar amplitude. It
does not contain an additional functional that directly reads residual
coexact shell tails.

The CLASS confrontation in Paper 27 uses the resulting scalar amplitude and
spectral parameters as numerical inputs. It does not add a new source-side
functional of the full covariance `G^(1)`.

Therefore the current Paper 27 scalar-source use of `h_vec` belongs to the
current scalar-bridge quotient observable class.

Chain:

```text
Lemma 27.O4
<- Definition 27.O1
<- Paper 23 Theorem 23.3
<- Paper 27 Spatial CCR Lift Theorem
<- Paper 31 rank-one scalar-amplitude quotient theorem
<- Paper 27 verified CLASS input inventory
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` on the current Paper 27 source-input
inventory.

## Theorem 27.O5: Current Scalar-Bridge Observable Exhaustion

For the current scalar-bridge quotient observable class, the residual
shell-tail freedom on `h_vec` is physically null.

Equivalently, for every observable `O` in Definition 27.O1 and every residual
`DeltaG` in Definition 27.O2,

```text
O(G + DeltaG) = O(G)
```

whenever both sides are admissible.

### Proof

By Definition 27.O1, every observable in the class depends on `G^(1)` only
through `B G^(1) B^dagger` and possibly the Paper 31 rank-one quotient of that
compressed covariance. By Definition 27.O2, a residual satisfies
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
<- Theorem 27.G6
<- Theorem 27.B8
<- Paper 23 Theorem 23.3
<- Paper 27 Spatial CCR Lift Theorem
<- Paper 31 rank-one scalar-amplitude quotient theorem
<- P1
<- P2
```

Status: `DERIVED/THEOREM` for the current scalar-bridge quotient observable
class.

## Corollary 27.O6: No Hidden Native `A_s` Fit Parameter

Residual shell-tail freedom on `h_vec` is not a hidden fit parameter for native
`A_s`.

### Proof

Native `A_s` belongs to the Paper 31 rank-one scalar-amplitude quotient. By
Theorem 27.O5, bridge-null residuals cannot change any observable in that
class. Therefore they cannot tune native `A_s`.

This conclusion is independent of whether the full ambient state on `h_vec` is
selected.

Chain:

```text
Corollary 27.O6
<- Theorem 27.O5
<- Paper 31 rank-one scalar-amplitude quotient theorem
<- Corollary 27.R6
<- Corollary 27.B9
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem 27.O7: Universal All-Future-Observable Exhaustion No-Go

The claim

```text
all residual directions on h_vec are physically null for every possible IO
observable
```

does not follow from P1, P2, current IO geometry, or the current scalar-bridge
architecture.

### Proof

Theorem 27.O5 proves exhaustion only for observables that factor through the
Paper 23 bridge compression. That factorization is an intrinsic membership
condition.

Now consider a hypothetical future observable whose definition includes a
linear functional on a higher coexact shell coefficient of the covariance, for
example

```text
O_f(G) = Tr(P_n G P_n)
```

for a coexact shell projector `P_n` orthogonal to the rank-one scalar-amplitude
quotient, or a polarization/non-Gaussian/vector diagnostic that explicitly
depends on a higher-shell covariance block.

Such an observable is mathematically compatible with the carrier structure.
It is not a current IO physical observable, and it may later be excluded by
additional physics, backreaction, or class discipline. But its existence as an
algebraic observable shows that bridge-nullity for `B G B^dagger` is not the
same thing as nullity for every conceivable future observable on `h_vec`.

Therefore universal all-future-observable exhaustion requires an additional
theorem classifying all IO physical observables on `h_vec`, or proving that
every residual-shell functional is gauge/null, stress-energy-forbidden, or
outside P2-admissible physics. That theorem is not yet proved.

Chain:

```text
Theorem 27.O7
<- Theorem 27.O5
<- existence of higher-shell projectors in Omega^1_coex(S^3)
<- Theorem 27.G7 (residual shell-tail family remains infinite)
<- standard operator algebra: linear functionals can separate nonzero
   covariance differences
<- P1
<- P2
```

Status: `DERIVED/NO-GO` for universal all-future-observable exhaustion.

## Remaining Frontier

The joint-observable route has now split into a closed and an open part.

Closed:

```text
Current scalar-bridge quotient observables:
    residual shell tails are null.
```

Open:

```text
All possible future IO observables on h_vec:
    not exhausted.
```

The only way to upgrade the open part is to prove a stronger admissible
observable classification theorem:

```text
Every IO-admissible physical observable on h_vec either:
  (a) factors through the Paper 23 scalar bridge quotient,
  (b) belongs to a separate carrier sector such as TT and therefore does not
      read h_vec residuals,
  (c) is stress-energy/backreaction-forbidden by P1,
  (d) is gauge/null,
  or (e) is an imported exterior observable with a separately fixed state.
```

That theorem may be approachable, but it is not automatic. It would be a
framework-level observable-classification theorem, not a state-selection
theorem.

## Final Boundary

Best current Paper 27 status after this pass:

```text
Current scalar-bridge observable exhaustion:
    DERIVED/THEOREM.

Native A_s residual fit freedom:
    excluded.

Universal all-future h_vec observable exhaustion:
    DERIVED/NO-GO from current inputs.

Full h_vec state selection:
    OPEN/PREMISE_GAP.
```

