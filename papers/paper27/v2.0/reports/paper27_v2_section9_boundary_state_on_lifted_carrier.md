# Paper 27 v2.0 Section 9 Draft: Boundary State on the Lifted Carrier

Date: 2026-05-16

## Executive Verdict

The canonical carrier is theorem-grade; the full canonical state on that carrier is not.

Paper 27 Theorem 27.1 fixes the scalar-bridge carrier

```text
h_vec = L^2(R, dnu) tensor H_g tensor Omega^1_coex(S^3)
```

inside the standard homogeneous left-invariant gauge. That result is
`DERIVED/THEOREM`.

However, the current Papers 1-26 stack plus the Paper 31 bridge-quotient picture
does **not** force a unique equilibrium state on the full `h_vec`. The obstruction
is structural: a CCR carrier does not determine a quasifree state until a
positive one-particle dynamics/modular generator and state class are fixed.
The existing reduced Paper 17 KMS/A-vacuum package has the wrong spectral type
to contain the full coexact Hawking carrier as an exact modular subsystem.

The theorem-grade positive result is scoped:

```text
On the rank-one lowest-shell scalar-amplitude bridge quotient, the state is
uniquely the Hawking beta_H-KMS one-mode state.
```

That scoped result is already banked in Paper 31 as the rank-one active-line /
C2q quotient theorem. It closes the native scalar-amplitude source state on the
lowest-shell quotient, not the full state on `h_vec`.

## Status Labels

- Full carrier state on `h_vec`: `OPEN/PREMISE_GAP`.
- Claim that the current reduced Paper 17 KMS state already restricts to the
  full Hawking coexact carrier: `DERIVED/NO-GO` within the current reduced
  Paper 17 modular class.
- Rank-one lowest-shell scalar-amplitude quotient state:
  `DERIVED/CONDITIONAL_VERIFIED` in the Paper 31 bridge-quotient scope.
- Structural constraints on admissible states: `DERIVED/THEOREM`.

## Definition 27.9.1: Lifted Scalar-Bridge Carrier

The lifted scalar-bridge carrier is the one-particle space

```text
h_vec = L^2(R, dnu) tensor H_g tensor Omega^1_coex(S^3)
```

fixed by Paper 27 Theorem 27.1. It is the unique minimal non-gauge 1-form
carrier compatible with the Paper 23 scalar bridge, the gauge/null quotient,
the coexact Hodge branch on `S^3`, and the standard homogeneous left-invariant
gauge.

Chain:

```text
Definition 27.9.1
<- Paper 27 v2.0 Theorem 27.1 / prior Theorem 27.5 (Spatial CCR Lift)
<- Paper 17 shared one-particle factor L^2(R,dnu) tensor H_g
<- Paper 22 v2.0 Theorem 22.2 (Hodge Spectrum)
<- Paper 22 v2.0 Theorem 22.4 (Channel Floor)
<- Paper 22 v2.0 Theorem 22.5 (Homogeneous Gauge Placement)
<- Paper 23 Theorem 23.2 (N = n +/- 1 selection rule)
<- Paper 23 Theorem 23.3 (No-Doubling covariance form)
<- Paper 23 Theorem 23.4 (scalar bridge uniqueness)
<- Hodge decomposition on S^3 with H^1(S^3)=0 [standard differential geometry]
<- P1 (observable universe inside a Schwarzschild black hole)
<- P2 (physics inside equals physics outside)
```

## Definition 27.9.2: Full-Carrier Equilibrium State

A full-carrier equilibrium state on `h_vec` means a centered quasifree CCR state
on the gauge/null-reduced Weyl algebra over `h_vec`, with covariance `G >= 0`,
compatible with the stated bridge symplectic quotient and invariant under the
homogeneous `SU(2)` symmetry of the standard left-invariant gauge.

This definition does not select a state. It only defines the admissible state
class.

Chain:

```text
Definition 27.9.2
<- Definition 27.9.1
<- standard CCR/Weyl quasifree-state construction [Bratteli-Robinson; Araki-Woods]
<- Paper 23 Lemma A / quasi-free restriction after gauge-null quotient
<- P2 (standard exterior quantum field theory imported for interior physics)
```

