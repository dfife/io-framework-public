# Paper 28 - One-Form Trace-Log Gaussian Extension Theorem Audit

Date: 2026-03-31

## Executive result

This is the strongest field-side closure obtained so far.

- `derived`: if the boundary field is the coexact Ashtekar-Barbero `1`-form and
  the canonical extension is a centered `SO(3)`-invariant one-loop Gaussian
  extension, then the shell generator is

  \[
  w_\ell = \log s_\ell = \frac12 \log \lambda_\ell,
  \qquad
  s_\ell = \sqrt{\lambda_\ell}.
  \]

- `derived`: a covariance payload `alpha` acts by the inverse Gaussian kernel

  \[
  N_\ell = e^{-\alpha w_\ell}
          = s_\ell^{-\alpha}
          = \lambda_\ell^{-\alpha/2}.
  \]

- `conditional`: with the proved IO coefficient

  \[
  \alpha = \frac{K_{gauge}}{x},
  \]

  this yields the Paper 28 shell law.

At the pivot shell `N=712`:

- plus branch: `n_s = 0.963832748117`
- minus branch: `n_s = 0.963934220358`
- equal branch average: `n_s = 0.963883481680`
- exact shell target: `n_s = 0.963908639282`

## Theorem

On the canonical `S^2` coexact carrier:

1. Primitive line-transport dimensionality forces the spectral scale

   \[
   s = \sqrt{r_s^2 \Delta_1^{coex}}.
   \]

2. The standard one-loop determinant contributes per mode

   \[
   w_\ell = \frac12 \log \lambda_\ell = \log s_\ell.
   \]

3. For a centered invariant Gaussian extension with covariance payload `alpha`,
   the inverse covariance kernel is

   \[
   O_\ell = e^{\alpha w_\ell},
   \]

   so the bridge-read covariance is

   \[
   N_\ell = O_\ell^{-1}
           = e^{-\alpha w_\ell}
           = s_\ell^{-\alpha}
           = \lambda_\ell^{-\alpha/2}.
   \]

This is exactly the determinant-selected Gaussian shell law.

## Finite-shell consequences

Geometric baseline:

- `N=2`: `ns_geom=0.959744817084`
- `N=3`: `ns_geom=0.935461910844`
- `N=5`: `ns_geom=0.961744170971`
- `N=10`: `ns_geom=0.98729103068`
- `N=20`: `ns_geom=0.996409865383`
- `N=50`: `ns_geom=0.999385987859`
- `N=100`: `ns_geom=0.999843946473`
- `N=200`: `ns_geom=0.999961104729`
- `N=500`: `ns_geom=0.999991711483`
- `N=712`: `ns_geom=1.000032943241`
- `N=1000`: `ns_geom=1.000045409534`
- `N=2000`: `ns_geom=1.000314665137`

One-form trace-log determinant route, plus branch:

- `N=2`: `ns_plus=0.914589437113`
- `N=3`: `ns_plus=0.890306530877`
- `N=5`: `ns_plus=0.918395006232`
- `N=10`: `ns_plus=0.946733289378`
- `N=20`: `ns_plus=0.957834269347`
- `N=50`: `ns_plus=0.962220453887`
- `N=100`: `ns_plus=0.963188507903`
- `N=200`: `ns_plus=0.963568564221`
- `N=500`: `ns_plus=0.963759467145`
- `N=712`: `ns_plus=0.963832748117`
- `N=1000`: `ns_plus=0.963867027411`
- `N=2000`: `ns_plus=0.964163294931`

One-form trace-log determinant route, minus branch:

- `N=2`: `ns_minus=0.942184391515`
- `N=3`: `ns_minus=0.911078005753`
- `N=5`: `ns_minus=0.931927285117`
- `N=10`: `ns_minus=0.953816339869`
- `N=20`: `ns_minus=0.961426779668`
- `N=50`: `ns_minus=0.963664053284`
- `N=100`: `ns_minus=0.963910817992`
- `N=200`: `ns_minus=0.96392978499`
- `N=500`: `ns_minus=0.963903963072`
- `N=712`: `ns_minus=0.963934220358`
- `N=1000`: `ns_minus=0.963939275786`
- `N=2000`: `ns_minus=0.964199419232`

Equal branch average:

- `N=2`: `ns_avg=0.928163669708`
- `N=3`: `ns_avg=0.900579346837`
- `N=5`: `ns_avg=0.925115809969`
- `N=10`: `ns_avg=0.950262565097`
- `N=20`: `ns_avg=0.95962735466`
- `N=50`: `ns_avg=0.962941737173`
- `N=100`: `ns_avg=0.963549533093`
- `N=200`: `ns_avg=0.963749142084`
- `N=500`: `ns_avg=0.963831709852`
- `N=712`: `ns_avg=0.96388348168`
- `N=1000`: `ns_avg=0.96390315021`
- `N=2000`: `ns_avg=0.964181356721`

Exact shell target:

- `N=2`: `ns_target=0.923620513186`
- `N=3`: `ns_target=0.899337606932`
- `N=5`: `ns_target=0.925619866973`
- `N=10`: `ns_target=0.951166726668`
- `N=20`: `ns_target=0.960285561429`
- `N=50`: `ns_target=0.963261683874`
- `N=100`: `ns_target=0.963719642385`
- `N=200`: `ns_target=0.963836800838`
- `N=500`: `ns_target=0.963867407539`
- `N=712`: `ns_target=0.963908639282`
- `N=1000`: `ns_target=0.963921105671`
- `N=2000`: `ns_target=0.964190361068`

At `N=712`, the pure shell slopes are:

- plus: `-0.036200195041`
- minus: `-0.036098722799`
- average: `-0.036149461533`
- exact target: `-0.036124303986`

The exact target and the determinant branches differ only by the usual finite-branch
`O(N^{-1})` correction.

## Interpretation

This removes one more layer of arbitrariness:

- the `1`-form nature of the boundary field fixes the primitive line spectral
  scale;
- the one-loop determinant fixes the logarithmic shell generator;
- the Gaussian extension then fixes the inverse covariance kernel.

So the remaining premise is no longer "why this shell law?".
It is only:

`conditional`: the physical A-vacuum canonical extension is exactly this one-loop Gaussian extension of the coexact 1-form field.

That is the narrowest frontier I currently see.
