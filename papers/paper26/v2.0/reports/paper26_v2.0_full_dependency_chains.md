# Paper 26 v2.0 Full Dependency Chains

Date: 2026-05-16

Purpose: provide manuscript-ready dependency chains for the active Paper 26 v2.0 theorem and lemma surfaces requested for the v2.0 update. Each chain is written in canonical inline form and terminates either at IO Premise 1, IO Premise 2, a named standard external physics/mathematics input, or an explicitly open premise gap.

Claim labels used here:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `RECONSTRUCTION`
- `OPEN/PREMISE_GAP`
- `SUPERSEDED`

Premise abbreviations:

- `P1`: the observable universe is inside a Schwarzschild black hole.
- `P2`: physics inside the horizon equals physics outside.

## 1. Theorem 26.C3 - Reduced Source-Covariance Propagator

Status: `DERIVED/CONDITIONAL_VERIFIED` on the reduced centered Gaussian source-covariance class feeding the Paper 23 linear scalar bridge.

Canonical chain:

```text
Theorem 26.C3 (Reduced Source-Covariance Propagator)
<- Definition 26.C3.1 (reduced tangential source carrier)
<- Definition 26.C3.2 (reduced centered Gaussian source-covariance class)
<- Definition 26.C3.3 (effective source damping convention)
<- Lemma 26.C3.4 (reduced operator ratio O_A = Q O_Gamma, Q = 1 + gamma_BI^2 = exp(K_gauge))
<- Lemma 26.C3.5 (boundary descent to the reduced Gaussian source class)
<- Lemma 26.C3.6 (one inverse power: G_A^(1) = exp(-K_gauge) G_Gamma^(1))
<- Paper 23 Theorem 23.3 (No-Doubling: C^(0) = B G^(1) B^dagger)
<- Paper 18 v1.6 Theorem 18.C (CMP modular realization on the reduced observer algebra; supplies the reduced central tangential gauge sector and K_gauge center)
<- Paper 17 v1.5 Theorem 17.1 (GTTP reduced thermal/gauge transfer and K_gauge = ln(1 + gamma_BI^2) on the active reduced branch)
<- Paper 14 Theorem 14.1 (horizon-intrinsic reformulation of the reduced tangential operator)
<- Paper 10 section 10.1 / Paper 24 v3.0 Appendix Step 23 banked algebraic identity (K_gauge derivation on the S^2 horizon tangential block: O_A = ((1 + gamma_BI^2)/r_s^2) I_2 and O_Gamma = (1/r_s^2) I_2 on the reduced carrier; DERIVED/THEOREM algebraic identity, no separate Paper 10 theorem number found in the available indexed text)
<- P1 (fixes the Schwarzschild horizon boundary and reduced tangential horizon carrier)
<- P2 (imports standard exterior gauge/boundary-field physics for the same horizon-local interaction structures)
<- IMPORTED/EMPIRICAL standard mathematics/physics:
   Witten 1989, Chern-Simons/boundary-WZW architecture;
   Elitzur, Moore, Schwimmer, and Seiberg 1989, canonical quantization of Chern-Simons-Witten theory;
   Gallardo and Montesinos 2011, boundary field theory induced by Chern-Simons theory;
   Cattaneo, Mnev, and Wernli 2023, BV-BFV Chern-Simons boundary effective action;
   standard centered Gaussian inverse-kernel covariance theorem.
```

Scope note: this closes C3 only after replacing the broad older C3 statement with the reduced-source theorem. It does not close astrophysical reionization optical depth, ionization history, the low-ell EE reionization bump, full Boltzmann transfer, C1, or C2c.

## 2. Theorem 26.1 - Bridge Variable Identification

Status: `DERIVED/CONDITIONAL_VERIFIED` on the longitudinal-gauge, no-anisotropic-stress, isotropic Oppenheimer-Snyder background assumption package.

Canonical chain:

