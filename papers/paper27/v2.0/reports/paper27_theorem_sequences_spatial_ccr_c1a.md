# Paper 27 Theorem Sequences: Spatial CCR Lift and C1a

Date: 2026-03-28

Status labels:

- `derived`
- `conditional`
- `open`

## 1. Spatial CCR Lift

## Goal

Upgrade the Paper 23 spatial CCR lift from a premise to a theorem, with the exact scope:

- `derived`: unique minimal carrier for the **scalar-bridge perturbation sector**
- not claimed: uniqueness of the entire perturbation program
- not claimed: absence of the separate TT sector of Paper 23

## Lemma 27.1: Background Coexact Placement

### Statement

In the standard homogeneous left-invariant gauge on the round `S^3` spatial sections of the OS interior, the homogeneous Ashtekar-Barbero background

`Ā = Γ + γK`

lies in the lowest coexact `1`-form channel and has no exact or harmonic Hodge component.

### Source

- Paper 22, Theorem 22.5 (Homogeneous Gauge Placement Theorem)

### Status

- `derived`

### Proof

Paper 22 proves that the left-invariant coframe `e^i` on round `S^3` is coclosed and satisfies

`Δ_1 e^i = (4/a^2)e^i`,

so it spans the lowest coexact `1`-form eigenspace. Since both `Γ^i` and `K^i` are homogeneous linear combinations of this coframe in the standard homogeneous gauge, `Ā = Γ + γK` lies in that same lowest coexact `1`-form channel. Exact additions arise only under gauge transformation and are gauge artifacts in this gauge-fixed homogeneous setting.

## Lemma 27.2: Hodge and Channel Decomposition of `1`-Forms on `S^3`

### Statement

On round `S^3`,

`Ω^1(S^3) = dΩ^0(S^3) ⊕ Ω^1_coex(S^3)`,

with no harmonic `1`-form branch. The exact and coexact branches are disjoint spectral series. The principal transverse spin-`1` branch is the coexact branch and has diagonal `SU(2)` floor `J_min = 1`; exact `1`-forms are derivative descendants of the scalar branch and inherit scalar floor `J_min = 0`.

### Sources

- Paper 22, Theorem 22.2 (Hodge Spectrum Theorem)
- Paper 22, Theorem 22.4 (Channel Floor Theorem)
- Paper 22 precision caveat following Theorem 22.4

### Status

- `derived`

### Proof

Paper 22 gives the de Rham data on `S^3`, including `H^1(S^3) = 0`, so there is no harmonic `1`-form branch. The Hodge Spectrum Theorem gives disjoint exact and coexact `1`-form spectral series, so the two branches are cleanly separated. The Channel Floor Theorem identifies the principal transverse spin-`1` branch with `J_min = 1`, while the precision caveat explicitly states that exact `1`-forms are derivative descendants of the scalar branch and therefore carry scalar floor `J_min = 0`, not vector floor `1`.

## Lemma 27.3: Scalar Bridge Structure on `1`-Form Input

### Statement

The Paper 23 scalar bridge is a zero-order, linear, `SU(2)`-equivariant scalar map on `1`-form input,

`B_N = Π_N^(0) ∘ S_Ā`,
`S_Ā(δA) = g^{ab} κ_{ij} Ā_a^i δA_b^j`,

unique up to normalization on the isotropic background, with shell rule

`N = n ± 1`.

It introduces no derivative scalarization of the active perturbation.

### Sources

- Paper 23, Theorem 23.2 (Selection Rule)
- Paper 23, Section 3.3 (One-Slot Classification)
- Paper 23, Section 3.4 (Coexact Consistency and Gauge Properties)
- Paper 23, Theorem 23.4 (Scalar Bridge Uniqueness)

### Status

- `derived`

### Proof

Paper 23 proves:

- the bridge amplitude is linear in the active perturbation and one-slot / degree-1
- the active perturbation enters with no derivatives
- the scalar bridge is unique up to normalization on the isotropic background
- vector shell `n` feeds scalar shells `N = n ± 1` only

Thus the scalar-bridge program requires a `1`-form carrier compatible with a zero-order linear scalar readout.

## Lemma 27.4: Gauge/Null Reduction in the Scalar-Bridge CCR Sector

### Statement

In the nonabelian linearized theory around nonzero background `Ā`, gauge directions are

`δ_ε A = D_Ā ε = dε + [Ā, ε]`,

not merely exact `1`-forms. However, in the specific Paper 23 scalar-bridge construction, after fixing the standard homogeneous left-invariant gauge and passing to the coexact-projected bridge carrier, the pure-exact gauge artifact is removed from the bridge sector. After quotienting gauge/null directions in the bridge CCR reduction, and since no harmonic `1`-form branch exists on `S^3`, the surviving minimal `1`-form carrier in the scalar-bridge sector is the coexact branch.

