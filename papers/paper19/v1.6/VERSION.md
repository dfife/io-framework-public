# Version

Paper: Paper 19

Bundle version: v1.6

Bundle date: May 2026

Release tag: `paper19-v1.6`

Primary repair:

- Paper 17 v1.5 R4/FIRAS observer-side readout normalization inherited.
- Retired independent CMB-temperature prediction language.
- Paper 19 support scripts updated from implicit `R4=1` / `T0=2.7253 K` to
  `R4_FIRAS=1.0031014644` and `T_FIRAS=2.7255 K`.
- Kappa-style audit added, including hidden-fitted-parameter and label-discipline checks.

Validation command:

```bash
python3 scripts/11_validate_expected_outputs.py
```

