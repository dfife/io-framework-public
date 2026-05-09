# Inventory Report

## Included

- R4/FIRAS readout-normalization audit inherited from Paper 17 v1.5.
- Theorem 20.3 radiation scope-boundary no-go support.
- Theorems 20.1 and 20.2 acoustic support.
- Corrected Big Bang nucleosynthesis wrapper scorecard values.
- Effective number of relativistic species import and kinetic-correction
  support.
- Big Bang nucleosynthesis abundance-ratio measurement-immunity support.
- Theorems 20.RAD1, 20.RAD2, and 20.RAD3 support.
- v2.0 kappa/scope audit report and machine-readable results.
- Standard-library validation script.

## Excluded Because v2.0 Removed The Active Sections

- Bare package reconstruction.
- Assembly-gap diagnostic.
- Torsion-Lambda branch.
- Delta N_eff target search and old radiation target sections.
- Reduced-to-full extension sketch superseded by Papers 31 and 32.
- Raw BOSS, Pantheon+, DESI, Planck, PRyMordial, CLASS, and CAMB assets.

## Review Findings

- `paper20-v1.8` was unpublished and is replaced, not preserved.
- No hidden continuous fitted parameter was found in the v2.0 live surfaces.
- R4 is not a Paper 20 fit. It is inherited as the Paper 17 v1.5 FIRAS-fixed
  readout normalization.
- The v2.0 draft has a minor acoustic-row presentation ambiguity: 0.429% and
  9.2 sigma come from adjacent exact rows. The bundle records both exact rows.
