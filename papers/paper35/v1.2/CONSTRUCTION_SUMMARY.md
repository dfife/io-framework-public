# Paper 35 v1.2 Bundle Construction Summary

## Script Inventory

| Script | Inputs | Outputs | Manuscript values verified | External dependencies |
|---|---|---|---|---|
| `01_eta_derivation_chain.py` | `data/imported_constants.json` | `results/eta_derivation_chain_results.json` | `eta_late = 5.747543733e-10`, `f_b = 0.3127083362`, `R4_FIRAS = 1.0031014644` | Standard constants only; FIRAS value imported as empirical thermal datum |
| `02_temperature_assignment.py` | `data/imported_constants.json` | `results/temperature_assignment_results.json` | `x_R4_source^(3 R4 K_gauge) = 1.0714710854`, `eta_BBN = 6.150846821e-10` | Standard constants only |
| `03_chiral_source_diagnostic.py` | `data/imported_constants.json` | `results/chiral_source_diagnostic_results.json` | `g_chi = K_gauge^4`, `eta_chiral = 5.786697164e-10`, chiral diagnostic `T_f = 2.2003938597e13 GeV` | Standard diagnostic convention only |
| `04_leptogenesis_target_reduction.py` | `data/imported_constants.json` | `results/leptogenesis_target_reduction_results.json` | `Y_B = 8.164124621e-11`, `epsilon1*kappa = 5.904012330e-8`, eta-derived Poplawski target scale `2.2001575354e13 GeV` | Standard leptogenesis formulas; no data files |
| `05_baryogenesis_registry_summary.py` | `data/theorem_registry.json` | `results/baryogenesis_registry_summary_results.json` | 48 theorem surfaces: 15 CLEAN, 33 CONDITIONAL_VERIFIED | None |
| `06_jwst_formation_time_table.py` | `data/imported_constants.json` | `results/jwst_formation_time_table_results.json` | z=10 ratio `1.4785718590`; JADES z=14 delta `135.7854547 Myr` | Cited JWST papers only; no data products |
| `07_desi_confrontation.py` | `data/imported_constants.json`; public DESI mean/cov URLs | `results/desi_confrontation_results.json` | active raw GCcomb chi2 = 69.484808933; flat-CPL fixed point `w0=-1.030263`, `wa=-0.111508` | Fetches public DESI files; checks SHA256; does not redistribute |
| `08_dark_matter_null_forecast.py` | `data/imported_constants.json` | `results/dark_matter_null_forecast_results.json` | `f_b = 0.3127083362`; LZ/XENONnT/PandaX cited limits | Cited limit papers/pages only; no data products |
| `09_r4_firas_impact_audit.py` | `data/imported_constants.json`; `results/*.json` | `results/r4_firas_impact_audit_results.json` | R4 blast-radius ledger, old/new eta and target values, CMB-prediction hygiene verdict | None |
| `10_validate_expected_outputs.py` | `results/*.json` | stdout PASS/FAIL summary | all headline checks; `SUMMARY total_checks=38 pass_count=38 fail_count=0` | None |

## Reports Included

- `reports/paper35_v12_r4_firas_kappa_audit_report.md`
- `reports/paper35_v12_r4_firas_kappa_audit_results.json`
- `reports/paper35_kappa_audit_report.md` retained as v1.1 historical audit artifact with v1.2 note
- `reports/paper35_kappa_audit_results.json` retained as v1.1 historical audit artifact with v1.2 note
- `reports/paper35_conditional_verified_audit_results.md`
- `reports/paper35_conditional_verified_audit_results.json`
- `reports/theorem_registry/`: 48 theorem-surface report/result pairs plus index. The registry contains v1.2 notes where older numeric target values are historical.

## Discipline Notes

- Paper 35 v1.2 does not claim an independent CMB-temperature prediction.
- R4 is inherited from Paper 17 v1.5 as a FIRAS-fixed empirical readout normalization and is frozen before Paper 35 calculations.
- The 33 `CONDITIONAL_VERIFIED` theorem surfaces are not unconditional proof.
- External datasets are cited/fetched/checksummed, not redistributed.
- Standard-literature formulas are cited and numerically evaluated only where Paper 35 uses the result.
- Script 08 is a consistency check, not a new dark-matter forecast model.
