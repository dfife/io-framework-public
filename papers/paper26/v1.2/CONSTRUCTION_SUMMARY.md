# Paper 26 v1.2 Construction Summary

This bundle was assembled from the active Paper 26 v1.1 manuscript state and
the private lab artifacts under `/opt/cosmology-lab/results/paper26/`.

The v1.2 support release adds public reproducibility infrastructure and a
kappa-style structural audit. It does not modify manuscript physics.

## Script-to-Claim Mapping

- `01_scalar_amplitude_chain.py` verifies the conditional scalar amplitude:
  `A_s = 2.0072459972737347e-9`.
- `02_tensor_conditionals.py` preserves the conditional tensor branch range:
  `r = 4.493164700207459e-4` to `6.35429445700943e-4`.
- `03_cmb_baryon_class_diagnostic.py` records the three baryon values and the
  current local CLASS diagnostic rows.
- `04_tau_eff_and_damping.py` verifies `tau_eff = K_gauge/2` and
  `A_eff = A_s exp(-K_gauge)`.
- `05_reionization_shape_tt_check.py` verifies that the audited high-l TT
  shape shift remains below `Delta chi2 = 0.4`.
- `06_kappa_audit_summary.py` makes the audit verdict machine-readable.
- `07_validate_expected_outputs.py` reruns the public scripts and checks all
  frozen values.

## Important Hygiene Note

The active v1.1 body text and inherited Step-style material are not fully
aligned on the bridge-variable phrasing. The bundle uses the v1.1 body theorem
as active and flags the inherited wording as a v1.2 manuscript hygiene item.

The v1.1 text also contains a legacy `chi2=7714` clustering diagnostic. The
current local reproducible artifact shipped here gives `chi2=8133.4934835173035`
for the comparable typed-native route. v1.2 should either update the manuscript
to the bundled row or explicitly label the legacy row.

## External Dependencies

The public validation path does not require CLASS or Planck likelihood files.
The relevant CLASS rows are frozen as audited JSON constants.
