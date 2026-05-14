# Paper 25 v2.0 Construction Summary

This bundle was assembled from the Paper 25 v2.0 working draft and the lab
artifacts under `/opt/cosmology-lab/results/paper25/`, with the active BBN
support row imported from the public Paper 24 v3.0 bundle.

The v2.0 support release changes the public bundle from the v1.3 Henderson-only
support row to the Paper 24 v3.0 Pastore `Q_GS` branch and adds an explicit
R4/FIRAS damage audit.

## Script-to-Claim Mapping

- `01_v_vs_vprime_constants.py` verifies the reduced-gauge numerical constants:
  `K_gauge = ln(1+gamma^2)`, `V' = 2 gamma`, `V'' = 2(1+gamma^2)`, and the
  three weak amplitude branches.
- `02_core_theorem_ledger.py` verifies that the public support surface keeps
  H1-H3 and Theorems 25.1-25.13 visible under canonical Claims Discipline
  labels.
- `03_two_time_correlator_closure.py` verifies the arithmetic of
  `Gamma_w(gamma)/Gamma_w(0) = (1+gamma^2) R(gamma)` with `R(gamma)=1` on the
  constructed extension.
- `04_bbn_branch_scorecards.py` verifies the active Paper 24 v3.0 Pastore
  branch scorecard and comparators: active quadratic branch
  `chi2=1.1650691917465592`, linear comparator `chi2=1.991998955082098`, and
  V' branch `chi2=401.7433381288046`.
- `05_paper22_correction_boundary.py` verifies the weak-amplitude correction
  from `K_gauge*sqrt(L_1)` to `K_gauge*L_1`.
- `06_kappa_audit_summary.py` makes the v2.0 kappa/R4 audit verdict
  machine-readable: no hidden continuous fitted parameter found in the active
  weak-sector support surface, and no active Paper 25 script uses R4.
- `07_validate_expected_outputs.py` reruns the public scripts and checks all
  frozen values.

## External Dependencies

The public validation path uses Python standard library only. It does not
redistribute PRyMordial, nuclear data files, or external observational data.
The audited PRyMordial rows are frozen as JSON values.

## Claim Boundary

The weak-sector identity pin is closed only inside H1-H3 and is therefore
`DERIVED/CONDITIONAL_VERIFIED`. The BBN scorecard is computational verification
of the selected branch, not proof of the branch. The V' branch is excluded
structurally by the centered two-time rate theorem and numerically by the
scorecard backstop.
