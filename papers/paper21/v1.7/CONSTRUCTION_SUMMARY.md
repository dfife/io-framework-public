# Paper 21 v1.7 Construction Summary

Status: `verified / bundle-construction`

## Scope Decision

The bundle includes every live Paper 21 v1.6/v1.7 number or theorem-support
artifact that has a clean script path and remains actively asserted by the
framework.

Dead route rerunners from the historical `P_resp` investigation are excluded.
They remain in the manuscript as no-go demonstrations and are summarized in the
kappa audit, but the public runnable bundle does not re-run them.

## Scripts

| Script | Inputs | Output | Manuscript value / theorem |
|---|---|---|---|
| `01_derive_L1_puncture_load.py` | `data/imported_constants.json` | `results/L1_puncture_load_results.json` | `L_1 = 0.22417` |
| `02_derive_L2_puncture_load.py` | `data/imported_constants.json` | `results/L2_puncture_load_results.json` | `L_2 = 0.13805` |
| `03_compute_ac1_closure.py` | `data/imported_constants.json` | `results/ac1_closure_results.json` | `J_theta = x^(-1/2)sqrt(1+gamma^2)`, AC1 closure |
| `04_prymordial_wrapper_conventions.py` | `data/imported_constants.json` | `results/prymordial_wrapper_conventions_results.json` | YPCMB / `PRyMresults()[3]` convention |
| `05_generate_bbn_scorecard.py` | `data/imported_constants.json` | `results/bbn_scorecard_results.json` | corrected Y_p, D/H, Li-7 pulls and chi-square |
| `06_operator_algebra_live_theorem_artifacts.py` | `data/imported_constants.json` | `results/operator_algebra_live_theorem_artifacts_results.json` | optical filtration, branch assignment, local nontraciality, Wigner-Eckart boundary |
| `07_validate_expected_outputs.py` | `results/*.json` | stdout PASS/FAIL summary | frozen-output validation |

## Existing Scripts Used

The public scripts are distilled from the private Paper 21 support scripts and
frozen outputs:

- `paper21_sharpening_03622_analysis.py`
- `paper21_ac1_opening_investigation_checks.py`
- `paper21_a4_bridge_theorem_checks.py`
- `paper21_two_formalization_theorems_analysis.py`
- `paper21_tio_branch_assignment_theorem_analysis.py`
- `paper21_pmultlift_tensor_weight_projection_analysis.py`
- `paper21_vNplus1_ypbbn_to_ypcmb_correction_audit.py`

## Gaps Filled

- Separate public scripts were created for `L_1` and `L_2` even though the
  private lab computed them together. This makes the bundle match the v1.7
  manuscript update plan and keeps each headline load independently auditable.
- A compact public wrapper-convention script was added because PRyMordial is not
  redistributed here.
- A compact operator-algebra theorem-artifact script was added to avoid shipping
  dead route rerunners while still preserving live theorem support.

## Deferred / Excluded

- Historical `P_resp` dead-route reruns are excluded by PI instruction.
- PRyMordial itself is not bundled; it remains an external solver.
- The bundle does not attempt to reproduce Paper 22's rate-dressing derivation.
  Paper 21 supplies `L_1` and `L_2`; later delivery into rate dressing is
  Paper 22/Paper 25 conditional bridge structure.
