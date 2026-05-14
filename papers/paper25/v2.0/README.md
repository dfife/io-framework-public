# Paper 25 v2.0 Reproducibility Bundle

This bundle supports Paper 25 v2.0 of the Interior Observer framework:
*The Weak-Sector Identity Pin / Quadratic Thermal Covariance, the
Channel-Budget Equation, and the V-vs-V' Class-Membership Theorem*.

The v2.0 bundle updates the public support package to the Paper 24 v3.0
Pastore `Q_GS` lithium branch and records the Paper 17 v1.5 R4/FIRAS repair
boundary. The active Paper 25 scripts do not use `R4`; observed CMB temperature
is not counted as an independent IO prediction.

## Quickstart

From the repository root:

```bash
python3 papers/paper25/v2.0/scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=27 pass_count=27 fail_count=0
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
six scripts and checks the generated JSON outputs against the Paper 25 v2.0
live values.

## Claim Discipline

The Paper 25 v2.0 public claim boundary is:

- The centered two-time weak-rate correlator is `DERIVED/THEOREM` inside the
  stated canonical-commutation-relation / Kubo-Martin-Schwinger package.
- The weak-sector identity pin is `DERIVED/CONDITIONAL_VERIFIED` on H1-H3.
  Paper 25 does not claim unconditional physical selection outside those
  premises.
- The active weak amplitude is `epsilon_w = K_gauge * L_1`, correcting the old
  one-point/amplitude branch `K_gauge * sqrt(L_1)`.
- The BBN scorecard is `VERIFIED` computational support. The theorem selects
  the branch; the frozen PRyMordial rows verify the consequence.
- The V' branch is structurally excluded by the two-time rate theorem and also
  catastrophically disfavored numerically. The numerical failure is a backstop,
  not the proof.
- `R4_FIRAS = 1.0031014644` is recorded for dependency hygiene only. It is not
  an active Paper 25 variable.

## Active Headline Values

- `epsilon_w = K_gauge * L_1 = 0.012300778733811872`
- `epsilon_n = (<K>/10) * L_2 = 0.02384221534546833`
- `D/H = 2.5072097840055007e-5 (-0.659673866483311 sigma)`
- `Y_p = 0.24770877182909237 (+0.6771929572730941 sigma)`
- `Li-7/H = 1.7414708079857392e-10 (+0.520873574147546 sigma)`
- `chi2(D/H + Y_p + Li-7) = 1.1650691917465592` (`1.17` rounded)

## Dependencies

The public validation path uses Python standard library only. PRyMordial is
not redistributed in this bundle. The audited PRyMordial output rows are frozen
in `data/imported_constants.json` with provenance to Paper 24 v3.0 and local
Paper 25 audit artifacts.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 25 v2.0*. Zenodo.

Associated release:

`paper25-v2.0`
