# Paper 32 v1.6 Bundle Version

Bundle: `paper32-v1.6-repro`

Paper version: `Paper 32 v1.6`

Date: May 2026

Classification: `verified / public-reproducibility-support / R4-FIRAS repaired`

## Version Summary

Paper 32 v1.6 republication support bundle.

This version preserves the Paper 32 v1.5 closure bundle and adds the R4/FIRAS
repair inherited from Paper 17 v1.5:

- the observed CMB temperature is retired as an independent IO prediction;
- `R4=1` is retained only as a historical diagnostic;
- active thermal readout uses `R4_FIRAS = 1.0031014644105183`;
- the framework constants script and validator now reproduce the FIRAS-fixed
  readout family;
- the v1.6 kappa audit separates Paper 32 KB7/P4 source-block closure from the
  Paper 17 optical thermal R4 normalization.

This version continues to provide public reproducibility support for:

- framework constants;
- Lambda-dropout local recollapse acceleration;
- `x_crit = Q^(-1/4)`;
- 111/222 Gyr late-time timescales;
- scoped KB.7 source-block validation;
- `n_s` and `A_s` derivation arithmetic;
- universal-GMP characterization;
- framework-closure kappa audit;
- R4/FIRAS impact audit.

## Release Tag

Expected annotated git tag:

```text
paper32-v1.6
```

## Boundary

The bundle supports Paper 32 v1.6 reproducibility and scope auditability. It
does not modify the Zenodo manuscript and does not include private exploratory
research state.
