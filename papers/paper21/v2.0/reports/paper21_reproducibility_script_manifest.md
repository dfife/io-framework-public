# Paper 21 v2.0 Reproducibility Script Manifest

Status: `VERIFIED / public-candidate filter applied`

Date: 2026-05-09

Boundary: the Paper 21 v2.0 public reproducibility bundle includes only scripts
that directly reproduce a live numerical value, theorem-support artifact, or
corrected scorecard claim appearing in the v2.0 draft. Retired routes are not
included.

## Included in Public Bundle

| Public script | Local provenance | Direct manuscript trace |
|---|---|---|
| `01_r4_firas_dependency_audit.py` | Paper 17 v1.5 R4/FIRAS repair artifacts | R4 dependency audit; confirms active Paper 21 BBN uses `T_IO`, not `T_obs` |
| `02_derive_L1_puncture_load.py` | `paper21_sharpening_03622_analysis.py` | `L_1 = 0.22417` |
| `03_derive_L2_puncture_load.py` | `paper21_sharpening_03622_analysis.py` | `L_2 = 0.13805` |
| `04_compute_ac1_closure.py` | `paper21_ac1_opening_investigation_checks.py`, `paper21_a4_bridge_theorem_checks.py` | AC1 Reduction Theorem; `J_theta = x^(-1/2) sqrt(1 + gamma^2)` |
| `05_prymordial_wrapper_conventions.py` | `paper21_vNplus1_ypbbn_to_ypcmb_correction_audit.py` | YPCMB / `PRyMresults()[3]` convention |
| `06_generate_bbn_scorecard.py` | `paper21_vNplus1_ypbbn_to_ypcmb_correction_audit.py` | corrected Y_p, D/H, Li-7 pulls and chi-square |
| `07_operator_algebra_live_theorem_artifacts.py` | `paper21_tio_branch_assignment_theorem_analysis.py`, `paper21_pmultlift_tensor_weight_projection_analysis.py`, `paper21_two_formalization_theorems_analysis.py` | optical filtration, branch assignment, local nontraciality, Wigner-Eckart boundary |
| `08_validate_expected_outputs.py` | bundle validator | frozen-output validation |

## Excluded by v2.0 Scope

The following local script families are not included because their corresponding
manuscript material was retired or superseded in v2.0:

- radiation-response route scans,
- `F_abs / Delta N_eff` route scripts,
- `P_resp` exploratory scripts,
- assembly-gap and bare-branch diagnostics,
- stiff-dilution and local-expansion variance reruns,
- nonseparable weak-sector route scans.

## Bundle Framing Rule

The active Paper 21 artifacts are:

```text
R4/FIRAS dependency audit
AC1/acoustic closure
SU(2) puncture partition and L_1/L_2 load derivation
T_IO branch assignment
local nontraciality / optical fixed-point theorem artifacts
YPCMB wrapper convention and scorecard arithmetic
```

The bundle should not present retired radiation-response route scripts as
active Big Bang nucleosynthesis evidence.
