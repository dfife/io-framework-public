# Paper 1 Source Ingestion Memo: Rovelli and Vidotto 2024

Date: 2026-05-22

Local source PDF:

```text
/opt/cosmology-lab/sources/paper1/Francesca_Vidotto_Published_July_2024.pdf
```

SHA256:

```text
32b14d1be69ef7eb6f2f668367220e77004643858c09301f454bde741c3b61bf
```

Public record:

```text
Carlo Rovelli and Francesca Vidotto,
"Planck stars, White Holes, Remnants and Planck-mass quasi-particles.
The quantum gravity phase in black holes' evolution and its manifestations",
arXiv:2407.09584 [gr-qc], submitted 2024-07-12, version 4 dated 2024-09-09,
doi:10.48550/arXiv.2407.09584.
```

arXiv URL:

```text
https://arxiv.org/abs/2407.09584
```

## Source Type

This is a review / synthesis paper, not an IO theorem source and not a direct
numerical validation of IO. For Paper 1 rebuild purposes it should be cited as:

```text
IMPORTED/EMPIRICAL background / IMPORTED standard-literature support
```

Use it to support that black-hole-to-white-hole / Planck-star / remnant
scenarios are active in the loop-quantum-gravity literature. Do not use it as a
proof of IO-specific equations unless the IO manuscript independently derives
the equation.

## Claims Potentially Relevant to Paper 1

### RV2024-1: Quantum-gravity effects become relevant in distinct black-hole regions

The paper distinguishes quantum-gravity onset regions in black-hole evolution:
the high-density collapsing matter region, the high-curvature interior outside
the matter distribution, and the near-horizon region made Planckian by Hawking
evaporation.

Use in Paper 1:

- Supports the reasonableness of treating the interior high-density endpoint,
  horizon dynamics, and evaporation/remnant stage as distinct physical regimes.
- Helps prevent a manuscript overmerge of horizon thermality, interior
  high-density bounce, and late remnant physics.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Does not prove the IO horizon-to-interior readout map.
- Does not prove IO's CMB/horizon identification.
- Does not fix IO normalization constants.

### RV2024-2: Oppenheimer-Snyder collapse is used as the simplest collapsing-star model

The paper uses the Oppenheimer-Snyder homogeneous pressureless collapse model
as the simplest model for a collapsing matter distribution and writes its
interior in comoving/proper-time Friedmann form.

Use in Paper 1:

- Supports the Paper 1 choice to frame the black-hole interior with an
  Oppenheimer-Snyder / closed-Friedmann interior geometry.
- Useful as external literature context, not as the derivation itself.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- IO must still derive its specific closed `K=+1` interior conventions and
  parameter identifications internally.
- This source does not license flat-space substitutions in IO calculations.

### RV2024-3: Loop-quantum-cosmology-style modification gives a high-density bounce

The review presents the standard LQC-style modified Friedmann form

```text
(a_dot/a)^2 = (8*pi/3) rho (1 - rho/rho_c)
```

with `rho_c` Planckian, yielding a non-singular bounce of the collapsing matter
distribution and a "Planck star" at maximal density.

Use in Paper 1:

- Supports citing a mainstream LQG/LQC route in which collapse is replaced by a
  high-density bounce.
- Can support a Paper 1 discussion of quantum-gravity pressure / effective
  repulsion as a standard literature route.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Does not derive IO's Einstein-Cartan torsion-bounce density.
- Does not by itself justify Poplawski's `15 rho_Pl` endpoint.
- Does not derive the Paper 32 connected spin-flux source coefficient.

### RV2024-4: Effective short-distance correction can appear as a repulsive inverse-fourth-power term

The paper rewrites the modified collapse dynamics in a form where the boundary
radius feels the usual Newtonian/Schwarzschild collapse term plus a repulsive
short-distance term proportional to an inverse fourth power of radius.

Use in Paper 1:

- Provides external context that high-density quantum-gravity completions of
  collapse can be represented as short-distance repulsive corrections.
- May be useful in comparing IO torsion-bounce behavior with LQG/LQC
  high-density bounce behavior.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Do not import the exact RV2024 effective metric as the IO metric unless a
  separate IO compatibility theorem is written.
