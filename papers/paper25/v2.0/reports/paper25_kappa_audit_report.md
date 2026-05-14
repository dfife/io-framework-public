# Paper 25 v1.2 Kappa-Style Structural Audit

Date: May 2026

Scope: Paper 25 v1.2, "The Weak-Sector Identity Pin / Quadratic Thermal
Covariance, the Channel-Budget Equation, and the V-vs-V' Class-Membership
Theorem."

Method: expose each load-bearing numerical or structural choice as a candidate
field, replace it by a free variable, and ask whether the existing theorem
stack, an explicit scoped premise, or a symmetry/invariance forces the value.
Classifications use the IO convention: DERIVED, DERIVED/SCOPED,
DERIVED/CONDITIONAL, CONDITIONAL/THEOREM, VERIFIED, RECONSTRUCTION, FITTED,
or HIDDEN PARAMETER.

## Executive Verdict

No unlabelled continuous fitted parameter was found in the active Paper 25 v1.2
claim stack.

The audit does find conditional structure, but it is visible rather than hidden.
The weak-sector identity pin closes only inside the H1-H3 premise package:

- H1: the Paper 22 Construction 1 + Paper 23 Lemma 23.A spatial KMS extension
  is the physical bridge state.
- H2: the minimal spatial CCR lift is the physical perturbation sector for
  weak-rate dressing.
- H3: the physical weak freeze-out rate is represented by a centered two-time
  KMS correlator, i.e. a rate/two-point object rather than a one-point
  amplitude.

Within that package, the decisive structural result is rigid: the centered
two-time bridge correlator is bilinear in the bridge Riesz vector F_0. A
linear V' = 2 gamma channel has no place to enter the physical weak rate. The
constructed-extension computation then gives R(gamma) = 1 and
Gamma_w(gamma)/Gamma_w(0) = 1 + gamma^2, so the logarithmic payload is
K_gauge = ln(1 + gamma^2).

The Paper 25 BBN scorecard is VERIFIED computational support, not a theorem.
The active v1.2 public scorecard is the Paper 24 final-push YPCMB path with
amplitude alignment:

- epsilon_w = K_gauge * L_1 = 0.012300778733811872.
- epsilon_n = (<K>/10) * L_2 = 0.02384221534546833.
- D/H = 2.509938817767262e-5, residual -0.5687060744245984 sigma.
- Y_p = 0.24771903130174175, residual +0.6797578254354383 sigma.
- Li-7/H = 1.7508826463710944e-10, residual +0.5512343431325627 sigma.
- chi2(D/H + Y_p + Li-7) = 1.0893566013769407.

Paper 25 v1.2 correctly treats the V' branch as structurally excluded by the
rate/two-point theorem and catastrophically disfavored numerically. The
numerical catastrophe is a backstop, not the proof.

## Candidate Field Catalog and Rigidity Tests

### 1. gamma_BI = 0.2375

Field replacement: gamma -> kappa_gamma.

Rigidity test: Paper 25 inherits gamma_BI as the external Barbero-Immirzi value
used throughout the IO framework. Paper 25 does not fit gamma to BBN. Changing
gamma changes K_gauge, Q, V', and the branch scorecards, but it would be a
framework-wide input change rather than an internal Paper 25 tuning freedom.

Classification: DERIVED/SCOPED upstream input for Paper 25; not fitted inside
Paper 25.

### 2. K_gauge = ln(1 + gamma^2)

Field replacement: K_gauge -> arbitrary f(gamma).

Rigidity test: Paper 18 fixes the reduced gauge-center generating potential
V(alpha) = -2 ln(cos alpha). At alpha = arctan(gamma), V = ln(1 + gamma^2).
If the weak observable is in the finite modular readout class, K_gauge is
forced. Paper 25's job is the class-membership step, not the functional form.

Classification: DERIVED upstream; DERIVED/CONDITIONAL as weak-sector payload
inside H1-H3.

### 3. V' = 2 gamma

Field replacement: V' -> kappa_Vprime.

