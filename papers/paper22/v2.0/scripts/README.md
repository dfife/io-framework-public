# Paper 22 v2.0 Scripts

Run the validator first:

```bash
python3 scripts/08_validate_expected_outputs.py
```

The individual scripts are:

- `01_r4_firas_dependency_audit.py` - records the Paper 17 v1.5 R4/FIRAS repair and verifies that Paper 22's active BBN scorecard does not depend on R4.
- `02_spatial_hodge_complex.py` - reproduces round-S3 Hodge spectra, Peter-Weyl bridge data, and framework constants.
- `03_tt_channel_floor.py` - reproduces transverse-traceless tensor branch multiplicities and channel-floor arithmetic.
- `04_gauge_placement_and_channel_architecture.py` - reproduces homogeneous gauge placement and channel architecture checks.
- `05_no_go_and_rate_paradigm_ledger.py` - reproduces live no-go and rate-paradigm ledger values.
- `06_amplitude_scorecard_and_comparators.py` - reproduces Theorems 22.23/22.24 amplitude, scorecard, comparator, and Li-7 consistency arithmetic.
- `07_kappa_audit_summary.py` - emits a compact machine-readable kappa-audit verdict.
- `08_validate_expected_outputs.py` - reruns every script and validates expected outputs.

All scripts use only the Python standard library. They are intentionally
compact so a non-IO reader can inspect the formulas and frozen inputs without
using the private exploratory lab.