```text
Theorem 26.1 (Bridge Variable Identification)
<- Paper 23 scalar bridge definition B_N(delta A) = Pi_N^(0)[g^{ab} kappa_ij Abar_a^i delta A_b^j]
<- Paper 23 Theorem 23.3 (No-Doubling covariance architecture; the bridge takes boundary one-particle covariance into the scalar channel without duplicating the source covariance)
<- Paper 22 v2.0 Theorem 22.1 (Spatial Closure on S^3)
<- Paper 22 v2.0 Theorem 22.2 (Hodge Spectrum on the closed S^3 spatial slice)
<- Paper 22 v2.0 Theorem 22.5 (homogeneous Ashtekar-Barbero gauge placement in the lowest coexact channel)
<- Standard scalar perturbation theory in longitudinal gauge with Phi = Psi and no anisotropic stress
<- Cailleteau et al. 2012, "Anomaly-free scalar perturbations with holonomy corrections in loop quantum cosmology" (Ashtekar/LQC scalar perturbation formulas for delta E, delta K, and delta A = delta Gamma + gamma delta K)
<- P1 (closed K=+1 Oppenheimer-Snyder / closed-FRW interior background)
<- P2 (imports standard exterior GR/Ashtekar-Barbero perturbation algebra inside the horizon)
```

Conditional-verification note: the local algebraic cancellation of the spin-connection trace in the isotropic bridge contraction is derived. The remaining condition is the use of the same scalar perturbation algebraic structure on the closed K=+1 Oppenheimer-Snyder background as in the cited Ashtekar/LQC perturbation formulas. To promote this to `DERIVED/THEOREM`, Paper 26 would need a fully local closed-K calculation of the perturbation formulas rather than a structural import from the flat-FRW literature.

## 3. Theorem 26.2 - Bridge-Gain Cancellation

Status: `DERIVED/CONDITIONAL_VERIFIED` on the dust superhorizon branch.

Canonical chain:

```text
Theorem 26.2 (Bridge-Gain Cancellation)
<- Theorem 26.1 (Bridge Variable Identification)
<- Paper 23 Theorem 23.3 (No-Doubling: C^(0) = B G^(1) B^dagger)
<- conserved dust superhorizon branch: Phi = const, Phi' = 0, k << aH, equation of state w = 0
<- standard cosmological perturbation theory: comoving curvature perturbation R is conserved outside the horizon for adiabatic modes; R = (5/3) Phi on the dust branch
<- Mukhanov 2005, "Physical Foundations of Cosmology", section 7.3 (standard R/Phi conversion and superhorizon conservation)
<- P1 (closed Oppenheimer-Snyder interior supplies the dust/closed-FRW background branch used by Paper 26)
<- P2 (imports standard exterior cosmological perturbation theory for the same local perturbation equations)
```

Conditional-verification note: the cancellation is not a free normalization and does not use the observed scalar amplitude. It is valid on the dust superhorizon branch. Radiation-era conversion, subhorizon evolution, and closed-K canonical normalization choices are outside this theorem's local scope.

## 4. Lemma C2.1 - Background/Perturbation Channel Separation

Status: `DERIVED/THEOREM`.

Canonical chain:

```text
Lemma C2.1 (Background/Perturbation Channel Separation)
<- Paper 2 Theorem 2.1 (interior Hawking temperature from the horizon thermodynamic/Cardy/Carlip-Virasoro radial-timelike counting channel)
<- Paper 23 Theorem 23.3 (scalar perturbation covariance from the spatial/coexact bridge channel: C^(0) = B G^(1) B^dagger)
<- Paper 22 v2.0 Theorem 22.1 (closed S^3 spatial slice)
<- Paper 22 v2.0 Theorem 22.2 (S^3 coexact Hodge spectrum)
<- Paper 22 v2.0 Theorem 22.5 (homogeneous gauge placement in the spatial coexact channel)
<- IMPORTED/EMPIRICAL standard physics:
   Hawking 1975 black-hole temperature;
   Bekenstein-Hawking horizon thermodynamics;
   Carlip horizon conformal-symmetry/Cardy counting;
   standard cosmological perturbation theory separating background thermodynamics from perturbation covariance.
<- P1 (Schwarzschild horizon and closed Oppenheimer-Snyder interior)
<- P2 (standard exterior horizon thermodynamics and perturbation theory are admissible inside)
```

Scope note: Lemma C2.1 does not select the Hawking state on the S^2 coexact carrier. It only proves that the background temperature channel and the scalar perturbation covariance channel are not the same counting channel. C2c remains separate.

## 5. Lemma C2.2 - Carrier Identification

Status: `DERIVED/THEOREM`.

Canonical chain:

```text
Lemma C2.2 (Carrier Identification: S^2 ell=1 coexact carrier via U_coex)
<- Step 379 / reduced carrier-lift construction U_coex
<- Paper 22 v2.0 Theorem 22.1 (Spatial Closure: the bulk spatial slice is S^3)
<- Paper 22 v2.0 Theorem 22.2 (Hodge Spectrum: lowest coexact S^3 bridge carrier)
<- Paper 22 v2.0 Theorem 22.5 (homogeneous Ashtekar-Barbero gauge placement in the lowest coexact channel)
<- Paper 23 Theorem 23.3 (scalar bridge source covariance lives on the boundary one-particle covariance feeding the spatial bridge)
<- Paper 23 Theorem 23.4 (bridge uniqueness by Schur's lemma on the relevant irreducible channel)
<- standard representation theory of SU(2), SO(3), and the Hopf/Maurer-Cartan lift:
   S^3 is SU(2);
   the lowest coexact S^2 ell=1 carrier is the spin-1/adjoint representation;
   the lowest coexact S^3 n=1 bridge shell contains the same spin-1 carrier;
   the normalized U_coex map is the unitary equivariant intertwiner between these carriers.
<- P1 (S^2 Schwarzschild horizon boundary and S^3 closed interior geometry)
<- P2 (standard differential geometry and representation theory are admissible for the inside/outside bridge)
```

Scope note: Lemma C2.2 identifies the carrier. It does not select the physical state on that carrier. The remaining state-selection statement is C2c.

Open endpoint preserved:

```text
C2c (Hawking state selection) [OPEN/PREMISE_GAP]
<- would need a theorem proving that the boundary one-particle covariance G^(1) entering Paper 23 is specifically the S^2 Hawking thermal covariance at T_H on the U_coex carrier, rather than another mathematically admissible state.
```

## 6. Lemma 26.TK1 - Thomson Kernel

Status: `DERIVED/THEOREM`.

Canonical chain:

```text
Lemma 26.TK1 (Thomson Kernel)
<- standard scalar CMB Boltzmann perturbation equations: the primitive opacity factor kappa' = a n_e sigma_T appears in the visibility function g(z) = -(d kappa/dz) exp(-kappa) and in the photon-baryon momentum-transfer terms
<- standard Thomson scattering cross section sigma_T and photon-baryon tight-coupling physics
<- CLASS implementation verification: thermodynamics.c and perturbations.c use the same primitive opacity factor in the relevant visibility and photon-baryon coupling slots
<- Ma and Bertschinger 1995, "Cosmological Perturbation Theory in the Synchronous and Conformal Newtonian Gauges"
<- Dodelson 2003, "Modern Cosmology", standard recombination/visibility and acoustic-coupling equations
<- Blas, Lesgourgues, and Tram 2011, "The Cosmic Linear Anisotropy Solving System (CLASS) II: Approximation schemes"
<- P2 (standard exterior Thomson scattering and scalar Boltzmann perturbation equations are admissible inside the IO model)
```

Scope note: TK1 proves a shared primitive opacity factor only. It does not prove that visibility and acoustic loading must share the same IO baryon class. That class-membership step is AV1.

## 7. Theorem 26.AV' - Visibility Readout Closure

Status: `DERIVED/CONDITIONAL_VERIFIED` on AV1.

Canonical chain:

```text
Theorem 26.AV' (Visibility Readout Closure)
<- Lemma 26.TK1 (shared primitive Thomson opacity factor)
<- AV1 [OPEN/PREMISE_GAP] (Thomson-gated scalar CMB observables belong to the acoustic baryon class)
<- Paper 12 Baryon Dictionary Principle acoustic branch (omega_b,eff = (<K>/4) omega_m,geom for the acoustic baryon readout)
<- Paper 18 v1.6 Theorem 18.V (V(alpha) / observable-class baryon readout framework; once the observable class is fixed, the baryon slot is fixed by the class)
<- Paper 19 Theorem 19.JC4 (inventory and clustering baryon classes closed; CMB acoustic baryon-loading slot explicitly not authorized by the clustering branch)
<- P1 (closed IO geometry and framework constants entering <K>, Delta, x, and gamma_BI)
<- P2 (standard exterior photon-baryon Thomson physics and scalar CMB perturbation equations are admissible inside)
```

Open endpoint preserved:

