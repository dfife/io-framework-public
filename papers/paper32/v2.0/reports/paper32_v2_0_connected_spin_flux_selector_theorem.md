# Paper 32 v2.0 Connected Spin-Flux Selector Theorem

Date: 2026-05-22

Purpose: close the narrow state/occupation selector needed by the Paper 32
fermionic/chiral IO-EC extension without claiming a universal state-selection
theorem.

## Executive Result

The selector can be closed for the specific Paper 32 EC source lift if the
source is typed as a connected horizon spin-flux fluctuation, not as an
absolute thermal excitation occupation of a Dirac mode.

The theorem selects:

```text
delta N_chi = sum_i (n_i - 1/2),
Var(delta N_chi) = N_{1/2}/4,
f_occ = sqrt(Var(delta N_chi))/N_{1/2} = 1/(2 sqrt(N_{1/2})).
```

This restores the `p=1/2` factor on theorem-grade grounds for this source
observable. It avoids the earlier blocker because the selected object is not
the ordinary horizon Killing-energy thermal occupation
`1/(exp(beta_H hbar omega)+1)`. It is the connected fluctuation of the
area-fixed `J=1/2` horizon puncture spin/chirality bit.

What this closes:

- the occupation selector for the effective EC source magnitude;
- the use of the centered occupation law in the Paper 32 fermionic/chiral
  bridge extension;
- the base factor `3/8` as `(3/4) x (1/2)` on the selected source.

What this does not close:

- a preferred chirality sign;
- exact equality of `R_eq,ext` and the imported Poplawski bounce radius;
- minimal Holst with active `gamma_BI` over the conservative ECKS/Nieh-Yan
  class.

Proposed label:

```text
DERIVED/CONDITIONAL_VERIFIED
```

Scope:

```text
on the Paper 32 extended fermionic/chiral IO-EC bridge, for the connected
lowest-shell horizon spin-flux source feeding the conservative ECKS/Nieh-Yan
support branch.
```

## Dependency Endpoints Used

The chains below terminate only at the following endpoints:

- `P1`: the observable universe is the interior of a Schwarzschild black hole.
  For this theorem, P1 supplies the spherical Schwarzschild horizon, the
  fixed-area horizon boundary, the closed support branch, and the absence of a
  parity-odd horizon datum.
- `P2`: physics inside the horizon equals physics outside. For this theorem,
  P2 imports standard exterior spin geometry and standard
  Einstein-Cartan-Sciama-Kibble (ECSK/ECKS) spin-torsion physics as the
  admissible local torsion completion.
- `IMPORTED/EMPIRICAL`: LQG isolated-horizon SU(2) puncture/Chern-Simons
  horizon microstate structure, as in Ashtekar-Baez-Corichi-Krasnov (1998),
  Rovelli (1996), and Engle-Noui-Perez (2010).
- `IMPORTED/EMPIRICAL`: standard Einstein-Cartan spin/torsion contact law and
  Weyssenhoff spin-fluid high-density behavior, as in Hehl et al. (1976) and
  the Poplawski bounce-density import already cited by Paper 1 / Paper 32.
- `IMPORTED/THEOREM`: standard spin geometry on a metric spin bundle: the
  spin connection induced by the Levi-Civita connection gives the unique
  metric-compatible radial spin parallel transport once the spinor carrier and
  support curve are fixed.
- `IMPORTED/THEOREM`: elementary representation theory and probability:
  Schur/Casimir uniqueness on an irreducible `J=1/2` quotient and Bernoulli
  projector variance.

The theorem does not terminate at a methodology rule, numerical agreement, or
the observed Poplawski scale. The Poplawski scale is used only for the
post-theorem numerical comparison.

## Definition 32.SF1: Connected Horizon Spin-Flux Source

Let the admitted Paper 32 fermionic/chiral bridge carrier contain the
lowest-shell `J=1/2` horizon puncture sector. On each puncture let
`n_i^chi` denote the occupation/projector for the selected spin/chirality sign
in the two-state `J=1/2` horizon bit.

The connected horizon spin-flux source is

```text
delta N_chi = sum_{i=1}^{N_{1/2}} (n_i^chi - omega(n_i^chi)).
```

The EC source lift uses the connected quadratic spin-flux magnitude

```text
omega[(delta N_chi)^2]
```

