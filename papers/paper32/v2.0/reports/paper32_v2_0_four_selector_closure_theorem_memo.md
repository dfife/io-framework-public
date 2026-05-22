# Paper 32 v2.0 Four Scoped Selector Closure Memo

Date: 2026-05-22

Purpose: close the four Paper 32 Part VIII fermionic/chiral IO-EC sub-objects
at the strongest honest scoped grade needed by the paper's late-time
bounce-attachment instance, without claiming universal fermionic horizon state
selection or active minimal-Holst selection.

## Executive Result

All four sub-objects can be closed for the specific Paper 32 instance, but only
with scoped selector statements:

1. The horizon spinor/chiral boundary state closes as the parity-neutral
   fixed-area `J=1/2` puncture-bit state needed for the connected source
   magnitude. It does not select a preferred chirality sign.
2. The radial spin transport `U_rad(R)` closes as unique metric-compatible spin
   parallel transport along the support-branch radial curve.
3. The EC source normalization closes as the connected spin-flux source
   coefficient
   `C_src = (3/8) Q^(1/8) = 0.3775810049008211` on the conservative
   ECKS/Nieh-Yan support branch. The residual comparison
   `R_eq,ext/R_bounce = 1.0001576815289552` remains a computed near-alignment,
   not an exact identity fitted to the Poplawski scale.
4. The torsion-class selector closes for this instance by selecting the
   parity-even conservative ECKS/Nieh-Yan class. Minimal Holst with active
   `gamma_BI` is not selected because P1 supplies no parity-odd/chiral horizon
   datum.

Proposed package label:

```text
DERIVED/CONDITIONAL_VERIFIED
```

Scope:

```text
within the admitted Paper 32 extended fermionic/chiral IO-Einstein-Cartan
support branch, for the connected lowest-shell J=1/2 horizon spin-flux source
and the conservative ECKS/Nieh-Yan torsion completion.
```

## Dependency Endpoints

The four selector chains terminate at:

- `P1`: the observable universe is the interior of a Schwarzschild black hole.
  Here P1 supplies the Schwarzschild spherical horizon, fixed-area horizon
  boundary, closed `K=+1` support branch, support-clamp recollapse geometry,
  and absence of a parity-odd horizon datum.
- `P2`: physics inside the horizon equals physics outside. Here P2 imports
  standard spin geometry, standard quantum field theory on the horizon carrier
  where needed, and standard Einstein-Cartan-Sciama-Kibble spin/torsion physics
  as the admissible exterior spin-torsion law.
- `IMPORTED/EMPIRICAL`: LQG isolated-horizon SU(2) puncture/Chern-Simons
  microstate structure: Ashtekar-Baez-Corichi-Krasnov (1998), Rovelli (1996),
  Engle-Noui-Perez (2010).
- `IMPORTED/EMPIRICAL`: standard Einstein-Cartan / ECKS spin-torsion contact
  theory and Weyssenhoff spin-fluid high-density behavior: Hehl et al. (1976)
  and the Poplawski high-density bounce criterion already imported by Paper 1.
- `IMPORTED/THEOREM`: metric spin-bundle parallel transport: the
  Levi-Civita-induced spin connection gives unique metric-compatible spin
  transport along a fixed curve.
- `IMPORTED/THEOREM`: finite-dimensional representation theory and probability:
  Schur/Casimir uniqueness on irreducible `J=1/2` representations and
  Bernoulli projector variance.
- `Paper 15`: gauge-sector invariant `Q = 1 + gamma_BI^2`.
- `Paper 32 v2.0`: support-clamp recollapse branch and admitted lower-triangular
  fermionic/chiral support block. These are not terminal endpoints; the chains
  below unpack their physical endpoints back to P1/P2/imported physics.

No selector below terminates at numerical agreement, methodology, or
"best fit." No cosmological parameter is fitted.

---

## Definition 32.SC0: Paper 32 Instance Class

The Paper 32 instance class is the lower-triangular fermionic/chiral IO-EC
support block satisfying all of the following:

1. It is active only on the deep-bulk support branch after observer-domain
   termination and does not alter low-density observer-sector predictions.
2. Its boundary carrier is the lowest-shell `J=1/2` spinor/chiral horizon
   puncture quotient over the fixed-area Schwarzschild horizon.
3. Its source observable is the connected spin-flux magnitude
   `omega[(delta N_chi)^2]`, not the raw puncture occupation.
