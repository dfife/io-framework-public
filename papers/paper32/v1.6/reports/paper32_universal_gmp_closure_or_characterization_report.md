# Paper 32 universal GMP: closure or characterization

## Question

Does GMP extend to the full local algebra beyond the realized typed bridge
class, or is the scope limitation irreducible? If irreducible, what exactly
lives outside the typed class, and does GMP hold there?

## Headline

- `derived / explicit no-go`: universal GMP on the **full local algebra** is
  false on the present stack.
- `derived / scoped`: GMP is fully closed on the **realized typed bridge
  class**.
- `derived / scoped`: that typed class is exhaustive for all **physically
  realized bridge-placement observables**.
- `derived`: the remaining scope wall is irreducible but now fully
  characterized.

## 1. What Paper 32 actually closes

Paper 32 Theorem 32.B fixes the complete linearized IO map as a typed extended
carrier with three blocks:

1. source/readout block `P_src`,
2. thermodynamic/history block `U_therm = U_rec^hist ⊕ U_reio^loc`,
3. perturbation block `U_pert^(S^3)` with typed couplings from source and
   thermodynamics.

Paper 32 Theorem 32.E then closes GMP only on the realized bridge/readout side:

- tensor type,
- channel floor `J_min = s`,
- background placement,
- multiplicity-one bridge grammar

force geometric mode placement.

So GMP is theorem-grade on the realized typed bridge class.

Authorities:
- `/opt/cosmology-lab/results/paper32/paper32_bridge_selection_and_typed_gmp_theorems.md`
- `/opt/cosmology-lab/results/paper32/paper32_typed_boundary_to_bulk_projection_theorem.md`

## 2. What physical objects live outside the typed bridge class

### 2.1 Recombination/history block

Physical realized class:

- `Y_rec = (x_e, T_m, D_-(q;z), L_-(z))`

This is a history-state radiative-transfer object. Paper 31 proves:

- exact Stage-2 closure requires the characteristic/history carrier,
- `N_D^IO = 1` on the characteristic field,
- no extra post-bridge complement acts there.

So this block is physical and realized, but it is **not** a puncture-load to
spatial-channel placement observable. GMP is not false there; it is simply not
the right predicate.

Authorities:
- `/opt/cosmology-lab/results/paper31/paper31_stage2_characteristic_field_inheritance_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_stage2_lossless_characteristic_markov_theorem.md`

### 2.2 Reionization local-history block

Physical realized class:

- function-valued local ionization/emissivity histories on OS proper time

Paper 31 and 32 prove this is:

- a local-history block,
- not another scalar boundary coefficient,
- not another source/readout complement.

Again, GMP is not the right predicate there because there is no bridge channel
placement question.

Authorities:
- `/opt/cosmology-lab/results/paper31/paper31_reionization_inheritance_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reionization_functional_nogo_theorem.md`
- `/opt/cosmology-lab/results/paper32/paper32_typed_boundary_to_bulk_projection_theorem.md`

### 2.3 Closed-`S^3` perturbation hierarchy

Physical realized class:

- `H_pert^(S^3)` downstream of source plus thermodynamic history

This block is physical and realized, but it is not itself an independent
bridge-placement operator class. It is the downstream bulk evolution sector.

Authority:
- `/opt/cosmology-lab/results/paper32/paper32_s3_native_solver_specification_theorem.md`
- `/opt/cosmology-lab/results/paper32/paper32_typed_boundary_to_bulk_projection_theorem.md`

## 3. What lives outside on the larger full local algebra

Paper 27 already proves an explicit non-geometric bypass class on the larger
local algebra:

`Q_w^(ng) = R_w tensor I_th tensor I_sp tensor sqrt(L1) P_1`

This has identity spatial leg and bypasses the bridge entirely.

So on the **full local algebra**, universal GMP is not merely unproved. It is
false on the present stack.

Authorities:
- `/opt/cosmology-lab/results/paper27/paper27_gmp_pass_fail_audit.md`
- `/opt/cosmology-lab/results/paper27/paper27_gmp_counterexample_physical_threat_audit.md`

## 4. Final classification

There are three domains:

1. **Realized typed bridge/readout observables**
   - GMP holds.
   - This is the exact Paper 32 typed bridge class.

2. **Realized physical but non-bridge observables**
   - recombination characteristic/history
   - reionization local histories
   - downstream closed-`S^3` perturbation hierarchy
   - GMP is inapplicable here, not false.

3. **Abstract larger-algebra bypass operators**
   - identity-spatial-leg non-geometric classes survive
   - GMP fails there as a universal claim.

## Final verdict

`derived`: universal GMP on the full local algebra does **not** close.

`derived / scoped`: the typed bridge class is exhaustive for physically
realized **bridge-placement** observables, so GMP is universal on that physical
subclass.

`derived`: the scope wall is therefore irreducible, but fully characterized:

- outside the typed bridge class, the physical complement is the non-bridge
  history/solver sector, where GMP is not the right statement;
- outside the realized physical architecture, the larger local algebra still
  contains explicit non-geometric bypass operators, where universal GMP fails.

So there is no remaining live frontier on this question.
