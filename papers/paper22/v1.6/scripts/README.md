# Paper 22 v1.6 Scripts

Run all checks with:

```bash
python3 scripts/07_validate_expected_outputs.py
```

The individual scripts are:

- `01_spatial_hodge_complex.py` - Hodge spectra, Peter-Weyl bridge, and framework constants.
- `02_tt_channel_floor.py` - TT branch multiplicities and `J_min=s` channel-floor law.
- `03_gauge_placement_and_channel_architecture.py` - homogeneous gauge placement and `j=1/j=2` channel architecture.
- `04_no_go_and_rate_paradigm_ledger.py` - live no-go/response ledger values; dead route scans are summarized, not rerun.
- `05_amplitude_scorecard_and_comparators.py` - Theorems 22.23/22.24 amplitude, scorecard, comparator, and Li-7 consistency arithmetic.
- `06_kappa_audit_summary.py` - compact machine-readable kappa-audit verdict.
- `07_validate_expected_outputs.py` - one-command referee validator.

These scripts use only the Python standard library. PRyMordial is not
redistributed in this bundle; the corrected YPCMB output row is frozen in
`data/imported_constants.json` with provenance.