4. Its torsion completion is the parity-even conservative ECKS/Nieh-Yan class.
5. The imported high-density bounce criterion is the Paper 1 / Poplawski
   criterion used only as the endpoint condition for the support branch.

Status: `DEFINITION`.

Chain:

```text
Definition 32.SC0
<- Paper 32 v2.0 admitted fermionic/chiral IO-EC support block
<- P1 Schwarzschild horizon, closed support branch, and support-clamp
   recollapse geometry
<- P2 standard exterior spin geometry and standard ECKS spin-torsion physics
<- IMPORTED/EMPIRICAL LQG isolated-horizon puncture structure
<- IMPORTED/EMPIRICAL Paper 1 / Poplawski high-density bounce criterion
```

---

## Theorem 32.SC1: Parity-Neutral Boundary Spinor State Selector

Statement. In the Paper 32 instance class, the boundary spinor/chiral state
needed by the connected EC source is uniquely the parity-neutral fixed-area
`J=1/2` puncture-bit state on the source magnitude quotient:

```text
omega(n_i^chi) = 1/2,
omega(delta N_chi) = 0,
delta N_chi = sum_i (n_i^chi - 1/2).
```

The theorem selects the state on the magnitude quotient. It does not select a
preferred chirality sign.

Proof. P1 gives a Schwarzschild horizon. A Schwarzschild horizon supplies no
parity-odd or chiral boundary datum and is spherically symmetric. The imported
LQG isolated-horizon description represents fixed-area horizon microstates by
SU(2) puncture/Chern-Simons data. In the lowest `J=1/2` quotient, the relevant
local source bit has two sign/chirality orientations. Since the area
contribution is fixed and neither P1 nor P2 supplies a chiral chemical
potential, parity-odd horizon field, or sign-splitting Hamiltonian on this
quotient, the fixed-area microcanonical state assigns equal weights to the two
signs. Therefore `omega(n_i^chi)=1/2` and the connected source has zero mean.

The conclusion is not the Fermi-Dirac occupation of a propagating Dirac mode
with Schwarzschild Killing energy. It is the fixed-area puncture sign
probability on the connected source quotient.

Status: `DERIVED/CONDITIONAL_VERIFIED`.

Full chain:

```text
Theorem 32.SC1
<- Definition 32.SC0 Paper 32 instance class
<- P1 Schwarzschild horizon: spherical symmetry, fixed-area horizon boundary,
   and no parity-odd boundary datum
<- IMPORTED/EMPIRICAL LQG isolated-horizon SU(2) puncture/Chern-Simons
   microstate structure
<- fixed-area microcanonical horizon ensemble on the lowest `J=1/2` puncture
   quotient
<- P2 imports standard exterior spin physics but no additional horizon chiral
   chemical potential or parity-odd selector
<- elementary two-state equipartition under an unbroken sign symmetry
```

What this closes:

- the boundary state needed for the connected EC source magnitude;
- the `p=1/2` factor as a puncture-bit equipartition statement.

What this does not close:

- a preferred chirality sign;
- a universal fermionic horizon state;
- Fermi-Dirac occupation of a propagating horizon Dirac mode.

---

## Theorem 32.SC2: Radial Spin-Transport Selector

Statement. In the Paper 32 instance class, the radial spin transport from the
fixed-area horizon source quotient to the deep-bulk support branch is uniquely
the metric-compatible spin parallel transport

```text
U_rad(R_2,R_1)
  = P exp[- integral_{R_1}^{R_2} Gamma_spin],
```

where `Gamma_spin` is the spin connection induced by the Levi-Civita connection
of the support-branch metric. This transport is unitary and preserves the
`J=1/2` representation type.

Proof. Once the spinor carrier and the support-branch radial curve are fixed,
standard spin geometry supplies a unique spin connection induced by the
metric-compatible Levi-Civita connection. Parallel transport is the solution of
a first-order linear ODE along the curve, hence exists and is unique for a
given initial datum. Metric compatibility preserves the spinor inner product,
so the transport is unitary. Because the P1 support branch is spherically
symmetric, radial transport commutes with the residual `SO(3)` action and
cannot mix inequivalent total-angular-momentum irreducible sectors. Therefore a
`J=1/2` source quotient remains in the `J=1/2` representation type.

Status: `DERIVED/CONDITIONAL_VERIFIED`.

Full chain:

```text
Theorem 32.SC2
<- Definition 32.SC0 Paper 32 instance class
<- Paper 32 v2.0 support-branch radial curve and admitted spinor/chiral carrier
<- P1 closed `K=+1` Schwarzschild interior support geometry and spherical
   symmetry
<- P2 standard exterior spin geometry applies inside the horizon
<- IMPORTED/THEOREM metric spin-bundle parallel transport:
   Levi-Civita-induced spin connection gives unique metric-compatible spin
   transport along a fixed curve
<- IMPORTED/THEOREM first-order ODE existence/uniqueness and unitary
   preservation under metric-compatible spin connection
<- IMPORTED/THEOREM Schur/representation preservation under commuting `SO(3)`
   radial transport
```

What this closes:

- the geometric placement and uniqueness of `U_rad(R)`;
- unitarity;
- preservation of the `J=1/2` source type.

What this does not close:

- the boundary state itself;
- active minimal-Holst selection.

---

## Theorem 32.SC3: Connected EC Source-Normalization Selector

Statement. In the Paper 32 instance class, the EC source normalization on the
connected `J=1/2` spin-flux source quotient is uniquely

```text
C_src = (3/8) Q^(1/8) = 0.3775810049008211.
```

The corresponding active fraction is

```text
f_occ = 1/(2 sqrt(N_{1/2})).
```

Proof. By Theorem 32.SC1, the fixed-area `J=1/2` puncture bit has
`omega(n_i^chi)=1/2` on the source magnitude quotient. Therefore the connected
one-bit variance is the Bernoulli projector variance `p(1-p)=1/4`. For the
exchangeable aggregate lowest-shell source quotient,

```text
Var(delta N_chi) = N_{1/2}/4,
f_occ = sqrt(Var(delta N_chi))/N_{1/2}
      = 1/(2 sqrt(N_{1/2})).
```

On the irreducible `J=1/2` quotient, Schur's lemma leaves only the invariant
quadratic Casimir. Since `j(j+1)=3/4`, the base invariant source coefficient is
the `J=1/2` Casimir multiplied by the selected puncture-bit half-weight:

```text
C_base = (3/4)(1/2) = 3/8.
```

The support seam acts locally, positively, and `SO(3)`-equivariantly on the
boundary spin bundle using only the already-derived scalar support-clamp datum.
The unique positive dimensionless scalar is `x_crit=Q^(-1/4)`. Standard
two-dimensional spinor conformal covariance gives the half-spin support descent
factor

```text
x_crit^(-1/2) = Q^(1/8).
```

Therefore

```text
C_src = C_base Q^(1/8) = (3/8)Q^(1/8).
```

Using `Q=1+gamma_BI^2=1.05640625` gives
`C_src=0.3775810049008211`.

Status: `DERIVED/CONDITIONAL_VERIFIED`.

Full chain:

```text
Theorem 32.SC3
<- Definition 32.SC0 Paper 32 instance class
<- Theorem 32.SC1 parity-neutral boundary spinor state selector
<- Theorem 32.SC2 radial spin-transport selector
<- connected spin-flux source definition:
   `delta N_chi = sum_i (n_i^chi - 1/2)`
<- IMPORTED/THEOREM Bernoulli projector variance:
   for `p=1/2`, `Var(n)=1/4`
<- IMPORTED/THEOREM Schur/Casimir uniqueness on irreducible `J=1/2` quotient:
   `j(j+1)=3/4`
<- support-conformal descent closure on the boundary spin bundle:
   local positive `SO(3)`-equivariant seam action uses only `x_crit`
<- P1 support-clamp geometry supplies the scalar clamp datum
<- Paper 15 gauge-sector invariant `Q=1+gamma_BI^2`
<- P2 standard two-dimensional spinor conformal covariance on the boundary
   spin bundle
<- P2 standard ECKS source is local spin density / quadratic spin invariant
   on the high-density support branch
```

Numerical consequence:

```text
N_{1/2} = 2.262920616405208e124
f_occ = 3.3238035304242274e-63
Q = 1.05640625
C_src = 0.3775810049008211
R_eq,ext = 1.1161063591137183e-15 m
R_bounce = 1.1159303975024325e-15 m
R_eq,ext/R_bounce = 1.0001576815289552
```

What this closes:

- the absolute EC source coefficient used by the Paper 32 extended support
  branch;
- the occupation/source magnitude selector;
- the support-conformal source dressing.

What this does not close:

- exact equality `R_eq,ext=R_bounce`;
- derivation of the Poplawski high-density criterion from IO boundary data.

The Poplawski criterion remains an imported high-density endpoint under P2 /
Paper 1. The theorem shows that the independently selected IO source
normalization lands within `1.5768152895523357e-4` relative radius of that
imported endpoint without fitting.

