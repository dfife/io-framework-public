# Paper 31: Complete IO Transfer Map

Date: 2026-04-03

## Scope

This document assembles the full CMB/Boltzmann transfer chain for the active IO
framework and marks, at each stage:

- what standard CLASS/CAMB computes,
- what IO modifies and why,
- which baryon slot enters,
- which background/projection branch applies,
- which internal authority supports the assignment,
- whether the assignment is `derived`, `conditional`, or `open`,
- and what the killed Paper 31 routes imply about the remaining structure.

Claim discipline:

- `derived`: theorem-grade from the current stack plus the lab premises
- `verified`: numerically reproduced and checked
- `conditional`: valid if the stated class-membership / branch claim holds
- `open`: not yet theorem-closed

## Fixed reference package

Active late-time background package:

- `H0 = 68.91`
- `Omega_m = 0.335776379575470`
- `Omega_k = -0.005613722564239`
- `Omega_Lambda = 0.669837342989`
- `N_eff = 3.044`

Carried baryon slots:

- `omega_b,geom = 0.02108`
- `omega_b,eff = 0.02910`
- `omega_b,clustering = 0.017053042566349`

Closed Weyl-response data:

- `alpha_delta = 3/2`
- `alpha_Phi = 2`
- `Sigma_IO / mu_IO = x^(-1/2)`
- exact curved kernel
  \[
  M_{\rm IO}(k)=x^{-1/2}\left(\frac{k^2-3K}{k_p^2-3K}\right)^{-1/4}.
  \]

## Executive map

| Stage | Standard CLASS/CAMB object | IO modification | Main slot/branch status |
| --- | --- | --- | --- |
| 1. Background | FRW `H(z)`, `rho_i(z)`, distances, conformal time | projected Schur branch; `sqrt(Delta)` in homogeneous energy readout, `P_k` in curvature slot | background law `derived`, live Schur package `verified` |
| 2. Thermodynamics | `x_e(z)`, `T_b(z)`, `dkappa/dtau`, `g(tau)` | chemistry/opacity strongly point to `omega_b,geom`; reduced visibility/readout inherits acoustic class | split is not fully closed |
| 3. Tight coupling | `delta_g`, `theta_g`, `delta_b`, `theta_b`, `R`, `tau_c` | only Thomson/diffusion leg survives in minimal ODE basis | exact CMB-era slot map still `open` |
| 4. Free streaming | photon multipole hierarchy and metric forcing | no theorem-grade new hierarchy term yet; scalar Weyl family is `alpha_Phi=2` | primary hierarchy still `open` |
| 5. Source assembly | `S_T`, `S_E`, `S_B` from local and integrated blocks | all tested source/readout dressings are dead | missing object is not a source-packet factor |
| 6. LOS integration | closed-FRW radial/hyperspherical transfer to `C_l` | standard closed `K=+1` geometry survives; exact Weyl kernel enters only on lensing side | primary LOS geometry `derived`, full CMB class still `open` |
| 7. Lensing | `phi`, `kappa`, `gamma`, lensed `C_l` | scalar lensing package on `alpha=2`; exact curved Weyl kernel is implemented | `derived / scoped` |
| 8. Observable extraction | likelihood inference for `A_s`, `tau`, baryon slots | GR Planck extraction is biased by Weyl slip; no stable final replacement pair yet | bias direction `derived / conditional`, final pair `open` |

## Stage 1 — Background

### Standard

CLASS/CAMB compute the homogeneous FRW background:

- `H(z)`
- `rho_i(z)`
- conformal time `tau`
- comoving distances and curvature functions

### IO modification

`derived`:
the observer-facing homogeneous readout is
\[
H_{\rm obs}^2=\sqrt{\Delta}\,C_{\rm bare}.
\]

`derived`:
the retained Schur curvature factor enters only in the curvature slot, not in
the homogeneous `sqrt(Delta)` projector:
\[
P_k=\exp(-\Delta/2).
\]

So the active observer branch is the projected Schur branch: matter, radiation,
and vacuum inherit the `sqrt(Delta)` readout, while curvature is suppressed by
the Schur factor.

### Baryon slot

No special CMB baryon slot enters here beyond the ordinary matter inventories.

### Projection

