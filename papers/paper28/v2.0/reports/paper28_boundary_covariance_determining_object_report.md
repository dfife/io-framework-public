# Paper 28 - What Determines G^(1)(ell)?

Date: 2026-03-31

## Direct answer

`derived`: in linear Gaussian perturbation theory, the one-particle covariance
`G^(1)(ell)` is determined by one object:

\[
Q = \Gamma_{eff}''[\bar A]
\]

restricted to the canonical coexact carrier.

Once that quadratic operator `Q` and the state-to-covariance functional are
specified, the shell law is fixed.

So the real missing physical object has a precise name:

**the coexact-sector boundary effective Hessian**.

## Candidate physics and what each gives

1. Standard free-field Gaussian:
   - `Q = Delta_1^coex`
   - bridge-relevant shell law: `lambda_ell^(-1/2)`
   - pivot `n_s = -0.002067888629`

2. Ordinary Hawking/KMS on the intrinsic Hodge generator:
   - `Q = Delta_1^coex`, state = KMS on `sqrt(Q)`
   - shell law: `exp(-4 pi sqrt(lambda_ell))`
   - pivot `n_s = -8958.753929307341`

3. Determinant-selected Gaussian one-form extension:
   - `Q = (sqrt(Delta_1^coex))^(K_gauge/x)`
   - shell law: `lambda_ell^(-K_gauge/(2x))`
   - pivot `n_s = 0.963832748117`

4. Exact surviving shell target:
   - shell law: `k_MS(N)^(-K_gauge/x)`
   - pivot `n_s = 0.963908639282`

## Conclusion

`derived`: linearity and Gaussianity do **not** fix `G^(1)` by themselves.
They only tell us that `G^(1)` comes from the quadratic boundary operator
`Q = Gamma_eff''[Abar]`.

`verified`: among the concrete candidates tested so far:

- free-field `Q = Delta` gives the wrong coefficient;
- ordinary Hawking/KMS on `sqrt(Delta)` is badly wrong;
- the determinant-selected Gaussian `Q = (sqrt(Delta))^(K_gauge/x)` is the only
  candidate that lands on the surviving mild shell law.

So the sharp remaining physics question is:

**what is the actual coexact-sector Hessian `Gamma_eff''[Abar]` for the boundary Ashtekar-Barbero perturbation field?**
