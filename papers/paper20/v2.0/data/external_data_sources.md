# External Data Sources

This bundle does not redistribute external observational datasets.

- FIRAS cosmic microwave background temperature: Fixsen 2009,
  `T_CMB = 2.7255 +/- 0.0006 K`.
- Big Bang nucleosynthesis denominators: IO Framework Conventions v2.0
  Section 1, reproducing Observational Conventions v1.0.
- Planck acoustic angle reference: Planck 2018 results.
- Standard Model effective number of relativistic species and neutrino
  reheating bookkeeping are treated as imported standard physics under
  Premise 2.
- PRyMordial, CLASS, CAMB, scipy, numpy, pandas, and mpmath are external
  dependencies for heavyweight private reruns. The public quick validator uses
  only Python standard-library modules and frozen outputs.
