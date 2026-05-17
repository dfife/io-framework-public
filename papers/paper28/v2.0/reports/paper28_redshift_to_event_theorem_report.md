# Paper 28 - Redshift-To-Event Theorem On The OS Background

Date: 2026-03-31

## Theorem statement

On the OS interior written in conformal FRW form
\[
ds^2 = a(\eta)^2\left[-d\eta^2 + d\chi^2 + \sin^2\chi\, d\Omega^2\right],
\]
consider:

- a comoving source worldline,
- a comoving observer worldline,
- a radial null signal connecting emission event `E_e` to observation event
  `E_s`.

Then the observed cosmological redshift satisfies the exact background relation
\[
1+z = \frac{a(\eta_s)}{a(\eta_e)}.
\]

For the corrected OS cycloid
\[
a(\eta)=\frac{r_s}{2}(1-\cos\eta),
\]
and present observer epoch
\[
a(\eta_s)=R_U=\frac{r_s}{x},
\]
this gives the exact event map
\[
u(z):=\frac{a(\eta_e)}{r_s}=\frac{1}{x(1+z)},
\]
\[
\eta(z)=\arccos\!\left(1-\frac{2}{x(1+z)}\right),
\]
\[
\chi(z)=\eta_s-\eta(z),
\]
\[
\tau(z)=\frac{r_s}{2c}\left[\eta(z)-\sin\eta(z)\right].
\]

So the redshift-to-event map on the homogeneous OS background is explicit and
closed.

## Proof

For radial null propagation in conformal FRW,
\[
0 = ds^2 = a(\eta)^2(-d\eta^2 + d\chi^2),
\]
so
\[
d\chi = \pm d\eta.
\]

Hence the same source and observer satisfy
\[
\chi_s-\chi_e = \int_{\eta_e}^{\eta_s} d\eta
              = \int_{\eta_e+\delta\eta_e}^{\eta_s+\delta\eta_s} d\eta,
\]
which implies
\[
\delta\eta_s=\delta\eta_e
\]
for successive wave crests.

Proper time intervals measured by comoving observers are
\[
\delta\tau = a(\eta)\,\delta\eta.
\]
Therefore
\[
\frac{\delta\tau_s}{\delta\tau_e}
=
\frac{a(\eta_s)}{a(\eta_e)}
=
\frac{\nu_e}{\nu_s}
=
1+z.
\]

This proves
\[
1+z=\frac{a(\eta_s)}{a(\eta_e)}.
\]

Substituting `a(\eta_s)=r_s/x` and `a(\eta_e)=r_s u` gives
\[
u(z)=\frac{1}{x(1+z)}.
\]
The formulas for `eta(z)`, `chi(z)`, and `tau(z)` then follow directly from the
OS cycloid.

QED.

## Claim boundary

- `derived`: the redshift-to-event map is exact on the homogeneous OS/FRW
  background for comoving source and observer worldlines.
- `derived`: the formation-clock map on that background is therefore
  \[
  t_{\rm form}(z)=\tau(z)=\tau(u(z)).
  \]
- `conditional`: peculiar velocities, local gravitational potentials, and
  nonlinear structure corrections shift the exact source event away from the
  homogeneous background event, just as in standard cosmology. Those are
  perturbative corrections to the background theorem, not replacements for it.

## Numerical verification

The audit reproduces the same event map used in the earlier JWST clock tables:

- `/opt/cosmology-lab/results/paper28/paper28_redshift_to_event_theorem_audit.py`
- `/opt/cosmology-lab/results/paper28/paper28_redshift_to_event_theorem_results.json`
