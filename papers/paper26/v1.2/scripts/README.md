# Paper 26 v1.2 Scripts

Run the validator first:

```bash
python3 scripts/07_validate_expected_outputs.py
```

Script roles:

- `01_scalar_amplitude_chain.py`: recomputes the conditional Hawking-boundary
  scalar-amplitude formula.
- `02_tensor_conditionals.py`: emits the conditional tensor branch numbers.
- `03_cmb_baryon_class_diagnostic.py`: emits frozen CLASS baryon-class
  diagnostic rows and the v1.1 legacy-row hygiene note.
- `04_tau_eff_and_damping.py`: recomputes `tau_eff = K_gauge/2` and
  `A_eff = A_s exp(-K_gauge)`.
- `05_reionization_shape_tt_check.py`: validates the high-l TT
  reionization-shape-insensitivity claim.
- `06_kappa_audit_summary.py`: emits a machine-readable audit verdict.
- `07_validate_expected_outputs.py`: reruns all scripts and checks expected
  values.