- Does not select the IO torsion source law.

### RV2024-5: Black-to-white transition can be local/non-global and is not forbidden by Birkhoff locality

The paper argues that Birkhoff's theorem is local rather than a global
obstruction and that tunnelling in a compact quantum region can allow a black
hole to evolve into an anti-trapped / white-hole region.

Use in Paper 1:

- Useful support for an IO rebuild discussion that a black-hole interior
  bounce/white-hole continuation is not automatically ruled out by classical
  exterior uniqueness arguments.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Does not prove the IO post-bounce observer dictionary.
- Does not select hard vs soft restart.
- Does not prove a cyclic IO universe.

### RV2024-6: Evaporated black holes can have small horizons and large interiors

The paper reviews the result that a black hole's interior volume can grow with
advanced time and that an old evaporated black hole can have a small horizon
with a large interior volume.

Use in Paper 1:

- Strongly relevant to IO's "interior observer" framing.
- Supports caution against flat-space intuition that small boundary area implies
  small interior state capacity.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Does not prove IO's specific observable universe volume, mass, or radius
  identifications.
- Does not by itself derive a hidden support branch.

### RV2024-7: LQG area gap suggests Planck-scale remnant / quasi-particle mass

The review states that the LQG area gap gives a lowest nonzero horizon area
with `j=1/2`, leading to a Planck-mass remnant/quasi-particle scale.

Use in Paper 1:

- Useful for citing the `j=1/2` area-gap/minimal-horizon-sector idea in the
  broader LQG literature.
- Relevant background for later Paper 32 puncture-sector selector discussions.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Does not fix IO's Barbero-Immirzi value `gamma_BI=0.2375`.
- Does not prove the Paper 32 connected `J=1/2` spin-flux selector; that remains
  an IO theorem package.
- Does not imply particle dark matter exists in IO. IO's dark-sector handling is
  geometric/effective, so this source should be cited only as external LQG
  remnant context unless Paper 1 explicitly discusses alternatives.

### RV2024-8: Information can remain in interior/remnant degrees of freedom

The review argues against the need for an information paradox by distinguishing
horizon thermodynamic states from interior distinguishable states and noting
that the number of interior states need not be bounded by the instantaneous
horizon-area thermodynamic entropy.

Use in Paper 1:

- Supports the conceptual distinction between near-horizon thermodynamic
  degrees of freedom and large-interior hidden degrees of freedom.
- Useful context for IO's distinction between observer-side boundary readout
  and hidden support/interior degrees of freedom.

Claim label:

```text
IMPORTED/EMPIRICAL background
```

Boundary:

- Does not prove any IO entropy ledger.
- Does not derive a specific IO Hilbert-space quotient.

## Not To Import As Paper 1 Theorems

Do not use this source to claim:

- IO's CMB temperature is predicted independently.
- The CMB is the event horizon.
- IO's exact `T_IO`, `R4_FIRAS`, `K_gauge`, `x`, or `Q` normalizations.
- IO's Einstein-Cartan-Holst torsion cosmological constant.
- Poplawski's `15 rho_Pl` criterion unless separately cited to the relevant
  Poplawski/ECKS literature.
- Particle dark matter exists in IO.
- The Paper 32 late-time cycle or restart selectors are derived.

## Recommended Paper 1 Citation Use

Use this source in the Paper 1 rebuild as a literature-context citation for:

1. Planck-star / black-to-white-hole / remnant scenarios in LQG.
2. High-density quantum-gravity bounce replacing singular collapse.
3. OS collapse as a standard simple model for black-hole interior collapse.
4. Large-interior/small-horizon black-hole remnant intuition.
5. The LQG area-gap/minimal-horizon-sector context.

Do not use it as a load-bearing endpoint for IO-specific numerical predictions.

## MCP / Ledger Recommendation

Add this memo to the lab-state index as a Paper 1 source-ingestion artifact.
If a later Paper 1 theorem chain cites this source, create a separate
Claims/Theorem Ledger entry for the exact imported claim being used. Until then,
the source should remain a `source_ingestion` / `background_import` record, not
a theorem.

Final status:

```text
INGESTED AS BACKGROUND IMPORT FOR PAPER 1 REBUILD
```