rather than the uncentered one-point occupation

```text
omega[N_chi]^2.
```

Intrinsic membership test:

An observable belongs to this source class iff it is a support-sector
Einstein-Cartan spin-contact source built from the connected two-point
fluctuation of the horizon `J=1/2` puncture spin/chirality bit and vanishes
when the puncture configuration is replaced by its area-fixed horizon
equilibrium mean.

Chain:

```text
Definition 32.SF1
<- Paper 32 v2.0 admitted fermionic/chiral IO-EC extension: a lowest-shell
   spinor/chiral boundary block is added only for the deep-bulk support branch
<- P1 Schwarzschild horizon and fixed-area boundary sector
<- IMPORTED/EMPIRICAL LQG isolated-horizon SU(2) puncture/Chern-Simons
   microstate structure
<- P2 standard exterior spin geometry and standard ECKS spin-contact source
   as a local spin-density source, not an independent propagating torsion field
```

## Lemma 32.SF2: Raw Occupation Is Not An Admissible Support Source

Statement. The uncentered horizon occupation `N_chi = sum_i n_i^chi` is not an
admissible Paper 32 support-sector source for the EC completion.

Proof. The Paper 32 support-sector source is required to be inactive on the
low-density horizon-clamp branch and to enter only as the deep-bulk torsion
completion. A raw nonzero horizon mean occupation is present already at the
area-fixed horizon state and would source a background EC contribution on the
support branch before the high-density endpoint. This is exactly the failure
recorded by the full-population and uncentered-occupation no-go audits: feeding
the raw puncture population makes the EC term dominate at or above the support
clamp. Therefore the source cannot be the raw one-point occupation. It must be
a connected fluctuation about the area-fixed horizon equilibrium.

Chain:

```text
Lemma 32.SF2
<- Definition 32.SF1 connected horizon spin-flux source class
<- Paper 32 v2.0 support-clamp / observer-domain preservation theorem:
   the low-density observer branch must remain the already-derived local
   recollapse/termination branch
<- Paper 32 full-population / uncentered-occupation no-go audits:
   raw puncture population sources the EC sector too early and violates the
   support-clamp boundary
<- P1 closed Schwarzschild interior with support-clamp branch and low-density
   observer-sector preservation
<- P2 standard ECKS source is local spin density on the high-density support
   branch and is algebraic/nonpropagating torsion
```

Status: `DERIVED/NO-GO` for uncentered occupation as the active EC support
source.

## Lemma 32.SF3: Area-Fixed Horizon Bit Equipartition

Statement. On the fixed-area `J=1/2` isolated-horizon puncture sector, absent a
parity-odd/chiral selector, the two spin/chirality signs are equiprobable:

```text
omega(n_i^chi) = 1/2.
```

Proof. In the `J=1/2` puncture sector the relevant local horizon bit has two
states related by the residual rotational/parity symmetry of the
spherically-symmetric Schwarzschild horizon. The fixed-area isolated-horizon
ensemble fixes the puncture area contribution but supplies no energy splitting
between the two signs and no chiral chemical potential. P1 gives a
Schwarzschild horizon and hence no parity-odd horizon datum; P2 imports
standard exterior physics but no extra horizon chiral bias. Therefore the
area-fixed microcanonical state assigns equal weight to the two signs.

This is not the same as the Fermi-Dirac occupation of a propagating Dirac mode
with Killing energy `hbar omega`. It is the horizon puncture spin/sign
orientation probability inside a fixed-area boundary ensemble.

Chain:

```text
Lemma 32.SF3
<- P1 Schwarzschild horizon: spherical symmetry and no parity-odd boundary datum
<- IMPORTED/EMPIRICAL LQG isolated-horizon puncture structure: horizon degrees
   of freedom carried by SU(2) punctures / Chern-Simons boundary states
<- fixed-area microcanonical horizon ensemble on the `J=1/2` puncture sector:
   area is fixed while the two spin/chirality signs are not split by an
   energy, chemical-potential, or parity datum
<- Paper 32 v2.0 chirality-selector no-go boundary: no current-stack theorem
   selects one chirality sign over the other
<- P2 imports no additional horizon chiral chemical potential
```

Status: `DERIVED/CONDITIONAL_VERIFIED` on the admitted `J=1/2` puncture-sector
description of the Paper 32 fermionic/chiral extension.

