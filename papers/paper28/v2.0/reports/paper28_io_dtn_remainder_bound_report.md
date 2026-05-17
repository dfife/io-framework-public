# Paper 28 - IO DtN Remainder Bound

Date: 2026-03-31

## Theorem

Let the full IO coexact DtN eigenvalues satisfy

\[
\sigma_\ell^{IO} = (\ell+1) + \varepsilon_\ell,
\qquad |\varepsilon_\ell| \le \frac{A}{\ell+1},
\]

so the deviation from the exact flat-PG coexact-ball law is shellwise
order `-1`.

For the determinant-selected covariance

\[
G_\ell \propto (\sigma_\ell^{IO})^{-\beta},
\qquad \beta = K_{gauge}/x,
\]

one has the exact slope-error bound

\[
\left|\frac{d\ln G_\ell}{d\ln(\ell+1)} + \beta\right|
\le \frac{2\beta A}{(\ell+1)^2 - A}.
\]

So any genuine full-IO correction that starts at order `-1` changes the
Paper 28 shell slope only at order `beta / ell^2`.

## Pivot shell ell = 711

- `beta = 0.036124303978219`
- `m = ell+1 = 712`

| A | max |delta slope| |
|---:|---:|
| 1 | 1.425182080755e-07 |
| 5 | 7.125966630742e-07 |
| 10 | 1.425207383139e-06 |
| 50 | 7.126599245250e-06 |
| 100 | 1.425460456402e-05 |
| 500 | 7.132931573524e-05 |

Even a fairly large order-`-1` coefficient `A = 100` changes the shell
slope by at most about `1.43e-5` at the pivot. For `A = 1..10`, the effect
is `1e-7` to `1e-6`.

## Conclusion

`derived`: if the full IO operator matches the exact PG-flat coexact DtN
law through subprincipal order, then all remaining shell corrections are
negligible for the Paper 28 tilt at CMB shells.

`conditional`: the only way to materially change the Paper 28 tilt would be
for the full IO Hessian to violate the flat-collar first-jet matching and
inject an `O(1)` shell deformation. The current archive gives no evidence
for such a term.
