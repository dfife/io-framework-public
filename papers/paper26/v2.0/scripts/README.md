# Paper 26 v2.0 Scripts

Run scripts from the bundle root or run the public validator from the repository
root.

## Numbered Scripts

- `01_scalar_amplitude_chain.py`: recomputes the active scalar-amplitude
  arithmetic from explicit factors.
- `02_tensor_conditionals.py`: records the conditional tensor branch range and
  scope boundary.
- `03_cmb_baryon_class_diagnostic.py`: records baryon-class diagnostic values
  and frozen CLASS-support rows. It does not rerun CLASS.
- `04_tau_eff_and_damping.py`: recomputes `tau_eff`, the damping factor, and
  the C3 reduced source-covariance scope metadata.
- `05_reionization_shape_tt_check.py`: verifies the high-multipole
  temperature-temperature reionization-shape check.
- `06_kappa_audit_summary.py`: emits the machine-readable kappa-audit summary.
- `c2c_analysis/01_c2c_as_forward_check.py`: verifies forward arithmetic for
  the Hawking-state scalar-amplitude factor and guards against a retired
  squared-occupation expression.
- `07_validate_expected_outputs.py`: reruns all public scripts and checks the
  frozen JSON outputs.

## Scope

The scripts use Python standard-library arithmetic and the frozen constants in
`../data/imported_constants.json`. They do not fit parameters, do not use the
observed CMB temperature as a prediction target, and do not claim full CMB
closure.
