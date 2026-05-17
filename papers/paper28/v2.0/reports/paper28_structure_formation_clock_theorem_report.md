# Paper 28 - Structure-Formation Clock Theorem In The OS Interior

Date: 2026-03-31

## Executive result

The clean theorem-grade statement is:

- `derived`: for any local physical process occurring on a comoving worldline in
  the OS interior, the physical elapsed time is the OS proper time `tau`.
- `derived`: the projected cosmological age `t_proj` is an observer-side
  optical/readout observable, not the proper time along that matter worldline.
- `derived`: therefore the physical clock for structure formation is
  `tau(E)`, where `E` is the galaxy-worldline event being discussed.
- `conditional`: if the observed redshift `z` identifies the event `E(z)` via a
  specified map such as `u(z)=1/[x(1+z)]`, then the formation-clock map is
  `tau(u(z))`.

The remaining open object is **not** the clock. The remaining open object is the
redshift-to-event map.

## Theorem 1 - Proper-time clock theorem

Let the OS interior metric be written in synchronous comoving form
\[
ds^2=-d\tau^2+a(\tau)^2\,h_0,
\]
with dust congruence
\[
u^\mu = (\partial_\tau)^\mu.
\]

Then along any comoving worldline `gamma`,
\[
d s^2|_\gamma = -d\tau^2,
\]
so the line element length between two events `E_1, E_2` on that worldline is
\[
\Delta \tau = \int_{E_1}^{E_2} d\tau.
\]

This is the unique invariant physical clock carried by that worldline.

### Proof

This is immediate from the metric. In synchronous comoving coordinates the
worldline tangent is `u = ∂_τ`, spatial coordinates are constant on a comoving
trajectory, and the restriction of the metric to that trajectory is
`ds^2 = -dτ^2`. Therefore the worldline proper time equals `τ`.

QED.

## Theorem 2 - Local-process parameter theorem

Any local matter process on that worldline is parameterized by `tau`, not by an
observer-side optical age variable.

### Proof sketch

Standard GR matter dynamics are local and covariant. For any local field or
fluid variable `X`, the physical time derivative measured in the local rest
frame is
\[
\dot X := u^\mu \nabla_\mu X.
\]
On the OS comoving worldline, `u = ∂_τ`, hence
\[
\dot X = \frac{dX}{d\tau}.
\]

This covers the standard classes relevant to galaxy formation:

1. **Gravitational collapse / fluid dynamics**
   \[
   \nabla_\nu T^{\mu\nu}=0
   \]
   decomposes into energy and Euler equations along `u^\mu`; the material
   derivative is `u^\mu \nabla_\mu = d/dτ`.

2. **Thermodynamics / gas cooling**
   the first-law / energy equation in the local rest frame is written in terms
   of the comoving derivative `d/dτ`.

3. **Nuclear reaction networks**
   abundances obey local-rate equations of the form
   \[
   \frac{dY_i}{d\tau}=F_i(Y_j,n,T,\ldots).
   \]

4. **Stellar evolution**
   stellar structure and burning times are local rest-frame proper-time
   quantities.

Therefore the physical duration of local galaxy-formation processes is measured
by `tau`.

QED.

## Theorem 3 - Projected-age non-clock theorem

The projected cosmological age `t_proj` is not, in general, the proper time
along the comoving matter worldline.

### Proof

Paper 19 already distinguishes the two observable classes:

- `H_bare`: local bulk kinematic expansion of the OS dust congruence
- `H_obs`: observer-side projected cosmological expansion readout

See:

- `/opt/cosmology-lab/results/paper19/paper19_friedmann_readout_selection_report.txt`

which states:

> there are two distinct expansion observables:
> `H_bare`: local bulk kinematic expansion of the OS dust congruence,
> `H_obs`: observer-side projected cosmological expansion readout.

and:

> the measured cosmological `H0` belongs to the `H_obs` class, not the local
> dust-ball class.

Thus the projected age obtained by integrating the projected expansion readout
is an observer-side inference from optical/source-slot readout structure, not
the invariant line element along a comoving matter worldline.

Equivalently: if `t_proj` were the same object as local proper time, then the
distinction between `H_obs` and `H_bare` would collapse, contrary to the
readout-selection theorem.

QED.

## Corollary 4 - Structure-formation clock selection

Let `E` be the emission/formation event on a galaxy's comoving worldline. Then
the physical age available for local structure formation by that event is
\[
\tau(E),
\]
not the observer-side projected age `t_proj(E)`.

### Proof

Combine Theorems 1–3.

QED.

## Corollary 5 - Redshift-labeled form

If a separate theorem or model identifies the event `E(z)` corresponding to an
observed redshift `z`, then the formation-clock map is
\[
t_{\rm form}(z)=\tau(E(z)).
\]

In particular, under the explicit FRW-style identification used in the JWST
audits,
\[
u(z)=\frac{1}{x(1+z)},
\]
one gets
\[
t_{\rm form}(z)=\tau(u(z))
=\frac{r_s}{2c}\left[\arccos(1-2u(z))-2\sqrt{u(z)(1-u(z))}\right].
\]

This last step is `conditional` on the chosen `z -> E(z)` map.

## Claim boundary

- `derived`: local structure-formation physics in the OS interior runs on local
  proper time `tau`.
- `derived`: projected cosmological age is an observer-side optical/readout
  inference, not the local worldline clock.
- `derived`: the physical formation clock is `tau(E)` for the relevant galaxy
  worldline event `E`.
- `conditional`: writing that clock as an explicit function of observed
  redshift, `tau(u(z))`, requires a separate redshift-to-event identification.
