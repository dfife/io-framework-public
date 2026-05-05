# Paper 25 v1.3 Reproducibility Bundle

This bundle supports Paper 25 v1.3 of the Interior Observer framework:
*The Weak-Sector Identity Pin / Quadratic Thermal Covariance, the
Channel-Budget Equation, and the V-vs-V' Class-Membership Theorem*.

The bundle reproduces the live scripted artifacts behind the paper:

- the V versus V' reduced-gauge constants;
- the H1-H3 premise ledger and active theorem/status ledger;
- the centered two-time correlator and quadratic weak-rate closure;
- the active Paper 24 final-push BBN scorecard used by Paper 25 v1.2/v1.3;
- the linear-branch and V' branch comparators;
- the kappa-style structural audit summary.

It does not rerun every private exploratory dead-route scan. Those scans remain
private lab provenance. The public bundle ships the live support surface needed
to check the manuscript's current numbers and claim labels.

## Quickstart

From the repository root:

```bash
python3 papers/paper25/v1.3/scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=22 pass_count=22 fail_count=0
```

## Detailed Reproduction

The numbered scripts can also be run one at a time from this bundle root:

```bash
python3 scripts/01_v_vs_vprime_constants.py
python3 scripts/02_core_theorem_ledger.py
python3 scripts/03_two_time_correlator_closure.py
python3 scripts/04_bbn_branch_scorecards.py
python3 scripts/05_paper22_correction_boundary.py
python3 scripts/06_kappa_audit_summary.py
```

Each script writes a frozen JSON file in `results/`. The validator reruns all
six scripts and checks the generated JSON outputs against the paper's current
live values.

## Claim Discipline

The Paper 25 v1.3 public claim boundary is:

- The centered two-time weak-rate correlator is `DERIVED/THEOREM` inside the
  stated CCR/KMS package.
- The weak-sector identity pin is conditional on H1-H3; Paper 25 does not claim
  unconditional physical selection outside those premises.
- The active weak amplitude is `epsilon_w = K_gauge * L_1`, correcting the old
  one-point/amplitude branch `K_gauge * sqrt(L_1)`.
- The BBN scorecard is `VERIFIED` computational support. The theorem selects
  the branch; PRyMordial verifies the consequence.
- The V' branch is structurally excluded by the two-time rate theorem and also
  catastrophically disfavored numerically. The numerical failure is a backstop,
  not the proof.

The corrected active scorecard uses `YPCMB / PRyMresults()[3]` for helium. The
old `YPBBN / PRyMresults()[4]` value is retained only in private audit logs.

## Dependencies

The public validation path uses Python standard library only. PRyMordial is
not redistributed in this bundle. The corrected PRyMordial output rows are
frozen in `data/imported_constants.json` with provenance to the local Paper 25
correction audit.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 25 v1.3*. Zenodo.

Associated release:

`paper25-v1.3`