## Lemma 27.9.3: KMS Restriction Lemma

Let `omega` be a `beta`-KMS state on a C*-dynamical system `(A, alpha_t)`. If
`B subset A` is an `alpha_t`-invariant C*-subalgebra, then the restricted state
`omega|_B` is a `beta`-KMS state on `(B, alpha_t|_B)`.

### Proof

The KMS condition is tested on pairs of elements of the algebra. For
`b_1,b_2 in B`, the analytic strip function supplied by the KMS property of
`omega` on `A` is still defined and satisfies the same boundary relation,
because `B` is invariant under `alpha_t`. Therefore `omega|_B` satisfies the
KMS condition on `B`.

Chain:

```text
Lemma 27.9.3
<- KMS definition for C*-dynamical systems [standard operator algebra;
   Bratteli-Robinson, Operator Algebras and Quantum Statistical Mechanics]
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.9.4: Fixed One-Mode CCR KMS Uniqueness

For a one-complex-dimensional bosonic CCR/Weyl algebra with free one-particle
dynamics

```text
tau_t(W(z)) = W(exp(i t omega) z),   omega > 0,
```

there is a unique centered quasifree `beta`-KMS state at finite inverse
temperature `beta`. Its occupation number is

```text
n_beta(omega) = 1 / (exp(beta hbar omega) - 1).
```

### Proof

For a finite-dimensional bosonic oscillator with fixed positive one-particle
Hamiltonian, the Gibbs/KMS quasifree state is unique. Equivalently, the CCR
two-point function is fixed by the Bose factor and the canonical commutation
relation. In one dimension this leaves no matrix or shell-weight freedom after
`beta` and `omega` are fixed.

Chain:

```text
Lemma 27.9.4
<- Araki-Woods quasifree CCR KMS uniqueness / standard harmonic oscillator
   Gibbs-KMS theorem
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.9.5: Full `h_vec` State Non-Selection

The carrier identification in Definition 27.9.1 does not force a unique
equilibrium state on the full `h_vec`.

### Proof

A centered quasifree CCR state is fixed by a positive covariance operator
subject to the CCR positivity condition. A KMS state is fixed only after a
positive one-particle generator and inverse temperature are specified. The
carrier `h_vec` fixes the Hilbert space and gauge-reduced carrier type, but it
does not by itself select the one-particle generator on
`Omega^1_coex(S^3)`, the shell weighting, or the relation between the continuous
`L^2(R,dnu)` factor and the discrete coexact spatial spectrum.

Explicitly, if `H` is one positive self-adjoint dynamics on `h_vec`, then
`aH` with any constant `a > 0` is another positive self-adjoint dynamics on the
same carrier. Unless an external theorem fixes `a` and the full functional form
of `H`, the corresponding KMS covariances

```text
G_H      = (exp(beta H) - 1)^(-1)
G_(aH)   = (exp(beta a H) - 1)^(-1)
```

are distinct admissible quasifree covariances on the same carrier. Homogeneity
and `SU(2)` invariance constrain each shell to scalar blocks by Schur's lemma,
but they do not determine the scalar eigenvalue assigned to each shell.

Therefore the carrier theorem alone does not determine the full equilibrium
state.

Chain:

```text
Lemma 27.9.5
<- Definition 27.9.1
<- Definition 27.9.2
<- standard CCR quasifree-state classification
<- Schur's lemma for SU(2)-invariant shell blocks
<- P2
```

Status: `DERIVED/THEOREM` as a non-selection result.

## Lemma 27.9.6: Reduced Paper 17 KMS Class Spectral No-Go

The existing reduced Paper 17 thermal-plus-gauge KMS/A-vacuum class cannot
already contain the canonical full coexact Hawking carrier as an exact modular
subsystem.

### Proof

On the theorem-grade reduced Paper 17/Paper 18 sector, the reduced gauge input
is central:

```text
K_hat_g = K_gauge I.
```

