# Paper 26 v1.1 Kappa-Style Structural Audit

Date: May 2026

Scope: Paper 26 v1.1, "The Primordial Scalar Amplitude from the Hawking
Boundary State, Toward IO-Native Replacements for LambdaCDM-Borrowed Inputs,
Source-Side Reduction, the CMB Baryon Class Diagnostic, and the Effective
Optical Damping Parameter."

Method: expose each load-bearing numerical or structural choice as a candidate
field, replace it by a free variable, and ask whether an existing theorem,
symmetry, scoped extension premise, or standard external result forces the
original value. Classifications follow the IO conventions: DERIVED,
DERIVED/SCOPED, DERIVED/CONDITIONAL, CONDITIONAL, VERIFIED, RECONSTRUCTION,
FITTED, or HIDDEN PARAMETER.

## Executive Verdict

No unlabelled continuous fitted parameter was found in the active Paper 26
v1.1 claims.

However, Paper 26 is not an unconditional closure paper. Its headline numerical
replacements depend on four visible conditionals:

- C1: the background extrinsic/intrinsic gauge partition is inherited by the
  fluctuation covariance.
- C2c: the source covariance on the proved S2 coexact carrier is specifically
  the Hawking thermal covariance.
- AV1: Thomson-gated scalar CMB observables belong to the acoustic baryon
  class.
- C3: the CMB source covariance uses the inverse tangential propagator
  readout rather than a determinant/readout or another operator functional.

The audit therefore supports the public classification:

- `A_s = 2.0072459972737347e-9`: DERIVED/CONDITIONAL on C1 + C2c.
- `omega_b,vis = omega_b,eff = 0.02910`: DERIVED/CONDITIONAL on AV1.
- `tau_eff,IO = K_gauge/2 = 0.02743640887145733`: DERIVED/CONDITIONAL on C3;
  not identical to astrophysical reionization optical depth.
- reionization-shape irrelevance for TT high-l: VERIFIED computational
  diagnostic, not a proof for low-l EE.

## Hygiene Finding

The active body text of Paper 26 v1.1 states Theorem 26.1 as:

> the scalar bridge reads gamma delta K, and the spin-connection perturbation
> delta Gamma vanishes under the isotropic contraction.

Some inherited Step-style memory/appendix text uses an older opposite phrasing:
delta Gamma as the physical bridge variable with the gamma delta K component
cancelling. Future sessions must treat the v1.1 body theorem as the active
claim unless the manuscript is explicitly revised. Paper 26 v1.2 should add a
short clarification or remove the stale phrasing from inherited appendix
material.

This is a manuscript-hygiene issue, not a discovered fitted parameter.

## Candidate Fields and Rigidity Tests

### 1. gamma_BI = 0.2375

Field replacement: gamma -> kappa_gamma.

Rigidity test: Paper 26 inherits gamma_BI from the framework/LQG input. It is
not fitted to Planck in Paper 26. Changing it would alter every IO paper that
uses K_gauge and Q.

Classification: DERIVED/SCOPED upstream input for Paper 26; not fitted inside
Paper 26.

### 2. Dust superhorizon conversion factor 25/9

Field replacement: 25/9 -> kappa_R.

Rigidity test: 25/9 is the square of the standard dust-branch relation
R = (5/3) Phi. The choice of dust branch is stated and tied to late-time
normalization. A radiation-branch conversion would produce a different value,
so the branch assumption must remain visible.

Classification: DERIVED on the dust superhorizon branch; scoped branch choice.

### 3. S2 coexact lowest shell ell=1

Field replacement: ell=1 -> ell=k or use the radial/time-frequency channel.

Rigidity test: Lemma C2.1 separates background thermodynamic/Cardy counting
from perturbation bridge covariance. Lemma C2.2 constructs the lowest-shell
S2-to-S3 coexact carrier. The carrier is therefore not arbitrary, but the
choice of Hawking thermal state on that carrier remains C2c.

Classification: C2a DERIVED; C2b DERIVED GEOMETRIC CONSTRUCTION; C2c
CONDITIONAL.

### 4. Hawking exponent beta_H hbar omega_1 = 4 pi sqrt(2)

Field replacement: beta omega -> kappa_beta.

Rigidity test: Once the S2 ell=1 coexact carrier and Hawking temperature are
chosen, the exponent is forced by omega_1 = sqrt(2)c/r_s and
beta_H = 4 pi r_s/(hbar c). All dimensional factors cancel.

Classification: DERIVED conditional on C2c state selection.

### 5. Bose occupation g_H = 1/(exp(4 pi sqrt(2)) - 1)

Field replacement: use Maxwell-Boltzmann, vacuum variance, or another
occupation law.

Rigidity test: Bose occupation is forced for a bosonic Hawking thermal state.
The state selection is the conditional part; the occupation formula is not
free once C2c is admitted.

Classification: DERIVED/CONDITIONAL on C2c.

### 6. Canonical coordinate normalization 1/sqrt(2)

Field replacement: 1/sqrt(2) -> 1, 1/(2 sqrt(2)), or kappa_norm.

Rigidity test: The factor is the standard harmonic-coordinate variance n/omega
with dimensionless omega = sqrt(2). Earlier alternative normalizations exist in
the private audit record and produce different amplitudes. Paper 26's active
choice is justified by canonical thermal-coordinate normalization, not by a
fit.

Classification: DERIVED from standard canonical normalization once the
coordinate convention is admitted; not fitted.

### 7. Extrinsic fraction f_K = gamma^2/(1+gamma^2)

Field replacement: f_K -> kappa_f.

