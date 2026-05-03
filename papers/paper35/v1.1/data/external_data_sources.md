# External Data Sources and Licensing Discipline

This bundle does not redistribute external observational datasets. It cites
external sources and records checksums for the specific public files needed to
recompute the frozen outputs.

## DESI DR2 BAO

- Use in bundle: `scripts/07_desi_confrontation.py` fetches public DESI DR2
  GCcomb BAO mean/covariance files from the CobayaSampler `bao_data`
  repository at runtime.
- Redistributed here: no.
- Source mean file:
  `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt`
- Mean file SHA256 used for frozen output:
  `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585`
- Source covariance file:
  `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt`
- Covariance file SHA256 used for frozen output:
  `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509`
- Paper references:
  DESI DR2 cosmology `https://arxiv.org/abs/2503.14738`;
  DESI DR2 dark-energy analysis `https://arxiv.org/abs/2503.14743`.

## Planck / CMB Comparison Values

- Use in bundle: comparison context only for eta discussion. This bundle does
  not require or redistribute Planck likelihood files.
- Redistributed here: no.
- Reference source: Planck 2018 cosmological parameters and standard BBN/CMB
  eta conventions should be cited from the manuscript bibliography.

## JWST Sources

- Use in bundle: redshifts, approximate stellar masses, and SFR values already
  stated in the Paper 35 working table.
- Redistributed here: no MAST data products, spectra, images, or catalogs.
- References are listed by URL in `data/imported_constants.json` and
  `data/bibliography.md`.

## Direct-Detection Limits

- Use in bundle: manuscript-cited limit values only. No experimental data
  tables or likelihood products are redistributed.
- Redistributed here: no.
- LZ reference: `https://arxiv.org/abs/2410.17036`.
- XENONnT reference: `https://www.weizmann.ac.il/particle/xenon/publications`.
- PandaX-4T reference: `https://pandax.sjtu.edu.cn/Publications`.

## Standard-Literature Formulas

The bundle cites, but does not rederive as IO-specific physics:

- blackbody photon number density `n_gamma = 2 zeta(3) T^3 / pi^2`;
- Standard-Model sphaleron conversion `c_sph = 28/79`;
- Davidson-Ibarra bound;
- Casas-Ibarra parameterization;
- standard type-I seesaw and Boltzmann leptogenesis equations;
- mean-baryon-mass conventions.

The scripts evaluate these formulas only where Paper 35 uses the numerical
result. They remain external standard-literature inputs.
