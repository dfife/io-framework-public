# Paper 28 - Coexact DtN Hessian Audit

Date: 2026-03-31

## Executive result

`derived`: the standard boundary-effective operator for a linear bulk field is
the Dirichlet-to-Neumann operator. On the model `B^3/S^2` coexact `1`-form
problem, its exact shell spectrum is

\[
\sigma_\ell = \ell + 1.
\]

So the one-loop shell generator is

\[
w_\ell = \log(\sigma_\ell) = \log(\ell + 1),
\]

which is exactly the logarithmic class required by the earlier necessity theorem.

## Why this matters

This is stronger than the earlier abstract trace-log route:

- the primitive line spectral scale is no longer only dimensional analysis;
- the physical quadratic boundary operator is a standard DtN Hessian;
- its one-loop determinant automatically gives a logarithmic shell generator.

## Exact model formulas

- `S^2` coexact Hodge-Laplacian shell:
  - `lambda_ell = ell(ell+1)`
- `B^3/S^2` coexact `1`-form DtN shell:
  - `sigma_ell = ell + 1`
- determinant-selected covariance:
  - `N_ell proportional to sigma_ell^(-K_gauge/x) = (ell+1)^(-K_gauge/x)`

Under the Paper 23 branches:

- plus branch `ell = N - 1` gives `N_ell proportional to N^(-K_gauge/x)`
- minus branch `ell = N + 1` gives `N_ell proportional to (N+2)^(-K_gauge/x)`

## Pivot shell N = 712

- geometric baseline times DtN plus branch: `n_s = 0.963858187553`
- geometric baseline times DtN minus branch: `n_s = 0.963959517376`
- geometric baseline times equal branch average: `n_s = 0.963908849852`
- geometric baseline times exact shell target: `n_s = 0.963908639282`

Pure covariance shell slopes at the pivot:

- DtN plus branch: `-0.036174755688`
- DtN minus branch: `-0.036073425892`
- DtN average: `-0.036124093333`
- exact target: `-0.036124303986`

Same-symbol first-order deformation check using shell laws `(N+c)^(-K_gauge/x)`:

- `c=-2`: `n_s = 0.963756286834`
- `c=-1`: `n_s = 0.963807308847`
- `c=-0.5`: `n_s = 0.963832766128`
- `c=0`: `n_s = 0.963858187553`
- `c=0.5`: `n_s = 0.963883573235`
- `c=1`: `n_s = 0.963908923451`
- `c=2`: `n_s = 0.963959517376`

## Conclusion

`derived`: a DtN boundary Hessian is the most natural standard-physics object for
the missing `G^(1)(ell)` selector in linear Gaussian boundary-to-bulk theory.

`verified`: on the exact `B^3/S^2` coexact `1`-form model, the determinant
DtN shell law lands essentially on the surviving Paper 28 target.

The remaining boundary is now very narrow:

`conditional`: the physical IO boundary effective Hessian for the Ashtekar-Barbero
perturbation field is the relevant coexact differential-form Dirichlet-to-Neumann
operator (or a same-symbol first-order deformation), with payload coefficient
`K_gauge/x`.
