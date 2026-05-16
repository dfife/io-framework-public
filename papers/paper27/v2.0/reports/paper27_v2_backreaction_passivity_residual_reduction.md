# Paper 27 v2.0 Backreaction and Passivity Residual Reduction

Date: 2026-05-16

## Question

Can the residual state-selection freedom on the lifted scalar-bridge carrier

```text
h_vec = L^2(R,dnu) tensor H_g tensor Omega^1_coex(S^3)
```

be reduced further by combining:

- P1: the observable universe is inside a Schwarzschild black hole;
- P2: physics inside the horizon equals physics outside;
- standard exterior quantum field theory on curved spacetime;
- semiclassical backreaction constraints;
- thermodynamic passivity/KMS selection?

## Executive Verdict

Yes, but not all the way to a unique full state.

The additional layer is real:

1. **Positive residual additions are excluded** from the exact P1 background
   state if they carry positive exterior energy, flux, or stress-energy not
   already included in the banked Hawking background. They would change the
   Schwarzschild mass, introduce non-Hawking flux, or add anisotropic
   stress-energy.

2. **Background equilibrium replacement states reduce to KMS candidates** under
   standard complete-passivity results. If the residual sector is required to
   be a stationary thermodynamic equilibrium sector for the exterior
   Schwarzschild horizon flow, complete passivity forces a KMS state at the
   relevant inverse temperature. For a fixed positive one-particle generator,
   the quasifree KMS covariance is unique.

3. **The remaining hard wall is generator/embedding identification.** The stack
   still does not prove that the full lifted carrier `h_vec` inherits the full
   exterior Schwarzschild/Hartle-Hawking one-particle generator on every
   residual shell. Without that theorem, passivity reduces the class of
   admissible states but does not uniquely select the full covariance.

Thus the residual freedom is reduced from:

```text
geometrically admissible coexact shell-functional smoothing tails
```

to:

```text
exterior-realizable, zero-backreaction, horizon-regular equilibrium candidates,
with positive-energy residual additions killed.
```

The full state remains `OPEN/PREMISE_GAP`, but the open gap is now sharply
localized:

```text
prove the full h_vec dynamics/embedding as the exterior Schwarzschild
Hawking/Hartle-Hawking coexact generator, or prove joint-observable exhaustion.
```

## Layer 1: Exact-P1 Backreaction Admissibility

### Definition 27.B1: Exact-P1 Background-Admissible State

A quasifree state on the lifted carrier is exact-P1 background-admissible if
its exterior stress-energy contribution is compatible with the fixed
Schwarzschild/OS background used by the framework:

1. it is Hadamard/horizon-regular on the exterior side imported by P2;
2. it preserves the Schwarzschild mass parameter `M_U` rather than adding an
   independent energy bath;
3. it introduces no non-Hawking net flux through the horizon;
4. it introduces no anisotropic stress incompatible with the round
   Schwarzschild horizon and closed homogeneous OS interior;
5. it is not a new direct interior-only matter interaction absent from
   exterior physics under P2.

This is not a new premise. It is the compatibility condition obtained by
reading P1 as a fixed-background Schwarzschild/OS statement and P2 as an
exterior-physics admissibility rule.

Chain:

```text
Definition 27.B1
<- P1 (fixed Schwarzschild horizon and OS interior geometry)
<- P2 (interior physics must match exterior physics)
<- semiclassical Einstein equation compatibility
<- standard QFT-on-curved-spacetime stress-energy admissibility
<- standard horizon regularity / Hadamard requirement
```

Status: `DERIVED/CONDITIONAL_VERIFIED` as an admissibility definition tied to
P1+P2 and standard exterior physics.

## Layer 2: Positive Residual Additions Are Excluded

### Lemma 27.B2: Positive-Energy Residual Addition Exclusion

Let `Delta G >= 0` be a nonzero residual covariance increment supported on the
coexact shell tower and invisible to the scalar-amplitude quotient:

```text
B Delta G B^dagger = 0.
```

Assume the residual sector is exterior-realizable with a positive
one-particle energy generator `H_ext >= 0` whose shell frequencies are strictly
positive on every non-gauge coexact shell. If

```text
Tr(H_ext Delta G) > 0,
```