- late-time observer-facing background: projected Schur
- bare OS package remains upstream only

### Authority

- Paper 20 bare/background closure architecture
- Paper 29 assembly-gap / Schur-branch closure
- Paper 31 Schur `N_eff` necessity audit

### Status

- background readout law: `derived`
- active Schur package: `verified`

### What the killed routes imply

The current CMB debt is not in the homogeneous background projector itself.
Paper 31 already showed that even with the exact Weyl kernel in place, the
remaining failure is a transfer-hierarchy issue, not a background readout issue.

Later sharpening:

- [paper31_reionization_openness_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_openness_theorem.md)
- [paper31_late_visibility_identification_theorem.md](/opt/cosmology-lab/results/paper31/paper31_late_visibility_identification_theorem.md)
- [paper31_reionization_functional_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_functional_nogo_theorem.md)
- [paper31_visibility_moment_separation_theorem.md](/opt/cosmology-lab/results/paper31/paper31_visibility_moment_separation_theorem.md)

This narrows the late-time part further: the framework still does not derive
the late reionization history `x_e(z)`, so neither the full low-`ell` EE
rescattering map nor the high-`ell` late-attenuation map are theorem-closed
from `x, gamma, K_gauge, Delta` alone. The second note also fixes the object
class: high-`ell` attenuation is not an independent scalar GTTP/readout target,
but another functional of the same late visibility history. The third note
sharpens the remaining no-go: the missing object is function-valued `x_e(z)`,
not one more scalar constant. The fourth note sharpens this further: one
optical-depth scalar moment cannot in general close both high-`ell` screening
and low-`ell` EE, because the latter depends on additional weighted visibility
moments.

Later Paper 31 closure now classifies the remaining object more sharply:

- [paper31_reionization_inheritance_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_inheritance_theorem.md)

This note proves that late reionization belongs to the inherited local
astrophysical-emissivity sector under Premise 2. Its local hydrogen inventory
is geometric, its evolution belongs to the OS-proper-time / local-source side,
and the scalar CMB sees it only through the projected late visibility kernel.

The correct import pipeline for any exterior reionization model is now also
closed:

- [paper31_external_reionization_import_theorem.md](/opt/cosmology-lab/results/paper31/paper31_external_reionization_import_theorem.md)
- [paper31_reionization_clock_transport_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_clock_transport_theorem.md)

That note proves the admissible IO import map is:

1. evolve local ionization on the OS-proper-time / geometric-hydrogen branch,
2. build the projected late visibility kernel,
3. only then compare to high-`ell` screening and low-`ell` EE.

The second note sharpens the no-go: even an exterior *history*
`x_e^{ext}(z)` cannot be copied directly as a function of observed redshift.
It must be transported through the local OS proper-time map first.

The resulting admissibility boundary is now also explicit:

- [paper31_cmb_reionization_admissibility_theorem.md](/opt/cosmology-lab/results/paper31/paper31_cmb_reionization_admissibility_theorem.md)

This note proves that, without an imported or derived `x_e(z)`, low-`ell` EE
and the high-`ell` screened amplitude direction are not pure zero-parameter
framework tests of the native constants alone.

One more late-sector closure now sharpens the import pipeline dynamically:

- [paper31_reionization_dynamical_transport_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_dynamical_transport_theorem.md)

This note proves that the imported local ionization ODE acquires an exact
observed-redshift transport factor
\[
R_{\rm reio}(z)=|d\tau_{\rm OS}/dz|\,/\,|dt_{\rm proj}/dz|>1
\]
on the active Schur branch. So reionization is dynamically easier per unit
observed redshift than in a naive projected-clock transplant.

One final late-sector boundary is now explicit:

- [paper31_reionization_emissivity_degeneracy_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_emissivity_degeneracy_theorem.md)
- [paper31_reionization_source_viability_inheritance_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_source_viability_inheritance_theorem.md)

This note proves that, even after correct IO import, scalar late-time CMB
observables determine at most an equivalence class of local source laws that
yield the same imported visibility history. They do not uniquely identify the
underlying emissivity / escape-fraction / clumping decomposition.

The second note proves the complementary positive result: the correct IO
transport map does not create a new reionization source deficit. At fixed
target `Q(z)`, it reduces the required net local proper-time drive by the exact
factor `1/R_reio(z)`.

