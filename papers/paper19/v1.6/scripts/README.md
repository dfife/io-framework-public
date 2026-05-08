# Paper 19 v1.6 Scripts

Run the quick validator first:

```bash
python3 scripts/11_validate_expected_outputs.py
```

The quick validator uses only frozen JSON outputs and the Python standard
library.

## Lightweight Scripts

- `01_bridge_theorems.py`: recomputes the alpha=3/2 bridge arithmetic.
- `02_modular_scalarization_audit.py`: checks that the modular echo is not a theorem.
- `03_bdp_domain_no_go.py`: verifies the path-average no-go for integration-domain tweaks.
- `09_r4_impact_audit.py`: writes the R4/FIRAS impact ledger.
- `10_kappa_audit_summary.py`: writes the machine-readable kappa-audit summary.
- `11_validate_expected_outputs.py`: validates frozen outputs.

## Heavy Optional Reruns

- `04_boss_fullshape_baryon_audit.py`: requires CAMB, numpy, and the public BOSS full-shape archive.
- `05_scalarization_jacobian.py`: requires sympy and script 04's CAMB/BOSS machinery.
- `06_corrected_scorecard.py`: requires CAMB, CLASS, scipy, numpy, BOSS data, and DESI BAO mean/covariance files supplied by the user.
- `07_self_consistent_background.py`: imports script 06 and has the same requirements.
- `08_bbn_scorecard.py`: requires an external PRyMordial checkout set via `PRYM_ROOT`.

External datasets are not redistributed. See `../data/external_data_sources.md`.