then `Delta G` is not exact-P1 background-admissible.

If the fixed-background constraint requires

```text
Tr(H_ext Delta G) = 0,
```

then positivity implies `Delta G` has support only in the zero-energy kernel of
`H_ext`. Since the physical coexact shells have strictly positive frequency,
the only admissible positive increment is gauge/null:

```text
Delta G = 0
```

on the physical residual coexact sector.

### Proof

For a quasifree bosonic sector with positive one-particle generator, a positive
covariance increment `Delta G >= 0` with support on strictly positive
frequency modes adds nonnegative energy. It adds strictly positive energy
unless the increment is supported entirely in the zero-energy kernel.

P1 fixes the Schwarzschild mass parameter and the OS support geometry. A
positive independent residual excitation changes the stress-energy budget,
mass parameter, or flux content unless it is already part of the banked Hawking
background. Therefore such an increment is not an admissible background-state
freedom. The coexact physical shells have no zero-frequency physical sector
after the Hodge/gauge quotient, so a positive zero-energy residual increment is
only gauge/null.

Chain:

```text
Lemma 27.B2
<- Definition 27.B1
<- positivity of the one-particle energy generator
<- positivity of quasifree bosonic energy expectation
<- Theorem 27.G6 (residuals are coexact shell-functional tails)
<- H^1(S^3)=0 and gauge-null removal from Lemma 27.G2
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` on exterior-realizable positive-energy
residual sectors.

### Consequence

The positive residual cone from Theorem 27.R5 is too broad for the exact-P1
background state. Positive residual additions are not hidden physical
background degrees of freedom unless they are stress-energy-null/gauge-null.

This is a strict improvement over Theorem 27.G6.

It does **not** yet prove uniqueness of arbitrary replacement states, because
two different positive covariances can differ by a signed smoothing operator
while preserving a global energy constraint.

## Layer 3: Non-Hawking Flux and Anisotropic Stress Exclusion

### Lemma 27.B3: Non-Hawking Flux Exclusion

An exterior-realizable residual state that produces a net horizon flux not
equal to the banked Hawking flux of the Schwarzschild background is not
exact-P1 background-admissible.

### Proof

P1 fixes the horizon geometry and mass parameter used by the framework. P2
allows exterior black-hole physics to determine the horizon flux structure.
Standard exterior quantum field theory assigns the Hawking flux/thermal
structure to the Schwarzschild horizon state. Adding an independent flux
changes the exterior stress-energy state and therefore the background
semiclassical geometry unless backreaction is included as a new dynamical
sector. Paper 27's lifted carrier is not that backreaction sector. Therefore
non-Hawking flux residuals are excluded from the background state.

Chain:

```text
Lemma 27.B3
<- Definition 27.B1
<- Hawking thermality for Schwarzschild horizons [Hawking 1975]
<- semiclassical stress-energy conservation on fixed Schwarzschild background
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` for exterior-realizable residual states.

### Lemma 27.B4: Horizon Symmetry Stress Exclusion

An exterior-realizable residual state that produces anisotropic horizon
stress-energy incompatible with the round Schwarzschild horizon is not
exact-P1 background-admissible.

### Proof

The P1 exterior horizon is round and Schwarzschild. A state whose renormalized
stress tensor has anisotropic angular components not already included in the
banked perturbation sector sources non-spherical backreaction. That is a
different spacetime, not the fixed P1 background used by Paper 27. Such a
state may be a perturbation of the background, but it is not an admissible
background equilibrium state for the scalar-amplitude source.

Chain:

```text
Lemma 27.B4
<- Definition 27.B1
<- spherical symmetry of Schwarzschild horizon geometry
<- semiclassical Einstein equation compatibility
<- standard QFT stress-energy transformation under rotations
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` for exterior-realizable residual states.

## Layer 4: Complete Passivity Reduces Replacement States to KMS Candidates

### Definition 27.B5: Background Equilibrium Residual State

A residual replacement state is a background equilibrium residual state if it
is:

1. exact-P1 background-admissible;
2. stationary under the exterior horizon time flow;
3. completely passive with respect to that flow, meaning no work can be
   extracted from any finite number of copies by cyclic operations.

