# Paper 25 v2.0 Bundle Manifest

## Top-Level Files

- `README.md`: bundle overview, quickstart, claim boundary, citation.
- `MANIFEST.md`: this inventory.
- `VERSION.md`: paper and bundle version metadata.
- `CITATION.cff`: machine-readable citation metadata.
- `LICENSE`: reuse and attribution note.
- `CONSTRUCTION_SUMMARY.md`: construction notes and script-to-claim mapping.
- `INVENTORY_REPORT.md`: inventory of included and excluded artifacts.
- `SHA256SUMS.txt`: SHA256 checksums for bundle files.

## Data

- `data/imported_constants.json`: framework constants, R4/FIRAS boundary,
  amplitudes, observational denominators, active BBN scorecards, and H1-H3
  premise text.
- `data/external_data_sources.md`: external-data and PRyMordial redistribution
  boundary.

## Environment

- `environment/requirements.txt`: Python dependency note.
- `environment/python_version.txt`: recommended Python version.
- `environment/apt_packages.txt`: system-package note.
- `environment/environment_seed.md`: random-seed note.
- `environment/external_dependencies.md`: dependency boundary note.

## Scripts

- `scripts/01_v_vs_vprime_constants.py`: recomputes V, V', V'', and weak
  amplitude branches.
- `scripts/02_core_theorem_ledger.py`: emits the live theorem/status/premise
  ledger through Theorem 25.13.
- `scripts/03_two_time_correlator_closure.py`: records the two-time rate
  closure and `R(gamma)=1` arithmetic.
- `scripts/04_bbn_branch_scorecards.py`: recomputes sigma-plane chi-square
  values from frozen audited BBN rows.
- `scripts/05_paper22_correction_boundary.py`: documents the Paper 22 weak
  amplitude correction.
- `scripts/06_kappa_audit_summary.py`: emits the compact v2.0 R4/kappa audit
  verdict.
- `scripts/07_validate_expected_outputs.py`: one-command validation entrypoint.
- `scripts/README.md`: script index.

## Results

- `results/v_vs_vprime_constants_results.json`
- `results/core_theorem_ledger_results.json`
- `results/two_time_correlator_closure_results.json`
- `results/bbn_branch_scorecards_results.json`
- `results/paper22_correction_boundary_results.json`
- `results/kappa_audit_summary_results.json`

## Reports

- `reports/paper25_v20_r4_kappa_audit_report.md`
- `reports/paper25_v20_r4_kappa_audit_results.json`
- `reports/paper25_kappa_audit_report.md`
- `reports/paper25_kappa_audit_results.json`
- `reports/paper25_v12_ypbbn_to_ypcmb_correction_memo.md`
- `reports/paper25_v12_ypbbn_to_ypcmb_correction_results.json`
- `reports/paper25_quadratic_weak_paper24_lithium_check_report.txt`
- `reports/paper25_quadratic_weak_paper24_lithium_check_results.json`
- `reports/paper25_v_vs_vprime_class_membership_report.txt`
- `reports/paper25_v_vs_vprime_class_membership_results.json`
- `reports/paper25_weak_two_time_correlator_report.txt`
- `reports/paper25_weak_two_time_correlator_results.json`
- `reports/paper25_vprime_bbn_catastrophe_and_last_angles_report.txt`
- `reports/paper25_vprime_bbn_catastrophe_and_last_angles_results.json`

## Validation

Validator command from repository root:

```bash
python3 papers/paper25/v2.0/scripts/07_validate_expected_outputs.py
```

Expected summary:

```text
SUMMARY total_checks=27 pass_count=27 fail_count=0
```
