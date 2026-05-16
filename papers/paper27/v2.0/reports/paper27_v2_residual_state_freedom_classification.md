# Paper 27 v2.0 Residual State Freedom Classification

Date: 2026-05-16

## Question

After Paper 27 fixes the lifted scalar-bridge carrier

```text
h_vec = L^2(R,dnu) tensor H_g tensor Omega^1_coex(S^3)
```

and after Paper 31 fixes the rank-one scalar-amplitude bridge-readable quotient
state, how much freedom remains in the full boundary/source state?

Does P1 reduce the remaining freedom to a finite set, or does essentially
infinite residual freedom remain?

## Executive Verdict

P1 sharply limits the geometry, spectrum, temperature scale, and lowest-shell
Hawking quotient. It does **not** reduce the full `h_vec` state to a finite
choice.

The remaining full-carrier state freedom is infinite-dimensional unless a new
full-state selection theorem is added. The freedom is not a free
scalar-amplitude parameter because the Paper 31 bridge quotient fixes the
rank-one `A_s` readout. But the full covariance on `h_vec` still admits
infinitely many residual components in directions invisible to the native
scalar-amplitude map.

The strongest theorem-grade statement is:

```text
The admissible full-carrier covariance space decomposes into a fixed
rank-one bridge-readable quotient plus an infinite-dimensional residual cone
contained in the joint null space of the currently fixed scalar-amplitude
readout.
```

Status:

- `DERIVED/CONDITIONAL_VERIFIED` for fixed scalar-amplitude quotient rigidity;
- `DERIVED/THEOREM` for infinite residual freedom relative to the current
  scalar-amplitude observable family;
- `OPEN/PREMISE_GAP` for full `h_vec` state selection.

## What P1 Fixes

P1 states that the observable universe is inside a Schwarzschild black hole.
For the present state-selection question, it fixes:

1. the existence of the Schwarzschild horizon boundary;
2. the horizon radius `r_s`;
3. the round horizon-sphere coexact spectrum

   ```text
   lambda_l^(1,coex) = l(l+1)/r_s^2;
   ```

4. the Hawking inverse temperature

   ```text
   beta_H = 4 pi r_s / (hbar c);
   ```

5. the lowest coexact quotient frequency

   ```text
   omega_1 = sqrt(2) c / r_s;
   ```

6. the dimensionless lowest-shell occupation exponent

   ```text
   beta_H hbar omega_1 = 4 pi sqrt(2).
   ```

Together with P2 and one-mode CCR/KMS uniqueness, this closes the rank-one
lowest-shell scalar-amplitude quotient state:

```text
g_H = 1/(exp(4 pi sqrt(2)) - 1).
```

## What P1 Does Not Fix

P1 does not by itself fix:

1. a positive one-particle generator on the full `h_vec`;
2. a full quasifree covariance operator on all coexact shells;
3. correlations or weights in directions killed by the scalar bridge;
4. the state in non-amplitude shell directions;
5. the state in later observable sectors not represented by the Paper 31
   rank-one quotient.

Those require a full state-selection theorem, not just the black-hole geometry.

## Definition 27.R1: Fixed Scalar-Amplitude Quotient

Let `B` be the scalar bridge map entering the Paper 23/Paper 31
source-covariance relation

```text
C^(0) = B G^(1) B^dagger.
```

The fixed scalar-amplitude quotient is the rank-one lowest-shell quotient
`Q_A` of the source carrier selected by the Paper 31 bridge-quotient theorem.
Its covariance is fixed by the Hawking one-mode KMS occupation

```text
G_A = g_H I_Q,
g_H = 1/(exp(4 pi sqrt(2)) - 1),
```

with the Paper 31 source normalization and bridge-visible fraction supplying
the native scalar amplitude.

Chain:

```text
Definition 27.R1
<- Paper 31 C2c' Rank-One Active-Line Source Theorem
<- Paper 31 C2q Lowest-Shell Hawking Quotient Theorem
<- Paper 31 Bridge-Quotient Theorem C^(0)=B G^(1) B^dagger
<- Paper 27 Theorem 27.1 / Theorem 27.5 (Spatial CCR Lift)
<- Paper 26 C2b carrier identification and beta_H hbar omega_1 = 4 pi sqrt(2)
<- one-mode CCR/KMS uniqueness [standard Araki-Woods / harmonic oscillator KMS]
<- Hawking temperature for Schwarzschild horizon [Hawking 1975]
<- P1
<- P2
```