The data-class frontier is now also explicit:

- [paper31_reionization_data_class_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_data_class_theorem.md)
- [paper31_cmb_lya_21cm_complement_theorem.md](/opt/cosmology-lab/results/paper31/paper31_cmb_lya_21cm_complement_theorem.md)
- [paper31_reduced_source_state_identifiability_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reduced_source_state_identifiability_theorem.md)

This note proves scalar late-time CMB alone cannot close the source law. A
second non-CMB local-emissivity-sensitive class is mathematically necessary.

The second note identifies the first theorem-grade complementary triad:
scalar late-time CMB + Ly-`alpha` UVB + 21-cm.

The third note proves that, on the natural reduced local source state, this
three-probe map is locally invertible.

The remaining wall is now explicit:

- [paper31_reduced_to_physical_source_underdetermination_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reduced_to_physical_source_underdetermination_theorem.md)

This note proves that reduced-state closure does not yet determine the unique
full physical emissivity/heating decomposition.

## Stage 2 — Thermodynamics / Recombination

### Standard

CLASS/CAMB compute:

- recombination chemistry `x_e(z)`
- baryon temperature `T_b(z)`
- differential Thomson opacity
  \[
  \kappa' = a n_e \sigma_T
  \]
- visibility
  \[
  g(\tau)=\kappa' e^{-\kappa}
  \]

### IO modification

`derived`:
standard recombination chemistry depends on the hydrogen inventory `n_H`, so
the local microphysical chemistry input is

- `omega_b,geom` for `n_H`
- therefore also `omega_b,geom` for local opacity `n_e = x_e n_H`

`derived / scoped`:
inside the reduced observer-side scalar CMB readout sector, the visibility
chain

- `kappa'`
- `kappa`
- `exp(-kappa)`
- `g`

is a gauge-neutral Thomson-gated optical/history readout and inherits the
acoustic slot:

- `omega_b,vis = omega_b,eff`

This is the AV1 theorem. It is a readout theorem, not a full chemistry theorem.

### Baryon slot

- chemistry / local `n_H`, `n_e`: strongest current internal route is `omega_b,geom`
- reduced visibility/readout operator: `omega_b,eff`

### Projection

- local recombination microphysics: bulk/local branch
- observer-side visibility readout: reduced optical scalar-acoustic class

### Authority

- Paper 21 `T_IO` branch assignment theorem
- Paper 26 IO-native recombination audit
- Paper 26 Thomson-kernel identity
- Paper 27 AV1 Thomson visibility class theorem

### Status

- chemistry `-> omega_b,geom`: `conditional`
- opacity as local electron inventory `-> omega_b,geom`: `conditional`
- reduced visibility/readout `-> omega_b,eff`: `derived / scoped`
- full recombination class closure: `open`
- bare `H_local` and bare `T_IO` Stage-2 candidates: `derived / scoped no-go`
- late reionization history `x_e(z)`: `derived / conditional inherited external sector`

### What the killed routes imply

`verified`:
the full typed recombination route

- chemistry on `omega_b,geom`
- opacity on `omega_b,geom`
- acoustic loading on `omega_b,eff`

was implemented and reproduced, but TT became catastrophic. Therefore the
missing IO transfer function is not just "typed chemistry + typed opacity" on
top of the current source grammar.

`derived / conditional`:
late reionization is also not another missing scalar boundary theorem here. It
is an inherited astrophysical-emissivity history on the local geometric /
proper-time branch. What remains open is an *internal* emissivity theorem, not
the class assignment itself.

Later Paper 31 sharpening now kills the first two obvious local Stage-2
candidates:

- [paper31_stage2_local_transport_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_local_transport_nogo_theorem.md)

This note proves that neither bare OS-clock local-H transport nor bare
`T_IO` recombination cooling can be the missing Stage-2 operator. In both
RecFast and HyRec they move the local hydrogen system toward earlier
recombination and lower `x_e(z)` at fixed observed redshift. So the surviving
Stage-2 renormalization must be a local atomic-radiative counterterm:

- enhanced upward photoionization / excitation,
- reduced effective escape,
- increased line trapping,
- or an equivalent local counterionizing operator.

