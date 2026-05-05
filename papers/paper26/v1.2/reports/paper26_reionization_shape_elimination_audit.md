# Paper 26 Reionization-Shape Elimination Audit

## Setup

Active IO branch:
- one-fluid / eff-equivalent pre-recombination baryon routing
- `omega_b = 0.0291`
- `omega_cdm = 0.13029026835999996`
- derived `A_s = 2.0072459972737347e-09`
- Route B `tau_eff = K_gauge/2 = 0.02743640887145733`
- geometric damping factor `exp(-K_gauge) = 0.9466055317260761`

## Baseline: CLASS `reio_camb`

- `chi2_TT_highl = 2281.086162`
- `chi2_TT_highl_plus_lowbins = 2285.975890`
- `A_eff = 1.9000701645543414e-09`
- low-`ell` EE bump peak on `2 <= ell <= 20`:
  - `ell_peak = 2`
  - `Dl_EE_peak = 1.5218490071033113e-02`
  - `sum_{2..20} Dl_EE = 6.0228913792537024e-02`

## `reio_none`

- `chi2_TT_highl = 1965.662093`
- `chi2_TT_highl_plus_lowbins = 1976.085634`
- low-`ell` EE peak:
  - `ell_peak = 20`
  - `Dl_EE_peak = 5.5811077303730148e-03`
  - `sum_{2..20} Dl_EE = 2.7369650012086497e-02`

## `reio_none` + post-hoc geometric damping

- apply `C_ell -> exp(-K_gauge) C_ell`
- `chi2_TT_highl = 2281.456815`
- `chi2_TT_highl_plus_lowbins = 2286.014069`
- `A_eff = 1.9000701645543414e-09`
- TT shape relative to baseline for `ell >= 30`:
  - `mean ratio = 0.999957912493`
  - `max |delta C_ell / C_ell| = 2.471564247957e-03`
- low-`ell` EE after damping:
  - `ell_peak = 20`
  - `Dl_EE_peak = 5.2831074507302617e-03`
  - `sum_{2..20} Dl_EE = 2.5908262102847749e-02`

## Reionization-shape sweep at fixed `tau`

Largest TT high-`ell` shift among the tested default-shape perturbations:
- case `width_0.2`
- `chi2_TT_highl = 2281.325035`
- `delta chi2 = +0.238873`
- `max |delta C_ell / C_ell|_{ell>=30} = 7.969040677931e-04`

## Claim boundary

- `verified`: TT high-`ell` can be tested with `reio_none` plus post-hoc geometric damping on the same Planck-lite code path.
- `verified`: low-`ell` EE does not get a reionization bump from a pure multiplicative geometric damping law.
- `derived boundary`: if the only IO late-time effect is geometric covariance damping, the CLASS `reio_camb` shape defaults are unnecessary for TT high-`ell` but still matter for the low-`ell` EE bump.