## Definition 27.R2: Scalar-Amplitude Residual Cone

The scalar-amplitude residual cone is

```text
R_A = {Delta G >= 0 : B Delta G B^dagger = 0}
```

where `Delta G` is a positive residual covariance on the gauge/null-reduced
source carrier.

Elements of `R_A` may change the full carrier state, but they do not change
the native scalar-amplitude covariance.

Chain:

```text
Definition 27.R2
<- Definition 27.R1
<- Paper 31 Bridge-Quotient Theorem C^(0)=B G^(1) B^dagger
<- standard positive-cone structure for quasifree CCR covariances
<- P2
```

## Lemma 27.R3: Residual Perturbation Preserves the Native Scalar Amplitude

Let `G_0` be any admissible covariance whose restriction to the fixed quotient
`Q_A` is `G_A`. Let `Delta G in R_A`. Then

```text
G_epsilon = G_0 + epsilon Delta G
```

has the same scalar-amplitude bridge covariance as `G_0` for every
`epsilon >= 0` for which the CCR positivity/domain conditions remain satisfied.

### Proof

By definition of `R_A`,

```text
B Delta G B^dagger = 0.
```

Therefore

```text
B G_epsilon B^dagger
= B(G_0 + epsilon Delta G)B^dagger
= B G_0 B^dagger + epsilon B Delta G B^dagger
= B G_0 B^dagger.
```

So the scalar-amplitude observable cannot distinguish `G_epsilon` from `G_0`.

Chain:

```text
Lemma 27.R3
<- Definition 27.R2
<- linearity of B G B^dagger
<- Paper 31 Bridge-Quotient Theorem
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.R4: Infinite Residual Directions Exist

The residual cone `R_A` is infinite-dimensional on the current lifted carrier.

### Proof

The lifted carrier contains the infinite coexact spatial sector

```text
Omega^1_coex(S^3) = direct sum over coexact vector shells.
```

The scalar-amplitude quotient `Q_A` is rank one: it is the lowest-shell
bridge-readable quotient used by the native scalar-amplitude chain. Removing
or fixing one rank-one quotient cannot exhaust an infinite-dimensional
coexact carrier.

More explicitly, choose any sequence of nonnegative coefficients `{a_j}` with
finite support on coexact shell directions orthogonal to the rank-one quotient
and invisible to the scalar-amplitude bridge compression. Define

```text
Delta G = sum_j a_j P_j,
```

where `P_j` are mutually orthogonal finite-rank projectors onto such residual
directions. Then `Delta G >= 0` and, by construction,

```text
B Delta G B^dagger = 0.
```

There are infinitely many independent choices of the finite-support sequence
`{a_j}` because the coexact shell tower is infinite. Hence `R_A` is
infinite-dimensional.

This proof uses only the current scalar-amplitude readout. It does not assert
that every residual direction remains invisible to every possible future
observable. It says only that current Paper 31 scalar-amplitude rigidity does
not make the full state finite or unique.

Chain:

```text
Lemma 27.R4
<- Definition 27.R1
<- Definition 27.R2
<- Paper 27 Theorem 27.1 / Theorem 27.5 (h_vec carrier)
<- Hodge decomposition and infinite coexact shell tower on S^3
<- Paper 31 rank-one scalar-amplitude quotient
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem 27.R5: Infinite Residual State Freedom after Fixed Scalar-Amplitude Quotient

### Statement

After imposing:

1. P1 Schwarzschild interior geometry,
2. P2 exterior-physics admissibility,
3. Paper 27 Spatial CCR Lift,
4. Paper 31 rank-one lowest-shell scalar-amplitude quotient selection,

the admissible full-carrier covariance space is not finite. It contains an
infinite-dimensional residual cone `R_A` of covariance perturbations that do
not alter the native scalar-amplitude observable.

Therefore P1 narrows the state-selection problem but does not reduce it to a
finite state choice. Full `h_vec` state selection remains `OPEN/PREMISE_GAP`.

### Proof

