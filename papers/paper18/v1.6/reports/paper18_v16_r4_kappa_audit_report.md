# Paper 18 v1.6 R4/FIRAS and Kappa-Style Structural Audit

Date: May 2026

Target: Paper 18 v1.5, repaired toward Paper 18 v1.6

Scope: review Paper 18 scripts and manuscript claims for R4 damage, CMB-temperature overclaiming, and hidden fitted parameters. This is a structural audit, not a manuscript edit.

## Executive Verdict

No hidden continuous fitted parameter remains after the v1.6 repair boundary is applied.

Paper 18 v1.5 did contain a real stale overclaim: it treated `T_obs = T_IO*x^K_gauge = 2.7253 K` as theorem-grade output in the Bogoliubov/GTTP chain while also admitting R4 as a normalization premise/open problem. That is not acceptable after the Paper 17 v1.5 audit. The v1.6 repair is to remove the independent CMB-temperature prediction claim and replace the observer-side thermal readout with:

```text
T_obs(R4) = T_IO*x^(R4*K_gauge)
R4_FIRAS = 1.0031014644
T_obs(R4_FIRAS) = T_FIRAS = 2.7255 K
```

The theorem-grade part is the uniqueness of the readout normalization inside the stated family, inherited from Paper 17 v1.5. FIRAS is the empirical observer-side thermal datum. The CMB temperature is not counted as an independent IO prediction.

## R4 Usage Map

| Artifact | v1.5 use | v1.6 repair | Impact |
| --- | --- | --- | --- |
| `paper18_bogoliubov_coefficients_checks.py` | `T_obs = T_IO*x^K_gauge` | `T_obs = T_IO*x^(R4_FIRAS*K_gauge)` | Observer packet frequencies shift to FIRAS-fixed values. Planck occupation factors and CCR checks remain exact. |
| `paper18_modular_bogoliubov_upgrade_checks.py` | Modular transport used `K_gauge*lambda` | Modular transport uses `R4_FIRAS*K_gauge*lambda` | The modular pushforward again matches direct observer KMS covariance exactly. |
| `paper18_legacy_observables_recalculation_checks.py` | `T0_IO = 2.7253` in radiation density and CLASS calls | `T0_IO = T_FIRAS` via R4 | BAO, sigma8/S8, apparent `w0`, and radiation density shift slightly. Branch remains conditional because `N_eff=Delta` is withdrawn. |
| `paper18_jwst_age_recalculation_checks.py` | IO branch `T0 = 2.7253` | IO branch `T0 = T_FIRAS` | High-z conditional age table shifts at sub-Myr scale. Sign and caveat unchanged. |
| `paper18_matter_power_shape_test.py` | CAMB IO branch `T0 = 2.7253` | CAMB IO branch `T0 = T_FIRAS` | P(k) no-go remains catastrophic; `amp_const` chi2 changes from `1056.3648` to `1056.5532`. |
| `paper18_zeq_kruskal_audit_checks.py` | `T0 = 2.7253` | `T0 = T_FIRAS` | `z_eq` shifts from `2824.7087` to `2823.8794`. No promotion. |

R4 is not used in the CMP, BDP, V(alpha), entropy-rank algebra, curvature branch comparison, or structural-attack scripts.

## Numerical Impact

Active repaired constants:

```text
R4_FIRAS = 1.0031014644
T_IO = 2.6635 K
T_FIRAS = 2.7255 K
T_obs(R4_FIRAS) = 2.725499999999342 K
```

Selected changed outputs:

| Quantity | v1.5 implicit R4=1 | v1.6 FIRAS-fixed R4 | Status |
| --- | ---: | ---: | --- |
| Observer peak frequency in Bogoliubov packet | `160.2186642119 GHz` | `160.2301215246 GHz` | Repaired thermal readout |
| BAO branch chi2 | `19.8016385388` | `19.8016651616` | Conditional `N_eff=Delta` diagnostic |
| S8 with geometric baryons | `0.8023354478` | `0.8021928658` | Conditional branch diagnostic |
| Apparent flat-CPL `w0` | `-1.0060161101` | `-1.0060161104` | Diagnostic only |
| JWST age at z=10 | `445.691945 Myr` | `445.691268 Myr` | Conditional branch diagnostic |
| P(k) full-shape chi2, amp_const | `1056.3648` | `1056.5532` | Still catastrophic no-go |
| Equality redshift | `2824.7087` | `2823.8794` | Conditional branch diagnostic |

None of these shifts rescues or changes the Paper 18 conclusion that `N_eff=Delta` is mathematically valid as an entropy-rank but withdrawn as the Friedmann radiation parameter.

