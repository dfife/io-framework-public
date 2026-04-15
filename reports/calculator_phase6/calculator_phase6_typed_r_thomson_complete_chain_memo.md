# Paper 37 Typed `R` / Thomson Complete Chain Theorem Memo

Date: 2026-04-15

## Purpose

This memo packages the complete current chain behind the typed `R` closure and
the live Thomson-history realization for Cosmo review.

It is meant to answer two precise questions:

1. Are the site-specific typed `R` composites merely plausible, or are they the
   unique admissible hierarchy operators on the current IO stack?
2. Does the live calculator actually build the Thomson tuple from the typed
   split history path, or does it still flatten everything into one opacity?

## Executive result

What is now closed:

- `derived / scoped as maps`:
  the full closed-scalar typed `R` hierarchy operator on the accepted
  equal-rate scoped branch
- `derived / scoped`:
  uniqueness of the site-wise typed `R` placements by elimination on the same
  accepted branch
- `derived / scoped as maps`:
  the live typed split Thomson-history realization
- `verified / implementation`:
  the live calculator code path now exposes that typed split explicitly

What this memo does **not** claim:

- it does not claim a theorem-grade nontrivial deformation
  `thomson_drag_rate != thomson_hierarchy_rate`
- it does not claim that the full TT spectrum is already physically validated
- it does not claim that the observed peak-height pattern is itself a primitive
  one-slot baryon observable

## Exact claim

On the current accepted IO stack, the full baryon-photon hierarchy does not
admit any one-slot reassignment

`R -> R(omega_b^*)`.

The surviving exact object is instead the site-wise typed hierarchy operator
built from the primitive local enthalpy ratio

`R_local,geom = 3 rho_b,geom / (4 rho_gamma)`

and the coupled Thomson tuple

`(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)`.

Accepted scope:

`thomson_hierarchy_rate = thomson_drag_rate`.

The unique admissible site placements are:

1. momentum coupling:

   `Gamma_gammab = thomson_drag_rate`

   `Gamma_bgamma = R_local,geom thomson_drag_rate = R_local,geom / tau_c`

2. pressure restoring force:

   `c_bgamma^2 = 1 / [3 (1 + R_local,geom)]`

3. inertia and dynamic odd/even loading:

   `M_bgamma = 1 + R_local,geom`

   `L_odd/even = R_local,geom / (1 + R_local,geom)`

4. Silk damping:

   `D_heat = R_local,geom^2 / [6 (1+R_local,geom)^2 thomson_drag_rate]`

   `D_visc = 16 / [90 (1+R_local,geom) thomson_hierarchy_rate]`

   `D_silk = D_heat + D_visc`

The live calculator realizes the Thomson tuple through the typed split history
path

`kappa'_loc -> visibility packet -> conformal Thomson tuple`,

not by passing one undifferentiated opacity scalar directly into the hierarchy.

## The theorem chain

### Step 0. Premise layer

The present chain uses the lab's accepted IO framework and one external
microphysical admissibility claim:

- Premise 1 fixes the interior black-hole cosmology framework and therefore the
  accepted closed-background/typed-boundary setting in which the perturbation
  stack lives.
- Premise 2 licenses use of accepted exterior photon-baryon microphysics
  locally inside the same physical laws.

Only Premise 2 is needed directly for the site-wise oscillator algebra. Premise
1 enters through the already accepted IO closed-geometry solver stack and does
not provide an independent typed-`R` degree of freedom.

### Step 1. Primitive local enthalpy theorem

Published authority:

- [paper29.sound_speed_selector](/opt/cosmology-lab/results/paper29)
- [paper31_baryon_assignment_stage1_report.md](/opt/cosmology-lab/results/paper31/paper31_baryon_assignment_stage1_report.md)

Calculator surface:

