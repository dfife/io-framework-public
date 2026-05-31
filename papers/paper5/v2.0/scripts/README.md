# Scripts

Run from the bundle root:

```bash
python scripts/05_validate_expected_outputs.py
```

Script inventory:

- `01_kerr_spin_temperature.py` computes the Kerr surface-gravity temperature
  diagnostic.
- `02_vaidyano_go.py` records the Vaidya null-dust anisotropic-stress no-go
  diagnostic.
- `03_mixed_friedmann_bbn.py` recomputes active-branch expansion-rate ratios
  at BBN, recombination, and today.
- `04_inherited_claims.py` freezes Paper 5 dependency pointers into a local
  ledger.
- `05_validate_expected_outputs.py` regenerates and validates all frozen JSON
  outputs.
