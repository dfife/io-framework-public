# Paper 30 v2.0 Alcock-Paczynski Residual Analysis

Date: 2026-05-19

Active branch inputs used by `papers/paper30/v2.0/scripts/01_full_twenty_test_recompute.py`:

* IO/Paper 29 projection branch: `H0 = 67.57585653582628 km/s/Mpc`, `Omega_m = 0.34868395067621694`, `Omega_k = -0.04579112576013168`, `Omega_Lambda = 0.69701575761593`, `Omega_r = 9.141746798467538e-05`, `r_d = 144.01351425392883 Mpc`.
* Fixed Planck LCDM comparator used by the active script: `H0 = 67.4 km/s/Mpc`, `Omega_m = 0.315`, `Omega_k = 0`, `Omega_Lambda = 0.6849081048663765`, `Omega_r = 9.189513362352906e-05`.
* Dataset: DESI DR2 BAO AP derived points from the same 6x6 covariance path used by the active recomputation script.

The active bundle gives IO `chi2 = 7.88341490487783`, probability-to-exceed `p = 0.24676969705560073`, matching the corrected dof `= 6` treatment for both fixed models.

## 1. Per-Point Residual Table

The residual is `data - model`. The `sigma` column is the diagonal 1-sigma uncertainty from the propagated AP covariance. The per-point chi2 contribution uses the full covariance via the symmetric inverse-square-root whitening convention; contributions sum to the full-covariance total chi2.

| z | F_AP obs | diag sigma | IO F_AP | Planck F_AP | data-IO | IO pull | IO chi2 contrib | data-Planck | Planck pull | Planck chi2 contrib |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.510 | 0.621824 | 0.017159 | 0.595158 | 0.593660 | +0.026667 | +1.554 | 2.398 | +0.028164 | +1.641 | 2.678 |
| 0.706 | 0.892077 | 0.020808 | 0.880698 | 0.877556 | +0.011379 | +0.547 | 0.301 | +0.014521 | +0.698 | 0.488 |
| 0.934 | 1.223256 | 0.019207 | 1.257492 | 1.251834 | -0.034236 | -1.782 | 3.180 | -0.028578 | -1.488 | 2.216 |
| 1.321 | 1.947788 | 0.045160 | 2.007067 | 1.996477 | -0.059279 | -1.313 | 1.723 | -0.048689 | -1.078 | 1.161 |
| 1.484 | 2.385605 | 0.136835 | 2.363099 | 2.350470 | +0.022506 | +0.164 | 0.027 | +0.035135 | +0.257 | 0.066 |
| 2.330 | 4.517943 | 0.096748 | 4.566817 | 4.547539 | -0.048873 | -0.505 | 0.255 | -0.029596 | -0.306 | 0.094 |

Totals:

* IO: `chi2 = 7.88341490487783`, dof `= 6`, `p = 0.24676969705560073`.
* Planck LCDM fixed reference: `chi2 = 6.702669976136264`, dof `= 6`, `p = 0.3492212777775587`.
* `Delta chi2 = chi2_IO - chi2_Planck = +1.1807449287415661`.

## 2. Leverage Analysis

Leave-one-out full-covariance chi2 values:

| removed z | IO chi2 | Planck chi2 | Delta chi2 |
|---:|---:|---:|---:|
| 0.510 | 5.493 | 4.032 | +1.461 |
| 0.706 | 7.583 | 6.215 | +1.367 |
| 0.934 | 4.704 | 4.486 | +0.217 |
| 1.321 | 6.162 | 5.544 | +0.618 |
| 1.484 | 7.858 | 6.639 | +1.218 |
| 2.330 | 7.631 | 6.610 | +1.021 |

The point whose removal most reduces IO chi2 is `z = 0.934`, reducing IO chi2 by `3.180`. The point whose removal most reduces Planck chi2 is `z = 0.510`, reducing Planck chi2 by `2.671` in the leave-one-out covariance calculation, with `z = 0.934` close behind by full-covariance contribution. The two largest IO contributions, `z = 0.934` and `z = 0.510`, account for `5.578` of the total `7.883`; removing both leaves `chi2_IO = 2.310` and `chi2_Planck = 1.812` on the remaining four-point subset.

