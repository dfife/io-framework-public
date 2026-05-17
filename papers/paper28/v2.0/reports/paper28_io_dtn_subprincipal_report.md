# Paper 28 - IO DtN Map To Subprincipal Order

## Discipline label

- label state: `CONDITIONAL_VERIFIED`
- registry check: Vectors 1-5 reviewed. No unresolved load-bearing circularity-vector hit remains on this surface after the present audit.
- chain verification: inline-verified through the cited Paper 28 operator/transport chain to assumed-good Papers 1-28 nodes; no hidden admission remains load-bearing on the active Paper 32 chain.
- admitted inputs surfaced here: none.
- usage rule: this theorem may be cited as a premise because it is `CONDITIONAL_VERIFIED`.


Date: 2026-03-31

## Executive result

`derived`: on the flat Painleve-Gullstrand collar reduction of the source-side
coexact Ashtekar-Barbero perturbation problem, the boundary effective
Hessian is exactly the Euclidean `B^3(r_s)/S^2(r_s)` coexact `1`-form
Dirichlet-to-Neumann operator.

Its exact shell law is

\[
\sigma_\ell = \frac{\ell+1}{r_s}
= \sqrt{\lambda_\ell+\frac{1}{4r_s^2}}+\frac{1}{2r_s},
\qquad \lambda_\ell=\frac{\ell(\ell+1)}{r_s^2}.
\]

So the exact operator identity is

\[
\Lambda_{\mathrm{DtN}}^{\mathrm{coex}}
= \sqrt{\Delta_{1,S^2}^{\mathrm{coex}}+\frac{1}{4r_s^2}}+\frac{1}{2r_s}.
\]

`conditional`: if the full reduced IO bulk operator agrees with this
flat-collar model to the boundary first jet, then the full IO DtN map can
differ only by lower-order shell terms. On the Paper 28 tilt, such
deformations are numerically tiny.

## Why this is the right reduced model

- The source field is a boundary Ashtekar-Barbero `1`-form.
- The active source carrier is the coexact `1`-form sector.
- The reduced tangential/gauge sector is effectively abelian and its
  `gamma` dependence is a shell-blind scalar factor `Q = 1 + gamma^2`.
- In Painleve-Gullstrand slicing, the Schwarzschild spatial source collar is
  flat, so the reduced coexact spatial operator is Maxwell/Laplace-type on a
  Euclidean ball model bounded by the round horizon sphere.

Therefore the shell selector is the coexact differential-form DtN operator.

## Exact shell identity check

| ell | lambda_ell | sigma_ell | sqrt(lambda+1/4)+1/2 | gap |
|---:|---:|---:|---:|---:|
| 1 | 2.000000 | 2.000000 | 2.000000 | 0.0e+00 |
| 2 | 6.000000 | 3.000000 | 3.000000 | 0.0e+00 |
| 5 | 30.000000 | 6.000000 | 6.000000 | 0.0e+00 |
| 10 | 110.000000 | 11.000000 | 11.000000 | 0.0e+00 |
| 20 | 420.000000 | 21.000000 | 21.000000 | 0.0e+00 |
| 50 | 2550.000000 | 51.000000 | 51.000000 | 0.0e+00 |
| 100 | 10100.000000 | 101.000000 | 101.000000 | 0.0e+00 |
| 200 | 40200.000000 | 201.000000 | 201.000000 | 0.0e+00 |
| 500 | 250500.000000 | 501.000000 | 501.000000 | 0.0e+00 |
| 711 | 506232.000000 | 712.000000 | 712.000000 | 0.0e+00 |
| 1000 | 1001000.000000 | 1001.000000 | 1001.000000 | 0.0e+00 |

## Pivot shell

- `N = 712`
- `k_MS = 712.997194945394`
- `Delta_geom = 0.666667715742`
- `n_s(geom) = 1.000032943241`
- `n_s(geom + DtN plus branch) = 0.963858187553`
- `n_s(geom + DtN minus branch) = 0.963959517376`
- `n_s(geom + DtN equal-branch average) = 0.963908849852`
- pure covariance shell slope, plus branch: `-0.036174755688`
- pure covariance shell slope, minus branch: `-0.036073425892`
- pure covariance shell slope, equal average: `-0.036124093333`

## Lower-order deformation sensitivity

Test shell laws

\[
\sigma_\ell^{(a)} = (\ell+1) + \frac{a}{\ell+1}
\]

which model genuine lower-order `O(ell^-1)` deviations from the exact
coexact-ball DtN spectrum.

| a | pivot n_s |
|---:|---:|
| -5.0 | 0.963857474017 |
| -2.0 | 0.963857902161 |
| -1.0 | 0.963858044912 |
| -0.5 | 0.963858116233 |
| 0.0 | 0.963858187553 |
| 0.5 | 0.963858258929 |
| 1.0 | 0.963858330194 |
| 2.0 | 0.963858473056 |
| 5.0 | 0.963858901034 |

These shifts are only at the `10^-7` to `10^-6` level. So once the Hessian is
in the coexact first-order DtN class with the same flat-collar first jet, the
Paper 28 tilt is effectively fixed.

## Conclusion

`derived`: the exact flat-collar reduced Ashtekar-Barbero source problem is
the coexact `1`-form Euclidean DtN problem, with shell law `sigma_ell =
(ell+1)/r_s`.

`conditional`: the full IO boundary effective Hessian equals that operator
up to lower-order terms if the reduced boundary-to-entry bulk operator agrees
with the flat-collar model to the boundary first jet.

`not derived`: the full reduced Ashtekar-Barbero bulk operator on the entire
boundary-to-entry strip has still not been written down exactly, so exact
global equality beyond the flat-collar model remains open.

But the remaining freedom is now extremely narrow: it cannot change the
leading or subprincipal shell law, and numerically it barely moves the pivot
tilt.
