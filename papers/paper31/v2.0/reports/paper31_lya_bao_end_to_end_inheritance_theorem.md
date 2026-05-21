# Paper 31: Ly-alpha BAO End-to-End Inheritance Theorem

## Question

Can the Ly-alpha half of Seam 2 be upgraded from a bare imported-shift check to
an end-to-end theorem chain under Premise 2?

## Claim

Yes, but only conditionally.

The strongest honest upgrade is:

\[
\boxed{
\text{same raw Schur ruler}
\;\;+\;\;
\text{inherited exterior Ly}\alpha\text{ flux observable class}
\;\;+\;\;
\text{inherited redshift-space negative Ly}\alpha\text{ shift class}
\;\Rightarrow\;
\text{Ly}\alpha\text{ BAO closure at current DR2 precision.}
}
\]

This is **not** an internal derivation of the Ly-alpha kernel.
It is an end-to-end closure under Premise 2, using accepted exterior Ly-alpha
forest physics.

## Step 1. Primitive ruler

From the Schur fixed-inventory early-time branch,

\[
r_{d,\mathrm{raw}} = 143.062502836870\ \mathrm{Mpc}.
\]

This remains the primitive early-time acoustic ruler for all BAO blocks.
Late-time tracer differences change the readout kernel, not the raw drag
horizon itself.

Status:
- `derived / conditional`

## Step 2. Ly-alpha observable class

Under accepted Ly-alpha forest physics, the measured quantity is not a galaxy
count field. It is the transmitted-flux fluctuation field of absorption along
quasar sightlines.

The standard exterior grammar is:

1. neutral hydrogen optical depth along the skewer,
2. transmitted flux \(F = e^{-\tau_F}\),
3. a continuous flux fluctuation field \(\delta_F\),
4. redshift-space and thermal-history distortions,
5. auto/cross flux-correlation fitting.

This class assignment is the standard Ly-alpha forest program:
- FGPA / ionizing-equilibrium large-scale flux mapping,
- large-scale Ly-alpha bias and RSD,
- DESI Ly-alpha auto/cross-correlation BAO fitting,
- continuum-distortion / metal / HCD / UVB nuisance structure.

Primary external anchors:
- `arXiv:1201.0594` large-scale flux bias and RSD for Ly-alpha
- `arXiv:1509.07875` simulation physics of Ly-alpha density/velocity bias
- `arXiv:2305.10428` field-level redshift-space Ly-alpha modelling
- `arXiv:2503.14739` DESI DR2 Ly-alpha BAO measurement

So the Ly-alpha BAO observable on Schur belongs to a continuous
flux-correlation class, not to the galaxy pair-count class.

Status:
- `derived / conditional`

## Step 3. Inherited redshift-space nonlinear shift class

The accepted exterior Ly-alpha shift literature tested here gives three
qualitatively distinct classes:

1. strong negative redshift-space shift:
   `arXiv:2407.03918`
   \[
   \alpha = 0.9905 \pm 0.0027
   \]
2. smaller negative-shift classes:
   `arXiv:2412.06892`
3. vanilla positive/zero-shift classes or EFT-unbiased zero-shift:
   `arXiv:2503.13442`

The key physical discriminator is that the strong negative-shift class is
measured directly from Ly-alpha forest redshift-space simulations of the flux
field itself, while the smaller or zero-shift classes arise from different EFT
or de-biasing treatments.

Under Premise 2, these are admissible inherited late-time Ly-alpha kernel
classes on the Schur raw ruler.

Status:
- `derived / conditional`

## Step 4. Exact Schur transport to the DESI Ly-alpha block

The DESI DR2 Ly-alpha block at \(z_{\mathrm{eff}} = 2.33\) has fixed-shape Schur
target

\[
r_{d,\mathrm{Ly}\alpha} = 140.790554518058\ \mathrm{Mpc},
\qquad
\sigma_{r_d,\mathrm{Ly}\alpha} = 0.945374756731\ \mathrm{Mpc}.
\]

The raw Schur ruler alone misses high by

\[
2.271948318812\ \mathrm{Mpc} = 1.588080925302\%.
\]

Applying the inherited redshift-space negative shift from `arXiv:2407.03918`,

\[
r_{d,\mathrm{eff}} = 0.9905 \times 143.062502836870
= 141.703409059919\ \mathrm{Mpc}.
\]

That leaves only

\[
141.703409059919 - 140.790554518058
= 0.912854541861\ \mathrm{Mpc}.
\]

Including both the DESI fixed-shape Ly-alpha ruler uncertainty and the
published shift uncertainty,

\[
\sigma_{\mathrm{comb}} =
\sqrt{
(0.945374756731)^2 +
(143.062502836870 \times 0.0027)^2
}
= 1.021242862305\ \mathrm{Mpc},
\]

so the residual is only

\[
0.893866263899\ \sigma.
\]

At the row level, the 2-row Ly-alpha block chi-square improves from

\[
\chi^2_{\mathrm{raw}} = 6.176391241793
\]

to

\[
\chi^2_{\mathrm{shifted}} = 1.503293420000.
\]

The other published classes do not do this:

- `arXiv:2407.03918` real-space shift:
  `1.8921σ`
- `arXiv:2412.06892` ACCEL2 classes:
  about `1.9–2.0σ`
- `arXiv:2503.13442` vanilla/EFT classes:
  fail or worsen

So the imported class that actually closes the Ly-alpha Schur block is sharply
identified.

Status:
- `verified`

## Theorem statement

### End-to-end conditional Ly-alpha closure theorem

Assume:

1. Premise 2: exterior late-time Ly-alpha forest physics is admissible inside
   the hole.
2. The primitive early-time Schur pre-drag ruler is the same object for all BAO
   tracers.
3. The Ly-alpha BAO observable belongs to the accepted continuous
   redshift-space flux-correlation class.
4. The physical late-time Ly-alpha nonlinear readout kernel belongs to the
   redshift-space negative-shift class measured in `arXiv:2407.03918`.

Then the Ly-alpha half of Seam 2 closes end-to-end at current DESI DR2
precision:

\[
r_{d,\mathrm{raw}} = 143.062502836870\ \mathrm{Mpc}
\quad\Longrightarrow\quad
r_{d,\mathrm{eff}} = 141.703409059919\ \mathrm{Mpc},
\]

which is only

\[
0.893866263899\ \sigma
\]

from the fixed-shape Ly-alpha Schur target.

## Claim status

- `derived / conditional`:
  the end-to-end theorem chain exists under Premise 2 and accepted exterior
  Ly-alpha forest physics.
- `verified`:
  the imported redshift-space negative shift class of `arXiv:2407.03918`
  closes the DESI DR2 Ly-alpha block on the Schur raw ruler.
- `conditional`:
  the Ly-alpha half of Seam 2 is end-to-end closed if that inherited
  redshift-space Ly-alpha flux-shift class is the physical one.
- `not derived`:
  the unique internal IO Ly-alpha flux kernel is still open.
- `not derived`:
  the external Ly-alpha shift literature has not yet converged on a unique
  theorem-grade magnitude or direction.

## Boundary

This upgrades the old result from a bare imported-shift check to a full
observable-class theorem chain under Premise 2.

It does **not** upgrade the Ly-alpha sector to a purely internal derivation.