## Kappa Catalog and Classification

| Candidate field | Rigidity test | Classification |
| --- | --- | --- |
| `gamma_BI = 0.2375` | Imported as the Barbero-Immirzi value used across the framework; Paper 18 does not fit it to its observables. | Imported framework constant |
| `x = r_s/R_U` | Fixed by the active Schwarzschild-interior geometry branch; not varied in Paper 18 scripts. | DERIVED/SCOPED upstream |
| `K_geom = 4 ln x` | Forced by conformal 4-volume Radon-Nikodym ratio in the abelian history algebra. Changing 4 changes spacetime measure dimension. | DERIVED/THEOREM within C1-C5 |
| `K_gauge = ln(1+gamma^2)` | Inherited from Paper 17/Paper 14 gauge-side construction. Does not fix R4. | DERIVED/THEOREM on reduced gauge sector |
| Additive CMP product structure | Follows for product states/tensor product algebras on the reduced observer algebra. Full unreduced noncentral sectors remain scoped. | DERIVED/CONDITIONAL on C1-C5 |
| BDP observable type | Open covariant transport first variation is a line/1-form functional. | DERIVED/THEOREM in standard minimal-coupling matter class |
| BDP `x^-1` scaling | Forced for the line-transfer class on self-similar radial curves. | DERIVED/THEOREM in stated class |
| `V(alpha)=-2 ln cos alpha` | ODE rigidity and normalized gauge-center hierarchy force it in the stated class. | DERIVED/THEOREM |
| `Delta` entropy-rank | Uniform modular-cell covariance with total measure Delta has entropy-rank Delta. | DERIVED/THEOREM as math-only result |
| Physical `N_eff=Delta` | P(k) test falsifies the Friedmann-radiation identification. | WITHDRAWN / NO-GO for physical identification |
| `R4` optical readout normalization | Not forced by Paper 18 or Paper 17 modular stack alone; continuous rescaling remains allowed until FIRAS fixes it. | VISIBLE FIRAS-FIXED FIELD, not internally derived |
| `T_obs=2.7253 K` as IO prediction | Fails after R4 audit; the same datum fixes R4. | RETIRED overclaim |
| P(k) nuisance coefficients | Linear nuisance fits are used to test full-shape compatibility; they are not framework constants and must be visible. | Diagnostic fitted nuisances, not hidden framework parameters |
| Borrowed `A_s`, `n_s`, `tau` in CLASS diagnostics | Paper 18 states these are borrowed Planck-like inputs for sensitivity diagnostics. | Imported diagnostic inputs |

## Hidden-Parameter Finding

Paper 18 v1.5 had a hidden-status problem, not a hidden numerical optimizer:

```text
R4 was acknowledged as a premise/open problem but the text still promoted
T_obs = T_IO*x^K_gauge = 2.7253 K as theorem-grade.
```

After v1.6 repair, R4 is explicit, FIRAS-fixed, and frozen. No downstream script retunes R4 against BAO, P(k), JWST, BDP, or any other observable.

## CMB Prediction Removal

The following claim types must be removed or reworded in Paper 18 v1.6:

* `T_CMB = 2.7253 K` as an IO prediction.
* `T_obs = T_IO*x^K_gauge = 2.7253 K` as theorem-grade output.
* `Bogoliubov spectrum ... exact Planck spectrum at T_obs = T_IO*x^K_gauge` without mentioning FIRAS-fixed R4.
* Any scorecard row counting the observed CMB temperature as robust, N-independent IO evidence.

Safe replacement:

```text
Paper 18 inherits the Paper 17 v1.5 FIRAS-fixed readout theorem. The
Bogoliubov/CCR calculation proves Planck/KMS form in the reduced quasi-free
sector; the observer-side temperature entering that form is the FIRAS-fixed
readout T_obs(R4_FIRAS), not an independent CMB-temperature prediction.
```

## Final Recommendation

Proceed with Paper 18 v1.6 as a hygiene and reproducibility update:

1. Keep CMP, BDP, and V(alpha) theorem claims; they are R4-independent.
2. Keep the entropy-rank theorem but continue to label physical `N_eff=Delta` as withdrawn/no-go.
3. Keep the Bogoliubov spectrum theorem only as a Planck/KMS form theorem conditional on the reduced quasi-free sector and Paper 17 v1.5 FIRAS-fixed R4.
4. Remove independent CMB-temperature prediction language.
5. Publish the v1.6 reproducibility bundle with explicit R4 impact ledger and no hidden fitted-parameter claim.
