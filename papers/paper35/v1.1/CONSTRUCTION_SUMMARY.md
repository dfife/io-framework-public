# Paper 35 v1.1 Bundle Construction Summary

## Script Inventory

| Script | Inputs | Outputs | Manuscript values verified | External dependencies |
|---|---|---|---|---|
| `01_eta_derivation_chain.py` | `data/imported_constants.json` | `results/eta_derivation_chain_results.json` | `eta_late = 5.748778515e-10`, `f_b = 0.3127083362` | Standard constants only; no external dataset |
| `02_temperature_assignment.py` | `data/imported_constants.json` | `results/temperature_assignment_results.json` | `x^(3K_gauge) = 1.0712409439`, `eta_BBN = 6.150846821e-10` | Standard constants only |
| `03_chiral_source_diagnostic.py` | `data/imported_constants.json` | `results/chiral_source_diagnostic_results.json` | `g_chi = K_gauge^4`, `eta_chiral = 5.786697164e-10`, `T_f = 2.2003938597e13 GeV` | Standard diagnostic convention only |
| `04_leptogenesis_target_reduction.py` | `data/imported_constants.json` | `results/leptogenesis_target_reduction_results.json` | `Y_B = 8.165878573e-11`, `epsilon1*kappa = 5.905280727e-8` | Standard leptogenesis formulas; no data files |
| `05_baryogenesis_registry_summary.py` | `data/theorem_registry.json` | `results/baryogenesis_registry_summary_results.json` | 48 theorem surfaces: 15 CLEAN, 33 CONDITIONAL_VERIFIED | None |
| `06_jwst_formation_time_table.py` | `data/imported_constants.json` | `results/jwst_formation_time_table_results.json` | 46-48% high-z timing relief; object timing rows | Cited JWST papers only; no data products |
| `07_desi_confrontation.py` | `data/imported_constants.json`; public DESI mean/cov URLs | `results/desi_confrontation_results.json` | active raw GCcomb chi2 = 69.484808933; flat-CPL fixed point `w0=-1.030263`, `wa=-0.111508` | Fetches public DESI files; checks SHA256; does not redistribute |
| `08_dark_matter_null_forecast.py` | `data/imported_constants.json` | `results/dark_matter_null_forecast_results.json` | `f_b = 0.3127083362`; LZ/XENONnT/PandaX cited limits | Cited limit papers/pages only; no data products |
| `09_validate_expected_outputs.py` | `results/*.json` | stdout PASS/FAIL summary | all headline checks | None |

## Reports Included

- `reports/paper35_kappa_audit_report.md`
- `reports/paper35_kappa_audit_results.json`
- `reports/paper35_conditional_verified_audit_results.md`
- `reports/paper35_conditional_verified_audit_results.json`
- `reports/theorem_registry/`: 48 theorem-surface report/result pairs plus index.

## Discipline Notes

- The 33 `CONDITIONAL_VERIFIED` theorem surfaces are not unconditional proof.
- External datasets are cited/fetched/checksummed, not redistributed.
- Standard-literature formulas are cited and numerically evaluated only where
  Paper 35 uses the result.
- Script 08 is a consistency check, not a new dark-matter forecast model.
