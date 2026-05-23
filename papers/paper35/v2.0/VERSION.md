# Paper 35 v2.0 Bundle Version

- Paper: Paper 35
- Manuscript version: v2.0
- Bundle version: v2.0
- Release tag: `paper35-v2.0`
- Date: May 2026
- Status: public reproducibility support bundle

## Scope

This bundle supports Paper 35 v2.0:

`The Baryon Asymmetry from Boundary Chirality: Eta, JWST Timing, DESI, and Dark-Sector Null Tests in the Interior Observer Framework`

The v2.0 bundle reproduces:

- late-time eta with Paper 17 v1.5 FIRAS-fixed `R4`;
- local BBN temperature-assignment calculations;
- chiral source-era diagnostic quantities;
- standard external leptogenesis target reductions;
- baryogenesis theorem-surface registry summary;
- JWST formation-time table;
- DESI Paper 29 scoped BAO readout-kernel chi-square, fixed-model degrees of
  freedom, reduced chi-square, Gaussian chi-square survival probability,
  conditional P2-imported Ly-alpha shift branch, diagnostic raw no-readout
  active-branch chi-square, same-data fixed flat LambdaCDM comparator, and
  flat-CPL reinterpretation check;
- geometric dark-sector consistency ledger;
- R4/FIRAS impact audit, kappa audit, and conditional-verification reports.

## v2.0 Change Boundary

Compared with v1.2, this bundle extends script 07 and the validator to support
the Paper 35 v2.0 DESI scope discussion at the highest reproducible claim level.
The repaired output applies the Paper 29 scoped BAO readout kernel as the
primary active IO DESI result and retains the raw no-readout active branch as a
diagnostic. The new output shows:

- active IO scoped BAO readout `chi2 = 27.73511287626574` on the public DESI
  DR2 GCcomb vector;
- fixed-model degrees of freedom `dof = 13`;
- active IO scoped BAO reduced chi-square `2.133470221251211`;
- active IO scoped BAO chi-square survival probability `0.009851388595481134`;
- Paper 29 scoped readout factors `f_perp = exp(eta) = 1.036785027400534` and
  `f_parallel = exp(eta/2) = 1.01822641264138`;
- fixed flat LambdaCDM comparator `chi2 = 29.869750530692272`;
- fixed flat LambdaCDM reduced chi-square `2.2976731177455596`;
- fixed flat LambdaCDM chi-square survival probability `0.004917478561859067`;
- `Delta chi2(active scoped - LambdaCDM) = -2.1346376544265304`;
- raw no-readout active branch diagnostic `chi2 = 69.48480893315653`.
- conditional P2-imported Ly-alpha shift branch
  `chi2 = 26.296401887105667`, `PTE = 0.015508017004462981`;
- conditional P2-imported Ly-alpha shift branch with the imported
  `alpha = 0.9905 +/- 0.0027` shift uncertainty propagated as a rank-one
  covariance term: `chi2 = 26.290695872127714`,
  `PTE = 0.01553556040587586`;
- `Delta chi2(imported Ly-alpha branch with shift uncertainty - LambdaCDM) =
  -3.5790546585645586`.

These are same-data fixed-model diagnostics. They do not fit IO parameters and
do not convert the DESI erratum into a universal BAO theorem. The active DESI
claim inherits the Paper 29 scoped BAO-route boundaries. The imported Ly-alpha
branch is conditional on the external redshift-space Ly-alpha shift class under
Premise 2; it is not an internal IO derivation of the Ly-alpha shift.

## v1.2 Inherited Boundary

The CMB-temperature prediction wording is retired. FIRAS fixes the unique
observer-side thermal readout normalization `R4`, and Paper 35 propagates that
normalization without retuning. The baryogenesis registry status counts are
unchanged.

## Update Policy

The release tag `paper35-v2.0` is immutable once published. If errors are found after release,
the correction path is a new manuscript/bundle version such as `paper35-v2.1`,
not retagging.