The surviving support is now theorem-sharpened further:

- [paper31_stage2_atomic_radiative_support_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_atomic_radiative_support_theorem.md)

That note proves that, inside the accepted RecFast/HyRec recombination class,
the remaining exact Stage-2 operator can only live on the local
atomic-radiative coefficient sector itself: upward/downward rates,
detailed-balance factors, and escape/trapping operators.

The next Paper 31 sharpening now kills the first structured global candidate:

- [paper31_stage2_minimal_atomic_pair_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_minimal_atomic_pair_nogo_theorem.md)

That note proves that even the minimal transported atomic pair

\[
(\beta_B,R_{\rm up})\mapsto f_\Gamma^{-1}(\beta_B,R_{\rm up}),
\qquad
R_{\rm Ly\alpha}\mapsto f_\Gamma R_{\rm Ly\alpha}
\]

is not the exact solver. So the remaining exact support is now narrower still:
it must act non-uniformly on the multilevel radiative-transfer network itself.

The latest Paper 31 sharpening then closes the current local-callback class:

- [paper31_stage2_nonmarkovian_radiative_transfer_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_nonmarkovian_radiative_transfer_nogo_theorem.md)

That note proves that the exact HyRec FULL branch depends on explicit
radiation-history state (`Dfminus_hist`, `Dfminus_Ly_hist`, `Dfnu_hist`, `iz`)
and therefore cannot be hosted faithfully by the present pointwise
thermodynamics wrapper `dx_H/dz = F(z,x_e,T_m,...)`. So the surviving exact
Stage-2 object is now sharper than “a non-uniform local coefficient law.” It
is an extended history-state thermodynamics/radiative-transfer integrator.

The irreducible exact support of that augmentation is now also identified:

- [paper31_stage2_radiation_history_support_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_radiation_history_support_theorem.md)
- [paper31_stage2_characteristic_distortion_transport_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_characteristic_distortion_transport_theorem.md)
- [paper31_stage2_finite_moment_closure_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_finite_moment_closure_nogo_theorem.md)

That note proves the exact extra support is the incoming photon-distortion
history sector feeding the Ly-`alpha` / two-photon network, or an isomorphic
reduced variable sufficient to reconstruct it. The newer notes sharpen this:
the natural exact object is a function-valued distortion field on the conserved
comoving-frequency characteristic `q=aE`, and no fixed finite-dimensional
moment vector can replace it exactly.

The remaining field-law seam is now also closed:

- [paper31_stage2_characteristic_field_inheritance_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_characteristic_field_inheritance_theorem.md)

That note proves that, under Premise 2 and within the accepted exterior FULL
hydrogen radiative-transfer class, the exact Stage-2 characteristic-field
evolution law is inherited without an extra IO field-level renormalization.
So the open Stage-2 debt is no longer a hidden complement on the distortion
field itself. It is the local IO background-state map feeding that law, plus
the implementation of the extended-state solver.

That local background map is now partially closed too:

- [paper31_stage2_local_background_state_map_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_local_background_state_map_theorem.md)

This note proves:

- `H_loc(z)` is fixed exactly by the OS scale-factor theorem,
- `n_H(z)` remains the geometric local inventory,
- `T_R(z)` is class-closed as a local bulk radiation variable on the `T_IO`
  branch,
- and `T_m(z)` is a dynamical component of the extended FULL state, not a
  separate prescribed branch scalar.

So the remaining exact Stage-2 solver debt is now the implementation of the
inherited FULL extended-state law on that IO local background map.

That implementation seam is now closed negatively:

- [paper31_stage2_exact_full_local_map_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_exact_full_local_map_nogo_theorem.md)

Using a standalone exact FULL-HyRec benchmark with explicit `hubble_array`
validation, Paper 31 now proves:

- the external-H FULL path is numerically sound after a minimal
  endpoint-spacing repair,
- the exact IO local map `(H_loc, T_IO, n_H,geom)` still shifts Stage 2 toward
  lower `x_e(1100)` and a narrower visibility window,
- so the remaining exact Stage-2 debt is no longer implementation of the
  inherited FULL law alone.

The remaining exact Stage-2 object is now the local atomic-radiative
renormalization law inside the inherited FULL solver.

