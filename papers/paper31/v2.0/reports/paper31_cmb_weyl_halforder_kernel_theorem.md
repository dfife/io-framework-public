# Paper 31: CMB Weyl Half-Order Kernel Theorem

Date: 2026-04-02

## Question

Can the surviving IO CMB-lensing route be promoted beyond a mere fit surrogate,
using only the internal observable-class ladder plus standard spectral calculus
on the closed `S^3` scalar sector?

## Executive result

- `derived / scoped theorem`:
  the class gap
  \[
  \alpha_\delta - \alpha_\Phi = \frac32 - 2 = -\frac12
  \]
  implies that the minimal linear mode-by-mode intertwiner from the transport
  density class to the intrinsic-slice Weyl class is a **half-order inverse
  spectral operator** on the scalar harmonic sector.
- `derived / scoped theorem`:
  on closed `S^3`, with
  \[
  -\Delta_{S^3} Q_N = \lambda_N Q_N,
  \qquad
  \lambda_N = N(N+2),
  \]
  and physical inhomogeneous scalar shell weight `\lambda_N-3`, the minimal
  field-level multiplier is
  \[
  M_N^{\rm IO}
  =
  x^{-1/2}
  \left(
    \frac{\lambda_N-3}{\lambda_{N_p}-3}
  \right)^{-1/4}.
  \]
- `derived / asymptotic corollary`:
  in the high-shell / locally flat limit `\lambda_N \sim k^2`, this becomes
  \[
  M^{\rm IO}(k)
  \sim
  x^{-1/2}\left(\frac{k}{k_p}\right)^{-1/2}.
  \]
  So the CLASS surrogate
  \[
  lcmb\_rescale = x^{-1/2},
  \qquad
  lcmb\_tilt = -\frac12
  \]
  is the correct large-`N` / large-`k` representative of the internal
  half-order kernel.
- `verified`:
  on the one-fluid IO control branch, the exact half-order surrogate refit gives
  \[
  A_s = 1.996220997273735\times 10^{-9},
  \qquad
  \tau = 0.0021,
  \qquad
  \chi^2 = 2832.405044,
  \]
  which is substantially better than the GR-control best fit
  \[
  \chi^2 = 2888.310869.
  \]

So the best honest statement is:

\[
\boxed{
\text{The surviving CMB-side theorem target is a half-order Weyl kernel, whose
large-}k\text{ limit is exactly }x^{-1/2}(k/k_p)^{-1/2}.
}
\]

## 1. Internal class gap

The current stack already closes:

\[
\alpha_\delta = \frac32,
\qquad
\alpha_\Phi = 2.
\]

Therefore

\[
\Delta\alpha := \alpha_\Phi - \alpha_\delta = \frac12.
\]

Interpretation:

- the transport / continuity scalarization of the primitive line observable
  carries one extra half inverse-length;
- the intrinsic slice / Weyl scalarization carries one extra full inverse-length.

So the Weyl-side scalar family differs from the density-side family by exactly
one **half-order** in inverse length.

## 2. Spectral realization on `S^3`

On the closed scalar harmonic carrier,

\[
-\Delta_{S^3}Q_N = \lambda_N Q_N,
\qquad
\lambda_N = N(N+2).
\]

For the scalar constraint and intrinsic curvature identity, the physical scalar
weight is the shifted combination

\[
\lambda_N - 3 = (N-1)(N+3).
\]

This is the same operator appearing in

\[
\delta{}^{(3)}R_N = -4 a^{-2}(\lambda_N-3)\Phi_N.
\]

By standard spectral calculus on compact manifolds, an operator of order `s`
acts mode-by-mode as a multiplier `(\lambda_N-3)^{s/2}` on the physical scalar
shells. Therefore the relative map between the `\alpha=3/2` density class and
the `\alpha=2` Weyl class is represented minimally by

\[
(\lambda_N-3)^{-\Delta\alpha/2}
=
(\lambda_N-3)^{-1/4}.
\]

This is the key theorem step.

## 3. Normalized IO Weyl kernel

The already-derived class Jacobian contributes the field-level constant factor

\[
\frac{J_\Phi}{J_\delta} = x^{-1/2}.
\]

Normalizing at a reference shell `N_p` gives the dimensionless mode multiplier

\[
M_N^{\rm IO}
=
x^{-1/2}
\left(
\frac{\lambda_N-3}{\lambda_{N_p}-3}
\right)^{-1/4}.
\]

This is the minimal scalar harmonic kernel compatible with:

1. the internal class gap `\Delta\alpha = 1/2`,
2. the closed `S^3` scalar spectral calculus,
3. the already-derived Weyl-response factor `x^{-1/2}`.

## 4. Large-`N` / CLASS limit

For large shells,

\[
\lambda_N = N(N+2) \sim N^2,
\]

and under the usual local-FRW / flat-sky identification `k \propto N`, one gets

\[
(\lambda_N-3)^{-1/4}\sim k^{-1/2}.
\]

So the leading large-`k` representative is exactly

\[
M^{\rm IO}(k)
\sim
x^{-1/2}\left(\frac{k}{k_p}\right)^{-1/2}.
\]

That is why the CLASS surrogate with

```text
lcmb_rescale = x^(-1/2)
lcmb_tilt    = -1/2
```

is not ad hoc. It is the asymptotic image of the internal half-order kernel.

## 5. Numerical support

The exact half-order surrogate refit is recorded in
[paper31_planck_weyl_halforder_refit_report.txt](/opt/cosmology-lab/results/paper31/paper31_planck_weyl_halforder_refit_report.txt).

On the one-fluid IO control branch it gives

\[
A_s = 1.996220997273735\times 10^{-9},
\]
\[
\tau = 0.0021,
\]
\[
\chi^2 = 2832.405044.
\]

Compared with the GR-control best fit

\[
\chi^2_{\rm GR,best}=2888.310869,
\]

the improvement is

\[
\Delta\chi^2 = -55.905825.
\]

The fitted free-tilt optimum from the earlier scan was

\[
t_{\rm lens}=-0.4625,
\]

so the exact theorem value `-1/2` is already close to the phenomenological
best point.

## 6. Exact claim boundary

### Derived / scoped

- the class gap is `1/2`
- the minimal relative spectral order is therefore `-1/4` in `\lambda_N-3`
- the large-`k` kernel is `x^{-1/2}(k/k_p)^{-1/2}`

### Verified

- the exact half-order surrogate improves the PlanckLite fit over the GR
  control on the tested branch

### Conditional

- using CLASS's `lcmb_tilt` hook as a faithful enough representative of the
  true IO lensing-kernel modification

### Not derived

- the exact full curved-space CMB lensing kernel replacing the surrogate hook
- the full Planck `TT,TE,EE+lowE+lensing` re-extraction with that kernel
- the astrophysical meaning of the low `\tau` value returned by the
  `TTTEEE+lowTT` surrogate fit alone

## Bottom line

The CMB route survives at theorem level in the following form:

\[
\boxed{
\text{the internal Weyl-vs-density class gap induces a half-order inverse
spectral kernel,}
}
\]

whose large-`k` image is

\[
x^{-1/2}(k/k_p)^{-1/2}.
\]

That is the strongest clean CMB-side theorem currently available.