Rigidity test: V' is the tangent covector of the same Paper 18 potential. It is
not free. The audit question is whether the weak rate reads V or V'. Paper 25
forces V rather than V' by showing the physical weak rate is a two-time
correlator bilinear in F_0; V' requires a linear bridge channel.

Classification: DERIVED as tangent object; structurally excluded from the weak
rate under H1-H3.

### 4. V'' = 2(1 + gamma^2)

Field replacement: V'' -> kappa_Vdd.

Rigidity test: V'' is fixed by the Paper 18 potential. Paper 25 excludes it as
the weak logarithmic payload because the constructed extension gives
ln[Gamma_w(gamma)/Gamma_w(0)] = ln(1 + gamma^2), not 2(1 + gamma^2).

Classification: DERIVED as curvature object; excluded from the weak rate
CONDITIONAL on H1 via Theorem 25.12.

### 5. H1 spatial KMS extension identification

Field replacement: choose a different bridge state or KMS extension.

Rigidity test: The explicit extension is constructed and internally checked,
but Paper 25 does not prove that nature selects it unconditionally. This is
declared in the manuscript as H1.

Classification: CONDITIONAL premise, visible. Not a hidden parameter.

### 6. H2 minimal spatial CCR lift

Field replacement: choose a non-minimal perturbation-sector lift.

Rigidity test: Paper 25 uses the minimal lift as the physical weak-rate
dressing sector. The lift is not fitted to the BBN scorecard, but the physical
identification is admitted as a premise.

Classification: CONDITIONAL premise, visible. Not a hidden parameter.

### 7. H3 centered two-time KMS rate identification

Field replacement: treat the weak modification as a one-point amplitude or as
an uncentered correlator with a nonzero linear term.

Rigidity test: H3 is the decisive physical input. It is standard rate physics
in the Fermi Golden Rule sense, but in the IO theorem stack it is still the
physical-identification premise that lets the weak sector read a two-point
object. Paper 25 declares H3 explicitly.

Classification: CONDITIONAL premise, visible. Not a hidden parameter.

### 8. Centering of the bridge field

Field replacement: omega_br(Phi(F)) -> kappa_1 != 0.

Rigidity test: In the centered quasi-free KMS bridge state used by Paper 25,
the one-point bridge term vanishes. If this centering is relaxed, a linear
interference channel may reappear. Paper 25's exclusion of V' is therefore
conditional on the centered KMS rate package, not a free post-hoc tuning.

Classification: DERIVED inside the centered quasi-free package; CONDITIONAL on
H1-H3 as a physical claim.

### 9. Bilinearity of C_br(t)

Field replacement: C_br(t) -> linear-plus-quadratic functional of F_0.

Rigidity test: For a gauge-invariant quasi-free bosonic state, the bridge
two-time correlator is a sum of pairings and is bilinear in F_0 for all t.
The proof does not use the observed BBN values.

Classification: DERIVED/THEOREM inside the stated CCR/KMS package.

### 10. R(gamma) = 1

Field replacement: R(gamma) -> arbitrary positive function.

Rigidity test: R(gamma) = 1 follows on the explicit constructed extension when
beta_IO and the active one-particle Hamiltonian eigenvalue are gamma-blind.
If a different physical bridge state is selected, R(gamma) is not forced by
Paper 25 alone.

Classification: DERIVED on constructed extension; CONDITIONAL on H1.

### 11. epsilon_w = K_gauge * L_1

Field replacement: epsilon_w -> K_gauge * L_1^p or c * K_gauge * L_1.

Rigidity test: K_gauge is fixed by the weak payload; L_1 is inherited from the
Paper 21 puncture-load construction. The exponent p = 1 is forced by the
rate/two-point bilinearity correction relative to the retired sqrt(L_1) branch,
inside H1-H3. A free coefficient c would be a hidden parameter, but Paper 25
sets c = 1 by the normalized bridge-rate readout and does not tune it to BBN.

Classification: DERIVED/CONDITIONAL on H1-H3 plus upstream L_1; no fitted
coefficient found.

### 12. epsilon_n = (<K>/10) * L_2