The one-particle reduced modular generator acts on the continuous
`L^2(R,dnu)` thermal factor, scaled by the central gauge weight. Its spectral
type is therefore the continuous translation/dilation spectral type of the
reduced thermal factor.

The canonical Hawking coexact angular carrier on a round horizon sphere has
discrete Hodge spectrum

```text
lambda_l^(1,coex) = l(l+1)/r_s^2,  l >= 1,
omega_l = c sqrt(lambda_l).
```

The full coexact angular generator is pure point. A nonzero unitary
intertwiner cannot identify a purely absolutely continuous spectral subsystem
with a pure-point angular Hodge generator. Hence the present reduced Paper 17
KMS package cannot already contain the full canonical coexact Hawking carrier
as an exact modular subsystem.

This does not rule out a future enlarged state construction. It rules out only
the claim that the current reduced Paper 17 state already proves the full
carrier state selection.

Chain:

```text
Lemma 27.9.6
<- Paper 17 reduced thermal-plus-gauge KMS/A-vacuum class
<- Paper 18 reduced central gauge scalar K_hat_g = K_gauge I
<- standard spectral theorem for self-adjoint generators
<- Hodge spectrum on the round S^2/S^3 coexact angular carrier
<- P1
<- P2
```

Status: `DERIVED/NO-GO` within the current reduced Paper 17 modular class.

## Theorem 27.9.7: Boundary State Non-Selection on the Full Lifted Carrier

### Statement

Within the current Papers 1-26 stack, even augmented by the Paper 31
bridge-quotient picture, the full equilibrium state on

```text
h_vec = L^2(R,dnu) tensor H_g tensor Omega^1_coex(S^3)
```

is not uniquely forced.

What is theorem-grade is the following classification:

1. The carrier is fixed: `DERIVED/THEOREM`.
2. Admissible full-carrier states are constrained to gauge/null-reduced
   quasifree CCR states compatible with the scalar bridge: `DERIVED/THEOREM`.
3. Symmetry makes shell blocks scalar on irreducible `SU(2)` components, but
   does not fix their eigenvalues: `DERIVED/THEOREM`.
4. The existing reduced Paper 17 KMS class cannot be used as a hidden proof of
   the full coexact Hawking state: `DERIVED/NO-GO`.
5. The full state-selection problem remains `OPEN/PREMISE_GAP`.

### Proof

Definition 27.9.1 fixes the Hilbert carrier. Definition 27.9.2 defines the
admissible state class. Lemma 27.9.5 shows that a CCR carrier and symmetry
constraints do not determine a unique covariance on the full carrier. Lemma
27.9.6 rules out the most tempting hidden-closure claim: that the existing
Paper 17 reduced KMS/A-vacuum already contains the full coexact Hawking carrier
as a modular subsystem.

The external Hawking/Hartle-Hawking/KMS literature supplies a distinguished
thermal state on suitable black-hole field algebras, but the current IO stack
does not prove the missing invariant embedding and generator-identification
map from that full black-hole algebra to the full `h_vec` covariance used by
the scalar bridge. Therefore the full state on `h_vec` is constrained but not
selected.

Chain:

```text
Theorem 27.9.7
<- Definition 27.9.1
<- Definition 27.9.2
<- Lemma 27.9.5
<- Lemma 27.9.6
<- Kay-Wald 1991 / Hartle-Hawking-Israel external black-hole KMS state results
   used only as external context, not as a completed carrier-identification map
<- P1
<- P2
```

Status: `DERIVED/NO-GO` against full-state uniqueness from the current stack;
full `h_vec` state remains `OPEN/PREMISE_GAP`.

## Corollary 27.9.8: Rank-One Lowest-Shell Quotient State Selection

### Statement

On the rank-one lowest-shell scalar-amplitude bridge quotient, the physical
state is uniquely the Hawking `beta_H`-KMS one-mode state:

```text
g_H = 1 / (exp(4 pi sqrt(2)) - 1).
```

This is a scoped result. It applies to the one-dimensional bridge quotient used
by the native scalar-amplitude source-side chain. It does not select the state
on the full `h_vec`.

### Proof

