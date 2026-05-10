# Paper 22 v2.0 Bundle Construction Summary

## Scope

This bundle supports Paper 22 v2.0. It is a repair and reproducibility update
over the v1.6 bundle.

Changes relative to v1.6:

- Added a dedicated R4/FIRAS dependency audit script.
- Updated constants metadata to record `R4_FIRAS = 1.0031014644`.
- Confirmed Paper 22's active Big Bang nucleosynthesis scorecard is not
  R4-dependent.
- Updated public claim labels to the current canonical Claims Discipline set.
- Shipped the v2.0 R4/kappa audit report and JSON.

## Bundle Location

`papers/paper22/v2.0/`

## Scripts

- `01_r4_firas_dependency_audit.py`
- `02_spatial_hodge_complex.py`
- `03_tt_channel_floor.py`
- `04_gauge_placement_and_channel_architecture.py`
- `05_no_go_and_rate_paradigm_ledger.py`
- `06_amplitude_scorecard_and_comparators.py`
- `07_kappa_audit_summary.py`
- `08_validate_expected_outputs.py`

## Live Values Covered

- `R4_FIRAS = 1.0031014644`, imported from Paper 17 v1.5.
- `x = 1.51899780195519`.
- `K_gauge = 0.05487281774291466`.
- `epsilon_w = 0.012300778733811872`.
- `epsilon_n = 0.02384221534546833`.
- `D/H_sigma = -0.5529801681809717`.
- `Y_p_sigma = +0.7045360432106975`.
- `chi2(D/H + Y_p) = 0.8021581025844415`.
- `Li7/H = 5.363335812718549e-10`.
- `Li7_sigma = +12.204309073285641`.
- `two-parameter comparator chi2(D/H + Y_p) = 1.9345853017600352`.
- `Li-7 uniform benchmark fractional difference = 0.005093424637516164`.

## Deferred / Not Bundled

- Private exploratory dead-route scans are not rerun.
- PRyMordial is not redistributed.
- Superseded appendix rows are reported in the audit as manuscript-cleanup
  targets; they are not treated as active bundle outputs.

## Validation Command

```bash
python3 papers/paper22/v2.0/scripts/08_validate_expected_outputs.py
```

Expected:

```text
SUMMARY total_checks=23 pass_count=23 fail_count=0
```