```text
AV1 [OPEN/PREMISE_GAP]
<- needs a visibility-slot inheritance theorem proving that Thomson-gated scalar CMB visibility/readout observables inherit the acoustic baryon class, with no independent inventory-class or clustering-class baryon slot surviving in the observer-side visibility functional.
```

Implementation note: the proof assigns the observer-side visibility/readout slot. It does not reassign recombination chemistry. The manuscript should keep the chemistry/readout split visible because standard CLASS uses one baryon density for both unless explicitly modified.

## 8. Open Premise Endpoints

These endpoints are intentionally not promoted in Paper 26 v2.0.

```text
C1 [OPEN/PREMISE_GAP]
<- Paper 15 Theorem 15.1 proves the background gauge norm split Q(q_gamma) = 1 + gamma_BI^2 and the extrinsic fraction gamma_BI^2/(1 + gamma_BI^2).
<- C1 additionally assumes the fluctuation covariance inherits the same intrinsic/extrinsic split.
<- closure would require a fluctuation-covariance split theorem proving mixed covariance <delta Gamma . delta K> = 0 and component variances in the Paper 15 background ratio.
```

```text
C2c [OPEN/PREMISE_GAP]
<- Lemma C2.1 and Lemma C2.2 close channel separation and carrier identification.
<- C2c additionally selects the S^2 Hawking thermal covariance at T_H as the boundary one-particle covariance G^(1) on the proved carrier.
<- closure would require a state-selection theorem on the U_coex carrier, not just KMS uniqueness after a state/dynamics class has already been selected.
```

```text
AV1 [OPEN/PREMISE_GAP]
<- Lemma 26.TK1 proves the shared primitive Thomson opacity factor.
<- AV1 additionally asserts visibility/readout class membership in the acoustic baryon class.
<- closure would require a visibility-slot inheritance theorem for the scalar CMB readout functional.
```

```text
H1 [OPEN/PREMISE_GAP at the original Paper 25 v2.0 stack level]
<- H1 identifies the bridge KMS extension as the physical thermal state on the weak bridge algebra.
<- closure would require a state-selection theorem for the bridge KMS state rather than only uniqueness within the selected class.
```

```text
H2 [OPEN/PREMISE_GAP at the original Paper 25 v2.0 stack level]
<- H2 identifies the minimal spatial CCR lift as the physical perturbation sector.
<- closure would require a theorem that the minimal spatial CCR lift is forced by P1 + P2 + the Paper 22/Paper 23 bridge architecture.
```

## 9. Manuscript and Scope Issues Surfaced

1. Appendix Step 382 conflicts with the body statement of Theorem 26.1. The body says the scalar bridge reads the extrinsic-curvature perturbation gamma delta K and the spin-connection perturbation delta Gamma vanishes under isotropic contraction. Step 382 says delta Gamma is the physical bridge variable and the extrinsic curvature perturbation cancels. The v2.0 manuscript should use the body Theorem 26.1 wording unless a new derivation changes the theorem.

2. Appendix Step 387 contains a squared-occupation A_s expression, `(25/9) * [2/(exp(4 pi sqrt(2)) - 1)]^2 * [gamma^2/(1+gamma^2)]`, while the body uses the active non-squared occupation formula `(25/9) * [gamma^2/(1+gamma^2)] * [1/sqrt(2)] * 1/(exp(4 pi sqrt(2)) - 1)`. The squared appendix expression should not remain active unless it is deliberately re-derived and reconciled.

3. Appendix Step 400 gives `tau_eff,IO = gamma^2/(1+gamma^2) * tau_geom`, which conflicts with the new Theorem 26.C3 result `tau_eff,IO = K_gauge/2`. If C3 is updated per the reduced source-covariance theorem, Step 400 must be replaced.

4. Existing open-problem and conditionals lists still naming C3 as `OPEN/PREMISE_GAP` should be narrowed. C3 can be removed as an independent open premise only under the reduced centered Gaussian source-covariance theorem wording. Reionization history and the low-ell EE bump remain open.

5. Theorem 26.1 should remain `DERIVED/CONDITIONAL_VERIFIED`, not `DERIVED/THEOREM`, until the closed K=+1 Oppenheimer-Snyder scalar Ashtekar perturbation calculation is written locally rather than imported by algebraic analogy from flat-FRW perturbation formulas.