### Sources

- Paper 23, Section 3.4 (Coexact Consistency and Gauge Properties)
- Paper 23, Lemma A inside Theorem 23.3 (quasi-free restriction requires gauge/null quotient)
- Paper 22, Theorem 22.2 (`H^1(S^3)=0`, no harmonic `1`-forms)

### Status

- `derived` for the scalar-bridge sector

### Proof

Paper 23 is explicit that the correct nonabelian gauge variation is `D_Ā ε`, not `dε`. It is equally explicit that, in the standard homogeneous gauge actually used in the scalar-bridge program, the construction is performed on the coexact-projected perturbation carrier and is insensitive to the pure-exact gauge artifact. Lemma A then requires quotienting gauge/null directions before the CCR restriction is nondegenerate. Since `S^3` has no harmonic `1`-forms, the only surviving minimal `1`-form branch in this gauge-fixed bridge sector is `Ω^1_coex(S^3)`.

## Theorem 27.5: Spatial CCR Lift Theorem

### Statement

The unique minimal one-particle carrier for the Paper 23 **scalar-bridge perturbation sector** is

`h_vec = L²(R, dν) ⊗ H_g ⊗ Ω^1_coex(S^3)`.

Equivalently: among `1`-form perturbation carriers on `H_IO^(spatial)`, the coexact branch is the unique minimal carrier compatible with

1. the homogeneous coexact background placement of Theorem 22.5,
2. the `S^3` Hodge/channel decomposition of Theorems 22.2 and 22.4,
3. the zero-order one-slot scalar bridge structure and `N = n ± 1` shell rule of Paper 23,
4. the gauge/null quotient required for the bridge CCR reduction.

### Sources

- Paper 17, shared one-particle factor `L²(R,dν) ⊗ H_g`
- Paper 22, Theorems 22.2, 22.4, 22.5
- Paper 23, Theorems 23.2, 23.4, 23.3 / Lemma A, Section 3.4

### Status

- `derived`

### Proof

Paper 17 fixes the nonspatial one-particle factor `L²(R,dν) ⊗ H_g`, so only the spatial carrier remains to be selected. Lemma 27.1 places the background in the lowest coexact `1`-form channel. Lemma 27.2 shows that the admissible `1`-form branches on `S^3` split into exact and coexact, with no harmonic branch, and that the principal transverse vector branch is the coexact branch. Lemma 27.3 shows that the scalar-bridge program requires a zero-order linear scalar map on `1`-form input with the precise shell rule `N = n ± 1`. Lemma 27.4 then removes the pure-exact gauge artifact from the gauge-fixed bridge sector and quotients gauge/null directions before CCR reduction. With the harmonic branch absent, the minimal surviving `1`-form carrier is `Ω^1_coex(S^3)`. Tensoring with the already-fixed Paper 17 factor gives the stated one-particle space.

### Scope

This theorem concerns only the **scalar-bridge carrier**. It does not assert that the full perturbation theory has no TT sector. Paper 23 explicitly constructs a separate TT bridge and TT perturbation sector.

## Corollary 27.6: No-Doubling Upgrade

### Statement

With Theorem 27.5 in place, the Paper 23 No-Doubling theorem

`C^(0) = B G^(1) B†`

is upgraded from conditional to derived within the scalar-bridge CCR sector.

### Source

- Paper 23, Theorem 23.3 and Lemma A

### Status

- `derived`

### Proof

The only Paper 23 premise removed here is the spatial CCR lift. Once Theorem 27.5 fixes the one-particle carrier, Lemma A is a standard quasi-free restriction statement on the gauge/null-reduced bridge CCR algebra and the No-Doubling conclusion follows exactly as in Paper 23.

## Downstream Upgrade Boundary

The following are upgraded:

- the Paper 23 spatial CCR lift
- the Paper 23 No-Doubling theorem

The following remain open:

- `PSRP`
- boundary covariance exponent
- the full theorem-grade `n_s` derivation

## 2. C1a: Vanishing Mixed Covariance

## Goal

Formalize the narrow part of Paper 26 premise `C1` that can plausibly be closed:

- `C1a`: `⟨δΓ · δK⟩ = 0`

without claiming closure of

- `C1b`: variance ratio `γ²/(1+γ²)`

## Lemma 27.7: Reduced `1⊕3` Carrier

### Statement

On the reduced Paper 15 carrier

`H_q = R·1 ⊕ Im(H)`,

