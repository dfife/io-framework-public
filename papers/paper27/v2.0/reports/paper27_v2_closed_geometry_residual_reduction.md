# Paper 27 v2.0 Closed-Geometry Residual Reduction

Date: 2026-05-16

## Question

Can the closed Hilbert-space geometry supplied by P1 reduce the residual
full-carrier state freedom beyond Theorem 27.R5?

Specifically: after the scalar-amplitude quotient is fixed, do compact
closed-space geometry, homogeneity, Hodge decomposition, gauge quotient,
finite-energy/Hadamard regularity, and the Schwarzschild/OS setting reduce the
remaining residual freedom to a finite set, or only to a structured infinite
family?

## Executive Verdict

P1 gives substantial additional restrictions. It reduces the residual freedom
from an arbitrary positive covariance cone to a geometrically classified
coexact shell-functional residual.

However, P1 still does **not** reduce the freedom to a finite set. The residual
state space remains infinite-dimensional, but in a much narrower and more
reviewer-defensible form:

```text
G_residual = F(Delta_coex) on the coexact S^3 shell tower,
```

with:

- exact and harmonic sectors removed;
- shell blocks scalar by homogeneity/SU(2) equivariance;
- one rank-one scalar-amplitude quotient fixed by Paper 31;
- high-shell behavior constrained by finite-energy/Hadamard-type regularity;
- residual freedom reduced to a smoothing/shell-tail sequence invisible to the
  current scalar-amplitude readout.

This is a real improvement over the raw residual-cone theorem. It says the
remaining freedom is not arbitrary. But it remains infinite unless a new
theorem fixes the full one-particle dynamics/KMS generator or proves a joint
observable exhaustion over the residual shells.

## P1 Factors That Limit Selection

### 1. Closed compact spatial geometry

P1 plus the IO OS interior gives a closed `K=+1` spatial bulk with `S^3`
spatial topology. For the coexact carrier, the Hodge Laplacian has pure point
spectrum with finite multiplicities.

This removes continuous spatial-spectrum freedom.

### 2. Hodge decomposition and topology

On `S^3`,

```text
Omega^1(S^3) = d Omega^0(S^3) direct-sum Omega^1_coex(S^3)
```

and

```text
H^1(S^3) = 0.
```

The harmonic 1-form sector is absent. The exact sector is gauge/null for the
scalar-bridge CCR reduction. Therefore the residual physical 1-form state
space lives only in the coexact transverse sector.

### 3. Homogeneity and isotropy

The standard homogeneous left-invariant gauge and the closed `S^3 ~= SU(2)`
geometry force admissible scalar-source residual states to be equivariant under
the relevant homogeneous symmetry.

By Schur's lemma, covariance blocks on irreducible coexact shell components are
scalar multiples of the identity. Thus the residual covariance cannot be an
arbitrary matrix on each shell; it reduces to shell weights.

### 4. Locality / geometric naturality

A local, homogeneous, geometric covariance must commute with the coexact
Laplacian and therefore is represented by functional calculus:

```text
G = F(Delta_coex)
```

on the coexact sector, at least modulo smoothing residuals allowed by
Hadamard-equivalence. This collapses the problem from arbitrary operators to a
function/sequence on the discrete shell spectrum.

### 5. Finite energy and Hadamard-type ultraviolet regularity

Standard QFT on curved spacetime does not allow arbitrary high-shell behavior.
Finite energy and Hadamard-type regularity constrain the ultraviolet asymptotic
form of the covariance.

On compact spatial sections, this means the residual shell weights cannot grow
arbitrarily and differences between physically equivalent Hadamard states are
smoothing. Thus high-shell freedom becomes rapidly decaying tail freedom.

### 6. Fixed scalar-amplitude quotient

Paper 31 fixes the rank-one lowest-shell bridge-readable quotient. Therefore
the residual sequence must satisfy the bridge-null condition

```text
B Delta G B^dagger = 0
```

for the scalar-amplitude observable.

The residual cannot change native `A_s`.

## Definition 27.G1: Geometrically Admissible Residual State

A residual covariance `Delta G` on the lifted scalar-bridge carrier is
geometrically admissible if it satisfies:

1. positivity: `Delta G >= 0`;
2. scalar-amplitude invisibility: `B Delta G B^dagger = 0`;
3. coexact support: `Delta G` acts on the gauge/null-reduced
   `Omega^1_coex(S^3)` carrier;
4. homogeneous symmetry: `Delta G` commutes with the homogeneous `SU(2)` action
   used in the standard left-invariant gauge;
5. geometric locality/naturality: `Delta G` is a function of the coexact Hodge
   Laplacian modulo smoothing terms;
