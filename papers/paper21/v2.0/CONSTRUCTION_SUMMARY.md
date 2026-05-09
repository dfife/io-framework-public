# Paper 21 v2.0 Construction Summary

Status: `VERIFIED / bundle-construction`

## Scope Decision

The bundle includes every live Paper 21 v2.0 number or theorem-support artifact
that has a clean script path and remains actively asserted by the framework.
The v2.0 paper removes the former radiation-response investigation, so those
dead-route rerunners are not included.

## Scripts

| Script | Inputs | Output | Manuscript value / theorem |
|---|---|---|---|
| `01_r4_firas_dependency_audit.py` | `data/imported_constants.json` | `results/r4_firas_dependency_audit_results.json` | R4/FIRAS dependency; confirms R4 does not enter active BBN scorecard |
| `02_derive_L1_puncture_load.py` | `data/imported_constants.json` | `results/L1_puncture_load_results.json` | `L_1 = 0.22417` |
| `03_derive_L2_puncture_load.py` | `data/imported_constants.json` | `results/L2_puncture_load_results.json` | `L_2 = 0.13805` |
| `04_compute_ac1_closure.py` | `data/imported_constants.json` | `results/ac1_closure_results.json` | `J_theta = x^(-1/2)sqrt(1+gamma^2)`, AC1 closure |
| `05_prymordial_wrapper_conventions.py` | `data/imported_constants.json` | `results/prymordial_wrapper_conventions_results.json` | YPCMB / `PRyMresults()[3]` convention |
| `06_generate_bbn_scorecard.py` | `data/imported_constants.json` | `results/bbn_scorecard_results.json` | corrected Y_p, D/H, Li-7 pulls and chi-square |
| `07_operator_algebra_live_theorem_artifacts.py` | `data/imported_constants.json` | `results/operator_algebra_live_theorem_artifacts_results.json` | optical filtration, branch assignment, local nontraciality, Wigner-Eckart boundary |
| `08_validate_expected_outputs.py` | `results/*.json` | stdout PASS/FAIL summary | frozen-output validation |

## Existing Scripts Used

The public scripts are distilled from the private Paper 21 support scripts and
frozen outputs:

- `paper21_ac1_opening_investigation_checks.py`
- `paper21_a4_bridge_theorem_checks.py`
- `paper21_two_formalization_theorems_analysis.py`
- `paper21_tio_branch_assignment_theorem_analysis.py`
- `paper21_pmultlift_tensor_weight_projection_analysis.py`
- `paper21_vNplus1_ypbbn_to_ypcmb_correction_audit.py`
- Paper 17 v1.5 R4/FIRAS readout correction artifacts

## Gaps Filled

- Added an explicit R4/FIRAS dependency audit because v2.0 inherits the
  Paper 17 v1.5 correction and must not preserve the retired R4 = 1 shorthand.
- Kept `L_1` and `L_2` as separate public scripts so each headline puncture
  load is independently auditable.
- Updated labels in public script outputs to the current canonical claim
  discipline. `DERIVED/SCOPED` and plain `CONDITIONAL/THEOREM` are not used as
  public bundle labels.

## Deferred / Excluded

- Historical `P_resp` dead-route reruns are excluded by PI instruction.
- The former `F_abs / Delta N_eff` investigation is excluded because v2.0
  retires it as active framework material.
- PRyMordial itself is not bundled; it remains an external solver.
- The bundle does not attempt to reproduce Paper 22's rate-dressing derivation.
  Paper 21 supplies `L_1` and `L_2`; later delivery into rate dressing is
  Paper 22/Paper 25 bridge structure.