Field replacement: denominator 10 -> kappa_m or payload <K> -> kappa_K.

Rigidity test: Paper 25 inherits this from Paper 22/Paper 24. The denominator
10 is tied to TT multiplicity mult_TT(n=2), and L_2 is inherited from Paper 21.
The channel-to-payload assignment remains a TBS/GMP-scoped structure rather
than a Paper 25-only theorem.

Classification: DERIVED/CONDITIONAL upstream, visible.

### 13. Channel-budget equation

Field replacement: epsilon_w/L_1 + K_geom = 10 epsilon_n/L_2 = <K> becomes an
arbitrary balance equation.

Rigidity test: The equality follows from the modular decomposition
<K> = K_geom + K_gauge once the channel-to-payload assignments are admitted.
The assignment is not fitted numerically in Paper 25, but it is conditional on
the bridge/channel package.

Classification: DERIVED/CONDITIONAL on channel-to-payload assignment.

### 14. Linear branch comparator

Field replacement: choose the old sqrt(L_1) branch as active despite Paper 25.

Rigidity test: The linear branch is retained as a historical comparator. It is
not the active theorem branch because it treats a rate as a one-point amplitude.

Classification: SUPERSEDED comparator; not active evidence.

### 15. V' branch catastrophe

Field replacement: use V' sqrt(L_1) as weak payload.

Rigidity test: The branch is not selected by fitting. It is the structurally
identified alternative tangent readout. Its chi2 remains catastrophic under the
corrected YPCMB wrapper, but this is a numerical backstop.

Classification: EXCLUDED comparator; VERIFIED numerically.

## Anti-Fit Backstop

Could the active weak payload have been chosen to match BBN data?

The audit answer is no for the internal Paper 25 choice being tested. The
candidate alternatives are fixed by the theorem grammar:

- K_gauge * sqrt(L_1): the old one-point/amplitude branch.
- K_gauge * L_1: the two-point/rate branch.
- V' * sqrt(L_1): the tangent/one-point branch.

Paper 25 does not scan a continuous coefficient to minimize chi2. The active
branch is selected by the rate-versus-amplitude theorem. The BBN scorecard is a
verification backstop after branch selection.

Residual risk: the selection depends on H1-H3 being the physical weak-sector
premise package. That is visible conditional structure, not fitting.

## Conditional-Visibility Check

Paper 25 v1.2 explicitly declares H1-H3 in Section 1.4 and repeatedly labels
Theorem 25.11/25.12 and the complete closure chain as conditional where
needed. The conditionality is visible enough for a reader to see that Paper 25
does not claim unconditional closure outside the stated bridge-rate package.

For a future v1.3 manuscript update, the Code and Data Availability section
should cite this audit and the public reproducibility bundle so the conditionals
and branch scorecards are reviewable outside the private lab.

## What Future Sessions Must Not Say

- Do not say Paper 25 unconditionally proves the weak-sector identity outside
  H1-H3.
- Do not say the BBN chi2 proves the theorem. The theorem selects the branch;
  PRyMordial verifies the consequence.
- Do not use the private kinetic-runner Li-7 rows as the active Paper 25
  lithium scorecard. The active v1.2 scorecard uses the Paper 24 final-push
  YPCMB path.
- Do not treat the V' numerical catastrophe as the sole reason V' is excluded.
  The structural exclusion is the centered two-time correlator theorem.

## Audit Conclusion

Paper 25 v1.2 survives the formal kappa-style audit with no hidden continuous
fitted parameter found. The correct classification is:

- core bilinearity and no-linear-bridge theorem: DERIVED/THEOREM inside the
  CCR/KMS package;
- V' exclusion: DERIVED/THEOREM under the centered two-time rate formulation;
- V'' exclusion and R(gamma)=1: CONDITIONAL/THEOREM on H1;
- active weak amplitude epsilon_w = K_gauge * L_1:
  DERIVED/CONDITIONAL on H1-H3 plus upstream L_1;
- BBN scorecard: VERIFIED computational support;
- remaining bridge-state/physical-sector choices: visible conditional premises,
  not hidden fitting.