By the full-covariance whitened contribution convention, IO fits better than Planck at `z = 0.510`, `z = 0.706`, and `z = 1.484`. Planck fits better at `z = 0.934`, `z = 1.321`, and `z = 2.330`.

## 3. z-Dependence of Residuals

Linear regression of diagonal residual pulls `(data - model) / sigma` against redshift:

* IO: intercept `+0.638`, slope `-0.7088 per unit z`, slope standard error `0.8679`, slope significance `-0.817 sigma`, two-sided p-value `0.460`.
* Planck: intercept `+0.786`, slope `-0.6850 per unit z`, slope standard error `0.8111`, slope significance `-0.844 sigma`, two-sided p-value `0.446`.

Verdict: no statistically meaningful redshift trend is detected in either model. The AP residual pattern is consistent with point-level scatter in this six-point sample, not a resolved systematic z-trend.

## 4. Closed-K Geometry Signature Check

The IO closed-K AP prediction is higher than the fixed flat Planck prediction at every DESI DR2 redshift, and the offset grows monotonically with redshift:

| z | IO - Planck F_AP | `(data-IO) - (data-Planck)` |
|---:|---:|---:|
| 0.510 | +0.001498 | -0.001498 |
| 0.706 | +0.003142 | -0.003142 |
| 0.934 | +0.005658 | -0.005658 |
| 1.321 | +0.010591 | -0.010591 |
| 1.484 | +0.012629 | -0.012629 |
| 2.330 | +0.019277 | -0.019277 |

Shape verdict: the model separation has a clean monotonic closed-geometry signature, but the observed residuals do not independently trace that signature as a detection. Because IO is uniformly higher than Planck, the residual-difference column is exactly the negative of the prediction difference. At the mid/high-z points where Planck gains most of the chi2 advantage, the data sit below both predictions, so the current six-point AP sample mildly prefers less upward AP shift than the closed-K IO branch supplies. This is not a significant z-trend and should not be framed as a curvature detection.

## 5. Jackknife Distribution of Delta chi2

Leave-one-out `Delta chi2 = chi2_IO - chi2_Planck` values:

`[+1.461, +1.367, +0.217, +0.618, +1.218, +1.021]`

Summary:

* Mean `Delta chi2 = +0.984`.
* Sample standard deviation `= 0.480`.
* Range `= +0.217` to `+1.461`.

Verdict: the full-sample `Delta chi2 = +1.181` is not a robust, uniform model-separation signal. It is strongly leveraged by the `z = 0.934` point; removing that point reduces the loss to `Delta chi2 = +0.217`. The sign remains positive in all six jackknife subsets, so Planck remains slightly favored under this statistic, but the magnitude is scatter-sensitive.

## 6. Recommended Section 3.4 Rewrite

The Alcock-Paczynski test is the only mild loss in the twenty-test scorecard. Using the DESI DR2 six-point AP vector and its full covariance, the fixed IO projection branch gives `chi2 = 7.883` for six points (`p = 0.247`), while the fixed Planck LCDM comparator gives `chi2 = 6.703` (`p = 0.349`), so `Delta chi2 = +1.181` against IO. Both fits are statistically acceptable; neither model is excluded. The loss is concentrated rather than broad: the largest IO leverage comes from `z = 0.934` (`-1.78 sigma`, full-covariance contribution `3.18`), followed by `z = 1.321` (`-1.31 sigma`, contribution `1.72`), while IO fits the `z = 0.510`, `z = 0.706`, and broad `z = 1.484` points slightly better than Planck under the same full-covariance whitening convention. A residual-pull regression against redshift gives an IO slope of `-0.709 +/- 0.868` per unit redshift, only `0.82 sigma` from zero, so the present six-point pattern is not a significant redshift trend. The closed-K IO branch predicts a monotonic upward AP shift relative to flat Planck, but the current residuals do not constitute a clean curvature-signature detection; the AP loss is best treated as point-level scatter with high future leverage. No IO parameter is refit in this comparison, so the AP row remains a genuine pre-registered mild loss and a useful target for DESI/Euclid follow-up.

Bottom-line recommendation: Tightening would materially improve Section 3.4. The current text is directionally honest, but it misses that the loss is strongly leveraged by `z = 0.934`, that the low-redshift `z = 0.510` point actually favors IO over Planck under the full-covariance contribution convention, and that the residual pattern does not support a curvature-signature claim.
