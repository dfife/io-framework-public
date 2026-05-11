# Paper 23 v2.0 R4/FIRAS and Kappa-Style Structural Audit

Date: May 2026

Scope: Paper 23 v2.0 working draft in `results/Full Papers/Interior_Observer_Paper23_v2_0.docx`, local Paper 23 scripts/results in `results/paper23/`, and the current public claim-label convention.

## Executive Verdict

No hidden continuous fitted parameter was found in the active Paper 23 v2.0 perturbation-theory and spectral-index chain.

R4 is not used in the active Paper 23 scalar spectral-index calculation. The active result is

```text
1 - n_s = K_gauge / x = 0.03612435625139463,
n_s = 0.9638756437486053,
residual against Planck 1 - n_s = 0.0351 +/- 0.0042: +0.2439 sigma.
```

That result depends on the Paper 23 bridge/premise package, not on the observer-side CMB thermal readout. Therefore replacing the retired `R4 = 1` convention with `R4_FIRAS = 1.0031014644` does not numerically move Paper 23's active spectral-index value.

However, Paper 23 v2.0 still has manuscript hygiene issues:

- It contains one stale independent CMB-temperature prediction phrase that must be removed or rewritten.
- It contains inherited Paper 22 appendix scorecard values from v1.3/v1.4-era text that conflict with Paper 22 v2.0.
- It still uses noncanonical labels such as `CONDITIONAL/THEOREM`, plain `CONDITIONAL`, `DERIVED/VERIFIED`, and unqualified `DERIVED` where the public claim-discipline system now requires canonical labels.
- It uses many abbreviations and IO-local terms that should be expanded or replaced for first-time readers.

## R4 Usage and Damage Review

### R4 in active Paper 23 calculations

`R4_FIRAS = 1.0031014644` is inherited from Paper 17 v1.5 as an `IMPORTED/EMPIRICAL` observer-side thermal-readout normalization fixed by FIRAS. It is not an input to the active Paper 23 spectral-index computation.

The active spectral-index computation uses:

```text
gamma_BI = 0.2375
x = r_s / R_U = 1.51899780195519
K_gauge = ln(1 + gamma_BI^2) = 0.054872817742914665
1 - n_s = K_gauge / x = 0.03612435625139463
```

No `T_obs`, `T_CMB`, `R4`, or FIRAS normalization appears in that calculation.

### Stale CMB-temperature prediction wording

The v2.0 draft includes this stale claim in the conclusion:

```text
The spectral index therefore joins T_CMB, rho_Lambda, a0, f_b, and theta_* as one of the framework's zero-parameter predictions...
```

This must be rewritten. The active framework no longer counts the observed CMB temperature as an independent prediction. Correct framing:

```text
The spectral index therefore joins the framework's non-thermal-readout predictions as a zero-parameter result within the stated Paper 23 premise package. The observed CMB temperature is not counted as an independent IO prediction; it fixes the observer-side thermal readout normalization in Paper 17 v1.5.
```

### CMB-related text that is acceptable if framed narrowly

References to CMB-relevant perturbation shells, Planck spectral-index comparison, FIRAS as a blackbody-spectrum measurement, and use of `T_0 = 2.725 K` as an imported late-time thermal datum are acceptable only if they do not count the observed CMB temperature as a prediction.

## Stale Inherited Paper 22 Values

The v2.0 draft history says inherited Paper 22 appendix values were updated, but the extracted appendix still contains stale rows:

```text
D/H_sigma = -0.61, Y_p_sigma = +1.06, chi^2 = 1.50, comparator = 3.067
Li7/H = 5.391e-10 (+12.29 sigma), matching uniform benchmark to 0.07%
```

These are no longer the active Paper 22 values. If these inherited rows remain in Paper 23 at all, they should be replaced by Paper 22 v2.0 values:

```text
D/H_sigma = -0.5529801681809717
Y_p_sigma = +0.7045360432106975
chi^2(D/H + Y_p) = 0.8021581025844415
two-parameter comparator chi^2(D/H + Y_p) = 1.9345853017600352
Li7/H = 5.363335812718549e-10
Li7_sigma = +12.204309073285641
uniform-benchmark fractional consistency = 0.005093424637516164 (0.51%)
```

Because the appendix is now an active record rather than a historical archive, superseded inherited rows should usually be removed unless they support a live no-go or live comparison.

## Candidate Kappa Fields

