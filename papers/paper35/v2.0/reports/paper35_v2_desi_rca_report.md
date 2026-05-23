# Paper 35 v2.0 DESI RCA Report

Date: 2026-05-23

Status: forensic diagnostic and repaired bundle boundary. This report does not
fit IO parameters to DESI. It documents why the raw no-readout DESI
`Delta chi2 = +39.615` diagnostic is not the live active IO BAO observable in
Paper 35 v2.0.

## Executive Finding

The raw active-branch calculation

`D_M/r_d`, `D_H/r_d`, `D_V/r_d`

on the public DESI DR2 GCcomb vector gives

- raw no-readout active IO diagnostic: `chi2 = 69.48480893315653`,
- fixed flat LambdaCDM comparator: `chi2 = 29.869750530692272`,
- raw diagnostic `Delta chi2(IO - LambdaCDM) = 39.61505840246426`.

That raw calculation is retained in the bundle as a diagnostic only. It omits
the already-banked Paper 29 scoped BAO readout kernel.

The active theorem-supported Paper 35 v2.0 DESI comparison applies the Paper 29
scoped BAO readout kernel to the galaxy/quasar block and leaves the Ly-alpha
block as the current identity component:

- `eta = K_gauge/x = 0.03612460534699016`,
- `f_perp = exp(eta) = 1.0367850274005339`,
- `f_parallel = exp(eta/2) = 1.01822641264138`.

On the same DESI DR2 GCcomb data vector and covariance this gives

- active IO scoped BAO readout: `chi2 = 27.735112876265742`,
- degrees of freedom: `13`,
- reduced chi-square: `2.133470221251211`,
- chi-square survival probability: `0.009851388595481134`,
- fixed flat LambdaCDM comparator: `chi2 = 29.869750530692272`,
- fixed flat LambdaCDM reduced chi-square: `2.2976731177455596`,
- fixed flat LambdaCDM survival probability: `0.004917478561859067`,
- scoped-readout `Delta chi2(IO - LambdaCDM) = -2.1346376544265304`.

Therefore the apparent DESI failure was a calculation-selection error: Paper 35
script 07 originally evaluated the raw active background after Paper 29 had
already promoted the DESI BAO observable to a scoped AP-shell readout-kernel
calculation.

## External Data Verification

Script 07 fetches public DESI DR2 BAO files from the CobayaSampler `bao_data`
repository and verifies SHA256 checksums before computing the Gaussian
chi-square.

- Mean file:
  `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt`
- Mean SHA256:
  `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585`
- Covariance file:
  `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt`
- Covariance SHA256:
  `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509`

The likelihood uses the full public 13x13 covariance and the 13-entry
`ALL_GCcomb` compressed BAO vector. No DESI data file is redistributed in this
bundle.

## Scope Boundary

The repaired DESI claim inherits the Paper 29 scoped BAO-route boundaries:

- scoped to the standard AP-shell / anisotropic BAO readout imported under P2;
- hybrid isolated pre-drag ruler only, not full Stage-2 CMB closure;
- galaxy/quasar kernel only on the typed covariance genealogy;
- Ly-alpha block only through the current internal IO identity component;
- not universal BAO closure across all tracer/readout definitions.

Do not describe the repaired result as universal DESI closure or full CMB
closure. The correct Section 4 phrasing is that the raw no-readout branch is a
diagnostic, while the active scoped BAO observable is the Paper 29 readout-kernel
comparison reproduced by script 07.

## Reproducibility

The repaired values are produced by:

`scripts/07_desi_confrontation.py`

and frozen in:

`results/desi_confrontation_results.json`

They are validated by:

`scripts/10_validate_expected_outputs.py`

Expected validation summary:

`SUMMARY total_checks=49 pass_count=49 fail_count=0`
