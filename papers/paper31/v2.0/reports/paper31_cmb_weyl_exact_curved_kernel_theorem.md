# Paper 31: Exact Closed-S3 Weyl Kernel Theorem

Date: 2026-04-02

## Question

Can the half-order Weyl kernel be written exactly in the variables used by the
closed-universe Einstein-Boltzmann code, rather than only through its
large-`k` surrogate?

## Executive result

- `derived / scoped theorem`:
  on the closed scalar sector, the exact IO Weyl multiplier is
  \[
  M_{\rm IO}(k)
  =
  x^{-1/2}
  \left(
    \frac{k^2-3K}{k_p^2-3K}
  \right)^{-1/4},
  \]
  where `K > 0` is the closed-space curvature parameter, `k^2 = \lambda_N`, and
  `k_p` is the chosen pivot wavenumber.
- `derived`:
  in CLASS variables, since `q^2 = k^2 + K` for scalars,
  the same kernel is
  \[
  M_{\rm IO}(q)
  =
  x^{-1/2}
  \left(
    \frac{q^2-4K}{q_p^2-4K}
  \right)^{-1/4}.
  \]
- `derived`:
  for `k^2 \gg K`, this reduces to the already-closed surrogate
  \[
  x^{-1/2}\left(\frac{k}{k_p}\right)^{-1/2}.
  \]

So the half-order IO Weyl kernel is not merely asymptotic. It has an exact
closed-`S^3` realization in the curvature variables used by the transfer code.

## 1. Internal scalar operator

The current stack already fixes the physical scalar weight to

\[
\lambda_N-3
=(N-1)(N+3),
\]

through the intrinsic slice-curvature identity

\[
\delta {}^{(3)}R_N = -4 a^{-2}(\lambda_N-3)\Phi_N.
\]

The class gap closes to

\[
\alpha_\Phi-\alpha_\delta = \frac12,
\]

so the minimal scalar intertwiner is the negative half-order spectral power

\[
(\lambda_N-3)^{-1/4}.
\]

## 2. Curved-space translation

On a closed spatial slice of curvature `K = 1/R_{\rm curv}^2`, the scalar
harmonic eigenvalue in CLASS variables is

\[
k^2 = K\,N(N+2)=\lambda_N.
\]

Therefore

\[
\lambda_N-3K = k^2-3K.
\]

Since CLASS uses scalar `q` related by

\[
q^2 = k^2 + K,
\]

the same physical operator is

\[
\lambda_N-3K = q^2 - 4K.
\]

Hence the exact normalized Weyl kernel is

\[
M_{\rm IO}(k)
=
x^{-1/2}
\left(
\frac{k^2-3K}{k_p^2-3K}
\right)^{-1/4}
=
x^{-1/2}
\left(
\frac{q^2-4K}{q_p^2-4K}
\right)^{-1/4}.
\]

## 3. Large-k limit

For `k^2 \gg K`,

\[
\left(\frac{k^2-3K}{k_p^2-3K}\right)^{-1/4}
=
\left(\frac{k}{k_p}\right)^{-1/2}\left[1+O\!\left(\frac{K}{k^2}\right)\right].
\]

So the earlier `lcmb_tilt = -1/2` surrogate is exactly the flat/high-shell
limit of the closed-space kernel.

## 4. Code realization

The transfer hook in the local CLASS fork now supports the exact curved factor

\[
\left(
\frac{k^2 + sK}{k_p^2 + sK}
\right)^{p},
\]

through the new input parameters

- `lcmb_curved_shift`
- `lcmb_curved_order`

The exact IO closed-space choice is

```text
lcmb_rescale      = x^(-1/2)
lcmb_tilt         = 0
lcmb_pivot        = k_p
lcmb_curved_shift = -3
lcmb_curved_order = -1/4
```

for the `k`-space form, equivalently `-4` on the `q`-space form if a future
hook is written directly in `q`.

## 5. Meaning

This does not yet close the full CMB observable problem. But it does remove one
old ambiguity:

- `derived`: the exact curved-space form of the half-order kernel is now fixed
- `verified`: the old `k^{-1/2}` route was the correct asymptotic image, not an
  arbitrary fit ansatz

The remaining CMB task is observational, not algebraic:
rerun the strongest available Planck-style extraction with this exact curved
kernel rather than with the older flat surrogate.

## 6. Numerical support

The exact curved kernel is now implemented in the local CLASS fork through the
parameters

- `lcmb_curved_shift`
- `lcmb_curved_order`

and the one-fluid IO control refit is recorded in
[paper31_planck_weyl_exact_curved_refit_report.txt](/opt/cosmology-lab/results/paper31/paper31_planck_weyl_exact_curved_refit_report.txt).

Using the exact choice

```text
lcmb_rescale      = x^(-1/2)
lcmb_tilt         = 0
lcmb_curved_shift = -3
lcmb_curved_order = -1/4
```

the best point is

\[
A_s = 1.996220997273735\times 10^{-9},
\qquad
\tau = 0.0021,
\qquad
\chi^2 = 2832.407664.
\]

Compared with the previous large-`k` surrogate refit,

\[
\Delta \chi^2 = +0.002620,
\]

with the best-fit `A_s`, `tau`, `A_eff`, and `100theta_s` unchanged at the
reported precision.

So the exact closed-space implementation confirms that the earlier half-order
surrogate was already capturing the relevant Planck-scale effect.
