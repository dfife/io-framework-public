# Paper 22 v2.0 Reproducibility Bundle

This bundle supports Paper 22 v2.0 of the Interior Observer framework:
*The Spatial Hodge Complex and the Rate-Dressing Bridge*.

It reproduces the live scripted artifacts behind the paper:

- R4/FIRAS dependency audit inherited from Paper 17 v1.5;
- round-S3 Hodge spectra and Peter-Weyl bridge;
- transverse-traceless tensor branch multiplicities and Channel Floor Theorem arithmetic;
- homogeneous gauge placement and channel architecture;
- live no-go and rate-paradigm ledger values;
- corrected YPCMB Big Bang nucleosynthesis scorecard arithmetic;
- Theorem 22.23/22.24 amplitude, comparator, and Li-7 consistency arithmetic;
- kappa-style structural audit verdicts.

It does not rerun private exploratory dead-route scans. Those scans remain
provenance and no-go support in the private lab and in the shipped audit
reports, not active public theorem evidence.

## Quickstart

From the repository root:

```bash
python3 papers/paper22/v2.0/scripts/08_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=23 pass_count=23 fail_count=0
```

## Detailed Reproduction

The numbered scripts can also be run one at a time from this bundle root:

```bash
python3 scripts/01_r4_firas_dependency_audit.py
python3 scripts/02_spatial_hodge_complex.py
python3 scripts/03_tt_channel_floor.py
python3 scripts/04_gauge_placement_and_channel_architecture.py
python3 scripts/05_no_go_and_rate_paradigm_ledger.py
python3 scripts/06_amplitude_scorecard_and_comparators.py
python3 scripts/07_kappa_audit_summary.py
```

Each script writes a frozen JSON file in `results/`. The validator reruns all
seven computational scripts and checks the generated JSON outputs against the
paper's current live values.

## Claim Discipline

The Paper 22 v2.0 public claim boundary is:

- The spatial Hodge/TT/channel infrastructure is `DERIVED/THEOREM` inside the
  closed Oppenheimer-Snyder spatial-slice scope.
- The energy-density injection and full-radiation routes are killed by no-go
  results; `F_abs` is not an active Friedmann/radiation-density correction.
- The zero-parameter amplitude construction is
  `DERIVED/CONDITIONAL_VERIFIED` on `GMP + TBS`, with weak payload closure
  inherited from `WMR(H1-H3)`.
- `GMP` and `TBS` remain `OPEN/PREMISE_GAP` fields, not unconditional
  theorems.
- The formal bridge operator is conditional; Paper 22 does not claim an
  unconditional derivation of `P_resp`.
- The independent CMB-temperature prediction is retired. FIRAS fixes
  `R4_FIRAS = 1.0031014644` in Paper 17 v1.5. Paper 22's active BBN scorecard
  does not depend on R4.

The corrected active scorecard uses `YPCMB / PRyMresults()[3]` for helium.
The old `YPBBN / PRyMresults()[4]` value is retained only as an audit field.

## Dependencies

The public validation path uses Python standard library only. PRyMordial is
not redistributed in this bundle. The corrected PRyMordial output row is frozen
in `data/imported_constants.json` with provenance to the local correction audit.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 22 v2.0*. Zenodo.
https://doi.org/10.5281/zenodo.19198706

Associated release:

`paper22-v2.0`