Paper 31's bridge-quotient theorem shows that the scalar-amplitude chain sees
the source covariance only through

```text
C^(0) = B G^(1) B^dagger
```

and therefore only through the quotient `H_src / ker(B)`. On the lowest-shell
active scalar branch, that quotient is one-dimensional and has the canonical
boundary representative `Omega^1_coex(S^2, ell=1)`.

For the round Schwarzschild horizon sphere,

```text
lambda_1^(1,coex) = 2/r_s^2,
omega_1 = sqrt(2) c / r_s,
beta_H = 4 pi r_s / (hbar c),
beta_H hbar omega_1 = 4 pi sqrt(2).
```

By P1 the boundary is a Schwarzschild black-hole horizon. By P2, standard
black-hole QFT applies to the boundary mode. Lemma 27.9.4 then fixes the
unique one-mode KMS occupation at Hawking inverse temperature:

```text
g_H = 1 / (exp(beta_H hbar omega_1) - 1)
    = 1 / (exp(4 pi sqrt(2)) - 1).
```

Rotational symmetry makes the `ell=1` triplet covariance scalar; the normalized
rank-one bridge quotient inherits one mode's occupation. Therefore there is no
remaining state freedom on this quotient.

Chain:

```text
Corollary 27.9.8
<- Paper 31 C2c' Rank-One Active-Line Source Theorem
<- Paper 31 C2q Lowest-Shell Hawking Quotient Theorem
<- Paper 31 Bridge-Quotient Theorem C^(0)=B G^(1) B^dagger
<- Paper 27 Theorem 27.1 / Theorem 27.5 (Spatial CCR Lift)
<- Paper 26 C2b carrier identification and beta_H hbar omega_1 = 4 pi sqrt(2)
<- Lemma 27.9.4
<- Hawking temperature for Schwarzschild horizon [Hawking 1975]
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` in the rank-one lowest-shell
scalar-amplitude bridge-quotient scope.

## Theorem 27.9.9: Bridge-Readable State Rigidity and Full-Carrier Residual Freedom

### Statement

Let `G_1` and `G_2` be two admissible centered quasifree covariances on the
lifted carrier `h_vec`. Restrict attention to the Paper 31 scalar-amplitude
bridge-readable sector, i.e. the rank-one lowest-shell quotient selected by

```text
C^(0) = B G^(1) B^dagger
```

on the active scalar-amplitude branch.

If `G_1` and `G_2` satisfy the Paper 31 quotient-state condition on that
rank-one sector, then

```text
B G_1 B^dagger = B G_2 B^dagger
```

for the scalar-amplitude observable. Consequently, all remaining full-carrier
state freedom lies in directions that are invisible to the native scalar
amplitude: `ker(B)`, non-amplitude shell directions, or later observables not
represented by the rank-one scalar-amplitude quotient.

Equivalently: the scalar-amplitude bridge-readable state is rigid, while the
full state on `h_vec` remains underdetermined.

### Proof

Paper 31's bridge-quotient theorem proves that the scalar-amplitude chain sees
the source covariance only through the compressed covariance

```text
C^(0) = B G^(1) B^dagger.
```

Therefore two source covariances that agree on the quotient
`H_src / ker(B)` are indistinguishable to the scalar-amplitude chain.

Corollary 27.9.8 fixes the state on the rank-one lowest-shell quotient. That
quotient has the canonical boundary representative
`Omega^1_coex(S^2, ell=1)`, frequency

```text
omega_1 = sqrt(2) c / r_s,
```

and Hawking inverse temperature

```text
beta_H = 4 pi r_s / (hbar c).
```

By the one-mode CCR/KMS uniqueness theorem, the occupation on that quotient is
uniquely

```text
g_H = 1 / (exp(beta_H hbar omega_1) - 1)
    = 1 / (exp(4 pi sqrt(2)) - 1).
```

Thus any admissible Paper 31-compatible scalar-amplitude source state has the
same quotient covariance and hence the same `B G B^dagger` for the native
scalar-amplitude observable.

Now let `Delta G = G_1 - G_2`. Since the two states agree on the rank-one
bridge-readable quotient, the scalar-amplitude compression satisfies

