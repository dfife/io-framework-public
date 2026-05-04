# Paper 21 reproducibility script manifest

Status: bundle-scope draft / public-candidate filter applied

Date: 2026-05-04

Boundary: a Paper 21 public reproducibility bundle should include only scripts that directly reproduce a numerical value, theorem, no-go theorem, or corrected scorecard claim appearing in Paper 21 v1.6. Exploratory support scripts without a direct manuscript trace are excluded from the public bundle even if they remain useful locally.

## Include in public bundle

### Active AC1 / acoustic closure

| Script | Direct manuscript trace | Output |
|---|---|---|
| `paper21_ac1_opening_investigation_checks.py` | AC1 Reduction Theorem; `J_theta = x^(-1/2) sqrt(1+gamma^2)`; `theta_* = 0.599 deg`; degree-2 no-go | `paper21_ac1_opening_investigation_results.json`, `.txt` |
| `paper21_a4_bridge_theorem_checks.py` | A4 Bridge Theorem; collection/harmonic projection no-new-slot checks | `paper21_a4_bridge_theorem_results.json`, `.txt` |

### Puncture weights, optical branch, and branch assignment

| Script | Direct manuscript trace | Output |
|---|---|---|
| `paper21_sharpening_03622_analysis.py` | `Z_punc = 1.4221`; `f_E({1,2}) = L_1 + L_2 = 0.3622`; `L_1 = 0.22417`, `L_2 = 0.13805` | `paper21_sharpening_03622_results.json`, `.txt` |
| `paper21_two_formalization_theorems_analysis.py` | Theorem 21.I, Theorem 21.J, No-go 21.K | `paper21_two_formalization_theorems_results.json`, `.txt` |
| `paper21_tio_branch_assignment_theorem_analysis.py` | Theorem 21.L and Corollary 21.L1; `T_IO` vs `T_obs` BBN branch assignment | `paper21_tio_branch_assignment_theorem_results.json`, `.txt` |
| `paper21_pmultlift_tensor_weight_projection_analysis.py` | Theorem 21.O; No-go 21.P; local nontraciality and Wigner-Eckart selection failure | `paper21_pmultlift_tensor_weight_projection_results.json`, `.txt` |
| `paper21_metric_tensor_product_theorem_analysis.py` | Theorem 21.M and No-go 21.M1/M3 route statements | `paper21_metric_tensor_product_theorem_results.json`, `.txt` |

### Radiation-response no-go / provenance claims that appear in v1.6