Chain:

```text
Definition 27.B5
<- Definition 27.B1
<- P1 horizon Killing/modular flow where the exterior Schwarzschild horizon
   approximation is used
<- P2 exterior thermodynamic admissibility
<- Pusz-Woronowicz complete passivity theorem
```

Status: `DERIVED/CONDITIONAL_VERIFIED` as an equilibrium-class definition.

### Lemma 27.B6: Complete Passivity Implies KMS

On a C*-dynamical system with the exterior horizon time evolution, any faithful
normal completely passive equilibrium state is a KMS state for that evolution,
or a ground state in the zero-temperature case. For the Schwarzschild horizon
thermal sector, the relevant nonzero temperature is the Hawking temperature.

Therefore, a background equilibrium residual state is not an arbitrary
Hadamard state. It is a KMS candidate at the Hawking inverse temperature
provided the residual carrier is identified with the exterior horizon thermal
dynamics.

### Proof

This is the standard Pusz-Woronowicz theorem: complete passivity characterizes
KMS equilibrium states and ground states. The Schwarzschild horizon sector has
the Hawking temperature imported under P2 from exterior black-hole QFT, so the
thermal equilibrium branch is the `beta_H`-KMS branch.

Chain:

```text
Lemma 27.B6
<- Definition 27.B5
<- Pusz and Woronowicz (1978), passive states and KMS states for general
   quantum systems
<- Hawking temperature for Schwarzschild horizons [Hawking 1975]
<- P1
<- P2
```

Status: `DERIVED/THEOREM` as an external physics theorem applied to the
defined equilibrium class.

## Layer 5: Fixed-Generator KMS Uniqueness

### Lemma 27.B7: Fixed-Generator Quasifree KMS Uniqueness

For a bosonic CCR algebra over the reduced coexact carrier with a fixed
positive one-particle generator `H_ext`, the gauge-invariant quasifree
`beta_H`-KMS covariance is unique:

```text
G_beta = (exp(beta_H H_ext) - 1)^(-1)
```

on the positive-frequency one-particle sector.

### Proof

For a fixed positive one-particle Hamiltonian on a CCR algebra, the
gauge-invariant quasifree KMS state at inverse temperature `beta` has the
Bose-Einstein covariance `(exp(beta H)-1)^(-1)`. The CCR/KMS condition fixes
the two-point function mode by mode. Therefore no shell-weight freedom remains
once `H_ext` is fixed.

Chain:

```text
Lemma 27.B7
<- Lemma 27.B6
<- standard Araki-Woods quasifree CCR KMS uniqueness
<- fixed positive exterior one-particle generator H_ext
<- P2
```

Status: `DERIVED/THEOREM` conditional only on fixed-generator identification.

## Theorem 27.B8: Backreaction-Passivity Residual Reduction

Within the exterior-realizable background-state class, the residual freedom
left by Theorem 27.G6 reduces as follows:

1. positive-energy residual additions are excluded by fixed P1 backreaction
   compatibility;
2. non-Hawking flux residuals are excluded;
3. anisotropic-stress residuals incompatible with the round Schwarzschild
   horizon are excluded;
4. background equilibrium replacement states are reduced by complete passivity
   to Hawking-temperature KMS candidates;
5. for any sector whose full exterior one-particle generator is fixed, the
   quasifree KMS covariance is unique.

The only surviving non-unique freedom is therefore:

```text
stress-energy-null / gauge-null residuals,
or replacement-state freedom in sectors whose exterior one-particle generator
or Hartle-Hawking restriction embedding has not yet been proved.
```

### Proof

Theorem 27.G6 reduces the residual state problem to coexact shell-functional
smoothing tails. Lemma 27.B2 removes all positive residual additions that
carry positive exterior energy, because they would change the fixed P1
stress-energy budget. Lemma 27.B3 removes independent non-Hawking flux.
Lemma 27.B4 removes anisotropic horizon stress incompatible with the round
Schwarzschild geometry. Lemma 27.B6 reduces stationary thermodynamic
background replacement states to KMS candidates. Lemma 27.B7 then gives
uniqueness once the full one-particle generator is fixed.