Paper 31 now sharpens that support further:

- [paper31_stage2_degree_split_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_degree_split_nogo_theorem.md)
- [paper31_stage2_q_resolved_support_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_q_resolved_support_theorem.md)

Using the exact FULL benchmark, Paper 31 now kills not only the global
inverse-upward / escape / diffusion class, but also the finite channel split
between one-photon resonant transfer and two-photon `2s`/higher-shell kernels.

So the remaining exact Stage-2 support is now singular: a non-uniform
`q`-resolved virtual-state renormalization law.

Paper 31 then kills the first natural multiplicative candidate on that support:

- [paper31_stage2_q_character_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_q_character_nogo_theorem.md)

So the remaining exact Stage-2 object must be more structured than a single
multiplicative DtN-character on `q`.

## Stage 3 — Perturbation Evolution (tight coupling)

### Standard

CLASS/CAMB solve the tightly coupled photon-baryon system for

- `delta_g`, `theta_g`
- `delta_b`, `theta_b`
- metric variables
- baryon loading
  \[
  R = \frac{3\rho_b}{4\rho_\gamma}
  \]
- Thomson time
  \[
  \tau_c = 1/\kappa'
  \]

### IO modification

`derived`:
the same local Thomson kernel `kappa'` controls both

- visibility, and
- photon-baryon momentum transfer / drag

But

`derived / no-go`:
the equations do **not** force `R` and `kappa'` to use the same baryon slot.
Mixed routing is mathematically allowed.

`verified`:
inside the minimal local acoustic ODE basis

