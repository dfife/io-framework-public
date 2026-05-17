# Paper 28 - Unified JWST Clock-Map Theorem On The OS Background

Date: 2026-03-31

## Theorem statement

Let the IO universe be modeled by the homogeneous Oppenheimer-Snyder interior.
Write the metric in synchronous comoving form
\[
ds^2=-d\tau^2+a(\tau)^2 h_0,
\]
or equivalently in conformal FRW form
\[
ds^2=a(\eta)^2\left[-d\eta^2+d\chi^2+\sin^2\chi\,d\Omega^2\right].
\]

Assume:

- galaxy-forming matter follows comoving OS worldlines,
- the observed source is represented by the homogeneous background emission
  event connected to the observer by a radial null signal,
- the present observer epoch satisfies
  \[
  a(\eta_s)=R_U=\frac{r_s}{x}.
  \]

Then the following hold.

### Part I - Local structure-formation clock

For any local physical process on a comoving matter worldline, the physical
elapsed time is the OS proper time `tau`.

Equivalently, the physical formation clock at a galaxy-worldline event `E` is
\[
t_{\rm form}(E)=\tau(E).
\]

### Part II - Projected age is not the local matter clock

The projected cosmological age belongs to the observer-side optical/readout
class and is not, in general, the proper time along the comoving matter
worldline.

So the structure-formation clock is not the projected FRW age `t_proj`.

### Part III - Exact background redshift-to-event map

For a comoving source, a comoving observer, and a radial null signal in the
homogeneous OS background,
\[
1+z=\frac{a(\eta_s)}{a(\eta_e)}.
\]

For the corrected OS cycloid
\[
a(\eta)=\frac{r_s}{2}(1-\cos\eta),
\]
this gives the exact background event map
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

### Unified corollary - JWST formation-clock map

Therefore, on the homogeneous OS background, the physical time available for
galaxy formation at observed redshift `z` is
\[
t_{\rm form}(z)=\tau(z)=\frac{r_s}{2c}\left[\eta(z)-\sin\eta(z)\right],
\]
with
\[
\eta(z)=\arccos\!\left(1-\frac{2}{x(1+z)}\right).
\]

Equivalently,
\[
t_{\rm form}(z)=
\frac{r_s}{2c}\left[
\arccos\!\left(1-\frac{2}{x(1+z)}\right)
-2\sqrt{\frac{1}{x(1+z)}\left(1-\frac{1}{x(1+z)}\right)}
\right].
\]

This is the theorem-grade JWST clock map on the homogeneous OS background.

## Proof

### Step 1 - Proper-time clock

Along a comoving worldline, spatial coordinates are constant, so from the
synchronous OS metric
\[
ds^2|_\gamma=-d\tau^2.
\]
Hence the unique invariant physical clock carried by that worldline is `tau`.

Standard local GR matter dynamics use the comoving derivative
\[
u^\mu \nabla_\mu = \frac{d}{d\tau},
\]
so local collapse, gas cooling, nuclear reaction networks, and stellar
evolution are parameterized by `tau`.

### Step 2 - Projected age is an observer-side readout

The projected cosmological age is obtained by integrating the observer-side
projected expansion readout rather than the local bulk dust expansion. So it is
an observational inference from photon/readout structure, not the invariant
line element along the galaxy matter worldline.

Therefore the physical formation clock is `tau(E)`, not `t_proj(E)`.

### Step 3 - Redshift-to-event map

For radial null propagation in conformal FRW,
\[
0=ds^2=a(\eta)^2(-d\eta^2+d\chi^2),
\]
so
\[
d\chi=\pm d\eta.
\]

For two successive wave crests connecting the same comoving source and observer,
the null integrals are equal, giving
\[
\delta\eta_s=\delta\eta_e.
\]

Comoving proper intervals satisfy
\[
\delta\tau=a(\eta)\,\delta\eta,
\]
so
\[
\frac{\delta\tau_s}{\delta\tau_e}
=\frac{a(\eta_s)}{a(\eta_e)}
=\frac{\nu_e}{\nu_s}
=1+z.
\]

Thus
\[
1+z=\frac{a(\eta_s)}{a(\eta_e)}.
\]

Substituting
\[
a(\eta_s)=\frac{r_s}{x},
\qquad
a(\eta_e)=r_s u
\]
gives
\[
u(z)=\frac{1}{x(1+z)}.
\]
The formulas for `eta(z)`, `chi(z)`, and `tau(z)` follow directly from the OS
cycloid.

QED.

## Claim boundary

- `derived`: on the homogeneous OS background, local structure formation runs
  on OS proper time `tau`, not on projected FRW age.
- `derived`: on that same background, the observed redshift fixes the emission
  event through
  \[
  u(z)=1/[x(1+z)].
  \]
- `derived`: therefore the homogeneous-background JWST formation-clock map is
  exactly
  \[
  t_{\rm form}(z)=\tau(u(z)).
  \]
- `conditional`: peculiar velocities, local gravitational potentials, and
  nonlinear structure generate perturbative corrections around this homogeneous
  background theorem, just as in standard cosmology.

## Numerical anchors

Using

- `r_s = 6.6835e26 m`
- `x = 1.519`
- `c = 299792458 m/s`

the theorem gives:

- `z=10`: `t_form = 0.7023379333 Gyr`
- `z=12`: `t_form = 0.5450883247 Gyr`
- `z=14`: `t_form = 0.4388659557 Gyr`
- `z=17`: `t_form = 0.3331013378 Gyr`
- `z=20`: `t_form = 0.2639107601 Gyr`

## Reproducibility

- `/opt/cosmology-lab/results/paper28/paper28_structure_formation_clock_theorem_report.md`
- `/opt/cosmology-lab/results/paper28/paper28_redshift_to_event_theorem_report.md`
- `/opt/cosmology-lab/results/paper28/paper28_redshift_to_event_theorem_audit.py`
- `/opt/cosmology-lab/results/paper28/paper28_jwst_clock_map_theorem_audit.py`
- `/opt/cosmology-lab/results/paper28/paper28_jwst_clock_map_theorem_results.json`
