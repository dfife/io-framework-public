# Paper 31: Practical IO Baryon-Slot Audit

Date: 2026-04-04

## Question

The practical IO `C_ell` calculator had been using a single `omega_b` value.
Paper 31, however, carries three baryon densities:

- `omega_b,geom = 0.02108`
- `omega_b,eff = 0.0291`
- `omega_b,clustering = 0.017053042566349`
- conditional structured proxy `omega_b,struct = 0.02594110201749857`

The objective here is not to fit a new baryon value. It is to determine whether
the current practical calculator is failing because it collapses the three carried
baryon slots into one number, or because the current explicit three-slot wiring in
the patched CLASS fork is itself not the right implementation of the Paper 31 map.

## Fixed IO Package

- `H0 = 68.91`
- `Omega_k = -0.005613722564239`
- `A_s = 2.0072459972737347e-09`
- `J_Phi = x^(-1/2) = 0.8113740489243784`
- `f_Gamma = 1/(1+gamma^2) = 0.946605531726076`
- `c_vis = f_Gamma^2 = 0.896062032694407`
- `d_drag = 1`
- `h_hier = f_Gamma^3 = 0.8482172769182377`
- `reio_parametrization = reio_none`

## Matrix A: `omega_cdm` Adjusted With The Clustering Slot

This treats `omega_b,clustering` as the baryon piece of the carried Schur matter
target and sets `omega_cdm = omega_m,target - omega_b,clustering`.

- one-number structured baseline: `chi2 = 2135.722987`, `100theta_s = 1.056106033`
- explicit all-struct sanity check: `chi2 = 2145.420496`, `100theta_s = 1.056155123`

| geom | eff | clust | chi2 | 100theta_s |
| --- | --- | --- | ---: | ---: |
| `geom` | `eff` | `clustering` | 9704.208559 | 1.039409537 |
| `geom` | `eff` | `geom` | 8835.170320 | 1.039409538 |
| `geom` | `eff` | `eff` | 7499.516003 | 1.039409525 |
| `geom` | `struct` | `geom` | 3828.559608 | 1.052649722 |
| `struct` | `struct` | `geom` | 2647.490927 | 1.056155120 |
| `struct` | `struct` | `struct` | 2145.420496 | 1.056155123 |

Best row in this matrix:

- `geom = struct`, `eff = struct`, `clust = eff` -> `chi2 = 1938.753178`

## Matrix B: `omega_cdm` Held Fixed

This isolates the slot effect itself by keeping `omega_cdm` equal to the
one-number practical branch value.

- one-number structured baseline: `chi2 = 2135.722987`, `100theta_s = 1.056106033`
- explicit all-struct sanity check: `chi2 = 2135.722987`, `100theta_s = 1.056106033`

| geom | eff | clust | chi2 | 100theta_s |
| --- | --- | --- | ---: | ---: |
| `geom` | `eff` | `clustering` | 11213.344360 | 1.031396798 |
| `geom` | `eff` | `geom` | 9508.943098 | 1.035081842 |
| `geom` | `eff` | `eff` | 7228.152845 | 1.042048065 |
| `geom` | `struct` | `geom` | 3300.573453 | 1.048294243 |
| `struct` | `struct` | `geom` | 1924.535755 | 1.051760180 |
| `struct` | `struct` | `struct` | 2135.722987 | 1.056106033 |

Best row in this matrix:

- `geom = struct`, `eff = struct`, `clust = geom` -> `chi2 = 1924.535755`

## Executive Result

1. `verified`: the explicit three-slot code path itself is numerically viable.
   When all three explicit slots are set equal to `omega_b,struct`, it reproduces
   the one-number structured branch exactly when `omega_cdm` is also held fixed.

2. `verified`: the literal Paper 31 baryon theorem map is catastrophic in the
   current CLASS fork. Using
   `geom = omega_b,geom`, `eff = omega_b,eff`, `clust = omega_b,clustering`
   gives very poor confrontations in both matrices.

3. `verified`: the strongest improvement comes from lowering the baryon slot that
   feeds the background/metric-source role while keeping the chemistry/acoustic
   side near the practical structured value.

   On the pure slot-isolation matrix, moving from the one-number structured baseline
   to `geom = struct`, `eff = struct`, `clust = geom` improves the confrontation by
   `Delta chi2 = -211.187232`.

4. `conditional / diagnostic`: that best-performing row is not theorem-grade, because
   it does not respect the derived chemistry assignment `geom = omega_b,geom`.
   So it is a debugging clue, not a promoted physical branch.

5. `derived / diagnostic`: the user concern was correct. The practical calculator gap
   is not just 'CLASS uses one baryon number'; it is also that the present explicit
   three-slot implementation does not faithfully realize the Paper 31 baryon map.

## Code-Level Interpretation

The current fork wires:

- chemistry / HyRec hydrogen inventory -> `omega_b_geom`
- acoustic loading `R` -> `omega_b_eff`
- background matter and scalar perturbation stress-energy source -> `omega_b_clustering`

That last choice is exactly where the Paper 31 theorem stack already warned that
the scalar metric source is not licensed to use the late clustering branch.

So the main surviving diagnostic is:

- the calculator likely needs a more careful split between
  local chemistry / opacity, acoustic loading, and background/metric-source baryon
  roles than the current `geom/eff/clustering` implementation provides.

## Reproducibility

- script: [paper31_practical_io_baryon_slot_audit.py](/opt/cosmology-lab/results/paper31/paper31_practical_io_baryon_slot_audit.py)
- fixed-cdm matrix: [paper31_practical_io_baryon_slot_audit_fixed_cdm.json](/opt/cosmology-lab/results/paper31/paper31_practical_io_baryon_slot_audit_fixed_cdm.json)
- variable-cdm matrix: [paper31_practical_io_baryon_slot_audit_variable_cdm.json](/opt/cosmology-lab/results/paper31/paper31_practical_io_baryon_slot_audit_variable_cdm.json)
