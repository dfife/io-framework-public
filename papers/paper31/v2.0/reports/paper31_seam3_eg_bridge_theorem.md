# Paper 31 Seam 3: `E_G` Bridge Theorem

Date: 2026-04-02

## Statement

Assume:

1. Premise 2 of the IO framework: interior weak-lensing and clustering obey the
   same accepted operator grammar as the exterior theory.
2. The density observable entering late-time growth belongs to the closed Paper
   19 clustering class
   \[
   \alpha_\delta = 3/2.
   \]
3. The Weyl/lensing observable belongs to the projected-curvature /
   intrinsic-slice family
   \[
   \alpha_\Phi = 2.
   \]

Then the IO Weyl-response bridge gives

\[
\frac{\Sigma_{\rm IO}}{\mu_{\rm IO}}
=
\frac{J_\Phi}{J_\delta}
=
x^{\alpha_\delta-\alpha_\Phi}
=
x^{-1/2}.
\]

Therefore the standard linear `E_G` statistic transforms as

\[
E_G^{\rm IO}(z)
=
\frac{\Sigma_{\rm IO}}{\mu_{\rm IO}}
\frac{\Omega_{m,0}}{f(z)}
=
x^{-1/2}\frac{\Omega_{m,0}}{f(z)}.
\]

Status:

- `derived / scoped theorem`

## Proof sketch

External cosmology already treats weak lensing and clustering as different
response channels:

- clustering / RSD probe the matter-response channel
- weak lensing probes the Weyl/light-response channel

This is exactly the logic behind the standard `E_G` statistic and the
`mu` / `Sigma` / `eta` phenomenology.

Internally:

- Paper 19 closes the density contrast observable at `alpha = 3/2`
- the Paper 31 internal `alpha_Phi` theorem closes the Weyl family at
  projected-curvature / intrinsic-slice `alpha = 2`
- the Paper 31 scalar weak-lensing Hodge theorem closes the scalar
  observer-side lensing package

Taking the ratio of the two Jacobians gives

\[
\frac{J_\Phi}{J_\delta}
=
\frac{x^{1-\alpha_\Phi}}{x^{1-\alpha_\delta}}
=
x^{-1/2}.
\]

The standard exterior definition of `E_G` is then multiplied by the same ratio.
QED.

## Numerical consequence

With

\[
x = 1.519,
\]

the suppression factor is

\[
x^{-1/2}=0.8113740489243784.
\]

On the active projected Schur clustering branch, the reproducible rerun in
[paper31_seam3_eg_bridge_theorem_report.txt](/opt/cosmology-lab/results/paper31/paper31_seam3_eg_bridge_theorem_report.txt)
gives:

\[
E_G^{\rm no\ slip}(z=0.57)=0.421165935448,
\]
\[
E_G^{\rm IO,\alpha=2}(z=0.57)=0.341723110314.
\]

Against the classic benchmark

\[
E_G(z=0.57)=0.42\pm0.056
\]

from Alam et al. 2016, the pulls are:

- no-slip projected Schur: `+0.02 sigma`
- `alpha = 2` Weyl bridge: `-1.40 sigma`

So the Weyl bridge survives this benchmark, but only mildly.

## Joint-boundary remark

Using the classic `E_G` benchmark and the carried weak-lensing target
`S8 = 0.79 \pm 0.02`, the implied `alpha_\Phi` intervals do **not** overlap at
`1 sigma` on the projected growth branch:

- from `E_G`: `alpha_\Phi \in [1.207, 1.849]`
- from `S8` with active `A_s`: `alpha_\Phi \in [2.013, 2.134]`
- from `S8` with older IO `A_s`: `alpha_\Phi \in [1.951, 2.072]`

So the theorem does not produce a perfect simultaneous `1 sigma` closure of
both `S8` and the classic `E_G` benchmark.

The honest status is therefore:

- `derived / scoped working theorem` for the scalar Weyl response,
- `verified mild tension` with classic `E_G`,
- `not derived`: full Seam 3 closure from one exact `alpha_\Phi` value.

## Interpretation

This matters because `E_G` is designed to be insensitive to galaxy bias and
`sigma8`. So unlike `S8`, the `E_G` test does **not** reduce to a primordial
amplitude-selection issue.

That makes `E_G` the cleanest external falsifier of the `alpha = 2`
Weyl-response theorem.

## Sources

- [paper19_pk_timelike_class_report.txt](/opt/cosmology-lab/results/paper19/paper19_pk_timelike_class_report.txt)
- [paper19_scalarization_jacobian_report.txt](/opt/cosmology-lab/results/paper19/paper19_scalarization_jacobian_report.txt)
- [paper31_seam3_weyl_response_bridge_theorem.md](/opt/cosmology-lab/results/paper31/paper31_seam3_weyl_response_bridge_theorem.md)
- [paper31_seam3_eg_bridge_theorem_report.txt](/opt/cosmology-lab/results/paper31/paper31_seam3_eg_bridge_theorem_report.txt)
- [Alam et al. 2016](https://arxiv.org/abs/1610.09410)
- [Reyes et al. 2010](https://arxiv.org/abs/1003.2185)
- [Bartelmann & Schneider 2001](https://arxiv.org/abs/astro-ph/9912508)
- [MGCAMB 2019](https://arxiv.org/abs/1901.05956)
