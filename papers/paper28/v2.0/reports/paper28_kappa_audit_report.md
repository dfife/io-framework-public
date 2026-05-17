# Paper 28 v2.0 Kappa-Style Audit and R4 Damage Report

## Executive Verdict

No hidden fitted parameter was found in the active Paper 28 v2.0 bundle chain.

The active public bundle is limited to theorem-support material for:

- the primitive line-scale root uniqueness result;
- the one-form trace-log Gaussian extension;
- the coexact Dirichlet-to-Neumann boundary Hessian spectral-index chain;
- the lower-order DtN remainder and flat-collar `O(1)` deformation exclusion;
- the homogeneous Oppenheimer-Snyder JWST formation-clock map;
- the R4/FIRAS damage audit.

The bundle does not include retired or diagnostic scripts that hardcode
`T_cmb = 2.7253` or older CMB-temperature prediction language.

## Source Manuscript Availability

At bundle build time, `results/Full Papers/Interior_Observer_Paper28_v2_0.docx`
was not present. The audit used the available Paper 28 working draft and the
support artifacts under `results/paper28/`.

Release-risk note: before Zenodo upload, reconcile this bundle against the
final Paper 28 v2.0 manuscript if it has been saved under a different filename
or appears later in `Full Papers/`.

## R4 Review

### Active Bundle Scripts

No active bundle script uses `R4 = 1`, `R4_FIRAS`, `T_obs`, or `T_CMB` as a
computational input. `R4_FIRAS = 1.0031014644` is recorded only as framework
boundary metadata from Paper 17 v1.5.

Verdict: no active R4 damage in the bundle scripts.

### Excluded CMB-Temperature Artifacts

The local Paper 28 folder contains old or diagnostic artifacts with
CMB-temperature-era constants or historical excerpts. These are excluded from
the public v2.0 bundle:

- `paper28_archive_review_results.json`
- `paper28_archive_review_report.txt`
- `paper28_mixed_fluid_transfer_investigation.py`
- `paper28_mixed_fluid_transfer_results.json`
- working-draft lines containing `T_cmb = 2.7253`

These artifacts are useful audit history but should not be treated as active
Paper 28 v2.0 CMB-temperature predictions.

## Hidden-Parameter Walkthrough

### `gamma_BI`, `K_gauge`, and `x`

The bundle uses:

```text
gamma_BI = 0.2375
K_gauge = ln(1 + gamma_BI^2) = 0.05487281774291466
x = 1.519
K_gauge/x = 0.036124303978219
```

`gamma_BI` and `x` are inherited framework constants. Paper 28 v2.0 does not
fit them to `n_s`, JWST timings, or any other Paper 28 output.

Verdict: no hidden fit.

### Primitive Line-Scale Root

The result fixes `q = 1/2` by dimensionality: a one-form line-transport
operator must scale as inverse length, while the one-form Laplacian scales as
inverse length squared.

Verdict: `DERIVED/THEOREM`.

### One-Form Trace-Log Gaussian Extension

Given the coexact one-form carrier and a centered one-loop Gaussian extension,
the per-mode determinant generator is:

```text
w_l = log(s_l) = (1/2) log(lambda_l)
```

The final physical identification of the A-vacuum canonical extension with
this Gaussian class remains conditional.

Verdict: `DERIVED/CONDITIONAL_VERIFIED`.

### Coexact DtN Hessian

On the flat Painleve-Gullstrand source collar, the coexact
Dirichlet-to-Neumann shell law is:

```text
sigma_l = l + 1
```

The pivot values reproduced in the bundle are:

```text
DtN plus branch       n_s = 0.963858187553
DtN minus branch      n_s = 0.963959517376
DtN equal average     n_s = 0.963908849852
exact shell target    n_s = 0.963908639282
```

The remaining condition is the identification of the full reduced IO boundary
Hessian with the coexact DtN class beyond the stated collar/subprincipal
control.

Verdict: `DERIVED/CONDITIONAL_VERIFIED`.

### Lower-Order DtN Remainder and `O(1)` Exclusion

The bundle validates the bound:

```text
|d ln G / d ln(l+1) + beta| <= 2 beta A / ((l+1)^2 - A)
```

at pivot `l = 711`, with the largest recorded check:

```text
A = 100 -> 1.4254604564015358e-05
```

This shows ordinary lower-order DtN corrections cannot materially move the
Paper 28 pivot tilt. Genuine `O(1)` shell deformations are excluded on the
flat collar under the Laplace-type operator hypothesis.

Verdict: `DERIVED/CONDITIONAL_VERIFIED`.

### JWST Formation-Clock Map

The homogeneous Oppenheimer-Snyder formation-clock map is derived from local
proper time along comoving worldlines and radial null redshift:

```text
u(z)   = 1/[x(1+z)]
tau(z) = (r_s/(2c)) [acos(1 - 2u) - 2 sqrt(u(1-u))]
```

Bundle anchors:

```text
z = 10 -> 0.7023379333 Gyr
z = 12 -> 0.5450883247 Gyr
z = 14 -> 0.4388659557 Gyr
z = 17 -> 0.3331013378 Gyr
z = 20 -> 0.2639107601 Gyr
```

Peculiar velocities, local potentials, and nonlinear structure are
perturbative corrections around the homogeneous background theorem.

Verdict: `DERIVED/THEOREM` on the homogeneous OS background.

## Claim-Label Audit

The available working draft uses older lower-case labels and noncanonical
status terms. Active v2.0 manuscript theorem statements should migrate to the
public taxonomy:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `RECONSTRUCTION`
- `RECONSTRUCTION/RESEARCH_ONLY`
- `OPEN/PREMISE_GAP`
- `SUPERSEDED`

Noncanonical language found in the working draft/support artifacts:

- `derived`
- `verified`
- `conditional`
- `derived / scoped theorem`
- `SEMICLASSICAL PRINCIPLE`
- `conditional_effective_fluid_proxy`
- `verified_no_go`
- `not derived`

Recommendation: update active theorem/result labels to canonical form. Keep
older language only in clearly historical notes.

## Abbreviations and IO-Internal Terms Flagged

Abbreviations requiring first-use expansion or replacement:

- `IO`
- `CMB`
- `JWST`
- `OS`
- `DtN`
- `PG`
- `KMS`
- `CCR`
- `TT`
- `CLASS`
- `PSRP`
- `BDP`
- `GTTP`
- `GMP`
- `WMR`
- `C1`, `C1b`, `C2c`, `C3`
- `AV1`
- `H1-H3`
- `FRW`
- `BBN`

IO-internal or informal terms requiring definition or replacement:

- `A-vacuum`
- `scalar bridge`
- `bridge covariance`
- `primitive line scale`
- `payload coefficient`
- `dead route`
- `surviving route`
- `rescue`
- `banked`
- `source-side`
- `slot`
- `branch`

## Final Audit Classification

Paper 28 v2.0 can be bundled as a theorem-support and validation package for
the active spectral-index/DtN chain and homogeneous JWST clock-map theorem.

The main surviving scope boundaries are explicit:

- physical A-vacuum canonical extension identification remains conditional;
- full IO DtN equality beyond the flat source collar remains conditional;
- homogeneous JWST clock map does not include nonlinear structure corrections;
- old CMB-temperature prediction language must remain retired.