| Candidate field | Rigidity test | Classification | Finding |
|---|---|---|---|
| `R4` / optical readout normalization | Free under modular-projection stack; fixed empirically by FIRAS in Paper 17 v1.5 | `IMPORTED/EMPIRICAL` for Paper 23 dependency ledger | Not active in Paper 23 spectral-index calculation |
| `gamma_BI = 0.2375` | Imported Barbero-Immirzi value used in gauge payload | `IMPORTED/EMPIRICAL` upstream constant | Visible, not fitted in Paper 23 |
| `K_gauge = ln(1 + gamma_BI^2)` | Fixed by gauge-sector construction once `gamma_BI` is fixed | `DERIVED/CONDITIONAL_VERIFIED` through upstream gauge chain | No Paper 23 freedom |
| `x = r_s / R_U` | Fixed by framework geometric normalization branch | upstream framework constant | No Paper 23 freedom |
| Degree of gauge payload, `K_gauge/x` rather than `2K_gauge/x` | No-Doubling theorem tests one-slot versus two-slot covariance structure | `DERIVED/CONDITIONAL_VERIFIED` if premise package is visible | No hidden fitted parameter; doubled route is rejected numerically and structurally |
| Boundary-to-bulk bridge operator | Unique up to normalization locally; shell branch multiplicity one | `DERIVED/CONDITIONAL_VERIFIED` if bridge premises are stated | Overall normalization cancels in spectral slope |
| Shell correction factor `(n-1)(n+3)/(n(n+1))` | Fixed by closed-S3 Mukhanov-Sasaki wavenumber dictionary | `DERIVED/THEOREM` inside closed-FRW perturbation setup | No fit |
| Pivot-shell mapping | Fixed by `k R_U` dictionary and closed-S3 spectrum | `VERIFIED` numerical mapping | No fit |
| White boundary baseline `C_l = 4 pi / N` | Fixed by isotropic point process on S2 | `DERIVED/CONDITIONAL_VERIFIED` if boundary covariance premise is visible | Not a fitted amplitude |
| Primordial Scalar Readout Principle | Not derived by Paper 23; must be declared | `OPEN/PREMISE_GAP` | Load-bearing if theorem depends on it |
| Boundary Covariance Exponent | Not derived by Paper 23; must be declared | `OPEN/PREMISE_GAP` | Load-bearing if theorem depends on it |
| Spatial canonical-commutation-relation lift | Not derived by Paper 23; must be declared | `OPEN/PREMISE_GAP` | Load-bearing if theorem depends on it |
| Tensor gamma-neutrality / `n_t = 0` | Not closed by active Paper 23 scalar theorem | `OPEN/PREMISE_GAP` unless chained to later paper | Keep conditional/open |

## Hidden-Parameter Assessment

The active scalar spectral-index result does not contain a hidden continuously adjustable parameter. Once `gamma_BI`, `x`, and the Paper 23 premise package are fixed, the scalar tilt is fixed. The rejected doubled route gives

```text
2 K_gauge / x = 0.07224871250278926,
```

which is about `+8.8449 sigma` from the Planck value for `1 - n_s`. This is not a tunable branch; it is the route killed by the No-Doubling theorem.

The risk is not hidden numerical fitting. The risk is label hygiene: premise-package claims must not be labeled as unconditional theorems unless their chains are explicitly shown back to Premise 1, Premise 2, or frozen imported physics.

## Claim-Label Findings

Canonical public labels are:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `RECONSTRUCTION`
- `RECONSTRUCTION/RESEARCH_ONLY`
- `OPEN/PREMISE_GAP`
- `SUPERSEDED`
- `Historical/SUPERSEDED`

Paper 23 v2.0 should not use `DERIVED/SCOPED`, `CONDITIONAL/THEOREM`, plain `CONDITIONAL`, `DERIVED/VERIFIED`, or unqualified `DERIVED` for load-bearing statements.

Recommended migrations:

- Main spectral-index theorem: `DERIVED/CONDITIONAL_VERIFIED` if the bridge/premise chain is stated explicitly.
- No-Doubling theorem: `DERIVED/CONDITIONAL_VERIFIED` under the same premise package.
- Closed-S3 perturbation equations and harmonic spectrum: `DERIVED/THEOREM`.
- Numerical Planck comparison for `n_s`: `VERIFIED`.
- `R4_FIRAS`: `IMPORTED/EMPIRICAL`.
- Primordial Scalar Readout Principle, Boundary Covariance Exponent, and spatial canonical-commutation-relation lift: `OPEN/PREMISE_GAP` unless the v2.0 manuscript provides a direct chain to Premise 1/Premise 2.
- Tensor `n_t = 0` and tensor-to-scalar-ratio status: `OPEN/PREMISE_GAP` unless promoted by a cited later theorem.

## Abbreviations to Expand for First-Time Readers

The manuscript should define or replace at first use:

`IO`, `OS`, `FRW`, `CMB`, `BBN`, `LQG`, `CCR`, `KMS`, `TT`, `AQFT`, `PSRP`, `FIRAS`, `GTTP`, `GMP`, `TBS`, `WMR`, `PRyMordial`, `YPCMB`, `YPBBN`, `S3`, `S2`, `SU(2)`, `SO(4)`, `U(1)`, `K=+1`, `n_s`, `n_t`, `A_s`, `P_resp`, `F_abs`, `B_N`, and `G^(1)`.

## IO Slang / Nonstandard Terms to Replace or Define

Terms that should be defined in standard physics language or avoided:

- bridge
- one-slot
- two-slot
- rung
- payload
- degree wall
- no-doubling
- live/open stack
- theorem-grade
- killed route
- readout
- Paper stack
- white baseline
- horizon puncture load
- spatial Hodge complex
- rate-dressing
- GMP/TBS/WMR shorthand

Some of these are acceptable if defined as terms of art, but the first occurrence should use standard physics wording and then introduce the shorthand.

## Reproducibility-Bundle Inclusion Boundary

Include scripts that reproduce active numbers or live theorem-support surfaces:

1. R4/FIRAS dependency audit.
2. Closed-S3 scalar perturbation equations and discrete wavenumber dictionary.
3. Scalar bridge operator, branch selection, and uniqueness/proportionality checks.
4. White baseline and Hopf selection bookkeeping.
5. No-Doubling theorem and spectral-index numerical evaluation.
6. Tensor perturbation support statements.
7. Kappa-audit summary.
8. Frozen-output validator.

Do not include dead exploratory routes as executable bundle scripts. Preserve them in the private lab folder and cite them only if they remain live no-go evidence.
