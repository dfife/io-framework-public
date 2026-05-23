# Paper 35 v2.0 DESI Full RCA Report

## Scope

This RCA audits the Paper 35 v2.0 DESI DR2 GCcomb BAO confrontation from the
public DESI data vector through the IO active-branch formulas, upstream Paper 29
readout factors, Ly-alpha handling, covariance treatment, and frozen bundle
validation. It does not fit IO parameters to DESI. Any fit-like calculation in
this report is explicitly marked diagnostic and is not promoted to a manuscript
claim.

## Data and observational uncertainty verification

The bundle uses the public CobayaSampler DESI DR2 GCcomb BAO Gaussian vector:

- mean file:
  `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt`
- mean SHA256:
  `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585`
- covariance file:
  `https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt`
- covariance SHA256:
  `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509`

The DESI covariance is the full `13 x 13` joint covariance used by the script;
the chi-square calculation is `r^T C^{-1} r`. The earlier raw diagnostic tension
was not caused by diagonal-only error handling or by ignoring off-diagonal
covariance.

The DESI observational covariance does not include IO-theory-side uncertainty in
an imported Ly-alpha nonlinear redshift-space BAO shift. If the P2-imported
exterior Ly-alpha shift class is used, the bundle now adds the shift uncertainty
as a first-order rank-one covariance term on the Ly-alpha rows only:

`C_aug = C_DESI + sigma_alpha^2 J J^T`, with
`J_i = d(M_i / alpha) / d alpha = -M_i / alpha^2`.

The imported Ly-alpha value is the redshift-space isotropic shift class
`alpha = 0.9905 +/- 0.0027`, from the external Ly-alpha BAO-shift literature
and previously banked in the Paper 29 full-DESI imported-Ly-alpha closure report
and the Paper 31 Ly-alpha BAO Shift Inheritance Theorem.

## Formula verification

The script evaluates the active closed-geometry FRW distances:

- `E(z)^2 = Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_k (1+z)^2 + Omega_Lambda`;
- `chi(z) = integral_0^z dz' / E(z')`;
- `D_M = (c/H0) S_k(chi)`, with `Omega_k < 0` using
  `S_k(chi) = sin(sqrt(-Omega_k) chi) / sqrt(-Omega_k)`;
- `D_H = c / (H0 E(z))`;
- `D_V = (z D_M^2 D_H)^(1/3)`;
- DESI model entries are `D_M/r_d`, `D_H/r_d`, or `D_V/r_d`.

The curvature sign is therefore consistent with the closed `K = +1` active
branch. The script does not use the flat-CPL reinterpretation as the primary
DESI model. The flat-CPL point is retained only as a fixed synthetic
reinterpretation diagnostic.

Active branch constants are the Paper 29/Paper 30 active-branch values:

- `H0 = 67.57585653582628 km/s/Mpc`;
- `Omega_m = 0.34868395067621694`;
- `Omega_k = -0.04579112576013168`;
- `Omega_Lambda = 0.69701575761593`;
- `Omega_r = 9.141746798467538e-05`;
- `r_d = 144.01351425392883 Mpc`;
- `eta = K_gauge/x = 0.03612460534699675` in this bundle;
- galaxy/quasar transverse factor `f_perp = exp(eta) = 1.0367850274005339`;
- galaxy/quasar radial factor `f_parallel = exp(eta/2) = 1.01822641264138`.

The fixed comparator is the same-data Planck-style flat LambdaCDM comparator:

- `H0 = 67.36 km/s/Mpc`;
- `Omega_m = 0.3153`;
- `Omega_k = 0`;
- `Omega_r = 9.219892755009396e-05`;
- `Omega_Lambda = 0.6846078010724499`;
- `r_d = 147.09 Mpc`.

The fixed comparator is not fitted to the DESI vector by this bundle.

## RCA finding 1: raw no-readout branch was not the live observable

The raw active branch without the Paper 29 scoped BAO readout kernel gives:

