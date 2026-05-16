# Paper 27 Memo: Spatial CCR Lift

Date: 2026-03-28

## Status

- `derived`: the archive already fixes the background carrier, the channel floors, the scalar bridge structure, the `N = n ± 1` shell rule, and the quasi-free restriction mechanism on a gauge-reduced bridge CCR algebra.
- `derived`: from those ingredients, the coexact-vector sector is the unique **minimal scalar-bridge / no-doubling perturbation sector**.
- `reconstruction`: the stronger sentence "the entire perturbation program lives only in this sector" is too strong, because the TT sector remains separately real in Paper 23.

## Honest Difficulty Assessment

This target is easier than `GMP`, `PSRP`, or the `A_s` seams, but it does **not** close in the naive wording.

What works:

- a theorem that the minimal one-particle sector underlying the Paper 23 scalar bridge and the No-Doubling Theorem is uniquely
  `h_vec = L²(R, dν) ⊗ H_g ⊗ Ω¹_coex(S³)`

What does not yet work:

- an unqualified theorem that *all* perturbative physics in the IO framework lives only in the coexact-vector sector.

So the route is viable if Paper 27 states the theorem with the right scope.

## Fixed Inputs From The Archive

The derivation uses only existing infrastructure:

1. `derived`: Shared Hilbert factor from Paper 17:
   `H_IO = Γ_s(L²(R, dν) ⊗ H_g)`

2. `derived`: spatialization from Paper 22:
   `H_IO^(spatial) = H_IO ⊗ H_spatial`

3. `derived`: Homogeneous Gauge Placement (Paper 22, Theorem 22.5):
   the background Ashtekar-Barbero connection `Ā = Γ + γK` lies in the lowest coexact 1-form channel on `S³`

4. `derived`: Channel Floor Theorem (Paper 22, Theorem 22.4):
   principal transverse branches have `J_min = s`, so
   scalar `J_min = 0`, vector `J_min = 1`, TT tensor `J_min = 2`

5. `derived`: Paper 23 scalar bridge structure:
   `B_N = Π_N^(0) ∘ S_Ā`,
   `S_Ā(δA) = g^{ab} κ_{ij} Ā_a^i δA_b^j`
   This is one-slot, linear in the active perturbation, and zero-order in `δA`

6. `derived`: Selection Rule (Paper 23, Theorem 23.2):
   vector shell `n` feeds scalar shells `N = n ± 1` only

7. `derived`: Scalar Bridge Uniqueness (Paper 23, Theorem 23.4):
   on the isotropic background, the zero-order `SU(2)`-equivariant scalar bridge is unique up to normalization

8. `derived`: Quasi-free restriction mechanism (Paper 23, Lemma A):
   the bridge CCR restriction is valid only after gauge/null directions are quotiented out so the restricted symplectic form is nondegenerate

## Theorem Candidate

### Theorem 27.SCCRL

Let `h = L²(R, dν) ⊗ H_g ⊗ K` be a one-particle perturbation space inside `H_IO^(spatial)` for the Paper 23 scalar bridge program. Assume:

1. `K` is a spatial carrier compatible with the homogeneous Ashtekar-Barbero background `Ā`
2. the scalar readout is implemented by a nonzero zero-order, one-slot, `SU(2)`-equivariant bridge of Paper 23 type
3. the bridge obeys the derived `N = n ± 1` shell rule
4. the induced bridge CCR algebra admits quasi-free restriction after quotient by gauge/null directions

Then the unique minimal choice of spatial carrier is

`K = Ω¹_coex(S³)`

and therefore the unique minimal one-particle sector is

`h_vec = L²(R, dν) ⊗ H_g ⊗ Ω¹_coex(S³)`

unique up to unitary equivalence and overall bridge normalization.

## Proof Skeleton

### Step 1: The thermal/gauge factors are already fixed

By Paper 17, the reduced observer one-particle factor is already fixed as

`L²(R, dν) ⊗ H_g`

So the only open slot in the Paper 23 lift is the spatial carrier `K`.

### Step 2: The bridge forces the active perturbation to be a 1-form carrier

The Paper 23 scalar bridge is

`S_Ā(δA) = g^{ab} κ_{ij} Ā_a^i δA_b^j`

This is a pointwise algebraic contraction between the background connection `Ā` and the active perturbation `δA`.

Consequences:

- scalar `0`-form carriers do not match the bridge tensor type
- TT rank-2 tensor carriers do not match the bridge tensor type
- any attempt to use scalars or tensors would require derivatives, codifferentials, or extra background slots

That would violate the already-derived Paper 23 facts:

- one-slot classification
- zero-order bridge structure
- scalar bridge uniqueness on the isotropic background

Therefore the active perturbation must live in a 1-form carrier.

### Step 3: On `S³`, gauge reduction kills the exact 1-form branch

For 1-forms on `S³`, Hodge decomposition gives

`Ω¹(S³) = dΩ⁰(S³) ⊕ Ω¹_coex(S³)`

because `H¹(S³) = 0`, so there is no harmonic 1-form sector.