## Lemma 32.SF4: Connected Binomial Fluctuation Law

Statement. For `N_{1/2}` independent or exchangeable minimal puncture bits in
the area-fixed lowest-shell quotient, with equiprobable two-state sign
statistics, the connected source has

```text
omega[(delta N_chi)^2] = N_{1/2}/4,
f_occ = 1/(2 sqrt(N_{1/2})).
```

Proof. For one bit, `n_i^chi` is a projector with probability `1/2`, hence

```text
Var(n_i^chi) = p(1-p) = 1/4.
```

The active quotient keeps only the aggregate connected one-channel fluctuation.
Exchangeability and absence of a further correlation selector make the
canonical aggregate variance the sum of the identical one-bit variances:

```text
Var(delta N_chi) = N_{1/2}/4.
```

Dividing the rms fluctuation by the total puncture count gives

```text
f_occ = sqrt(N_{1/2}/4) / N_{1/2} = 1/(2 sqrt(N_{1/2})).
```

Chain:

```text
Lemma 32.SF4
<- Lemma 32.SF3 area-fixed horizon bit equipartition
<- Definition 32.SF1 connected one-channel source quotient
<- IMPORTED/THEOREM elementary variance of Bernoulli projectors:
   for a projector with `p=1/2`, `Var(n)=p(1-p)=1/4`
<- exchangeability of identical fixed-area `J=1/2` horizon puncture bits,
   inherited from the P1 spherical horizon and the imported fixed-area LQG
   isolated-horizon ensemble
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Theorem 32.SF5: Connected Spin-Flux Selector Theorem

Statement. In the Paper 32 extended fermionic/chiral IO-EC theory, on the
lowest-shell `J=1/2` horizon puncture quotient feeding the conservative
ECKS/Nieh-Yan support branch, the admissible source occupation factor is
uniquely the connected area-fixed spin-flux fluctuation

```text
f_occ = 1/(2 sqrt(N_{1/2})),
```

not the horizon Killing-energy Fermi-Dirac occupation of a propagating Dirac
mode.

Proof. By Lemma 32.SF2, the raw occupation is not admissible: it creates an
EC source before the deep-bulk endpoint and violates the support-sector
decoupling boundary. The source must therefore be connected. By Lemma 32.SF3,
the fixed-area `J=1/2` horizon bit has probability `1/2` for either sign in
the absence of a chiral selector. By Lemma 32.SF4, the connected aggregate
fluctuation then has rms active fraction `1/(2 sqrt(N_{1/2}))`. No alternative
one-channel scalar remains on the realized quotient: a different mean would
require a chiral chemical potential or parity-odd selector; a different
variance would require an additional puncture-correlation law; and raw
occupation has already been excluded. Therefore the selector is unique on this
scoped source class.

Chain:

```text
Theorem 32.SF5
<- Definition 32.SF1 connected horizon spin-flux source
<- Lemma 32.SF2 raw occupation no-go
<- Lemma 32.SF3 area-fixed horizon bit equipartition
<- Lemma 32.SF4 connected binomial fluctuation law
<- Paper 32 v2.0 admitted fermionic/chiral IO-EC extension: the new block is a
   lower-triangular spinor/chiral support block that does not alter the
   low-density observer-sector predictions
<- radial spin transport closure: once the spinor carrier and support curve are
   fixed, the transport is the unique metric-compatible spin parallel transport
   generated by the Levi-Civita spin connection
<- IMPORTED/THEOREM standard spin geometry on a metric spin bundle
<- conservative ECKS/Nieh-Yan selector boundary: P2 admits the standard
   algebraic spin-torsion contact class; minimal Holst with active
   `gamma_BI` is not selected without an additional parity/chiral selector
<- IMPORTED/EMPIRICAL standard Einstein-Cartan-Sciama-Kibble spin/torsion
   physics and Weyssenhoff high-density spin-fluid behavior
<- P1 Schwarzschild/isolated-horizon boundary, fixed-area horizon puncture
   sector, closed K=+1 support branch, and no parity-odd horizon datum
<- P2 standard exterior physics inside the horizon, including standard spin
   geometry and ECKS spin-torsion source structure
<- IMPORTED/EMPIRICAL LQG isolated-horizon SU(2) puncture/Chern-Simons
   microstate physics
