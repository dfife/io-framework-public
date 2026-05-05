# Paper 22 v1.6 Reproducibility Bundle

This bundle supports Paper 22 v1.6 of the Interior Observer framework:
*The Spatial Hodge Complex and the Rate-Dressing Bridge*.

The bundle reproduces the live scripted artifacts behind the paper:

- round-S3 Hodge spectra and Peter-Weyl bridge;
- TT branch multiplicities and the Channel Floor Theorem;
- homogeneous gauge placement and channel architecture;
- live no-go and rate-paradigm ledger values;
- corrected YPCMB BBN scorecard arithmetic;
- Theorem 22.23/22.24 amplitude, comparator, and Li-7 consistency arithmetic;
- kappa-style structural audit verdicts.

It does not rerun every private exploratory dead-route scan. Those scans remain
provenance and no-go support in the private lab and in the shipped audit
reports, not active public theorem evidence.

## Quickstart

From the repository root:

```bash
python3 papers/paper22/v1.6/scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=20 pass_count=20 fail_count=0
```

## Detailed Reproduction

The numbered scripts can also be run one at a time from this bundle root:

```bash
python3 scripts/01_spatial_hodge_complex.py
python3 scripts/02_tt_channel_floor.py
python3 scripts/03_gauge_placement_and_channel_architecture.py
python3 scripts/04_no_go_and_rate_paradigm_ledger.py
python3 scripts/05_amplitude_scorecard_and_comparators.py
python3 scripts/06_kappa_audit_summary.py
```

Each script writes a frozen JSON file in `results/`. The validator reruns all
six scripts and checks the generated JSON outputs against the paper's current
live values.

## Claim Discipline

The Paper 22 v1.6 public claim boundary is:

- The spatial Hodge/TT/channel infrastructure is `DERIVED/THEOREM` inside the
  IO OS spatial-slice scope.
- The energy-density injection and full-radiation routes are killed by no-go
  results; `F_abs` is not an active Friedmann/radiation-density correction.
- The zero-parameter amplitude construction is
  `DERIVED/CONDITIONAL on GMP + TBS`, with weak payload closure inherited from
  `WMR(H1-H3)`.
- The formal bridge operator is conditional; Paper 22 does not claim an
  unconditional derivation of `P_resp`.

The corrected active scorecard uses `YPCMB / PRyMresults()[3]` for helium.
The old `YPBBN / PRyMresults()[4]` value is retained only as an audit field.

## Dependencies

The public validation path uses Python standard library only. PRyMordial is
not redistributed in this bundle. The corrected PRyMordial output row is frozen
in `data/imported_constants.json` with provenance to the local correction audit.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 22 v1.5*. Zenodo.
https://doi.org/10.5281/zenodo.19198706

Associated release:

`paper22-v1.6`