Definition 27.R1 fixes the rank-one scalar-amplitude quotient state. Lemma
27.R3 proves that any residual covariance in `R_A` leaves the scalar-amplitude
bridge covariance unchanged. Lemma 27.R4 proves that `R_A` is
infinite-dimensional on the current lifted carrier.

Thus the state space compatible with the fixed native scalar amplitude is not
a finite set. It contains infinitely many full-carrier covariances differing
outside the scalar-amplitude quotient.

P1 supplies the black-hole geometry and the spectrum on which this statement is
made. It fixes the lowest-shell Hawking quotient but does not specify a full
positive one-particle generator or covariance on every residual coexact shell.
Therefore P1 does not eliminate the infinite residual cone.

Chain:

```text
Theorem 27.R5
<- Definition 27.R1
<- Definition 27.R2
<- Lemma 27.R3
<- Lemma 27.R4
<- Paper 31 C2c' Rank-One Active-Line Source Theorem
<- Paper 31 C2q Lowest-Shell Hawking Quotient Theorem
<- Paper 31 Bridge-Quotient Theorem C^(0)=B G^(1) B^dagger
<- Paper 27 Theorem 27.1 / Theorem 27.5 (Spatial CCR Lift)
<- Paper 26 C2b carrier identification and beta_H hbar omega_1 = 4 pi sqrt(2)
<- Hawking temperature for Schwarzschild horizon [Hawking 1975]
<- standard CCR quasifree covariance theory and one-mode KMS uniqueness
<- Hodge decomposition on S^3
<- P1
<- P2
```

Status: `DERIVED/THEOREM` for infinite residual freedom relative to the current
scalar-amplitude observable family.

## Corollary 27.R6: Residual Freedom Is Not a Hidden `A_s` Parameter

The infinite residual freedom identified in Theorem 27.R5 is not a hidden
fitted parameter for the native scalar amplitude.

### Proof

Every residual covariance in `R_A` satisfies

```text
B Delta G B^dagger = 0.
```

Therefore it does not alter the scalar-amplitude covariance. The native
`A_s` value is fixed by the rank-one Hawking quotient and cannot be retuned by
choosing an element of `R_A`.

Chain:

```text
Corollary 27.R6
<- Theorem 27.R5
<- Lemma 27.R3
<- Paper 31 Bridge-Quotient Theorem
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Corollary 27.R7: What Would Make the Freedom Finite

The residual freedom would become finite, or vanish, only if a new theorem
fixed the full covariance on the residual coexact tower or proved that all
residual directions are gauge/null or quotient-equivalent to the fixed
rank-one state.

Candidate theorem forms:

1. Full Hawking restriction theorem:

   ```text
   G^(1) = G_HHI^(1)|_{h_vec}
   ```

   with an invariant embedding of `h_vec` into the Hartle-Hawking/Hawking
   algebra and a proved one-particle generator on the full coexact carrier.

2. Joint-observable exhaustion theorem:

   ```text
   intersection of kernels of all active IO observables = gauge/null sector.
   ```

   This would show that every non-gauge residual direction is read by some
   current observable and is therefore constrained.

3. Full quotient-collapse theorem:

   ```text
   h_vec / joint null(active observables) is finite-dimensional.
   ```

   This would reduce the problem to a finite covariance matrix.

None of these is currently banked in Papers 1-31. Without one of them, the
infinite residual cone remains.

Status: `OPEN/PREMISE_GAP` for full state selection.

## Interpretation

The user's intuition is right: adding `A_s` and the observed CMB context
narrows the state space dramatically. But it narrows it by fixing a projection,
not by fixing the full state.

The current theorem-grade picture is:

```text
full covariance G
= fixed scalar-amplitude quotient
  + infinite residual covariance invisible to current A_s readout.
```

This is not a problem for `A_s`. It is a frontier for future observable-class
closure. If later CMB transfer, tensor, visibility, or polarization observables
read more of the residual directions, those directions stop being parasitic and
must be fixed or ruled out.

## Final Verdict

P1 does not reduce the residual full-carrier state space to finite freedom.
Under the current IO stack, after the fixed scalar-amplitude quotient is
imposed, an infinite-dimensional residual covariance cone remains.

This residual freedom is harmless for native `A_s` but load-bearing for any
future claim that the full boundary/source state on `h_vec` is uniquely fixed.