Paper 23 Section 3.4 already fixes the physical meaning of the exact branch:

- the bridge is insensitive to pure-exact gauge artifact after coexact projection
- gauge/null directions must be quotiented out before the quasi-free restriction of Lemma A is valid

Therefore exact 1-forms cannot remain in the physical bridge one-particle space. They are null/gauge directions, not physical bridge degrees of freedom.

Once exact modes are removed and harmonic modes are absent, the only surviving 1-form carrier is

`Ω¹_coex(S³)`.

### Step 4: The background and shell rule single out the coexact principal vector branch

Paper 22, Theorem 22.5 puts the background `Ā` in the lowest coexact 1-form channel.

Paper 22, Theorem 22.4 says the principal vector branch is exactly the `J_min = 1` branch.

Paper 23, Theorem 23.2 then shows that this vector branch feeds scalar shells by the precise rule

`N = n ± 1`

and Paper 23, Theorem 23.4 shows the corresponding scalar bridge is unique up to normalization.

So the coexact vector branch is not merely allowed. It is the only gauge-reduced 1-form branch that:

- contains the background carrier
- supports the Paper 23 zero-order bridge
- realizes the derived shell rule
- preserves the quasi-free bridge restriction needed for No-Doubling

### Step 5: Exclusion of the competing sector types

#### Scalar sector

Fails because the Paper 23 bridge is a 1-form contraction. A scalar carrier would need a derivative or a different bridge architecture. That would not be the already-derived Paper 23 bridge.

#### Exact 1-form sector

Fails because it is gauge/null and must be quotiented out before the CCR restriction is nondegenerate.

#### TT tensor sector

Fails for the scalar bridge program because a one-slot zero-order scalar readout from one background vector plus one TT perturbation is not the Paper 23 bridge and would require a different intertwiner type. TT remains real as a separate perturbation sector, but not as the minimal scalar-bridge sector.

#### Mixed larger sectors

Any larger sector decomposes as

`Ω¹_coex(S³) ⊕ K_aux`

where `K_aux` is either

- gauge/null, hence quotiented out, or
- spectating with respect to the scalar bridge, hence not part of the **minimal** scalar-bridge perturbation sector

So larger sectors are not alternative minimal physical lifts. They are extensions with spectators or gauge baggage.

## What This Upgrades

If written carefully, this theorem promotes:

- the Paper 23 spatial CCR lift from `conditional` to `derived` for the scalar bridge / No-Doubling route
- the No-Doubling Theorem from `conditional/theorem` to `derived/theorem`

It does **not** by itself close:

- `PSRP`
- boundary covariance exponent
- the full `n_s` theorem

But it removes one of the three remaining premises behind `n_s`.

## Scope Boundary For Paper 27

Paper 27 should not say:

- "the coexact-vector sector is the entire perturbation sector of the framework"
- "TT perturbations are excluded"
- "every perturbative observable lives on `h_vec`"

Paper 27 can safely say:

- "the coexact-vector sector is the unique minimal one-particle CCR lift compatible with the scalar bridge, the `N = n ± 1` selection rule, and the No-Doubling mechanism"

That statement is both stronger than the old premise and faithful to the current archive.

## Prior Art

There is supporting structure in the literature, but not this exact IO theorem.

1. Closed-FRW perturbation theory already uses scalar/vector/tensor harmonic decomposition on compact spatial sections. Structural precedent:
   Kodama and Sasaki, *Cosmological Perturbation Theory* (1984), Oxford Academic:
   https://academic.oup.com/ptps/article/doi/10.1143/PTPS.78.1/1882757

2. AQFT / gauge quantization on curved spacetime repeatedly shows that topology and gauge quotient matter for the physical field algebra. Dappiaggi and Lang emphasize that the Maxwell field algebra can develop a nontrivial center unless restrictive topological assumptions are made:
   https://arxiv.org/abs/1104.1374

3. Benini’s thesis on Abelian gauge theories likewise shows that locality properties depend on global topology and on which observables survive the gauge/topology constraints:
   https://arxiv.org/abs/1503.00131

4. Murro and Schmid give a modern structural analogue: Hodge decomposition plus a radiation gauge suppresses unphysical Maxwell degrees of freedom, again showing that exact/gauge pieces are not part of the physical one-particle sector:
   https://arxiv.org/abs/2401.08403

5. Finster and Strohmaier provide another useful analogue: the Gupta-Bleuler framework keeps an indefinite ambient structure but extracts a positive physical subspace after gauge handling:
   https://arxiv.org/abs/1307.1632

These do not derive the IO result. But they support the reviewer-facing claim that:

- quotienting gauge/null directions before CCR quantization is standard
- topology of the spatial manifold matters
- a coexact/transverse physical carrier is structurally natural on compact spaces

## Recommended Paper 27 Next Move

Write this as a theorem with one explicit scope sentence:

> unique minimal scalar-bridge CCR lift

not

> unique perturbation sector of the whole framework

That wording should let the theorem close cleanly without colliding with the already-real TT branch.

