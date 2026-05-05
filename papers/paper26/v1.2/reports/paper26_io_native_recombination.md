# Paper 26 IO-Native Recombination Audit

## Physics Routing

- `derived`: the standard recombination chemistry depends on the hydrogen inventory `n_H`, so the IO-native input is `omega_b,geom`.
- `derived`: the Thomson opacity also counts actual free electrons `n_e = x_e n_H`, so it should follow `omega_b,geom`, not `omega_b,eff`.
- `derived`: the photon-baryon inertia ratio
  `R = 3 rho_b / (4 rho_gamma)`
  is an acoustic-loading quantity, so it should follow `omega_b,eff`.
- `derived`: the baryon temperature Compton-coupling rate simplifies so the explicit
  baryon-density dependence cancels; the density enters the thermal history through
  `n_H` in the heat capacity and chemistry, not as a separate extra `omega_b` factor.
- `derived`: late-time clustering `omega_b,clustering` does not enter the Peebles/HyRec chemistry or the visibility kernel directly.

## Standard Equation Bookkeeping

For hydrogen recombination, the Peebles equation has the standard form

`dx_e/dz = [ C_r / (H(z)(1+z)) ] [ beta_B(T_b) (1 - x_e) exp(-E_21/T_b) - n_H alpha_B(T_b) x_e^2 ]`

with

- `n_H = n_{H0} (1+z)^3`, `n_{H0} \propto omega_b,geom (1-Y_p)`
- `alpha_B`, `beta_B`, `Lambda_{2s1s}`, `K_H`, Lyman-alpha escape: standard atomic physics
- `H(z)`: IO background expansion

The visibility function requested by the user is

`g(z) = - d kappa / dz * exp(-kappa) = [kappa'(z)/H(z)] exp(-kappa)`

with `kappa'(z) = a n_e sigma_T = (1+z)^2 n_{H0} x_e sigma_T`.
Thus the opacity also uses `n_{H0} \propto omega_b,geom`.

The acoustic baryon loading remains

`R(z) = 3 rho_b,eff / (4 rho_gamma)`.

## Exact Outputs

Using the active IO branch:

- `H0 = 67.58`
- `Omega_k = -0.006`
- `omega_b,geom = 0.02108`
- `omega_b,eff = 0.0291`
- `omega_b,clustering = 0.01705`
- `A_s = 2.0072459972737347e-09`
- `tau = K_gauge/2 = 0.02743640887145733`

One-fluid control:

- `z_rec(class) = 1083.627653`
- `z_peak[g_tau] = 1083.805000`
- `z_peak[g(z)] = 1073.855000`
- `Delta z_rec(FWHM) = 198.849127`
- `r_s(z_peak) = 137.861469 Mpc`
- `D_A(z_peak) = 12.251319 Mpc`
- `r_A(z_peak) = 13168.391581 Mpc`
- `100 theta_s(z_peak) = 1.046911983`
- `chi2_TT_highl = 2281.086162`

IO-native typed recombination:

- `z_rec(class) = 1091.839931`
- `z_peak[g_tau] = 1091.765000`
- `z_peak[g(z)] = 1081.317500`
- `Delta z_rec(FWHM) = 207.054888`
- `r_s(z_peak) = 137.263506 Mpc`
- `D_A(z_peak) = 12.168103 Mpc`
- `r_A(z_peak) = 13169.751345 Mpc`
- `100 theta_s(z_peak) = 1.042263458`
- `chi2_TT_highl = 8133.493484`

Typed minus one-fluid:

- `delta z_peak[g(z)] = 7.462500`
- `delta Delta z_rec(FWHM) = 8.205761`
- `delta r_s(z_peak) = -0.597964 Mpc`
- `delta D_A(z_peak) = -0.083216 Mpc`
- `delta r_A(z_peak) = 1.359764 Mpc`
- `delta 100 theta_s(z_peak) = -0.004648524`
- `delta chi2_TT_highl = 5852.407321`

Planck-like reference for `100 theta_s`:

- `100 theta_s,Planck-like = 1.040373761`
- one-fluid offset: `+0.006538221`
- typed offset: `+0.001889697`

Visibility-peak caveat:

- `verified`: the redshift-space visibility `g(z)` peak is shifted below the conformal-time visibility peak `g_tau`.
- `verified`: the TT acoustic phase tracks the CLASS / `g_tau` definition (`100theta_s_class`), not the Jacobian-shifted `g(z)` peak ratio.

## Claim Boundary

- `verified`: the IO-native recombination model is now explicitly implemented in the CLASS fork by routing both chemistry and opacity through `omega_b,geom`, while keeping acoustic loading on `omega_b,eff`.
- `verified`: the resulting `x_e(z)` and `g(z)` are reproducible from the saved thermodynamics tables.
- `verified`: the TT fit consequence can be measured directly on the patched branch.
- `not derived`: this does not by itself derive the late-time reionization model; the run still uses the active `tau = K_gauge/2` closure branch.
