# External Data Sources

This bundle does not redistribute external observational datasets.

## DESI DR2 BAO GCcomb

- Source: CobayaSampler `bao_data`, DESI DR2 BAO Gaussian likelihood files.
- Mean URL: `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt`
- Mean SHA256: `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585`
- Covariance URL: `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt`
- Covariance SHA256: `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509`
- Fetch procedure: run `python3 scripts/03_desi_chronometer_confrontation.py`; files are downloaded to `data/.cache/` and checksum-verified.

## Cosmic Chronometers

- Source: 35-point compilation from MNRAS 542, 1063 (2025), Table A1, as used in the Paper 29 audit artifacts.
- Bundle handling: the 35 redshift, H(z), and uncertainty triples are embedded in `scripts/_common.py` to make the chi-squared calculation auditable. They are cited as a literature table, not as a redistributed restricted data file.

## FIRAS CMB Temperature

- Source: FIRAS CMB blackbody temperature measurement, inherited through Paper 17 v1.5.
- Bundle handling: `T_CMB = 2.7255 K` is an imported empirical observer-side datum, not an independent IO prediction.

## CAMB

- Source: CAMB public cosmology code.
- Use: accepted external solver for the drag sound horizon and tanh reionization representative under Premise 2.

## Euclid Spectroscopic RSD Bins

- Source: Euclid Collaboration, "Euclid preparation. Galaxy power spectrum modelling in redshift space", arXiv:2601.20826.
- Bundle handling: the script uses the paper's four non-overlapping spectroscopic bins centered at `z = 0.9, 1.2, 1.5, 1.8` with widths `0.2, 0.2, 0.2, 0.3`.

## Euclid Dark-Energy Forecast Margins

- Source: Euclid Collaboration, "Euclid preparation. VII. Forecast validation for Euclid cosmological probes", Astronomy & Astrophysics 642, A191 (2020), doi:10.1051/0004-6361/202038071.
- Bundle handling: no official Euclid DR1 + DESI DR3 joint covariance was available at build time. `compute_w0wa.py` records conservative published Euclid forecast marginal scales as placeholder falsification margins, not as an official DR1+DR3 forecast.