Thus the remaining gap is not arbitrary state freedom. It is the specific
missing theorem that identifies the full lifted-carrier residual dynamics with
the exterior Schwarzschild/Hawking one-particle generator, or alternatively a
joint-observable exhaustion theorem that proves the residual sector is
physically null.

Chain:

```text
Theorem 27.B8
<- Theorem 27.G6
<- Theorem 27.G7
<- Definition 27.B1
<- Lemma 27.B2
<- Lemma 27.B3
<- Lemma 27.B4
<- Definition 27.B5
<- Lemma 27.B6
<- Lemma 27.B7
<- Hawking 1975 Schwarzschild horizon temperature
<- Pusz-Woronowicz 1978 complete passivity/KMS theorem
<- Araki-Woods quasifree CCR KMS uniqueness
<- semiclassical Einstein equation compatibility
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED` for the exterior-realizable exact-P1
background-equilibrium state class.

## Corollary 27.B9: Positive Residuals Are Not Hidden Scalar-Amplitude Fits

Positive shell-tail residual additions cannot be used as hidden fit
parameters for the scalar amplitude.

Reason:

1. if they are positive-energy physical additions, Lemma 27.B2 excludes them
   from the exact-P1 background state;
2. if they are bridge-null mathematical residuals, they satisfy
   `B Delta G B^dagger = 0` and cannot change native `A_s`;
3. if they are replacement equilibrium states with fixed exterior generator,
   Lemma 27.B7 fixes the covariance uniquely.

Chain:

```text
Corollary 27.B9
<- Theorem 27.B8
<- Corollary 27.R6
<- Paper 31 rank-one scalar-amplitude quotient closure
<- P1
<- P2
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Remaining Hard Wall

The route does not fully close the state on `h_vec`.

The missing theorem is now precise:

```text
Full Exterior-Generator Embedding Theorem:
The physical one-particle dynamics on the complete lifted carrier h_vec is the
restriction of the exterior Schwarzschild Hawking/Hartle-Hawking one-particle
generator to the coexact bridge carrier.
```

If this theorem is proved, Lemma 27.B7 collapses the background-equilibrium
residual state to the unique Hawking KMS covariance. Full C2c would then close
for the background equilibrium class.

Without it, one cannot honestly claim full state uniqueness.

## New Routes Found and Exhausted

### Route A: fixed mass kills positive additions

Successful but scoped. It kills `Delta G >= 0` physical additions with
positive energy. It does not kill arbitrary signed covariance replacements.

### Route B: no-flux and no-anisotropic-stress

Successful but scoped. It excludes states that would change the Schwarzschild
horizon flux or spherical symmetry. It does not identify the full generator.

### Route C: complete passivity

Successful as a reduction. It forces equilibrium states to be KMS candidates.
It does not select a unique covariance until the one-particle generator is
identified.

### Route D: fixed-generator KMS uniqueness

Successful conditional theorem. If the generator is fixed, the covariance is
unique. The unresolved part is proving that the generator on all of `h_vec` is
the exterior Hawking generator.

### Route E: P1 alone

No full closure. P1 supplies geometry, symmetry, topology, horizon scale, and
backreaction compatibility, but not the full residual one-particle generator.

## Final Claim Boundary

Best current Paper 27 wording:

```text
The full lifted-carrier state is not yet uniquely selected. However, after the
closed-geometry and backreaction/passivity reductions, the remaining freedom is
not an arbitrary fit. Positive-energy residual additions are excluded from the
exact P1 background; equilibrium replacements must be Hawking-KMS candidates
once the exterior generator is fixed; and all bridge-null residuals are
invisible to native A_s. The only remaining open theorem is the full
exterior-generator embedding or an equivalent joint-observable exhaustion
theorem.
```

Status summary:

- scalar-amplitude quotient: `DERIVED/CONDITIONAL_VERIFIED`;
- closed-geometry residual classification: `DERIVED/THEOREM`;
- positive residual addition exclusion: `DERIVED/CONDITIONAL_VERIFIED`;
- complete-passivity reduction: `DERIVED/THEOREM` on the equilibrium class;
- fixed-generator KMS uniqueness: `DERIVED/THEOREM`;
- full `h_vec` state selection: `OPEN/PREMISE_GAP`.

