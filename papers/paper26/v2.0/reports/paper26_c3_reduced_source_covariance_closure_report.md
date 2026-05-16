# Paper 26 C3 Reduced Source-Covariance Closure Report

Date: 2026-05-16

## Executive Verdict

C3 can be closed only after narrowing the old Paper 26 wording.

The old statement,

> The physical source covariance relevant for CMB anisotropy is controlled by the inverse of Paper 10's reduced tangential quadratic operator O_A.

is too broad if read as a theorem about all CMB source physics, reionization physics, or the full TT/TE/EE transfer problem. In that broad form it remains overextended.

The theorem-grade replacement is:

> On the reduced centered Gaussian source-covariance class feeding the Paper 23 linear scalar bridge, the Ashtekar-Barbero source covariance carries one inverse power of the reduced tangential operator ratio O_A = (1 + gamma_BI^2) O_Gamma. Therefore G_A^(1) = exp(-K_gauge) G_Gamma^(1), C_ell^A = exp(-K_gauge) C_ell^Gamma, and tau_eff,IO = K_gauge / 2.

Status:

`DERIVED/CONDITIONAL_VERIFIED` for the reduced centered Gaussian source-covariance class.

The condition is not an adjustable parameter. It is an intrinsic observable-class restriction: centered, linear, reduced Gaussian source covariance on the already-reduced tangential boundary source sector feeding Paper 23's linear scalar bridge. The chain terminates at Premise 1, Premise 2, Paper 10/Paper 14 operator identities, Paper 17/Paper 18 reduced central tangential sector, Paper 23 linear bridge/no-doubling, and standard external Chern-Simons boundary-descent plus Gaussian covariance theory.

No observational value is used to select tau_eff. In fact tau_eff,IO = K_gauge/2 is not chosen to match Planck tau; it differs strongly from the LCDM-reported astrophysical tau. That is evidence against hidden fitting, not evidence for the theorem.

## Scope Boundary

Closed:

- the one-inverse-power law for the reduced centered Gaussian source covariance,
- the covariance damping factor exp(-K_gauge),
- the effective high-ell source damping identification tau_eff,IO = K_gauge/2,
- the C3 slot as used in the Paper 26 A_eff arithmetic.

Not closed:

- astrophysical reionization optical depth tau_reio,
- the ionization history x_e(z),
- the low-ell EE reionization bump,
- the full IO-native Boltzmann transfer pipeline,
- the absolute primordial scalar amplitude A_s,
- C1 or C2c,
- literal nonabelian WZW current-current propagators,
- arbitrary horizon observables outside the reduced centered Gaussian source-covariance class.

Therefore Paper 26 may remove C3 from the open-premise list only if the manuscript replaces broad C3 with this reduced-source theorem and keeps the reionization and low-ell EE caveats.

## Definitions

### Definition 26.C3.1 - Reduced tangential source carrier

The reduced tangential source carrier is the two-dimensional tangential connection carrier on the horizon boundary after the Paper 10/Paper 14 reduction. On this carrier,

```text
O_A     = ((1 + gamma_BI^2) / r_s^2) I_2,
O_Gamma = (1 / r_s^2) I_2,
O_A     = Q O_Gamma,
Q       = 1 + gamma_BI^2 = exp(K_gauge).
```

Chain: Paper 10 reduced tangential operator calculation; Paper 14 Theorem 14.1 horizon-intrinsic reformulation; Paper 17/Paper 18 reduced central tangential gauge sector; Premise 1.

### Definition 26.C3.2 - Reduced centered Gaussian source-covariance class

An observable belongs to the reduced centered Gaussian source-covariance class if:

1. its boundary source field lives on the reduced tangential source carrier of Definition 26.C3.1;
2. it is centered, so only the two-point covariance is relevant;
3. it is quasi-free/Gaussian on the reduced source field, with effective action

```text
S_eff[xi] = (1/2) <xi, K_A xi>;
```

4. the source observable entering the scalar bridge is linear in xi;
5. its bridge propagation is through the Paper 23 linear no-doubling map

```text
C^(0) = B G^(1) B^dagger;
```

6. all non-Ashtekar-Barbero spectral factors in K_A are gamma-blind, so the A-versus-Gamma distinction is exactly the scalar operator ratio Q.

This definition is intrinsic. Membership can be tested without using the conclusion tau_eff,IO = K_gauge/2.

Chain: Definition 26.C3.1; Paper 23 Theorem 23.3 no-doubling; standard quasi-free/Gaussian covariance theory; Premise 2.

### Definition 26.C3.3 - Effective source damping convention

For a multiplicative source-covariance damping factor D on a high-ell primary CMB covariance, define tau_eff by the standard phenomenological covariance convention

```text
D = exp(-2 tau_eff).
```