- `chi2 = 69.48480893315653`;
- `dof = 13`;
- `PTE = 2.8723766779727283e-10`;
- `Delta chi2(raw IO - LambdaCDM) = +39.61505840246426`.

This is a diagnostic-only calculation. Treating it as the live Paper 35 DESI
result is a calculation-selection error, because Paper 29 already scoped the
BAO observable through the galaxy/quasar AP-shell readout kernel.

## RCA finding 2: internal scoped BAO branch still leaves a high-tail DESI fit

The internal Paper 29 scoped BAO branch applies `f_perp = exp(eta)` and
`f_parallel = exp(eta/2)` on the galaxy/quasar block and leaves the Ly-alpha
rows at identity:

- `chi2 = 27.73511287626574`;
- `dof = 13`;
- `reduced chi2 = 2.133470221251211`;
- `PTE = 0.009851388595481134`;
- fixed LambdaCDM comparator `chi2 = 29.869750530692272`;
- fixed LambdaCDM comparator `PTE = 0.004917478561859067`;
- `Delta chi2(IO - LambdaCDM) = -2.1346376544265304`.

This branch beats the fixed LambdaCDM comparator on the same covariance, but its
absolute PTE is only about one percent. It is not a comfortable DESI fit.

Block split:

- galaxy/quasar rows: `chi2 = 25.9950048621104` on `11` rows,
  `PTE = 0.0065010327895826765`;
- Ly-alpha rows with identity kernel: `chi2 = 1.740108014155343` on `2` rows,
  `PTE = 0.41892892350975863`.

Therefore the remaining tension is not primarily the Ly-alpha block. It is in
the galaxy/quasar block after the exact Paper 29 readout factors are applied.

## RCA finding 3: banked P2-imported Ly-alpha shift was under-used

MCP and local result search found a banked upstream conditional route:

- `results/paper29/paper29_full_desi_imported_lya_closure_report.md`;
- `results/paper29/paper29_full_desi_imported_lya_closure_results.json`;
- `results/paper31/paper31_lya_bao_shift_inheritance_theorem.md`;
- `results/paper31/paper31_lya_bao_end_to_end_inheritance_theorem.md`.

Those artifacts bank a P2-imported exterior Ly-alpha redshift-space shift class
with `alpha_parallel = alpha_perp = 0.9905` and `sigma_alpha = 0.0027`.
This is not an internal IO derivation of the Ly-alpha shift, but it is a valid
conditional branch under Premise 2 and external Ly-alpha physics.

The Paper 35 bundle now archives that branch separately:

- central imported-shift branch:
  `chi2 = 26.296401887105667`, `PTE = 0.015508017004462981`;
- with the imported-shift uncertainty propagated as rank-one covariance:
  `chi2 = 26.290695872127714`, `PTE = 0.01553556040587586`;
- `Delta chi2(central imported-shift IO - LambdaCDM) =
  -3.5733486435866055`;
- `Delta chi2(imported-shift covariance IO - LambdaCDM) =
  -3.5790546585645586`.

The Ly-alpha block under the imported shift is:

- central-shift Ly-alpha-only `chi2 = 0.30139702499526777` on `2` rows,
  `PTE = 0.8601069710760224`;
- with shift covariance `chi2 = 0.29569101001731357` on `2` rows,
  `PTE = 0.8625643665227685`.

Corrected claim boundary: the strongest reproducible Paper 35 DESI branch is
the conditional P2-imported Ly-alpha branch, but the internal Ly-alpha selector
remains open. The branch should not be described as an unconditional IO theorem.

## RCA finding 4: remaining galaxy/quasar tension points upstream of Paper 35

A non-promotable fit diagnostic was run to localize the residual. Allowing only
the two readout factors to float against DESI gives approximately:

- best diagnostic `f_perp = 1.0250`;
- best diagnostic `f_parallel = 1.0146`;
- all-data best with Ly-alpha shift included:
  `chi2 = 17.6731`, `PTE = 0.1703`.

By contrast the exact Paper 29 factors are:

- `f_perp = 1.0367850274005339`;
- `f_parallel = 1.01822641264138`.

This diagnostic is not a correction and must not be promoted; it is a fit to
DESI. It does, however, identify the likely frontier: the Paper 29
galaxy/quasar AP readout exponent placement is stronger than DESI DR2 prefers.
If a further repair exists, it is probably a Paper 29 theorem/calculation audit
of AP-shell exponent placement, not a Paper 35 DESI-script bug.

Tested non-promotable exponent variants:

- current `(eta, eta/2)` exponents: `chi2 = 27.7351`;
- half-strength `(eta/2, eta/4)`: `chi2 = 23.3929`;
- `(2 eta/3, eta/3)`: `chi2 = 19.3578`;
- `(3 eta/4, 3 eta/8)`: `chi2 = 19.4130`.

These values are RCA evidence only. They are not zero-parameter IO predictions.

## Corrections applied in the v2.0 bundle working tree

1. `scripts/07_desi_confrontation.py` now archives the conditional
   P2-imported Ly-alpha shift branch in addition to the identity-Ly-alpha
   internal scoped branch.
2. `data/imported_constants.json` now records the imported Ly-alpha shift
   source, central value, uncertainty, and claim status.
3. `results/desi_confrontation_results.json` now contains both:
   `active_scoped_bao_readout` and
   `conditional_imported_lya_shift_bao_readout`.
4. `scripts/10_validate_expected_outputs.py` now validates the imported
   Ly-alpha branch values and shift uncertainty propagation.

Validator result after correction:

- `SUMMARY total_checks=58 pass_count=58 fail_count=0`.

## Recommended Paper 35 Section 4 language

The Section 4 DESI paragraph should distinguish three calculations:

1. raw no-readout active branch, diagnostic only:
   `chi2 = 69.4848`;
2. internal Paper 29 scoped BAO readout with identity Ly-alpha:
   `chi2 = 27.7351`, `PTE = 0.00985`;
3. conditional P2-imported Ly-alpha shift branch:
   `chi2 = 26.2907`, `PTE = 0.01554` after propagating the imported
   Ly-alpha shift uncertainty.

Suggested sentence:

> The live Paper 35 DESI comparison is not the raw active branch
> (`chi2 = 69.4848`, retained as a no-readout diagnostic), but the Paper 29
> scoped BAO observable. With the internal Ly-alpha identity component this
> gives `chi2 = 27.7351` on 13 entries (`PTE = 0.00985`), already better than
> the same-data fixed flat LambdaCDM comparator (`chi2 = 29.8698`). If the
> exterior Ly-alpha redshift-space shift class imported under Premise 2 is also
> used, with its `alpha = 0.9905 +/- 0.0027` uncertainty propagated, the result
> becomes `chi2 = 26.2907` (`PTE = 0.01554`). This conditional branch is the
> strongest reproducible DESI comparison in the current stack, while the
> remaining high-tail absolute fit is localized to the galaxy/quasar AP-kernel
> exponent placement inherited from Paper 29.

## Bottom-line RCA

The old `Delta chi2 = +39.6` failure was a calculation-selection error: it used
the raw no-readout branch instead of the Paper 29 scoped BAO observable. A
second issue was found: Paper 35 had not archived the already-banked
P2-imported Ly-alpha shift branch and its uncertainty propagation. That branch
improves the DESI comparison from `chi2 = 27.7351` to `chi2 = 26.2907`.

The remaining absolute tension is real at the current stack boundary. It is not
fixed by DESI covariance handling, closed-curvature sign, r_d substitution,
LambdaCDM comparator choice, or Ly-alpha observational uncertainty. The live
frontier is a Paper 29 AP-shell exponent-placement audit: either the exact
`exp(eta), exp(eta/2)` galaxy/quasar readout factors are theorem-correct and
DESI DR2 is a high-tail but comparator-beating confrontation, or the AP-shell
placement theorem is over-scoped and needs repair.
