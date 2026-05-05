# Paper 22 v1.6 Bundle Construction Summary

Status: public bundle construction / verified

Date: 2026-05-04

## What Was Built

The bundle was assembled at:

`papers/paper22/v1.6/`

It follows the existing IO public-bundle convention:

- parent paper folder: `papers/paper22/`
- version folder: `papers/paper22/v1.6/`
- numbered scripts;
- frozen JSON outputs;
- report artifacts;
- one-command validator;
- immutable release tag `paper22-v1.6`.

## Script Inventory

Public scripts included:

- `01_spatial_hodge_complex.py`
- `02_tt_channel_floor.py`
- `03_gauge_placement_and_channel_architecture.py`
- `04_no_go_and_rate_paradigm_ledger.py`
- `05_amplitude_scorecard_and_comparators.py`
- `06_kappa_audit_summary.py`
- `07_validate_expected_outputs.py`

These scripts are fully documented internally with purpose, usage, claim
boundaries, and output paths.

## What The Scripts Reproduce

- Theorem 22.1 / 22.2 Hodge-spectrum support.
- Theorem 22.3 / 22.4 TT branch and channel-floor arithmetic.
- Theorem 22.5 homogeneous gauge placement support.
- Live no-go and rate-paradigm ledger values.
- Theorem 22.23 amplitude construction arithmetic.
- Theorem 22.24 Li-7 internal consistency arithmetic.
- Corrected v1.4/v1.5 YPCMB scorecard arithmetic.
- The paper-level and Theorem 22.23 kappa-audit verdicts.

## Deferred By Scope

The bundle does not publish every private exploratory route scan from Rounds
6-26. Those scans are no-go/provenance support and are represented in the audit
reports rather than being exposed as active public scripts.

The bundle also does not redistribute PRyMordial. It records the corrected
YPCMB output row and validates the arithmetic derived from it.

## Validation

Expected validation command:

```bash
python3 papers/paper22/v1.6/scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=20 pass_count=20 fail_count=0
```