Rigidity test: Paper 15 proves the background gauge partition. Paper 26 C1
extends that background partition to fluctuation covariance. The extension is
not proved by Paper 15 and is explicitly conditional.

Classification: CONDITIONAL on C1; visible.

### 8. Scalar amplitude formula

Field replacement: replace any factor in

    A_s = (25/9) f_K (1/sqrt2) [exp(4 pi sqrt2)-1]^-1

with a fitted scalar.

Rigidity test: The active factors are discrete/structural choices, not scanned
to minimize Planck residual. The result lands at 2.007e-9, about -4.4% from
Planck's 2.100e-9. The residual is not tuned away.

Classification: DERIVED/CONDITIONAL on C1 + C2c. No fitted scalar found.

### 9. Conditional tensor-to-scalar ratio

Field replacement: choose tensor shell, tensor carrier, or transport by fit.

Rigidity test: Paper 26 presents the tensor number only as conditional. Tensor
bridge payload, boundary carrier, and transport remain open. The prediction is
not theorem-grade and is not used as a current closure claim.

Classification: CONDITIONAL/SPECIFICATION, not fitted.

### 10. Baryon densities omega_b,geom, omega_b,eff, omega_b,clustering

Field replacement: tune three baryon densities independently.

Rigidity test: The three values are inherited from Papers 12/18/19. Paper 26
does not fit them to CLASS. It tests which theorem-authorized observable class
is allowed in CMB slots. Paper 19 explicitly did not authorize
omega_b,clustering in CMB perturbation slots.

Classification: DERIVED/SCOPED upstream values; CMB slot assignment
CONDITIONAL where AV1 is used.

### 11. Thomson Kernel Lemma

Field replacement: visibility and acoustic oscillations use unrelated opacity
primitives.

Rigidity test: The primitive opacity factor kappa' = a n_e sigma_T appears in
both visibility and photon-baryon momentum-transfer equations. The full kernels
are not identical; Paper 26 correctly narrows the claim to the shared primitive
factor.

Classification: DERIVED equation-level fact.

### 12. AV1 visibility class assignment

Field replacement: same primitive Thomson factor does not imply same
observable class.

Rigidity test: This is exactly the remaining conditional. The shared primitive
factor narrows the argument, but observable-class membership is not forced by
the current theorem stack.

Classification: CONDITIONAL premise, visible.

### 13. CLASS baryon diagnostic chi-square numbers

Field replacement: choose baryon slot by best fit.

Rigidity test: The branch assignments are pre-declared. The resulting
diagnostics are computational consequences: clustering-only CMB use is
catastrophic, one-fluid/acoustic visibility branch is less bad but still not a
full Planck-quality fit.

Classification: VERIFIED diagnostic; not theorem proof.

### 14. tau_eff = K_gauge/2

Field replacement: tau_eff -> K_gauge, f_K, or fitted tau.

Rigidity test: If C3 selects inverse tangential propagation, the source
amplitude is damped by exp(-K_gauge). Standard TT amplitude convention is
A_eff = A_s exp(-2 tau), so tau_eff = K_gauge/2. The factor 1/2 is a convention
conversion, not a fit.

Classification: DERIVED/CONDITIONAL on C3.

### 15. A_eff = A_s exp(-K_gauge)

Field replacement: A_eff -> fitted TT ridge amplitude.

Rigidity test: A_eff follows from the active A_s and C3 damping rule. It lands
near the TT extraction but is not tuned to it. If C1/C2c or C3 falls, A_eff
falls with them.

Classification: DERIVED/CONDITIONAL; VERIFIED arithmetic.

### 16. Reionization shape irrelevance for TT high-l

Field replacement: reionization shape strongly changes high-l TT.

Rigidity test: CLASS shape sweeps show high-l TT chi-square shifts below 0.4
for the tested reionization-shape variations. This does not apply to low-l EE,
which remains shape-sensitive.

Classification: VERIFIED computational diagnostic; low-l EE caveat visible.

## Anti-Fit Backstop

The headline values are not produced by continuous optimization:

- A_s is constructed from C1/C2c plus standard Hawking/canonical factors.
- omega_b class assignments are inherited/tested, not adjusted continuously.
- tau_eff is K_gauge/2 by inverse-propagator convention conversion, not fitted
  to Planck tau.

The closest anti-fit risk is C2c: selecting a Hawking thermal state on the
proved S2 coexact carrier is physically natural inside IO, but it is not forced
by the theorem stack. Paper 26 labels this as conditional. Therefore the risk
is visible conditionality, not hidden fitting.

## Cross-Paper Dependency Check

Recent BBN YPCMB wrapper corrections in Papers 19-25 do not alter Paper 26's
headline A_s, baryon-class, or tau_eff formulas. They do matter for any
cross-paper BBN scorecard references in inherited appendix material. Future
Paper 26 v1.2 manuscript edits should refresh inherited BBN references to the
current corrected papers.

Paper 32/34/35 later conditional-visibility hygiene supports the same action:
Paper 26 should add or preserve a Scope/Open Premises section that explicitly
lists C1, C2c, AV1, and C3.

## Audit Conclusion

Paper 26 v1.1 survives the formal kappa-style audit in the narrow sense: no
hidden continuous fitted parameter was found. The correct public framing is
not "Paper 26 derives all CMB inputs theorem-grade." The correct framing is:

Paper 26 constructs IO-native replacements for A_s, CMB baryon-class readout,
and effective optical damping with zero fitted parameters, but the headline
numbers are conditional on C1, C2c, AV1, and C3. Reionization shape
insensitivity is verified for high-l TT only and does not solve low-l EE.

The v1.2 manuscript update should fix the bridge-variable wording conflict in
inherited step material and make the conditional-premise ledger prominent.