\[
\{R,\ \mathrm{metric\_euler},\ \kappa'\},
\]

only the Thomson/diffusion leg survives as a live improvement direction.

### Baryon slot

- `R` acoustic inertia slot: `open`
- Thomson sector `kappa'` / drag slot: `open`
- strongest historical acoustic candidate: `omega_b,eff`
- local chemistry/opacity motivation: `omega_b,geom`

### Projection

Current confrontations use the projected Schur CMB branch as the bulk
background. No theorem currently promotes that branch to the unique full CMB
typed hierarchy.

### Authority

- Paper 26 Thomson-kernel identity audit
- Paper 26 tight-coupling slot-consistency audit
- Paper 26 CMB gravity-source class audit
- Paper 31 acoustic-operator and hierarchy-separation theorems

### Status

- Thomson-kernel identity: `derived`
- mixed `kappa'` / `R` routing allowed: `derived`
- CMB-era baryon slot in tight coupling: `open`

Later Paper 31 sharpening now adds the first positive Stage-2 law:

- [paper31_recombination_clock_transport_theorem.md](/opt/cosmology-lab/results/paper31/paper31_recombination_clock_transport_theorem.md)

This note proves that primordial recombination inherits the same OS-clock
transport structure as late reionization. So the exact Stage-2 law must include

\[
\mathcal R_{\rm rec}(z)=|d\tau_{\rm OS}/dz|\,/\,|dt_{\rm proj}/dz|
\]

on the local recombination chemistry itself. The follow-up benchmark also
proves that a naive clock-only pullback of the current projected history
overshoots badly, so the remaining exact branch is now a
transported-and-renormalized thermodynamics law, not a perturbation-only patch
and not a simple raw pullback.

This class boundary is now formalized explicitly in:

- [paper31_stage2_transported_renormalized_class_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_transported_renormalized_class_theorem.md)

That note proves the exact surviving Stage-2 object must be:

1. local recombination thermodynamics on `\tau_OS`,
2. plus an additional local Stage-2 renormalization,
3. then projected/reduced observer-side visibility packaging.

### What the killed routes imply

`verified`:
physical typed `R` reassignments are dead on the exact-kernel control branch.

`derived / scoped`:
the isolated metric-driving leg is a gauge artifact, not a valid closure object.

So the remaining live object is not a simple typed `R` replacement and not an
isolated metric rescaling.

Later Paper 31 sharpening now upgrades this boundary:

- [paper31_deeper_thermodynamics_bulk_hierarchy_theorem.md](/opt/cosmology-lab/results/paper31/paper31_deeper_thermodynamics_bulk_hierarchy_theorem.md)

That theorem proves the entire perturbation-only multiplicative Thomson class
is already dead as an exact solver class, because it leaves

\[
x_e,\ T_b,\ \kappa',\ e^{-\kappa},\ g,\ c_b^2,\ z_{\rm rec},\ r_s,\ \theta_s
\]

exactly unchanged. So the surviving exact branch is no longer “some still-open
perturbation-only Thomson hierarchy.” It is now a deeper typed
thermodynamics/bulk hierarchy that must change the visibility/thermodynamic
history itself and then feed the perturbation hierarchy.

One further sharpening now closes the first obvious local Stage-2 transport
candidates:

- [paper31_stage2_local_transport_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_stage2_local_transport_nogo_theorem.md)

So the exact surviving Stage-2 object is not just a deeper thermodynamics law
in the abstract. It must specifically be a local atomic-radiative
renormalization that counteracts the too-fast bare local branch. The leading
remaining classes are:

- enhanced upward photoionization / excitation,
- reduced effective escape,
- increased line trapping,
- or equivalent detailed-balance renormalizations.

## Stage 4 — Perturbation Evolution (free streaming)

### Standard

After tight coupling, CLASS/CAMB evolve the photon Boltzmann hierarchy for the
multipoles and their metric forcing.

### IO modification

`derived / scoped`:
the scalar metric/Weyl seed belongs to the intrinsic slice-curvature family

\[
\alpha_\Phi = 2,\qquad J_\Phi=x^{-1}.
\]

This identifies the class of the scalar metric seed. It does **not** yet by
itself provide a full theorem-grade new free-streaming hierarchy term for the
primary unlensed CMB.

`verified`:
the direct acoustic metric-driving factor tested inside the local ODE system is
not a viable physical closure object.

### Baryon slot

No new independent baryon slot is closed here. The free-streaming hierarchy
inherits whatever typed structure survived Stage 3.

### Projection

- projected Schur background for current runs
- scalar metric seed carries the Weyl/slice-curvature class

### Authority

- Paper 23 scalar perturbation equations
- Paper 31 internal `alpha_Phi = 2` theorem
- Paper 31 acoustic hierarchy boundary theorem

### Status

- class of scalar Weyl seed: `derived / scoped`
- exact primary-hierarchy IO modification: `open`

### What the killed routes imply

The missing object is not a simple multiplicative metric-driving term in the
current hierarchy. If Stage 4 needs modification, it must be a deeper typed
operator than the minimal metric leg already killed.

## Stage 5 — Source Function

### Standard

CLASS assembles source functions `S_T`, `S_E`, `S_B` from:

- local Sachs-Wolfe block
- Doppler block
- local polarization block
- integrated metric/ISW block
- visibility factors `g`, `g'`, `exp(-kappa)`

### IO modification

This is where five source/readout families have now been killed.

`derived / scoped`:
on a fixed bulk branch, the unique typed-opacity visibility family is

\[
d\kappa_c = c\,d\kappa,\qquad
e^{-\kappa_c}=(e^{-\kappa})^c,
\]
\[
g_c=c\,d\kappa\,(e^{-\kappa})^c,
\qquad
g'_c=c\,(d^2\kappa+c\,d\kappa^2)(e^{-\kappa})^c.
\]

`derived / scoped`:
the unique minimal typed source extension beyond that family is the two-leg
metric+visibility family

\[
S_{\rm IO}[c,m]=S_{\rm ac/vis}[c]+S_{\rm curv}[m].
\]

### Baryon slot

- visibility/readout factors `kappa', kappa, exp(-kappa), g`: `omega_b,eff` on the reduced observer-side chain
- chemistry/source-side microphysics: still unresolved
- scalar metric source leg: Weyl/curvature class, not a baryon rung

### Projection

- source packet lives on projected Schur bulk solutions
- scalar metric seed uses the Weyl/slice-curvature class

### Authority

- Paper 27 AV1 theorem
- Paper 31 source-operator no-go
- Paper 31 typed-hierarchy separation theorem
- Paper 31 minimal typed-source family theorem

### Status

- visibility/readout typing: `derived / scoped`
- full source-function class closure: `open`

### Five killed source/readout routes

`verified`:
all of the following fail on the exact-kernel control branch:

1. uniform local visibility-packet projection
2. local channel-split source projection
3. the full one-parameter typed-opacity visibility family
4. the pure common metric-curvature source leg
5. the full minimal metric+visibility two-leg family

### What the killed routes imply

`derived / scoped`:
the missing IO transfer function does **not** live as a post-ODE scalar
multiplier on the source packet.

So Stage 5 is no longer the main frontier. The debt has already been pushed
upstream into the pre-LOS acoustic/Thomson history.

## Stage 6 — Line-of-Sight Integration

### Standard

CLASS/CAMB resample the sources and perform the line-of-sight integral against
the closed-FRW radial kernels to obtain transfer functions and then `C_l`.

### IO modification

`derived`:
inside-horizon status by itself does not change the standard closed-FRW null
propagation law. On the OS interior slice,

- standard closed `K=+1` angular-diameter relations survive
- standard line-of-sight closed-space geometry survives

For the primary unlensed CMB, no extra theorem-grade IO LOS multiplier beyond
the already-fixed background/source structure is currently closed.

Later Paper 31 sharpening now fixes the exact boundary on the old post-bridge
field-readout theorem target:

- [paper31_post_bridge_field_readout_theorem.md](/opt/cosmology-lab/results/paper31/paper31_post_bridge_field_readout_theorem.md)
- [paper31_post_bridge_field_class_nogo_theorem.md](/opt/cosmology-lab/results/paper31/paper31_post_bridge_field_class_nogo_theorem.md)

This note proves the strongest theorem-grade field/readout law available on the
current stack is only the one-slot inverse square-root complement
\[
X_{\rm obs}=f_\Gamma^{1/2}X_{\rm prim},
\qquad
f_\Gamma=(1+\gamma^2)^{-1},
\]
not the stronger per-leg law `X_obs = f_Gamma X_prim`. So the old
`f_\Gamma^2 / f_\Gamma^3` optical-history branch remains a successful
conditional ansatz, not a derived post-bridge field theorem.

The new no-go theorem goes one step further:

- the seam is now closed **negatively inside the present scalar primary CMB
  class**;
- the bridge, carrier lift, sky collection, harmonic projection, and primitive
  source-to-sky transfer are all one-slot / linear before final bilinearization;
- therefore there is no hidden second complement insertion inside the current
  class.

So any future rescue of the stronger `f_\Gamma`-per-leg law must come from a
genuinely new observable class or a new second-insertion theorem outside the
present stack.

For the CMB lensing transfer side, the exact Weyl kernel is now fixed and
implemented in the local fork.

### Baryon slot

No fresh baryon slot enters at LOS stage. It inherits Stage 2–5 outputs.

### Projection

- primary LOS geometry: projected Schur closed FRW
- lensing transfer: Weyl-modified through the exact curved kernel

### Authority

- Paper 20 theta-star angular sector / OS null propagation
- Paper 31 exact curved Weyl kernel theorem

### Status

- closed-FRW LOS geometry inside the hole: `derived`
- exact primary unlensed IO LOS closure: `open`
- exact curved Weyl lensing transfer kernel: `derived / scoped`

### What the killed routes imply

Because source-packet dressings failed and LOS geometry is standard, the missing
object is not a late transfer/harmonic-stage rescaling. It must already be
present in the solved perturbation/thermodynamics history.

## Stage 7 — Lensing

### Standard

Weak lensing and CMB lensing use the Weyl potential, the lensing potential, and
then convergence/shear/lensed `C_l`.

### IO modification

`derived / scoped`:
the scalar weak-lensing package closes:

- `Phi` is on `alpha_Phi = 2`
- the scalar lensing potential is the closed-FRW line-of-sight projection of
  that same seed
- convergence and E-mode shear are screen-Hessian descendants of the same
  scalar family

So

\[
\frac{\Sigma_{\rm IO}}{\mu_{\rm IO}} = x^{-1/2}.
\]

`derived / scoped`:
the exact curved CMB lensing kernel is

\[
M_{\rm IO}(k)=x^{-1/2}\left(\frac{k^2-3K}{k_p^2-3K}\right)^{-1/4}.
\]

### Baryon slot

No fresh lensing baryon slot is licensed. The scalar lensing response is a Weyl
observable, not a new matter-slot observable.

### Projection

- Weyl-modified
- scalar/Born lensing package only

### Authority

- Paper 31 internal `alpha_Phi = 2` theorem
- Paper 31 scalar weak-lensing Hodge theorem
- Paper 31 Weyl-response bridge theorem
- Paper 31 exact curved Weyl kernel theorem

### Status

- scalar/Born lensing package: `derived / scoped`
- vector/tensor/post-Born/nonlinear lensing: `open`

### What the killed routes imply

The Weyl side is no longer the main missing CMB algebra. The exact surviving CMB
debt is upstream of lensing: the primary scalar transfer hierarchy.

## Stage 8 — Observable Extraction

### Standard

Likelihood inference uses:

- high-`ell` TT/TE/EE
- low-`ell` temperature/polarization
- lensing reconstruction and/or lensed spectra

### IO modification

`verified`:
high-`ell` TT effectively constrains

\[
A_{\rm eff}=A_s e^{-2\tau}.
\]

`derived / conditional`:
because the IO Weyl bridge suppresses the lensing response relative to the GR
kernel, a GR-based Planck extraction biases inferred `A_s` and `tau` downward.

`verified`:
with the fuller native Planck likelihood installed locally and the exact curved
Weyl kernel active, the current one-fluid control branch still does **not**
yield a stable interior replacement pair `(A_s,\tau)`. The fit runs toward the
`tau` floor and lower `A_s`.

Later Paper 31 sharpening also fixes the post-bridge damping-class boundary:

- the theorem-grade one-slot field/readout route gives only
  \[
  C_\ell^{\rm obs}=f_\Gamma C_\ell^{\rm prim},
  \]
  i.e. the old `K_gauge/2` class;
- the stronger `f_\Gamma^2` optical-history branch is not yet theorem-grade.

### Baryon slot

Different likelihood sectors inherit different class assignments:

- background distances: projected Schur
- visibility/readout: reduced acoustic/optical class
- late-time clustering: clustering class
- scalar lensing response: Weyl/`alpha=2` class

### Projection

- parameter extraction is observer-side and Weyl-biased relative to GR

### Authority

- Paper 31 C1b/C3 formal audit
- Paper 31 exact-curved native Planck boundary
- Paper 31 complete observable-class map

### Status

- Planck-bias direction under Weyl slip: `derived / conditional`
- final observational replacement pair `(A_s,\tau)`: `open`
- native source-side `A_s = 2.007245997...` on the active scalar-source stack:
  `derived / scoped`

### What the killed routes imply

The observational bottleneck is no longer "install the exact lensing kernel."
That part is done. The remaining ambiguity is whether

1. the one-fluid control branch is only a surrogate for the true full CMB
   typed hierarchy, or
2. an additional deeper pre-LOS Thomson/diffusion operator is still missing.

## Final synthesis

### What is closed

- Stage 1 background readout law and active Schur package
- Stage 7 scalar lensing / Weyl-response bridge
- exact curved CMB lensing kernel
- reduced visibility/readout typing
- source-stage no-go boundaries
- minimal local acoustic no-go boundaries
- negative closure of the post-bridge field-readout seam inside the current
  scalar primary field class

### What is open

- exact recombination chemistry/opacity class closure
- exact CMB-era `R` slot
- exact CMB perturbation-source class
- exact full pre-LOS Thomson/diffusion operator
- exact full typed CMB branch beyond the one-fluid control compression
- final observational replacement pair `(A_s,\tau)`
- any stronger post-bridge field theorem than the derived square-root law,
  which now requires a genuinely new observable class or second-insertion
  theorem outside the current scalar primary chain

### Best honest Paper 31 transfer conclusion

`derived / scoped`:
the true full IO CMB branch is **not**

- any source-packet rescaling family,
- not the typed-opacity visibility family,
- not the minimal metric+visibility family,
- not a physical typed `R` reassignment inside the minimal local acoustic basis,
- and not an isolated metric-driving factor.

`conditional / reconstruction`:
if the CMB branch closes, the surviving place for the IO-native transfer
function is now a deeper pre-LOS Thomson/diffusion hierarchy inside the
perturbation evolution / thermodynamics chain, or a different typed bulk/readout
hierarchy altogether.
