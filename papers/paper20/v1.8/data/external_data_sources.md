# External Data Sources

This bundle does not redistribute external observational datasets.

- FIRAS CMB temperature: Fixsen 2009, `T_CMB = 2.7255 +/- 0.0006 K`.
- BBN denominators: IO Framework Conventions v2.0 Section 1, reproducing
  Observational Conventions v1.0.
- BOSS DR12 / Pantheon+ / DESI / Planck inputs appear only in frozen derived
  JSON outputs or in optional heavyweight scripts in the private lab. Raw
  external datasets are not included here.
- PRyMordial, CLASS, CAMB, scipy, numpy, pandas, and mpmath are external
  dependencies for full heavyweight reruns. The quick validator uses only the
  Python standard library and frozen outputs.

