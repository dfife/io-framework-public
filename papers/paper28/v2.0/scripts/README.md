# Script Inventory

Run the validation entry point:

```bash
python3 scripts/07_validate_expected_outputs.py
```

- `01_line_scale_root_uniqueness.py` checks the primitive line-scale root
  uniqueness result.
- `02_one_form_trace_log_extension.py` records the one-form trace-log Gaussian
  extension and pivot spectral-index values.
- `03_dtn_hessian_spectral_index.py` records the coexact DtN Hessian
  spectral-index chain.
- `04_dtn_remainder_and_o1_exclusion.py` validates the lower-order DtN
  remainder bound and flat-collar O(1) deformation exclusion.
- `05_jwst_clock_map.py` computes the homogeneous Oppenheimer-Snyder JWST
  formation-clock map.
- `06_kappa_r4_audit_summary.py` records the R4 and hidden-parameter audit
  disposition.
- `07_validate_expected_outputs.py` reruns all prior scripts and checks frozen
  outputs.