- [typed_r_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/typed_r_operator.py)
- [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Content:

`R_local,geom(z) = 3 rho_b,geom(z) / [4 rho_gamma(z)]`

is the primitive local baryon-photon enthalpy ratio. This fixes the local
thermodynamic object on the geometric inventory branch.

Status:

- `derived / scoped`

### Step 2. No-single-slot theorem

Published authority:

- [paper31_baryon_assignment_stage2_report.md](/opt/cosmology-lab/results/paper31/paper31_baryon_assignment_stage2_report.md)
- [paper32_typed_boundary_to_bulk_projection_theorem.md](/opt/cosmology-lab/results/paper32/paper32_typed_boundary_to_bulk_projection_theorem.md)
- [paper32_s3_native_solver_specification_theorem.md](/opt/cosmology-lab/results/paper32/paper32_s3_native_solver_specification_theorem.md)

Calculator surface:

- [perturbation_types.py](/opt/cosmology-lab/calculator/src/aio_calculator/perturbation_types.py)
- [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Content:

The hierarchy does **not** close by any hierarchy-wide substitution

`R -> R(omega_b,geom)`,
`R -> R(omega_b,eff)`,
or
`R -> R(omega_b,clustering)`.

Instead, `(kappa', R)` is already an irreducibly mixed typed object, and the
lower-triangular boundary forbids observer/readout baryon typing from
back-propagating into the primitive local plasma leg.

Status:

- `derived / scoped`

### Step 3. Thomson-history tuple theorem

Authority:

- [paper37_thomson_history_realization_theorem_report.md](/opt/cosmology-lab/results/paper37/paper37_thomson_history_realization_theorem_report.md)

Calculator surface:

- [thomson_history_contract.py](/opt/cosmology-lab/calculator/src/aio_calculator/thomson_history_contract.py)
- [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Content:

The local acoustic hierarchy must act on the coupled tuple

`(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)`

with

`tau_c = 1 / thomson_drag_rate`

and

`dtau_c = - d(thomson_drag_rate) tau_c^2`.

This kills any attempted closure that only modifies a downstream visibility
scalar or only touches `kappa'` at one site.

Status:

- `derived / scoped`

### Step 4. Full typed `R` hierarchy operator theorem

Authority:

- [paper37_typed_r_operator_theorem_report.md](/opt/cosmology-lab/results/paper37/paper37_typed_r_operator_theorem_report.md)

Calculator surface:

- [typed_r_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/typed_r_operator.py)
- [scalar_acoustic_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_acoustic_operator.py)
- theorem node `local.typed_r_operator` in [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Content:

The exact surviving operator is the site map

`(Gamma_gammab, Gamma_bgamma, c_bgamma^2, M_bgamma, L_odd/even, D_heat, D_visc, D_silk)`

built from

- one primitive local enthalpy ratio `R_local,geom`
- the Paper 37 Thomson tuple
- no observer-side baryon-slot back-propagation

This theorem also corrects the earlier momentum-coefficient convention on the
live calculator carrier:

`Gamma_bgamma = R_local,geom thomson_drag_rate`,

not

`thomson_drag_rate / R_local,geom`.

Status:

- `derived / scoped as maps`

### Step 5. Typed `R` site-uniqueness theorem

Authority:

- [paper37_typed_r_site_uniqueness_theorem_report.md](/opt/cosmology-lab/results/paper37/paper37_typed_r_site_uniqueness_theorem_report.md)

Calculator surface:

- theorem node `local.typed_r_site_uniqueness` in [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Content:

This is the named theorem Cosmo asked for. It proves by elimination that no
other site placement is admissible.

The elimination is:

1. pressure and inertia cannot move off `R_local,geom` without either
   observer-side back-propagation, a forbidden drag-vs-sound primitive split,
   or a new primitive local object not present in the stack
2. momentum exchange is fixed uniquely once the local carrier convention
   `tau_c = 1 / thomson_drag_rate` is fixed
3. Silk damping must split by sector, with heat carried by slip/drag and
   viscosity carried by the photon hierarchy
4. every surviving alternative collapses back into a killed family:
   one-slot substitution, primitive-site reassignment, observer-side
   back-propagation, convention mismatch, or loss of the drag/hierarchy split

Status:

- `derived / scoped`

### Step 6. Typed split Thomson-history realization theorem

Authority:

- [paper37_typed_thomson_split_history_implementation_audit_report.md](/opt/cosmology-lab/results/paper37/paper37_typed_thomson_split_history_implementation_audit_report.md)

Calculator surface:

- [thomson_history_contract.py](/opt/cosmology-lab/calculator/src/aio_calculator/thomson_history_contract.py)
- [scalar_tt_driver.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_tt_driver.py)
- theorem node `local.typed_thomson_split_history_realization` in [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Content:

The live TT implementation now makes the typed split explicit:

1. local chemistry / local opacity:

   `kappa'_loc(z) = a n_e(z) sigma_T`

2. observer-side optical packet:

   `d tau_obs / dz`, `tau_obs`, `g_obs = exp(-tau_obs) d tau_obs / dz`

3. conformal Thomson tuple:

   `thomson_drag_rate = |(d tau_obs / dz) / (dC / dz)|`

   `thomson_hierarchy_rate = thomson_drag_rate`

   `tau_c = 1 / thomson_drag_rate`

   `dtau_c = - d(thomson_drag_rate) tau_c^2`

So the implementation path is typed and layered rather than flattened.

Status:

- `derived / scoped as maps`
- `verified / implementation`

### Step 7. Closed scalar acoustic generator

Authority:

- [paper37_closed_scalar_acoustic_generator_theorem_report.md](/opt/cosmology-lab/results/paper37/paper37_closed_scalar_acoustic_generator_theorem_report.md)

Calculator surface:

- [scalar_acoustic_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_acoustic_operator.py)

Content:

The local closed-`S^3` scalar hierarchy now consumes the fully typed site map
instead of a fake one-slot `R`.

The live implementation uses the site-specific objects directly:

- momentum site through `baryon_momentum_exchange_rate`
- TCA/inertia through `baryon_inertia_factor`
- dynamic loading through `odd_even_dynamic_loading_factor`

This closes the actual hierarchy insertion sites at the current theorem-grade
map scope.

Status:

- `derived / scoped as maps`
- `verified / implementation`

## Live code path

For code review, the live typed split path is:

1. [recombination.py](/opt/cosmology-lab/calculator/src/aio_calculator/recombination.py)

   - `primitive_local_kappa_prime(z, x_e)`
   - `build_visibility_packet(history)`

2. [thomson_history_contract.py](/opt/cosmology-lab/calculator/src/aio_calculator/thomson_history_contract.py)

   - `build_typed_split_thomson_history_realization(...)`

3. [scalar_tt_driver.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_tt_driver.py)

   - `build_visibility_derived_conformal_thomson_history(...)`
   - consumes `realization.contract`

4. [typed_r_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/typed_r_operator.py)

   - builds the site-wise typed operator sample

5. [scalar_acoustic_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_acoustic_operator.py)

   - consumes the typed site objects in the hierarchy RHS

## What an attack must break

To break the current closure, Cosmo would need to land on at least one of these:

1. show that `R_local,geom` is **not** the primitive local enthalpy object
2. show that observer-side `omega_b,eff` is allowed to back-propagate into the
   local thermodynamic bulk leg without violating the lower-triangular boundary
3. show that the local hierarchy carrier convention is **not**
   `tau_c = 1 / thomson_drag_rate`
4. show that the heat and viscosity pieces of Silk damping do not belong to the
   slip/drag and hierarchy/shear sectors respectively
5. show that the live code path actually bypasses the typed split and reuses a
   flattened opacity scalar

Absent one of those attacks, the current site map is the unique admissible
typed closure on the accepted stack.

## Honest boundary

What is closed:

- the full typed `R` hierarchy operator
- uniqueness of the site-wise placements
- explicit typed split Thomson-history realization in the live code

What remains open:

- a theorem-grade nontrivial split
  `thomson_drag_rate != thomson_hierarchy_rate`
- full physical validation of the TT spectrum after the typed-`R` closure
- any claim that the final observed peak-height pattern is a primitive one-slot
  baryon observable

## Reproducibility

Primary reports:

- [paper37_typed_r_operator_theorem_report.md](/opt/cosmology-lab/results/paper37/paper37_typed_r_operator_theorem_report.md)
- [paper37_typed_r_site_uniqueness_theorem_report.md](/opt/cosmology-lab/results/paper37/paper37_typed_r_site_uniqueness_theorem_report.md)
- [paper37_typed_thomson_split_history_implementation_audit_report.md](/opt/cosmology-lab/results/paper37/paper37_typed_thomson_split_history_implementation_audit_report.md)

Primary code:

- [typed_r_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/typed_r_operator.py)
- [thomson_history_contract.py](/opt/cosmology-lab/calculator/src/aio_calculator/thomson_history_contract.py)
- [scalar_acoustic_operator.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_acoustic_operator.py)
- [scalar_tt_driver.py](/opt/cosmology-lab/calculator/src/aio_calculator/scalar_tt_driver.py)
- [provenance.py](/opt/cosmology-lab/calculator/src/aio_calculator/provenance.py)

Verification commands:

```bash
cd /opt/cosmology-lab/calculator
PYTHONPATH=src python -m pytest tests -q
python build_bundle.py
```

Current verification state at memo write time:

- `101 passed`
- bundle build clean