```text
B Delta G B^dagger = 0.
```

So `Delta G` may exist as full-carrier residual freedom, but it does not change
the scalar-amplitude covariance. Such freedom can live in `ker(B)`, in
non-amplitude shell directions, or in sectors read by observables other than
the Paper 31 rank-one scalar-amplitude quotient. It is therefore residual
full-carrier freedom, not a free scalar-amplitude parameter.

This proves bridge-readable rigidity without promoting the full `h_vec` state
to a unique Hawking state.

Chain:

```text
Theorem 27.9.9
<- Corollary 27.9.8 (rank-one lowest-shell quotient state selection)
<- Paper 31 C2c' Rank-One Active-Line Source Theorem
<- Paper 31 C2q Lowest-Shell Hawking Quotient Theorem
<- Paper 31 Bridge-Quotient Theorem C^(0)=B G^(1) B^dagger
<- Paper 23 Theorem 23.3 (No-Doubling covariance form)
<- Paper 23 Theorem 23.4 (scalar bridge uniqueness)
<- Paper 27 Theorem 27.1 / Theorem 27.5 (Spatial CCR Lift)
<- Paper 26 C2b carrier identification and beta_H hbar omega_1 = 4 pi sqrt(2)
<- Lemma 27.9.4 (one-mode CCR/KMS uniqueness)
<- Hawking temperature for Schwarzschild horizon [Hawking 1975]
<- P1 (observable universe inside a Schwarzschild black hole)
<- P2 (physics inside equals physics outside)
```

Status: `DERIVED/CONDITIONAL_VERIFIED` for the Paper 31 scalar-amplitude
bridge-readable quotient. Full-carrier state selection remains
`OPEN/PREMISE_GAP`.

## What Theorem 27.9.7 Does Not Cover

The no-go does not say that a full state on `h_vec` can never be derived. It
says the current stack does not derive it, and the current reduced Paper 17 KMS
state cannot secretly supply it.

To extend the result from the rank-one quotient to the full carrier, a future
theorem would need to prove all of the following:

1. an invariant embedding of the full `Omega^1_coex(S^3)` bridge carrier into
   the relevant black-hole Hawking/Hartle-Hawking field algebra;
2. identification of the induced one-particle generator on that carrier;
3. equality of the bridge covariance `G^(1)` with the restricted
   Hawking/Hartle-Hawking two-point function on that carrier;
4. compatibility of the resulting shell covariance with the Paper 28/Paper 31
   primitive DtN full-window scalar-source law.

Without those, full-carrier state selection remains open.

## Recommended Insertion Boundary for Paper 27 v2.0

Use the result as a new §9 with this top-line wording:

```text
Theorem 27.9.7 proves that the lifted scalar-bridge carrier is fixed but the
full equilibrium state on that carrier is not forced by the current stack.
The rank-one lowest-shell scalar-amplitude quotient is an exception: by the
Paper 31 bridge-quotient theorem, its state is uniquely the Hawking beta_H-KMS
one-mode state. Thus Paper 27 closes the carrier and classifies the state
selection boundary; it does not claim full-carrier Hawking state selection.
```

Do not write:

- "The boundary state on `h_vec` is uniquely Hawking."
- "Paper 17 KMS inheritance proves the bridge covariance is Hawking."
- "The full coexact carrier state is closed by Kay-Wald/Gerard."
- "`beta_H hbar omega_1 = 4 pi sqrt(2)` by itself proves the state."

Allowed wording:

- "Full-carrier state selection remains open."
- "The rank-one lowest-shell scalar-amplitude quotient state is
  `DERIVED/CONDITIONAL_VERIFIED` by the Paper 31 bridge-quotient theorem."
- "The scalar-amplitude bridge-readable state is rigid; residual full-carrier
  freedom is not a free scalar-amplitude parameter."
- "The current reduced Paper 17 modular class has a spectral-type obstruction
  to serving as the full coexact Hawking carrier."

Final verdict: theorem-grade scoped no-go plus bridge-readable quotient
rigidity; ready for physics review.
