# Paper 28 - Exclusion Of O(1) IO DtN Shell Deformations

Date: 2026-03-31

## Theorem

On the exact flat Painleve-Gullstrand spatial collar, suppose the reduced
source-side Ashtekar-Barbero bulk operator on the canonical coexact carrier is
Laplace-type. Then after the Euclidean boundary first jet is fixed, any
remaining Ashtekar-Barbero correction enters as a bounded shell-blind
endomorphism or scalar factor inside the square-root symbol.

Therefore the DtN eigenvalues satisfy

\[
\sigma_\ell^{IO} = (\ell+1) + O((\ell+1)^{-1}),
\]

so genuine `O(1)` shell deformations are excluded.

## Proof sketch

1. The constant-PG-time Schwarzschild spatial metric is exactly Euclidean, so
   the intrinsic collar geometry is the Euclidean ball model bounded by the
   round sphere `S^2(r_s)`.
2. The boundary first jet is therefore exactly the Euclidean one: same induced
   round metric and same second fundamental form / mean curvature.
3. Standard DtN symbol calculus fixes the principal term from `|xi|` and the
   subprincipal term from that first jet. On the Euclidean sphere this is the
   exact coexact-ball law `sigma_ell = ell+1`.
4. In the reduced Ashtekar-Barbero source sector, the proved `gamma` dependence
   is shell-blind: `O_A = Q O_Gamma` with `Q = 1 + gamma^2`. Any remaining
   local Ashtekar-Barbero term is therefore a bounded shell-blind endomorphism
   `E` on the coexact carrier.
5. A bounded zero-order term enters the DtN root as

\[
\sqrt{|\xi|^2 + E} = |\xi| + \frac{E}{2|\xi|} + O(|\xi|^{-3}),
\]

   so it contributes only `O(1/ell)` to shell eigenvalues, never `O(1)`.

## Explicit model

For a shell-blind endomorphism eigenvalue `mu^2`, the flat-collar shell law is

\[
\sigma_\ell(\mu^2) = \sqrt{\ell(\ell+1) + \frac14 + \mu^2} + \frac12,
\]

hence

\[
\sigma_\ell(\mu^2) - (\ell+1)
= \frac{\mu^2}{\sqrt{\ell(\ell+1)+\frac14+\mu^2}+\ell+\frac12}
= O((\ell+1)^{-1}).
\]

At the pivot shell `ell = 711` (`m = 712`):

| mu^2 | shell shift | simple bound mu^2/(ell+1) | pivot n_s |
|---:|---:|---:|---:|
| 0.00000000 | 0.000000000000e+00 | 0.000000000000e+00 | 0.963858187553 |
| 0.05640625 | 3.963896585901e-05 | 7.922226123596e-05 | 0.963858191555 |
| 1.00000000 | 7.027403416942e-04 | 1.404494382022e-03 | 0.963858258873 |
| 10.00000000 | 7.027372182733e-03 | 1.404494382022e-02 | 0.963858901756 |
| 100.00000000 | 7.027059876521e-02 | 1.404494382022e-01 | 0.963865329531 |

Even very large shell-blind bounded terms only produce `O(1/ell)` shell
shifts. They do not create a new `O(1)` spectral deformation class.

## Conclusion

`derived`: on the PG-flat collar, `O(1)` shell deformations of the IO coexact
DtN map are excluded for any Laplace-type reduced bulk operator with shell-blind
Ashtekar-Barbero lower-order terms.

`conditional`: to evade this conclusion one would need a full-IO reduced bulk
operator whose boundary symbol contains a genuinely shell-dependent zeroth-order
endomorphism not already fixed by the Euclidean first jet and not reducible to
the proved shell-blind `Q = 1 + gamma^2` factor. The current archive gives no
evidence for such a term.