the real slot `R·1` is the trivial `SU(2)` representation and the imaginary slot `Im(H)` is the adjoint `SU(2)` representation. The unique positive normalized multiplicative `SU(2)`-invariant quadratic observable on this carrier is

`Q(a+v) = a² + |v|²`.

### Source

- Paper 15, Quaternionic Norm Theorem

### Status

- `derived`

### Proof

This is exactly the Paper 15 reduced quaternionic carrier and norm theorem.

## Lemma 27.8: Reduced-Carrier Schur Orthogonality

### Statement

Let `G` be any centered `SU(2)`-equivariant quasi-free one-particle covariance on the reduced carrier

`H_q = R·1 ⊕ Im(H)`.

Then `G` is block diagonal with respect to the `1⊕3` splitting:

`G = a P_1 + b P_3`

for some `a,b >= 0`, and in particular the mixed blocks vanish:

`P_1 G P_3 = 0 = P_3 G P_1`.

### Sources

- Paper 15, reduced `1⊕3` carrier
- Paper 17, reduced gauge-sector / gauge-averaging framework
- standard Schur lemma on inequivalent irreducible `SU(2)` sectors

### Status

- `derived` on the reduced carrier

### Proof

`R·1` and `Im(H)` are inequivalent irreducible `SU(2)` representations. Any `SU(2)`-equivariant operator on their direct sum has no cross intertwiners because

`Hom_SU(2)(1,3) = 0 = Hom_SU(2)(3,1)`.

Hence the covariance operator is block diagonal.

## Theorem 27.9: Reduced-Carrier Mixed-Covariance Vanishing

### Statement

On the reduced `1⊕3` carrier, any centered `SU(2)`-equivariant quasi-free fluctuation state has

`⟨δΓ · δK⟩ = 0`.

### Sources

- Lemmas 27.7 and 27.8

### Status

- `derived` on the reduced carrier

### Proof

The mixed expectation is exactly the cross block of the covariance between the trivial and adjoint sectors. Lemma 27.8 kills this block.

## Corollary 27.10: Paper 26 C1 Narrows to C1b

### Statement

If the Paper 26 scalar fluctuation covariance descends to the reduced `1⊕3` carrier as an `SU(2)`-equivariant quasi-free covariance, then the mixed term required by `C1` vanishes:

`⟨δΓ · δK⟩ = 0`.

The surviving open part of `C1` is then only the variance-ratio statement

`⟨|δK|²⟩ / ⟨|δA|²⟩ = γ²/(1+γ²)`.

### Sources

- Paper 26, Section 2.6 (`C1`)
- Theorem 27.9

### Status

- mixed-term application: `conditional`
- narrowing of the open seam: `derived`

### Proof

Paper 26 states `C1` requires two ingredients: vanishing mixed covariance and the Rosetta variance ratio. Theorem 27.9 closes the first on the reduced carrier. Nothing in Papers 15, 17, 18, 25, or 26 fixes the block weights `a:b`, so the ratio statement remains open.

## Corollary 27.11: C1b Remains Open

### Statement

The current theorem stack does not derive

`⟨|δK|²⟩ / ⟨|δA|²⟩ = γ²/(1+γ²)`.

### Sources

- Paper 15, background norm theorem
- Paper 17 / 18, reduced central modular package
- Paper 26, Section 2.6

### Status

- `open`

### Proof

On the reduced `1⊕3` carrier, `SU(2)` symmetry alone only yields the general block-diagonal form

`G = a P_1 + b P_3`.

Paper 15 fixes a multiplicative background norm on a single quaternionic element `q_γ`; it does not identify the thermal fluctuation covariance with that same block ratio. Papers 17 and 18 reduce the gauge sector to the one-dimensional center generated by `K̂_g = K_gauge I`, which is too coarse to force a nontrivial `γ`-dependent `1↔3` variance split. Therefore the ratio remains underdetermined.

## 3. Natural Downstream Closures

What closes naturally in this pass:

- Spatial CCR lift
- No-Doubling
- the `C1a/C1b` split, with `C1a` formalized on the reduced carrier

What does **not** close automatically:

- `C1b`
- `C2c`
- `PSRP`
- boundary covariance exponent
- full `A_s`

## 4. Paper 27 Safe Summary

Paper 27 can now safely claim:

- `derived`: the unique minimal carrier for the Paper 23 scalar-bridge perturbation sector is
  `L²(R,dν) ⊗ H_g ⊗ Ω^1_coex(S^3)`
- `derived`: the Paper 23 No-Doubling theorem is upgraded with that carrier theorem
- `derived` on the reduced `1⊕3` carrier: `SU(2)` Schur orthogonality kills the `δΓ–δK` mixed covariance block
- `open`: the Rosetta variance ratio for fluctuations is still not proved

