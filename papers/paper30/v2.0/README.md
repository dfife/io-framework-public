# Paper 30 v2.0 Reproducibility Bundle

This bundle reproduces the active Paper 30 v2.0 twenty-test confrontation on the Paper 29 projection branch.

Run:

```bash
python3 scripts/02_validate_expected_outputs.py
```

The default validator checks the frozen output against the headline numerical claims used by the manuscript. To regenerate the frozen output first, run:

```bash
python3 scripts/02_validate_expected_outputs.py --recompute
```

R4/FIRAS boundary: Paper 30 does not fit or vary R4. The bundle records `R4_FIRAS = 1.0031014644` as an inherited dependency boundary and uses the FIRAS-fixed observer thermal datum `T_CMB = 2.7253 K` where thermal radiation density or high-redshift temperature propagation enters.

Historical `funrun_*` JSON files included under `data/legacy_context/` are comparison context only. They are not active theorem support and are not used as live branch constants.

AP residual tightening: `results/paper30_v2_0_AP_residual_analysis.md` records the post-tightening Alcock-Paczynski residual/leverage analysis for Section 3.4. The validator checks the AP probability-to-exceed values at `dof = 6` for both fixed-parameter models (`p_IO = 0.247`, `p_Planck = 0.349`), the six AP model values for both IO and Planck, the six diagonal AP uncertainties, the six IO full-covariance chi-square contributions, and the six jackknife `Delta chi2` values.
