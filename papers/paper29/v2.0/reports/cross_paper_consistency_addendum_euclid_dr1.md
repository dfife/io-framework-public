# Cross-Paper Consistency Addendum: Euclid DR1 Extension

## Matter Density

- Paper 29 §5.6 value: `Omega_m,IO = 0.349`.
- Bundle value: `Omega_m,IO = 0.34868395067621694`.
- Source boundary: active Paper 10 legacy projected observer branch as carried in the current Paper 29 draft and Paper 32 active-branch growth artifacts.
- Status: PASS for the manuscript-declared branch.

Important caveat: some Paper 32 archive/briefing artifacts discuss a later
Schur branch with `Omega_m ≈ 0.336`. The current Paper 29 v2.0 draft explicitly
uses the active Paper 10 legacy branch `(H0, Omega_m, Omega_k, Omega_Lambda) =
(67.58, 0.349, -0.046, 0.697)`. This addendum follows the manuscript branch
and flags the branch-history caveat for Cosmo review.

## f sigma_8

- Native scalar amplitude source: Paper 26/Paper 31/Paper 32 active scalar-source stack, `A_s_native = 2.0072459972737347e-09`.
- Paper 32 one-slot field transfer: `f_Gamma = 1/(1+gamma_BI^2) = 0.9466055317260761`.
- Theorem-supported amplitude: `A_s_theorem = 1.9000701645543414e-09`.
- Active-branch clustering normalization: `sigma8(0) = 0.9274824965120383`.
- Growth index: standard GR `gamma_growth = 6/11`.
- Status: PASS as an active-branch conditional-verified prediction.

The script intentionally does not fit `sigma8` to Euclid, DESI, Planck, or
weak-lensing data.

## Dark Energy Equation of State

- Paper 29 §5.8 value: `(w0, wa) = (-1, 0)`.
- Bundle value: `(w0, wa) = (-1, 0)`.
- Framework basis: constant `rho_Lambda`/cosmological-constant slot on the
active observer branch. No dynamical dark-energy field is introduced.
- Status: PASS.

## Forecast-Margin Boundary

No official Euclid DR1 + DESI DR3 joint `w0-wa` covariance was found in public
sources during bundle construction. The script records conservative published
Euclid forecast marginal scales from Euclid preparation VII:

- pessimistic WL-only flat `w0-wa`: `sigma_w0 = 0.16`, `sigma_wa = 0.59`;
- optimistic WL-only flat `w0-wa`: `sigma_w0 = 0.14`, `sigma_wa = 0.49`.

These are placeholder falsification scales pending an official DR1+DR3 joint
forecast. They should not be described as an official Euclid DR1 + DESI DR3
forecast covariance.