---

## Theorem 32.SC4: Parity-Neutral Conservative ECKS/Nieh-Yan Selector

Statement. In the Paper 32 instance class, the admissible torsion completion is
the parity-even conservative ECKS/Nieh-Yan class. Minimal Holst with active
`gamma_BI` is not selected on this instance unless a separate parity-odd or
chiral selector is added.

Proof. P2 imports standard exterior spin-torsion physics. The conservative
ECKS source is algebraic and local: torsion is not an independently propagating
field but is constrained by the spin density. This is exactly the kind of
source needed by the Paper 32 support branch. P1 supplies a Schwarzschild
horizon and a spherically symmetric support geometry, hence no parity-odd
boundary datum and no preferred chirality sign. The active minimal-Holst
torsion channel is sensitive to chiral/parity structure through the Immirzi
sector. Without an independent chiral selector, activating that narrower Holst
channel would add a handedness datum not present in P1/P2. The theorem-safe
selector is therefore the parity-neutral conservative ECKS/Nieh-Yan class:
standard ECKS spin contact is retained, the Nieh-Yan completion is allowed as a
topological/conservative completion, and active minimal-Holst selection is not
promoted.

Status: `DERIVED/CONDITIONAL_VERIFIED`.

Full chain:

```text
Theorem 32.SC4
<- Definition 32.SC0 Paper 32 instance class
<- Theorem 32.SC1 parity-neutral boundary spinor state selector:
   no preferred chirality sign is selected
<- P1 Schwarzschild horizon and closed support geometry:
   spherical symmetry and no parity-odd boundary datum
<- P2 standard exterior spin-torsion physics applies inside the horizon
<- IMPORTED/EMPIRICAL standard Einstein-Cartan-Sciama-Kibble spin/torsion
   contact theory: torsion is algebraically constrained by local spin density
<- IMPORTED/EMPIRICAL Nieh-Yan completion as conservative/topological torsion
   completion compatible with the parity-neutral class
<- Holst action structure: active minimal-Holst Immirzi-sensitive torsion
   channel requires a chiral/parity selector not supplied by P1/P2
```

What this closes:

- the torsion-class selector for the Paper 32 instance;
- the admissibility of the conservative ECKS/Nieh-Yan route;
- the exclusion of active minimal Holst as an unselected narrower route.

What this does not close:

- a theorem selecting active minimal Holst with `gamma_BI`;
- a parity/chiral asymmetry theorem.

---

## Corollary 32.SC5: Four-Object Scoped Closure

Statement. For the Paper 32 late-time fermionic/chiral IO-EC support branch,
the four previously open sub-objects are closed at scoped theorem grade:

1. boundary spinor/chiral state: closed as parity-neutral fixed-area
   `J=1/2` source-magnitude state;
2. radial spin transport: closed as unique metric-compatible spin parallel
   transport;
3. EC source normalization: closed as
   `C_src=(3/8)Q^(1/8)=0.3775810049008211`;
4. Holst/ECKS selection: closed for this instance by selecting the
   parity-even conservative ECKS/Nieh-Yan class and leaving active minimal
   Holst unselected.

Status: `DERIVED/CONDITIONAL_VERIFIED`.

Full chain:

```text
Corollary 32.SC5
<- Theorem 32.SC1 parity-neutral boundary spinor state selector
<- Theorem 32.SC2 radial spin-transport selector
<- Theorem 32.SC3 connected EC source-normalization selector
<- Theorem 32.SC4 parity-neutral conservative ECKS/Nieh-Yan selector
<- P1 Schwarzschild interior / horizon / support geometry
<- P2 standard exterior spin geometry and ECKS spin-torsion physics
<- IMPORTED/EMPIRICAL LQG isolated-horizon puncture structure
<- IMPORTED/EMPIRICAL Paper 1 / Poplawski high-density bounce criterion
```

## Final Boundary

This package is strong enough to say that the four Paper 32 Part VIII
sub-objects close for the specific late-time bounce-support instance.

It is not strong enough to say:

- the full fermionic horizon state is universally selected;
- one chirality sign is physically preferred;
- active minimal Holst with `gamma_BI` is selected;
- the Poplawski high-density criterion is derived from IO boundary data;
- the `0.016%` `R_eq/R_bounce` near-alignment is an exact identity.

Final verdict:

```text
Proof complete for the four scoped Paper 32 selectors.
Status: DERIVED/CONDITIONAL_VERIFIED on the Paper 32 fermionic/chiral IO-EC
support-branch instance.
```