6. finite-energy/Hadamard admissibility: its high-shell behavior is compatible
   with finite local energy and Hadamard ultraviolet regularity.

Chain:

```text
Definition 27.G1
<- Paper 27 Theorem 27.1 / Theorem 27.5 (Spatial CCR Lift)
<- Theorem 27.R5 (residual cone after fixed scalar-amplitude quotient)
<- Paper 22 v2.0 Theorem 22.2 (Hodge Spectrum)
<- Paper 22 v2.0 Theorem 22.4 (Channel Floor)
<- Paper 22 v2.0 Theorem 22.5 (Homogeneous Gauge Placement)
<- Hodge decomposition on S^3 with H^1(S^3)=0
<- standard QFT-on-curved-spacetime Hadamard/finite-energy admissibility
<- P1
<- P2
```

## Lemma 27.G2: Hodge-Topological Reduction

Any geometrically admissible residual 1-form covariance has no harmonic
component and no physical exact component. It is supported on
`Omega^1_coex(S^3)` after the scalar-bridge gauge/null quotient.

### Proof

On `S^3`, `H^1(S^3)=0`, so there is no harmonic 1-form sector. The Hodge
decomposition reduces 1-forms to exact plus coexact components. The exact
component is a gauge/null direction for the scalar-bridge CCR reduction and is
removed before the physical quasifree restriction. Therefore the physical
residual 1-form covariance is coexact.

Chain:

```text
Lemma 27.G2
<- Definition 27.G1
<- Hodge decomposition on S^3
<- H^1(S^3)=0
<- Paper 23 Lemma A / gauge-null quotient for bridge CCR restriction
<- Paper 27 Theorem 27.1 / Theorem 27.5
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.G3: Shell-Scalar Reduction by Homogeneity

On each irreducible coexact shell, a homogeneous `SU(2)`-equivariant residual
covariance is a scalar multiple of the identity.

### Proof

The coexact shell decomposition on the closed homogeneous `S^3 ~= SU(2)` bulk
decomposes the carrier into finite-dimensional irreducible representation
blocks under the relevant homogeneous action. A covariance commuting with that
action is an intertwiner on each irreducible block. By Schur's lemma, each such
intertwiner is scalar on the block.

Therefore the residual covariance is described shellwise by scalar weights,
not arbitrary matrices.

Chain:

```text
Lemma 27.G3
<- Definition 27.G1
<- coexact shell representation decomposition on S^3 ~= SU(2)
<- Schur's lemma
<- Paper 22 v2.0 Hodge/channel theorems
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.G4: Functional-Calculus Reduction

Modulo smoothing/Hadamard-equivalent residuals, a local homogeneous geometric
residual covariance on the coexact carrier is a function of the coexact Hodge
Laplacian:

```text
Delta G = F(Delta_coex).
```

### Proof

A local homogeneous geometric operator on a compact homogeneous Riemannian
manifold that commutes with the symmetry action and the Hodge decomposition is
diagonal in the Hodge spectral decomposition. Since the coexact Laplacian has
pure point spectrum with finite multiplicity, such an operator is represented
by functional calculus on `Delta_coex`, with one scalar value per shell.

Hadamard-equivalent smoothing differences may remain, but they are also
represented by rapidly decaying shell coefficients on the compact spectrum.

Chain:

```text
Lemma 27.G4
<- Definition 27.G1
<- Lemma 27.G2
<- Lemma 27.G3
<- spectral theorem for elliptic self-adjoint operators on compact manifolds
<- functional calculus for Delta_coex
<- standard Hadamard-equivalence/smoothing residual theorem for quasifree
   states on curved spacetime
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Lemma 27.G5: Regularity Reduces Freedom to a Smoothing Shell Tail

Finite-energy/Hadamard admissibility constrains the ultraviolet behavior of
the residual shell weights. Differences between admissible Hadamard quasifree
states are smoothing, hence their shell coefficients decay faster than any
fixed power relative to the principal ultraviolet singularity.

### Proof

Hadamard states share the same local ultraviolet singularity. On compact
spatial sections, the difference of two Hadamard two-point functions is smooth.
Expanding a smooth kernel in the eigenbasis of an elliptic operator gives
rapidly decaying spectral coefficients. Therefore once the principal UV
singularity is fixed, residual physically admissible freedom is a rapidly
decaying shell tail.

This still leaves infinitely many coefficients unless another theorem fixes
the tail.

Chain:

```text
Lemma 27.G5
<- Definition 27.G1
<- Lemma 27.G4
<- Hadamard local form and smooth-difference theorem for quasifree states
<- elliptic spectral decay of smooth kernels on compact manifolds
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem 27.G6: Closed-Geometry Residual Shell Classification

### Statement

