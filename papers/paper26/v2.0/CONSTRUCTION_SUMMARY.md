# Paper 26 v2.0 Construction Summary

This bundle was assembled from the active Paper 26 v2.0 working draft and the
private lab artifacts under `/opt/cosmology-lab/results/paper26/`.

The v2.0 release adds public reproducibility infrastructure, R4/FIRAS hygiene,
C3 reduced source-covariance closure metadata, a kappa-style structural audit,
and canonical Claims Discipline labels. It does not modify the manuscript on
Zenodo.

## Script-to-Claim Mapping

- `01_scalar_amplitude_chain.py` verifies the scalar amplitude:
  `A_s = 2.0072459972737347e-9`, with claim status
  `DERIVED/CONDITIONAL_VERIFIED` on C1 and C2c.
- `02_tensor_conditionals.py` preserves the conditional tensor branch range:
  `r = 4.493164700207459e-4` to `6.35429445700943e-4`.
- `03_cmb_baryon_class_diagnostic.py` records the three baryon values and the
  frozen CLASS-support diagnostic rows.
- `04_tau_eff_and_damping.py` verifies `tau_eff = K_gauge/2`,
  `A_eff = A_s exp(-K_gauge)`, and the Theorem 26.C3 reduced-class scope.
- `05_reionization_shape_tt_check.py` verifies that the audited
  high-multipole temperature-temperature shape shift remains below
  `Delta chi2 = 0.4`.
- `06_kappa_audit_summary.py` makes the audit verdict machine-readable.
- `c2c_analysis/01_c2c_as_forward_check.py` verifies the forward arithmetic of
  the candidate C2c Hawking-state factor and records that the retired
  squared-occupation expression is not the active body formula.
- `07_validate_expected_outputs.py` reruns the public scripts and checks all
  frozen values.

## Important Hygiene Notes

The v2.0 manuscript draft mostly carries the Paper 17 v1.5 R4/FIRAS boundary,
but inherited appendix material still contains two stale thermal-readout
surfaces:

- Step 35 Piece 5 should use `ln(T_obs/T_IO) = R4_FIRAS K_gauge ln(x)`, not
  `K_gauge ln(x)`.
- Step 88 should use `T_obs(R4) = T_IO x^(R4 K_gauge)` with
  `R4 = R4_FIRAS`, and should not be worded as an independent CMB-temperature
  prediction.

The active body theorem says the scalar bridge reads `gamma delta K` and the
`delta Gamma` component vanishes. Step 383 still contains inherited wording
that appears to leave the Levi-Civita perturbation as the surviving bridge
variable; this should be reviewed in the manuscript pass.

The legacy `chi2=7714` clustering diagnostic is not the current local
reproducible typed-native row. The bundled comparable typed-native diagnostic
is `chi2=8133.4934835173035`.

## External Dependencies

The public validation path does not require CLASS or Planck likelihood files.
The relevant CLASS-support rows are frozen as audited JSON constants.
