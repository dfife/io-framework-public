# Paper 17 v1.5 Kappa-Style Structural Audit

## Executive Verdict

No hidden continuous fitted parameter remains in the published v1.5 boundary. R4 is a visible load-bearing readout-normalization field, not derived internally, fixed uniquely by FIRAS, and frozen against downstream retuning.

The hostile-referee version is blunt: Paper 17 v1.4 overclaimed the observed CMB temperature. Paper 17 v1.5 fixes that by retiring the independent CMB-temperature prediction and making R4 explicit. The kappa audit does not find a remaining hidden continuous fitted parameter because the only continuous field, R4, is now visible, uniquely fixed by FIRAS, and forbidden from downstream retuning.

## Method

For each load-bearing scalar or structural choice, replace the item by a free field and ask whether the Paper 17 theorem stack forces the original value. If the stack admits a redefined family without breaking the stated constraints, the field is not internally derived. The audit then checks whether the free field is hidden, fitted, or visibly fixed by an admissible empirical datum.

## Findings

### gamma_BI external Barbero-Immirzi input

- Candidate field: `gamma_BI`
- Verdict: `EXTERNAL_INPUT_NOT_FITTED_IN_PAPER17`
- Evidence: Paper 17 carries gamma_BI=0.2375 from the LQG convention. It is not adjusted in Paper 17 and is not chosen against FIRAS or downstream observables.
- Recommendation: Keep as external framework input; do not present as derived by Paper 17.

### Gauge determinant exponent

- Candidate field: `a = dim(S2)/2`
- Verdict: `DERIVED`
- Evidence: Step 40 v1.5 states this a is internal to the gauge-side Gaussian determinant ratio used to derive K_gauge; it is not R4.
- Recommendation: Retain DERIVED label with explicit a != R4 clarification.

### Gauge payload scalar

- Candidate field: `K_gauge = ln(1+gamma_BI^2)`
- Verdict: `DERIVED/THEOREM_WITHIN_G1_G6`
- Evidence: The shared Hilbert space, A-vacuum GNS construction, SU(2) reduction, fiberwise KMS inheritance, and direct-integral modular reconstruction identify the modular-flow gauge payload as K_gauge.
- Recommendation: Publish as active theorem support; retain reduced-sector and G1-G6 scope.

### Product modular flow exclusion

- Candidate field: `Delta_prod = Delta_ph tensor Delta_g`
- Verdict: `DERIVED_NO_GO`
- Evidence: Product flow leaves photon observables blind to K_gauge; non-product A-vacuum/operator package is required.
- Recommendation: Retain as no-go support.

### A-vacuum and GNS construction

- Candidate field: `omega_A direct-integral state`
- Verdict: `CONSTRUCTED/VERIFIED_WITH_REDUCED_SCOPE`
- Evidence: Paper 17 constructs omega_A fiberwise from faithful normal KMS states. Toy-model numerical support gives max KMS residual 4.58e-16 in the private artifact; public bundle reproduces a finite-dimensional KMS check.
- Recommendation: Retain scope boundary: reduced thermal-plus-gauge sector, not full unreduced horizon algebra.

### Gauge averaging reduction

- Candidate field: `M_th tensor Z_g reduced algebra`
- Verdict: `DERIVED_WITH_REDUCED_SCOPE`
- Evidence: Compact SU(2) averaging and fiber irreducibility force the fixed-point algebra in the reduced tangential sector.
- Recommendation: Retain theorem status with reduced-sector scope.

### Optical readout family

- Candidate field: `T_obs(R4)=T_IO*x^(R4*K_gauge)`
- Verdict: `DERIVED_ALGEBRAIC_FAMILY`
- Evidence: Planck-preserving transfer plus conformal-depth additivity fixes multiplicative exponential form; Theorem 17.1 fixes K_gauge as payload. The scalar R4 remains a separate field.
- Recommendation: Never collapse the family to R4=1 unless Plan A is later proved.

### Optical readout normalization

- Candidate field: `R4`
- Verdict: `VISIBLE_FREE_FIELD_FIXED_BY_FIRAS_UNIQUENESS`
- Evidence: Field-redefinition R4 -> zeta preserves R1-R3 and modular payload structure. v1.5 makes the field explicit and fixes it uniquely by FIRAS via Theorem 17.2.
- Recommendation: No hidden-parameter finding remains, but all downstream T_obs/full-GTTP results must inherit FIRAS-fixed R4.

### FIRAS empirical datum

- Candidate field: `T_FIRAS=2.7255+/-0.0006 K`
- Verdict: `VERIFIED_EMPIRICAL_INPUT`
- Evidence: FIRAS is used as the observer-side thermal datum, not as a target used to validate an independent CMB-temperature prediction.
- Recommendation: Retain manuscript-facing label FIRAS-FIXED UNIQUE READOUT NORMALIZATION.

### R4 uniqueness theorem

- Candidate field: `R4_FIRAS = ln(T_FIRAS/T_IO)/(K_gauge ln x)`
- Verdict: `DERIVED_UNIQUENESS_GIVEN_EMPIRICAL_DATUM`
- Evidence: Because T_IO>0, T_FIRAS>0, x>0 with x!=1, and K_gauge!=0, log T_obs is affine in R4 with nonzero slope.
- Recommendation: Keep as theorem-grade uniqueness result inside the empirical-normalized readout family.

### Historical unit readout

- Candidate field: `R4=1`
- Verdict: `HISTORICAL_RETIRED_NOT_DERIVED`
- Evidence: The kappa field-redefinition audit and explicit c-family show R4=1 is close to FIRAS but not internally forced by the Paper 17 modular-projection stack.
- Recommendation: Do not count T_obs(1)=2.725306 K as a zero-parameter CMB prediction.

### Framework-constructible uniqueness enumeration

- Candidate field: `FIRAS-band algebraic candidate search`
- Verdict: `CONDITIONAL_VERIFIED_FOR_GAUGE_PAYLOAD_NOT_R4`
- Evidence: The enumeration finds 5545 raw in-band hits, but all structurally meaningful framework-native aliases collapse to K_gauge. It does not fix R4.
- Recommendation: Use only as support for K_gauge payload uniqueness; do not use as proof of R4=1.

## Hidden-Parameter Ranking

No hidden continuous fitted parameter is ranked because none remains hidden in v1.5. The prior hidden field was R4. It is now explicit in Section 8.1 and Section 9, fixed by FIRAS through Theorem 17.2, and exposed in the Open Problems ledger.

## Conditional-Visibility Check

- R4 appears explicitly in the premise/readout slot and Open Problems list.
- The manuscript states that downstream T_obs / T_CMB / full-GTTP calculations inherit FIRAS-fixed R4.
- Step 40 distinguishes the gauge determinant exponent `a = dim(S2)/2 = 1` from R4. This avoids a second hidden R4 surface.
- The observed CMB temperature is explicitly not counted as an independent IO prediction.

## Required Guardrails

- Do not say Paper 17 derives R4 = 1.
- Do not say IO independently predicts the observed CMB temperature.
- Correct statement: FIRAS fixes the unique observer-side readout normalization in the IO thermal readout family.
- If FIRAS changes, R4 changes by the published theorem formula and downstream R4-dependent results must be recomputed.

## Open Items

- Plan A derivation of R4=1 from operator algebra alone remains open.
- Extension from reduced thermal-plus-gauge sector to full unreduced horizon algebra remains open.
- GNS standardness/cyclicity/separating/self-adjointness/measurability remain proof-audit items.
