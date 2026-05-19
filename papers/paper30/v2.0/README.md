# Paper 30 v2.0 Reproducibility Bundle

This bundle reproduces the active Paper 30 v2.0 twenty-test confrontation on the Paper 29 projection branch.

Run:

```bash
python3 scripts/02_validate_expected_outputs.py
```

The validator reruns `scripts/01_full_twenty_test_recompute.py`, regenerates `results/full_twenty_test_recompute_results.json`, and checks the headline numerical claims used by the manuscript.

R4/FIRAS boundary: Paper 30 does not fit or vary R4. The bundle records `R4_FIRAS = 1.0031014644` as an inherited dependency boundary and uses the FIRAS-fixed observer thermal datum `T_CMB = 2.7253 K` where thermal radiation density or high-redshift temperature propagation enters.

Historical `funrun_*` JSON files included under `data/legacy_context/` are comparison context only. They are not active theorem support and are not used as live branch constants.
