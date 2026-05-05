# Paper 25 v1.3 Construction Summary

This bundle was assembled from the active Paper 25 v1.2 manuscript state and
the private lab artifacts under `/opt/cosmology-lab/results/paper25/`.

The v1.3 support release adds public reproducibility infrastructure only. It
does not modify the manuscript physics chain.

## Script-to-Claim Mapping

- `01_v_vs_vprime_constants.py` verifies the reduced-gauge numerical constants:
  `K_gauge = ln(1+gamma^2)`, `V' = 2 gamma`, `V'' = 2(1+gamma^2)`, and the
  three weak amplitude branches.
- `02_core_theorem_ledger.py` verifies that the public support surface keeps
  the H1-H3 conditionals and Theorem 25.1-25.12 status labels visible.
- `03_two_time_correlator_closure.py` verifies the arithmetic of
  `Gamma_w(gamma)/Gamma_w(0) = (1+gamma^2) R(gamma)` with `R(gamma)=1` on the
  constructed extension.
- `04_bbn_branch_scorecards.py` verifies the active scorecard and comparators:
  active quadratic branch `chi2=1.0893566013769407`, linear comparator
  `chi2=1.991998955082098`, and V' branch `chi2=401.7433381288046`.
- `05_paper22_correction_boundary.py` verifies the weak-amplitude correction
  from `K_gauge*sqrt(L_1)` to `K_gauge*L_1`.
- `06_kappa_audit_summary.py` makes the kappa-audit verdict machine-readable:
  no hidden continuous fitted parameter found; visible H1-H3 conditionality.
- `07_validate_expected_outputs.py` reruns the public scripts and checks all
  frozen values.

## External Dependencies

The public validation path uses Python standard library only. It does not
redistribute PRyMordial, nuclear data files, or external observational data.
The audited PRyMordial rows are frozen as JSON values.

## Claim Boundary

The weak-sector identity pin is closed only inside H1-H3. The BBN scorecard is
computational verification of the selected branch, not proof of the branch.
The V' branch is excluded structurally by the centered two-time rate theorem
and numerically by the scorecard backstop.