| Script | Direct manuscript trace | Output |
|---|---|---|
| `paper21_routeA_routeB_investigation.py` | Theorem 21.A, Theorem 21.Ba, scoped 21.Bb | `paper21_routeA_routeB_investigation_results.json`, `.txt` |
| `paper21_assembly_gap_radiation_analysis.py` | Theorem 21.C; assembly-gap decoupling; `d ln H0 / d ln N_eff = 4.96e-5`; `N_eff ~ 6708` diagnostic | `paper21_assembly_gap_radiation_results.json`, `.txt` |
| `paper21_final_two_probes_analysis.py` | Theorem 21.E and Theorem 21.F | `paper21_final_two_probes_results.json`, `.txt` |
| `paper21_freezein_expanding_revisit_analysis.py` | v1.2/v1.6 freeze-in sign-reversal/dead-route statement; `omega_b,geom` below target | `paper21_freezein_expanding_revisit_results.json`, `.txt` |
| `paper21_j2_geometric_freezeout_analysis.py` | Theorem 21.G and j=2/tensor-route narrowing | `paper21_j2_geometric_freezeout_results.json`, `.txt` |
| `paper21_bulk_propagation_selection_analysis.py` | Theorem 21.Q, No-go 21.R, Conditional reconstruction 21.S | `paper21_bulk_propagation_selection_results.json`, `.txt` |
| `paper21_lambda4_and_eopt_gap_closure_analysis.py` | Theorem 21.X, Theorem 21.Y, No-go 21.Z; `F_abs`; `lambda=4` conditional uniqueness | `paper21_lambda4_and_eopt_gap_closure_results.json`, `.txt` |
| `paper21_conformal_probe_projection_analysis.py` | Conditional 21.AA/21.AC; No-go 21.AB1, 21.AD, 21.AF; theta-shift and conformal-source failures | `paper21_conformal_probe_projection_results.json`, `.txt` |
| `paper21_a8_dilution_route_analysis.py` | Stiff `a^-8` route numbers quoted in §12B/§12C; `Delta N_eff,eff = 3840` at 10 MeV and collapse by 0.1 MeV | `paper21_a8_dilution_route_results.json`, `.txt` |
| `paper21_local_expansion_variance_analysis.py` | Local expansion variance no-go; tracking factor collapse; `Delta N_eff,eff = 2.75` | `paper21_local_expansion_variance_results.json`, `.txt` |
| `paper21_local_interaction_dressing_analysis.py` | Theorem/No-go 21.AG; uniform-rate family; D/H-matching `Y_p = +5.73 sigma` | `paper21_local_interaction_dressing_results.json`, `.txt` |
| `paper21_nonseparable_weak_sector_tests_analysis.py` | Chiral `g_A`, phase-space Jacobian, and `G_F` no-go summaries | `paper21_nonseparable_weak_sector_tests_results.json`, `.txt` |
| `paper21_gemini_followup_routes_analysis.py` | Geometric chemical potential, UV-tail, and active-sterile depletion no-go summaries | `paper21_gemini_followup_routes_results.json`, `.txt` |
| `paper21_presp_round2_five_angles_analysis.py` | V(alpha) radiation/scope-boundary route and torsion-spin magnitude no-go support in the nineteen-route ledger | `paper21_presp_round2_five_angles_results.json`, `.txt` |

### Corrected scorecard / wrapper hygiene

| Script | Direct manuscript trace | Output |
|---|---|---|
| `paper21_vNplus1_ypbbn_to_ypcmb_correction_audit.py` | Paper 21 v1.5/v1.6 corrected scorecard; YPBBN -> YPCMB; Path C amplitude alignment; L1/L2 independence check | `paper21_vN+1_ypbbn_to_ypcmb_correction_results.json`, memo |

## Exclude from public bundle by default

These scripts are useful local support/provenance, but they do not directly reproduce a theorem/no-go label or quoted numerical value in Paper 21 v1.6 strongly enough to justify public-bundle inclusion.

| Script | Reason for exclusion |
|---|---|
| `paper21_expanding_phase_foundational_audit_analysis.py` | Foundational convention support for freeze-in route; not itself a manuscript theorem/quoted number. |
| `paper21_item4_opening_assault_analysis.py` | Early Item 4 assault and Theorem 21.N support; final v1.6 body does not carry 21.N as a direct theorem claim. |
| `paper21_hybrid_response_functional_analysis.py` | Hybrid-functional exploration and Theorem 21.V support; final v1.6 body does not carry 21.V directly. |
| `paper21_optical_filtration_functional_analysis.py` | Intermediate Theorem 21.W support; final body carries the later fixed-point/optical-kill result through 21.Y/21.Z instead. |
| `paper21_casimir_response_modular_defect_analysis.py` | Intermediate Theorem 21.T/21.U diagnostics; final body carries the public `F_abs` and fixed-point no-go through the lambda/fixed-point scripts. |

## Bundle framing rule

The public bundle should not present the Part II route scripts as active BBN evidence. Their correct role is:

```text
historical no-go/provenance registry that constrained the later Paper 22 rate-dressing solution
```

The active Paper 21 artifacts are:

```text
AC1/theta_* closure
SU(2) puncture partition and L_1/L_2 load derivation
T_IO branch assignment
local nontraciality / optical fixed-point no-go boundaries
YPBBN -> YPCMB scorecard correction
```