Under P1/P2 and the current Paper 27/Paper 31 scalar-amplitude quotient
constraints, the residual full-carrier state freedom is not an arbitrary
positive covariance cone. It is reduced to a geometrically admissible coexact
shell-functional residual:

```text
Delta G = F_res(Delta_coex)
```

modulo smoothing/Hadamard-equivalent terms, with:

1. exact and harmonic components removed;
2. shell blocks scalar by homogeneity;
3. the scalar-amplitude rank-one quotient fixed;
4. high-shell behavior constrained by finite-energy/Hadamard regularity;
5. remaining freedom carried by a rapidly decaying residual shell sequence
   invisible to the native scalar-amplitude bridge.

### Proof

Lemma 27.G2 removes exact and harmonic sectors, leaving only the coexact
carrier. Lemma 27.G3 reduces homogeneous covariances to scalar shell weights.
Lemma 27.G4 identifies local homogeneous residual covariances with functional
calculus of the coexact Laplacian. Lemma 27.G5 constrains physically admissible
differences to smoothing shell tails. Theorem 27.R5 and Corollary 27.R6 impose
the fixed scalar-amplitude quotient and remove any ability to tune `A_s`.

Therefore the residual freedom is geometrically classified as a coexact
shell-functional smoothing tail, not an arbitrary covariance operator.

Chain:

```text
Theorem 27.G6
<- Definition 27.G1
<- Lemma 27.G2
<- Lemma 27.G3
<- Lemma 27.G4
<- Lemma 27.G5
<- Theorem 27.R5 (infinite residual freedom after fixed scalar-amplitude quotient)
<- Corollary 27.R6 (residual freedom is not an A_s parameter)
<- Paper 27 Theorem 27.1 / Theorem 27.5 (Spatial CCR Lift)
<- Paper 31 Bridge-Quotient Theorem and C2q rank-one quotient closure
<- Paper 22 v2.0 Hodge/channel theorems
<- standard Hodge theory, compact elliptic spectral theory, Schur's lemma,
   and Hadamard QFT on curved spacetime
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## Theorem 27.G7: Closed Geometry Does Not Make the Residual Finite

### Statement

The closed-geometry restrictions of Theorem 27.G6 do not reduce the residual
state freedom to a finite-dimensional space. An infinite-dimensional smoothing
shell-tail freedom remains unless a further full-state dynamics/KMS theorem or
joint-observable exhaustion theorem is supplied.

### Proof

After Theorem 27.G6, the residual freedom is represented by a rapidly decaying
shell sequence on the infinite coexact shell tower. The space of rapidly
decaying sequences is infinite-dimensional: for every finite shell index above
the fixed rank-one quotient, one may choose an independent small coefficient
with compact support in that shell, preserving rapid decay and scalar-amplitude
invisibility.

Thus compactness and regularity narrow the admissible class but do not make it
finite.

Chain:

```text
Theorem 27.G7
<- Theorem 27.G6
<- infinite coexact shell tower on S^3
<- existence of infinitely many compactly supported smooth spectral tails
<- P1
<- P2
```

Status: `DERIVED/THEOREM`.

## What Would Be Needed for Finite or Unique Selection

Closed geometry would become enough only if supplemented by one of the
following theorem-grade additions:

1. Full geometric KMS generator theorem:

   ```text
   H_full = c sqrt(Delta_coex)
   ```

   on the complete lifted carrier, plus proof that the physical state is the
   `beta_H`-KMS state for that generator.

2. Full Hartle-Hawking restriction theorem:

   ```text
   G^(1) = G_HHI^(1)|_{h_vec}
   ```

   with a proved invariant embedding of `h_vec` into the black-hole field
   algebra.

3. Joint observable exhaustion theorem:

   ```text
   intersection of kernels of all active IO observables = gauge/null sector.
   ```

   This would make every non-gauge residual direction load-bearing and
   constrain it.

4. Full quotient-collapse theorem:

   ```text
   h_vec / joint-null(active observables)
   ```

   is finite-dimensional.

None of these is currently established by P1 alone.

## Final Verdict

Yes, the closed Hilbert-space geometry gives additional theorem-grade
selection pressure. It reduces the residual state selection from an arbitrary
infinite covariance cone to a structured coexact shell-functional smoothing
tail.

No, it does not reduce the remaining freedom to finite freedom. The closed
`S^3` spectrum is discrete but infinite, and regularity still allows infinitely
many smooth shell-tail perturbations invisible to the current scalar-amplitude
readout.

The best current Paper 27 v2.0 upgrade is:

```text
Full state: OPEN/PREMISE_GAP.
Residual freedom: DERIVED/THEOREM infinite but geometrically classified.
Scalar-amplitude quotient: DERIVED/CONDITIONAL_VERIFIED and not tunable.
```
