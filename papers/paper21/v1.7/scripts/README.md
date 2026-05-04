# Scripts

Run order:

```bash
python3 scripts/01_derive_L1_puncture_load.py
python3 scripts/02_derive_L2_puncture_load.py
python3 scripts/03_compute_ac1_closure.py
python3 scripts/04_prymordial_wrapper_conventions.py
python3 scripts/05_generate_bbn_scorecard.py
python3 scripts/06_operator_algebra_live_theorem_artifacts.py
python3 scripts/07_validate_expected_outputs.py
```

The validator is the referee entry point. It checks every frozen output against
the expected Paper 21 v1.7 values and exits nonzero on failure.

All scripts use only Python standard-library modules.
