# Paper 20 v2.0 Scope, R4, and Kappa-Style Audit

## Executive Verdict

Paper 20 v2.0 is correctly narrower than the unpublished v1.8 support bundle.
The live manuscript no longer depends on the former bare package
reconstruction, assembly-gap diagnostic, torsion-Lambda branch, Delta N_eff
target search, or reduced-to-full extension sketch. Those artifacts are
therefore excluded from the v2.0 public bundle.

No hidden continuous fitted parameter was found in the live v2.0 surfaces.

The only load-bearing normalization inherited by Paper 20 is the optical
readout normalization R4. In v2.0 it is not claimed as internally derived by
Paper 20 and is not tuned against Paper 20 observables. R4 is inherited from
Paper 17 v1.5 as the FIRAS-fixed unique readout normalization:

```text
T_obs(R4) = T_IO * x^(R4 K_gauge)
R4_FIRAS = 1.0031014644
```

The observed cosmic microwave background temperature is not counted as an
independent Paper 20 prediction.

## Live v2.0 Surfaces

| Surface | v2.0 Status | Audit Verdict |
|---|---|---|
| Theorem 20.3 radiation scope-boundary | DERIVED/NO-GO at reduced-core scope | No hidden fit; reduced algebra lacks a fermionic family-count carrier. |
| Theorem 20.1 acoustic history reduction | DERIVED/THEOREM under AH1-AH7 | Premise package must remain visible. |
| Theorem 20.2 acoustic phase calibration | DERIVED/CONDITIONAL_VERIFIED through Paper 21 AC1 closure | Not fitted if AC1 closure is cited explicitly. |
| Corrected BBN comparison row | VERIFIED | Wrapper/amplitude inheritance, not a new Paper 20 fit. |
| Theorem 20.RAD1 radiation algebra | DERIVED/CONDITIONAL_VERIFIED as construction | Admissible construction, not uniqueness. |
| Theorem 20.RAD2 fermionic Bogoliubov consistency | DERIVED/CONDITIONAL_VERIFIED as consistency construction | Standard thermal physics import is visible. |
| Theorem 20.RAD3 bulk vacuum no-go | DERIVED/NO-GO | Wrong equation of state and negligible magnitude. |

## Removed v1.8 Bundle Materials

The following v1.8 bundle materials are no longer live Paper 20 v2.0 support
and were removed:

- Bare package reconstruction.
- Assembly-gap diagnostic.
- Torsion-Lambda branch script and outputs.
- Delta N_eff target search and old radiation target scaffolding.
- Reduced-to-full extension sketch, now superseded by Papers 31 and 32.

## R4 Impact

R4 appears only through inherited observer-side thermal readout statements:

```text
T_obs(R4) = T_IO * x^(R4 K_gauge)
```

The acoustic factor

```text
J_theta = x^(-1/2) * sqrt(1 + gamma_BI^2)
```

does not use R4. The corrected Big Bang nucleosynthesis wrapper row is also not
retuned by R4 inside Paper 20; the row is a wrapper/amplitude inheritance from
the Paper 20 correction sweep plus Paper 22 v1.5/v1.6 amplitudes.

## Manuscript Consistency Flag

The v2.0 draft uses the rounded acoustic sentence:

```text
theta*_pred = 0.599 deg, within 0.429% of Planck's 0.597 deg (9.2 sigma)
```

The frozen outputs distinguish two exact rows:

```text
legacy exact row:             0.5990414112379553 deg, 0.429421%, 9.85158 sigma
current bipartite rounded row: 0.598873398398795 deg,  0.401254%, 9.20538 sigma
```

This is not a fitted-parameter issue, but the manuscript should align the
percentage and sigma to the same exact row before final publication.

## Conclusion

Paper 20 v2.0 can be supported by a smaller public bundle than v1.8. The
published bundle should be `paper20-v2.0`; the unpublished `paper20-v1.8`
release/tag/directory should be retired.