This is a convention translating a covariance-level multiplicative factor into a tau-like high-ell damping parameter. It is not a claim that tau_eff is the astrophysical Thomson optical depth tau_reio.

Chain: standard CMB covariance damping convention; Paper 26 Section 4; Premise 2.

## Lemma 26.C3.4 - Reduced Operator Ratio

On the reduced tangential source carrier,

```text
O_A = Q O_Gamma,
Q = 1 + gamma_BI^2 = exp(K_gauge).
```

### Proof

Paper 10's reduced tangential calculation and Paper 14's horizon-intrinsic reformulation give

```text
O_A     = ((1 + gamma_BI^2) / r_s^2) I_2,
O_Gamma = (1 / r_s^2) I_2.
```

Dividing the two operators gives

```text
O_A = (1 + gamma_BI^2) O_Gamma.
```

By definition,

```text
K_gauge = ln(1 + gamma_BI^2),
```

so

```text
1 + gamma_BI^2 = exp(K_gauge).
```

Therefore O_A = exp(K_gauge) O_Gamma. QED.

Chain: Paper 10 reduced tangential operator calculation; Paper 14 Theorem 14.1; Paper 17/Paper 18 K_gauge definition; Premise 1.

## Lemma 26.C3.5 - Boundary Descent to the Reduced Gaussian Source Class

On the already-reduced tangential center, the Chern-Simons first-order objection does not block a Gaussian source covariance. Standard Chern-Simons boundary theory supplies a boundary effective source theory; on the reduced abelian/central sector, its degree-zero physical part is a quadratic conformal boundary theory. Therefore reduced centered linear source observables in Definition 26.C3.2 have covariance governed by the inverse quadratic kernel.

### Proof

The first-order Chern-Simons action would block C3 if the relevant observable were the literal nonabelian WZW current-current correlator or the bare perturbative Chern-Simons vacuum propagator. Paper 26 already excludes those routes.

The C3 observable class is different. It is a reduced centered source covariance entering the scalar bridge linearly through Paper 23's no-doubling map. On the Paper 17/Paper 18 reduced tangential center, the active gauge datum is a scalar central operator:

```text
Q_hat = (1 + gamma_BI^2) I,
K_hat_g = ln(Q_hat) = K_gauge I.
```

Thus the A-versus-Gamma distinction is effectively abelian on the reduced source carrier.

External Chern-Simons boundary theory supports this descent:

- Witten (1989) and Elitzur-Moore-Schwimmer-Seiberg (1989) establish the Chern-Simons/boundary-WZW architecture.
- Gallardo and Montesinos (2011) write Chern-Simons theory on a 3-manifold with boundary as a boundary field theory and count one physical local boundary degree of freedom for SU(2).
- Cattaneo, Mnev, and Wernli (2022/2023) show that, for Chern-Simons theories on cylinders, the physical degree-zero part of the BV-BFV effective action identifies with the Hamilton-Jacobi action without quantum corrections; in the three-dimensional abelian case the holographic dual is the two-dimensional free boson CFT.

Applying these standard external results under Premise 2 to the already-reduced central/abelian tangential sector gives a quadratic effective source action for Definition 26.C3.2. For a centered Gaussian source field xi with action

```text
S_eff[xi] = (1/2) <xi, K_A xi>,
```

standard Gaussian covariance theory gives covariance K_A^(-1). QED.

Chain: Premise 2; Paper 17/Paper 18 reduced central tangential sector; Paper 23 Theorem 23.3; Witten 1989; Elitzur-Moore-Schwimmer-Seiberg 1989; Gallardo-Montesinos 2011; Cattaneo-Mnev-Wernli 2022/2023; standard Gaussian covariance theorem.

## Lemma 26.C3.6 - One Inverse Power

For every observable in the reduced centered Gaussian source-covariance class,

```text
G_A^(1) = Q^(-1) G_Gamma^(1)
        = exp(-K_gauge) G_Gamma^(1).
```

### Proof

Let xi be the reduced Gaussian source field and let s = L xi be any centered linear source observable in the class. Then

```text
G_A^(1) = <s s>_A = L K_A^(-1) L^dagger.
```

By Definition 26.C3.2, all non-Ashtekar-Barbero spectral factors are gamma-blind, and the A-versus-Gamma distinction is the scalar factor Q from Lemma 26.C3.4. Therefore

```text
K_A = Q K_Gamma.
```

Since Q is a positive scalar on the reduced carrier,

```text
K_A^(-1) = (Q K_Gamma)^(-1) = Q^(-1) K_Gamma^(-1).
```

Thus

```text
G_A^(1) = L K_A^(-1) L^dagger
        = Q^(-1) L K_Gamma^(-1) L^dagger
        = Q^(-1) G_Gamma^(1).
```

Using Q = exp(K_gauge) gives the result. QED.

