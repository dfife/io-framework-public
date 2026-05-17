# Construction Summary

## Script Outputs

- `01_line_scale_root_uniqueness.py`
  - Output: `results/line_scale_root_uniqueness_results.json`.
  - Verifies: `q = 1/2` for primitive one-form line transport.

- `02_one_form_trace_log_extension.py`
  - Output: `results/one_form_trace_log_extension_results.json`.
  - Verifies: determinant trace-log shell law and pivot branch values.

- `03_dtn_hessian_spectral_index.py`
  - Output: `results/dtn_hessian_spectral_index_results.json`.
  - Verifies: coexact DtN shell law and pivot `n_s` values.

- `04_dtn_remainder_and_o1_exclusion.py`
  - Output: `results/dtn_remainder_and_o1_exclusion_results.json`.
  - Verifies: lower-order DtN remainder bound and flat-collar `O(1)`
    deformation exclusion.

- `05_jwst_clock_map.py`
  - Output: `results/jwst_clock_map_results.json`.
  - Verifies: homogeneous OS formation-clock map at redshifts 10, 12, 14, 17,
    and 20.

- `06_kappa_r4_audit_summary.py`
  - Output: `results/kappa_r4_audit_summary_results.json`.
  - Verifies: no active R4 damage and no active independent CMB-temperature
    prediction in the bundle.

- `07_validate_expected_outputs.py`
  - Output: pass/fail terminal report.
  - Verifies: every frozen output matches expected values.

## Exclusions

Retired CMB-temperature and mixed-fluid transfer artifacts are not included as
active scripts because they hardcode old CMB-temperature constants and do not
belong to the active Paper 28 v2.0 theorem-support bundle.