```

Status: `DERIVED/CONDITIONAL_VERIFIED`.

## Corollary 32.SF6: Base EC Source Coefficient

Statement. Under Theorem 32.SF5, the base invariant quadratic coefficient on
the selected `J=1/2` source quotient is

```text
C_base = (3/4)(1/2) = 3/8.
```

With the support-conformal descent theorem, the extended coefficient is

```text
C_src = (3/8) Q^(1/8) = 0.3775810049008211.
```

Proof. On `J=1/2`, the `SO(3)` Casimir is `j(j+1)=3/4`. The selected connected
source magnitude carries the equipartition factor `1/2` from Lemma 32.SF3.
Multiplying gives `3/8`. The already banked support-conformal spinor weight
contributes `Q^(1/8)`.

Chain:

```text
Corollary 32.SF6
<- Theorem 32.SF5
<- IMPORTED/THEOREM Schur/Casimir uniqueness on the irreducible `J=1/2`
   quotient: `j(j+1)=3/4`
<- support-conformal descent closure: the boundary spinor support source
   carries the half-spin conformal descent weight `Q^(1/8)` on the admitted
   Paper 32 spinor/chiral support block
<- P2 standard two-dimensional spinor conformal covariance on the boundary
   spin bundle
<- Paper 15 gauge-sector transfer invariant `Q = 1 + gamma_BI^2`
<- P1 Schwarzschild horizon boundary and closed support geometry
<- P2 standard exterior gauge/spin geometry imported into the interior
```

Status: `DERIVED/CONDITIONAL_VERIFIED` within the extended fermionic/chiral
IO-EC source class.

## Numerical Consequence

Using the already banked Paper 32 values:

```text
N_{1/2} = 2.262920616405208e124
f_occ = 1/(2 sqrt(N_{1/2})) = 3.3238035304242274e-63
Q = 1.05640625
C_src = (3/8) Q^(1/8) = 0.3775810049008211
R_eq,ext = 1.1161063591137183e-15 m
R_bounce = 1.1159303975024325e-15 m
R_eq,ext / R_bounce = 1.0001576815289552
```

Interpretation:

The selector restores the exact occupation/coefficient structure used by the
Paper 32 extension. It does not make `R_eq,ext` exactly equal to the imported
Poplawski bounce radius. The remaining `1.5768e-4` relative offset is a
prediction/near-alignment of the extended source model, not a fitted equality.

## What This Theorem Does Not Claim

- It does not select a preferred chirality sign; it selects the magnitude of
  the connected source, which is sign-independent.
- It does not claim all fermionic horizon states have `p=1/2`; only the
  area-fixed `J=1/2` puncture spin/sign bit used by this connected source does.
- It does not use the Fermi-Dirac occupation of a propagating Dirac shell.
- It does not prove minimal Holst with active `gamma_BI`; it stays on the
  conservative ECKS/Nieh-Yan support branch.
- It does not fit the coefficient to `R_bounce`.

## Literature Anchors

- Ashtekar, Baez, Corichi, Krasnov (1998), "Quantum Geometry and Black Hole
  Entropy", Phys. Rev. Lett. 80, 904: LQG black-hole entropy from horizon
  punctures and the Immirzi-dependent area spectrum.
- Rovelli (1996), "Black Hole Entropy from Loop Quantum Gravity", Phys. Rev.
  Lett. 77, 3288: early LQG puncture state-counting route to black-hole
  entropy.
- Engle, Noui, Perez (2010), "Black Hole Entropy and SU(2) Chern-Simons
  Theory", Phys. Rev. Lett. 105, 031302: SU(2)-invariant isolated-horizon
  Chern-Simons formulation.
- Hehl et al. (1976), "General Relativity with Spin and Torsion: Foundations
  and Prospects", Rev. Mod. Phys. 48, 393: standard Einstein-Cartan
  spin/torsion foundations.

## Final Verdict

Proof complete for the narrow selector:

```text
The connected spin-flux source selector closes at
DERIVED/CONDITIONAL_VERIFIED on the Paper 32 extended fermionic/chiral IO-EC
source class.
```

The Part VIII extension is now stronger than the previous memo stated: the
`p=1/2` factor can be justified, but only as an area-fixed puncture fluctuation
selector, not as a horizon Killing-energy KMS occupation.