Chain: Definition 26.C3.2; Lemma 26.C3.4; Lemma 26.C3.5; standard inverse-kernel covariance theorem.

## Theorem 26.C3 - Reduced Source-Covariance Propagator Theorem

For the reduced centered Gaussian source-covariance class feeding the Paper 23 linear scalar bridge, the physical A-branch source covariance is controlled by the inverse of Paper 10's reduced tangential quadratic operator. The resulting covariance damping factor is

```text
D_C3 = exp(-K_gauge).
```

Equivalently, in the covariance convention D = exp(-2 tau_eff),

```text
tau_eff,IO = K_gauge / 2.
```

Numerically, with gamma_BI = 0.2375,

```text
K_gauge = ln(1 + gamma_BI^2)
        = 0.05487281774291466,

tau_eff,IO = 0.02743640887145733.
```

### Proof

By Lemma 26.C3.6,

```text
G_A^(1) = exp(-K_gauge) G_Gamma^(1)
```

for every reduced centered Gaussian source covariance in the class.

The Paper 23 scalar no-doubling map is linear in the boundary covariance:

```text
C^(0) = B G^(1) B^dagger.
```

Therefore multiplying G^(1) by exp(-K_gauge) multiplies the propagated scalar source covariance by the same factor:

```text
C_ell^A = exp(-K_gauge) C_ell^Gamma.
```

Using Definition 26.C3.3,

```text
exp(-2 tau_eff,IO) = exp(-K_gauge),
```

so

```text
tau_eff,IO = K_gauge / 2.
```

The numerical value follows by direct substitution of gamma_BI = 0.2375. QED.

Chain: Premise 1; Premise 2; Definition 26.C3.1; Definition 26.C3.2; Definition 26.C3.3; Paper 10 reduced tangential operator calculation; Paper 14 Theorem 14.1; Paper 17/Paper 18 reduced central tangential sector; Paper 23 Theorem 23.3 no-doubling; Lemmas 26.C3.4-26.C3.6; Witten 1989; Elitzur-Moore-Schwimmer-Seiberg 1989; Gallardo-Montesinos 2011; Cattaneo-Mnev-Wernli 2022/2023; standard Gaussian covariance theorem.

Status: `DERIVED/CONDITIONAL_VERIFIED` for the reduced centered Gaussian source-covariance class.

## Anti-Fit Check

No observational value is used in the derivation.

The theorem uses only:

- gamma_BI = 0.2375, inherited as the framework Barbero-Immirzi input;
- K_gauge = ln(1 + gamma_BI^2);
- the reduced operator ratio O_A = (1 + gamma_BI^2) O_Gamma;
- inverse-kernel covariance propagation.

The resulting value tau_eff,IO = 0.02743640887145733 is not selected to match the Planck LCDM optical-depth extraction tau = 0.054 +/- 0.007. It is approximately half that reported value. This is exactly why Paper 26 must continue to state that tau_eff,IO is not astrophysical tau_reio and does not automatically produce the low-ell EE reionization bump.

## Manuscript Consequences

Recommended Paper 26 v2.0 changes:

1. Replace "Conditional Identification C3" with "Reduced Source-Covariance Propagator Theorem".
2. Replace the old C3 open-premise language with:

```text
Theorem 26.C3 closes the propagator identification on the reduced centered Gaussian source-covariance class feeding the Paper 23 linear scalar bridge. The theorem does not identify tau_eff,IO with astrophysical tau_reio and does not close reionization history or the low-ell EE bump.
```

3. In the conditional-premise inventory, remove C3 as an independent `OPEN/PREMISE_GAP`.
4. Keep the low-ell EE and reionization-history caveats as open.

## References

- E. Witten, "Quantum Field Theory and the Jones Polynomial," Communications in Mathematical Physics 121, 351-399 (1989).
- S. Elitzur, G. Moore, A. Schwimmer, N. Seiberg, "Remarks on the Canonical Quantization of the Chern-Simons-Witten Theory," Nuclear Physics B 326, 108-134 (1989), doi:10.1016/0550-3213(89)90436-7.
- A. Gallardo and M. Montesinos, "The boundary field theory induced by the Chern-Simons theory," Journal of Physics A 44, 135402 (2011), doi:10.1088/1751-8113/44/13/135402.
- A. S. Cattaneo, P. Mnev, and K. Wernli, "Quantum Chern-Simons Theories on Cylinders: BV-BFV Partition Functions," Communications in Mathematical Physics 400, 1203-1280 (2023), doi:10.1007/s00220-022-04513-8.

## Final Verdict

Proof complete for the reduced source-covariance class. Broad C3 must be narrowed. C3 can be removed as an independent Paper 26 open premise only under the theorem wording above and only with the stated reionization/low-ell EE guardrails.
