# Paper 25 v2.0 Scripts

Run the validator first:

```bash
python3 scripts/07_validate_expected_outputs.py
```

From the repository root, use:

```bash
python3 papers/paper25/v2.0/scripts/07_validate_expected_outputs.py
```

Script roles:

- `01_v_vs_vprime_constants.py`: recomputes the reduced-gauge constants and
  weak-amplitude branches.
- `02_core_theorem_ledger.py`: emits the live theorem/status/premise ledger.
- `03_two_time_correlator_closure.py`: records the centered two-time weak-rate
  closure and R(gamma)=1 constructed-extension arithmetic.
- `04_bbn_branch_scorecards.py`: recomputes sigma-plane chi-square values from
  the frozen audited PRyMordial rows.
- `05_paper22_correction_boundary.py`: documents the Paper 22 weak-amplitude
  correction boundary.
- `06_kappa_audit_summary.py`: emits a compact machine-readable audit verdict.
- `07_validate_expected_outputs.py`: reruns all scripts and checks frozen
  outputs against the active Paper 25 v2.0 values.
