# Paper 35 v1.1 Scripts

Run from the bundle root:

```bash
python3 scripts/09_validate_expected_outputs.py
```

Full regeneration order:

```bash
python3 scripts/01_eta_derivation_chain.py
python3 scripts/02_temperature_assignment.py
python3 scripts/03_chiral_source_diagnostic.py
python3 scripts/04_leptogenesis_target_reduction.py
python3 scripts/05_baryogenesis_registry_summary.py
python3 scripts/06_jwst_formation_time_table.py
python3 scripts/07_desi_confrontation.py
python3 scripts/08_dark_matter_null_forecast.py
python3 scripts/09_validate_expected_outputs.py
```

`07_desi_confrontation.py` fetches public DESI DR2 files at runtime and checks
SHA256. No external data files are redistributed.

Every script writes one frozen JSON output into `results/`.
