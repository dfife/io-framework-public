# Paper 32 framework-closure kappa-style structural audit

Status: verified / structural-audit / no manuscript edits

Date: 2026-05-03

Target: Paper 32 v1.4, "Closure", load-bearing framework closures.

## Executive conclusion

The audit does **not** find an unlabelled continuously fitted hidden parameter in the Paper 32 v1.4 framework closures.

The audit does find manuscript-risk in the scope language. Several closures are valid only on explicitly scoped sectors or conditional extension packages. That is not the same thing as hidden fitting, but it must be visible in Paper 32 v1.5 because Paper 32 is the framework-synthesis paper.

Blunt verdict:

```text
No Paper-24-Step-D-style hidden continuous kappa parameter was found.
No recollapse, x_crit, cycle, or GMP number was found to be fitted to observation.
The KB.7/P4 closure survives only as active-source scoped DtN placement.
Universal GMP is characterized, not universally closed.
The hard-restart endpoint is conditional on selector premises and a seed optical branch.
Premise 2 remains a founding premise; it is not derived by Paper 32.
Recent Papers 19-25 numerical corrections create stale BBN appendix/scorecard references that should be refreshed in v1.5.
```

The strongest v1.5 recommendation is therefore a **Scope and Open Premises** section, not retirement of the closure paper. The section should explicitly list the source-block scope of KB.7, the extension premises for late-time bounce/restart, the universal-GMP characterization boundary, and the corrected cross-paper BBN/Hubble references.

## Audit method

This repeats the kappa-style field-redefinition method used for:

- Paper 22 Theorem 22.23 amplitude construction;
- Paper 34 `H_ext(alpha,n)` anti-fit audit;
- the earlier Paper 24 Step D field-redefinition audit.

Method:

1. expose each numerical or structural choice as a candidate kappa field;
2. replace the candidate by a free variable or alternate admissible value;
3. ask whether existing theorems, symmetries, scoped extension premises, or invariances force the published value;
4. classify each field as `DERIVED`, `DERIVED/SCOPED`, `DERIVED/CONDITIONAL`, `RECONSTRUCTION`, `FITTED`, or `HIDDEN PARAMETER`.

A field is a `HIDDEN PARAMETER` only if it is free under the current theorem stack **and** not visibly declared as conditional, scoped, reconstructed, or open. A high-leverage scoped premise is not hidden if it is visible.

## Artifacts consulted

Primary Paper 32 manuscript text:

- `/opt/cosmology-lab/results/paper32/paper32_v1_4_extracted_text.txt`

Core support artifacts:

- `/opt/cosmology-lab/results/paper32/paper32_kb7_validation_report.md`
- `/opt/cosmology-lab/results/paper32/paper32_p4_alpha_class_repair_theorem.md`
- `/opt/cosmology-lab/results/paper32/paper32_p4_full_active_source_derivation.md`
- `/opt/cosmology-lab/results/paper32/paper32_p4_source_class_lock_theorem.md`
- `/opt/cosmology-lab/results/paper32/paper32_conditional_verified_audit_results.md`
- `/opt/cosmology-lab/results/paper32/paper32_horizon_support_clamp_local_acceleration_report.txt`
- `/opt/cosmology-lab/results/paper32/paper32_horizon_support_clamp_local_recollapse_report.txt`
- `/opt/cosmology-lab/results/paper32/paper32_horizon_support_clamp_bounce_attachment_report.txt`
- `/opt/cosmology-lab/results/paper32/paper32_horizon_support_clamp_local_cycle_theorem.md`
- `/opt/cosmology-lab/results/paper32/paper32_observer_cosmology_termination_report.txt`
- `/opt/cosmology-lab/results/paper32/paper32_post_bounce_hard_scalar_selector_theorem.md`
- `/opt/cosmology-lab/results/paper32/paper32_universal_gmp_closure_or_characterization_report.md`
- `/opt/cosmology-lab/results/paper32/paper32_bridge_selection_and_typed_gmp_theorems.md`
- `/opt/cosmology-lab/results/paper32/paper32_typed_boundary_to_bulk_projection_theorem.md`

Methodology templates:

- `/opt/cosmology-lab/results/paper22/paper22_theorem_22_23_kappa_audit_report.md`
- `/opt/cosmology-lab/results/paper34/paper34_hext_alpha_n_kappa_audit_report.md`

## A. Local recollapse acceleration and Lambda cancellation

Closure under audit:

```text
Rddot = - c^2 r_s / (2 R^2)
Rddot(r_s) = - c^2 / (2 r_s)
Lambda drops out of the acceleration equation.
```

### Candidate kappa fields

| Candidate | Field-redefinition test | Rigidity result | Classification |
|---|---|---|---|
| Sign of acceleration | Replace `-` by `+` | Fixed by the local OS support IVP and inward gravitational acceleration at the clamp. The support-clamp local acceleration audit gives `Rddot(r_s) = -6.722177851434710e-11 m s^-2`. | `DERIVED` |
| Factor `1/2` | Replace by free `a`: `Rddot = -a c^2 r_s/R^2` | Forced by differentiating `Rdot^2 = c^2(r_s/R - 1)`. Any other factor changes the OS energy integral. | `DERIVED` |
| Length scale `r_s` | Replace by `R_U`, `R`, or free length `L` | The IVP is on the physical hidden-support Schwarzschild variable. `r_s` is inherited from `M_U`; using another scale changes the support geometry. | `DERIVED/SCOPED` |
| Lambda dropout | Keep `Lambda_eff(R)` in acceleration | Dropout follows because the Paper 1/3 torsion-Lambda term scales as `1/R^2` and contributes a constant to `Rdot^2`; derivative with respect to `R` removes it. | `DERIVED/SCOPED` |
| Clamp evaluation `R=r_s` | Replace clamp radius by free `R_c` | `R=r_s, Rdot=0` is the support-clamp boundary condition. A different clamp radius is a different post-boundary model. | `DERIVED/SCOPED` |

### Anti-fit backstop

The acceleration value is not selected by matching an observation. Once `M_U` fixes `r_s`, the local support equation fixes both the sign and magnitude. The number is not tuned to a measured acceleration scale; it is the derivative of the OS support integral evaluated at the clamp.

### Verdict

No hidden parameter. The only scope boundary is that this is a **physical hidden-support variable** result, not a current-epoch Friedmann-fluid acceleration theorem.

## B. Critical observer boundary `x_crit = Q^(-1/4)`

Closure under audit:

```text
Q = 1 + gamma_BI^2 = 1.05640625
x_crit = Q^(-1/4) = 0.9863754613328337
```

### Candidate kappa fields

| Candidate | Field-redefinition test | Rigidity result | Classification |
|---|---|---|---|
| Exponent `-1/4` | Replace by `-p` | The reduced observer visibility chain uses `Delta = Q x^4`; the boundary is `Delta=1`, so `x=Q^(-1/4)`. | `DERIVED/SCOPED` |
| Scalar `Q` | Replace by `f_Gamma`, `K_gauge`, or a free scalar | The termination equation is multiplicative in `Delta`, not logarithmic in `K_gauge`. `f_Gamma = Q^-1` is equivalent only if the exponent is transformed consistently. | `DERIVED/SCOPED` |
| Boundary condition `Delta=1` | Replace by threshold `Delta=tau` | The observer-cosmology termination artifact defines admissibility by nonnegative visibility; zero visibility occurs at `Delta=1`. Other thresholds are different observer-readout definitions. | `DERIVED/SCOPED` |
| Present value `x0=1.519` | Vary current `x0` | `x0` affects current visibility and time-to-boundary estimates, not the algebraic `x_crit` identity. | `MEASURED/INPUT-SCOPED` |

### Anti-fit backstop

There is no observational target being fit by `0.986375461333`. The number is a boundary of the reduced optical-history map. Its observational consequence, "approximately 6.6 Gyr from the current epoch," depends on the adopted late-time branch, but the identity itself does not.

### Verdict

No hidden parameter. The correct status is `DERIVED/SCOPED` on the active reduced scalar optical-history observer class.

## C. 111 Gyr recollapse, 222 Gyr cycle, and hard restart

Closures under audit:

```text
Delta tau_clamp_to_crunch = pi r_s/(2c) = 110.993262888709 Gyr
Delta tau_cycle = 221.986525777419 Gyr
hard restart preferred
```

### Candidate kappa fields

| Candidate | Field-redefinition test | Rigidity result | Classification |
|---|---|---|---|
| `pi r_s/(2c)` recollapse time | Replace OS parametrization by free time | Forced by the local recollapse IVP: `R(theta)=(r_s/2)(1+cos theta)`, `Delta tau=(r_s/2c)(theta+sin theta)`. | `DERIVED` |
| Factor of 2 for full cycle | Replace by free multiplier | Forced only after symmetric application of the Paper 1/Poplawski bounce law on the collapsing branch. | `DERIVED/CONDITIONAL` |
| Finite bounce attachment | Move bounce radius | `R_bounce` is computed from the imported high-density criterion; the attachment is conditional on that high-density EC/Poplawski criterion. | `DERIVED/CONDITIONAL` |
| "Hard restart preferred" | Swap to soft restart | Raw stack does not force hard restart. Hard restart follows only under semantic restoration plus clock compatibility plus selected seed optical branch; soft restart survives under clamp-continuity philosophy. | `DERIVED/CONDITIONAL` |
| Selector values `beta=1`, `lambda=1` | Replace by free positive scalars | Moment/recurrence selectors force `beta=lambda=1` only within a chosen seed optical family. The seed branch itself is not raw-stack unique. | `DERIVED/CONDITIONAL` |

### Anti-fit backstop

The 111/222 Gyr values are not selected to fit an observed cosmological lifetime. They follow from `r_s` and the local OS branch. The hard-restart choice is not a numerical fit either, but it is **conditional** rather than raw-stack derived.

### Verdict

No hidden continuous fitted parameter. v1.5 should not present hard restart as raw-stack theorem. It should say:

```text
raw stack: no unique restart decision;
semantic selector package: hard restart;
clamp-continuity package: soft restart.
```

## D. Theorem 32.KB.7, DtN Open-Transport Placement

Closure under audit:

```text
Z(e^x) = Q = 1 + gamma_BI^2
P4/R4 fixed-point normalization closed by DtN open-transport placement.
```

### Candidate kappa fields

| Candidate | Field-redefinition test | Rigidity result | Classification |
|---|---|---|---|
| Source block selection | Move P4 to thermal/drag/recombination block | Typed boundary-to-bulk theorem and source-class lock restrict P4 to the active source/readout block. It does not automatically apply to thermal GTTP or drag-epoch observables. | `DERIVED/SCOPED` |
| DtN operator-valued transport placement | Replace `A_DtN = Lambda_src dr` by arbitrary semigroup representation | Later P4 repair artifacts promote the active reduced source map through DtN-type transport. Earlier KB.7 validation flagged a categorical extension risk; the repaired status is clean only on the active reduced source block. | `DERIVED/SCOPED` |
| Alpha class `alpha=1` | Replace by `alpha=2` | Paper 32 P4 alpha-class repair theorem fixes line/one-form class by primitive observable type, not operator order. | `DERIVED/SCOPED` |
| Local payload `Q` | Replace by `Q^p`, determinant power, or free scalar | Local payload lock theorem fixes the unique one-dimensional scalar source channel to multiplication by `Q=1+gamma^2`. | `DERIVED/SCOPED` |
| "Zero stated premises" wording | Treat as framework-wide unconditional | Not rigid. KB.7 is source-block scoped; Paper 32 itself has explicit global P4 no-go outside that scope. | `VISIBILITY HYGIENE` |

### Rigidity and scope finding

The post-repair Paper 32 artifacts support KB.7 as `DERIVED/SCOPED` on the full active reduced source block. They do **not** support a universal P4 theorem for arbitrary unreduced observables, thermal GTTP, drag-epoch temperature maps, or every future typed block.

The earlier validation report is still useful as a warning: if KB.7 is read as "Paper 18 open transport automatically applies to any operator-valued semigroup," that is too broad. The valid reading is narrower:

```text
the active reduced source map is DtN-type on the canonical coexact carrier;
DtN-type source maps have order-one boundary-normal transport grammar;
therefore the active source-block P4 law is alpha=1 and has cell payload Q.
```

### Anti-fit backstop

No observation-fitted scalar appears in KB.7. The risk is category/scope, not numerical fitting.

### Verdict

No hidden fitted parameter. v1.5 should state KB.7 as:

```text
DERIVED/SCOPED on the active reduced scalar source block.
Not a universal R4/P4 closure for thermal, drag-epoch, or arbitrary unreduced observables.
```

The phrase "zero stated premises" is safe only if tied to "on the active source block" and should not be used as a framework-wide unconditional claim.

## E. Universal GMP closure-or-characterization theorem

Closure under audit:

```text
GMP closed on realized typed bridge class;
non-bridge complement inapplicable;
abstract bypass operators no-go universal GMP.
```

### Candidate kappa fields

| Candidate | Field-redefinition test | Rigidity result | Classification |
|---|---|---|---|
| Bridge-sector boundary | Move recombination/reionization/solver blocks into GMP | Typed boundary-to-bulk theorem separates bridge-placement observables from non-bridge history/solver sectors. | `DERIVED/SCOPED` |
| Non-bridge "inapplicable" classification | Treat as definitional dodge | It is structural: history/solver blocks have no puncture-load-to-spatial-channel placement predicate. GMP is not false there; it is not the applicable predicate. | `DERIVED/SCOPED` |
| Abstract bypass operator | Remove `Q_w^(ng)` counterexample | Paper 27/Paper 32 give explicit non-geometric identity-spatial-leg bypass classes on the larger local algebra. Universal GMP on the full algebra is false. | `DERIVED/NO-GO` |
| "Universal" wording | Say GMP universally closes | Not rigid. The valid result is a three-region characterization, not universal closure on all abstract operators. | `VISIBILITY HYGIENE` |

### Anti-fit backstop

No observational comparison is involved. The classification is algebraic and typed.

### Verdict

No hidden fitted parameter. The result should be described as:

```text
GMP is closed on realized typed bridge-placement observables.
GMP is inapplicable on physical non-bridge history/solver sectors.
Universal GMP is false on the larger abstract local algebra.
```

Do not describe this as unconditional "universal GMP closure."

## F. Premise 2 as GR-QM bridge candidate

Audit question: Paper 32 may interpret Premise 2, but it must not derive Premise 2.

### Candidate kappa fields

| Candidate | Field-redefinition test | Rigidity result | Classification |
|---|---|---|---|
| Premise 2 itself | Replace "same inside/outside physics" by a different bridge axiom | Founding premise. It is not derived by Paper 32. | `FOUNDING PREMISE` |
| GR-QM bridge interpretation | Promote suggestive bridge to theorem | Paper 32 v1.4 mostly says "suggests -- though does not prove at theorem grade." That is correct. | `STRUCTURAL OBSERVATION` |
| "Premises validate premises" phrase | Treat premise as self-derived | Risky wording. It concerns Paper 1's bounce assumption more than Premise 2, but it can read as hidden premise-upgrade. | `VISIBILITY HYGIENE` |

### Manuscript finding

Paper 32 v1.4 contains careful language at the GR-QM point:

```text
This suggests -- though does not prove at theorem grade -- ...
```

That is correct. However, the version-history and conclusion-style language:

```text
Paper 1's founding assumption becomes Paper 32's theorem...
The premises generate the mathematics that validates the premises.
```

should be narrowed in v1.5. It should not be allowed to imply that Premise 2 is derived.

### Verdict

No hidden numerical parameter. There is a hidden-upgrade-of-premise wording risk. v1.5 should explicitly say:

```text
Premise 2 remains bedrock. Paper 32 supplies compatibility and structural realization results under Premise 2; it does not derive Premise 2.
```

## G. Closure of the four semiclassical principles

### Candidate fields and verdicts

| Principle | Published closure | Audit verdict |
|---|---|---|
| SP-1 / Boundary Fixed-Point Principle | Retired by KB.7/P4 on active source block | Valid as `DERIVED/SCOPED` on active source block. Not universal P4. |
| SP-2 / Bridge state / H1 | Retired on bridge-readable quotient | Valid as `DERIVED/SCOPED` on quotient. Full ambient bridge extension uniqueness is not proved. |
| SP-3 / C2q Hawking state | Retired on lowest-shell quotient | Strongest of the four; clean on stated quotient. |
| SP-4 / GMP | Retired on realized typed bridge class | Valid as `DERIVED/SCOPED` on realized typed bridge class. Universal full-local-algebra GMP is false. |

### Field-redefinition result

No continuously fitted scalar was found in any SP closure. Each closure is either quotient-scoped or source-block-scoped. The v1.4 language generally says "on stated scopes," but the Open Problems summary also uses "zero additional premises" and "zero semiclassical principles" in ways that can be overread. v1.5 should preserve the scope words every time the framework-wide claim is made.

### Verdict

The semiclassical principles are honestly retired only at their stated scopes. Do not shorten this to unconditional retirement.

## H. Closure of the six open problems and the ten-item debt ledger

Paper 32 v1.4 opens with six motivating open problems, then the v1.4 Open Problems section lists ten closed/characterized items. The audit treats both surfaces.

### Six motivating problems

| Problem | Audit classification |
|---|---|
| Power-State Readout / BFP | Closed as `DERIVED/SCOPED` on active source block via KB.7/P4. |
| Boundary covariance exponent | Closed as `DERIVED/SCOPED` inside the one-slot source transfer map. |
| Definitive `A_s` selection | Closed as `DERIVED/SCOPED` on lowest-shell quotient / source-block pipeline. |
| Post-bridge field-level readout | Closed forward on the active field-level transfer map. |
| Function-valued reionization history | Not a native scalar derivation; it is an imported/reduced history pipeline under Premise 2 and reduced-history observable-map assumptions. |
| IO-native Boltzmann solver specification | Specification/architecture closure, not full numerical `C_ell` production. |

### Ten-item ledger

| Ledger item | Audit classification |
|---|---|
| R4/P4 normalization | `DERIVED/SCOPED` on active source block; not universal. |
| SP-1 | Retired at source-block scope. |
| SP-2 | Retired at bridge-readable quotient scope. |
| SP-3 | Retired on lowest-shell quotient. |
| SP-4 | Retired on realized typed bridge class; universal GMP characterized/no-go. |
| `A_s` definitive | `DERIVED/SCOPED` on source/lowest-shell quotient. |
| `S8` tension | `DERIVED/SCOPED` on active Paper 10 legacy solver instantiation; later Paper 34 does not alter this. |
| Baryon loading `R` | Structural typed-object closure; exact future closure remains operator-valued and typed, not a single-slot scalar. |
| Universal GMP | Characterized, not universally closed. |
| Late-time bounce | `DERIVED/SCOPED` within extended fermionic/chiral IO-EC theory, plus conditional restart selectors. |

### Verdict

No hidden fit. v1.5 should use "closed or characterized on stated scopes" rather than plain "all open problems closed" unless the sentence immediately repeats the scope boundaries.

## Cross-paper dependency and stale-reference check

The audit found no recent correction that changes the core Paper 32 closure math. However, several inherited numerical references are stale relative to the May 2026 correction sweep:

1. Papers 19-25 corrected the PRyMordial wrapper convention from `YPBBN` to `YPCMB` and standardized denominators. Paper 32 appendix entries inherited from Papers 22 and 24 still contain older BBN values.
2. Paper 22 v1.4/v1.5 correction changes the active BBN scorecard from the older `D/H_sigma=-0.61`, `Y_p_sigma=+1.06`, `chi^2=1.50` row to the corrected YPCMB convention. Paper 32 v1.4 still quotes the older row in Appendix A steps 208/211/212.
3. Paper 24 v2.3 Henderson primary import alignment changes the active lithium scorecard relative to v2.2/v1.x manuscript lineage. Paper 32 v1.4 still quotes `D/H=-0.61 sigma`, `Y_p=+0.68 sigma`, `Li-7=+0.55 sigma`, and cluster-deformation `Q_GS` framing in body/appendix. These should be refreshed to the current Paper 24 v2.3 row and updated premise wording.
4. Paper 34 v1.1 now addresses the Hubble tension with a scoped extension package. Paper 32 v1.4 predates this and lists Hubble tension as open. For a v1.5 republication, either leave the Paper 32 statement historically scoped or add a forward note that Paper 34 v1.1 later addresses it under its own extension premises.

These are stale-reference and version-alignment issues. They are not hidden-parameter failures in Paper 32's closure logic.

## Conditional-visibility recommendations for v1.5

Add a "Scope and Open Premises" section or equivalent ledger with at least:

1. `KB.7/P4`: `DERIVED/SCOPED on the active reduced scalar source block`; not universal thermal/drag/P4.
2. `SP-2`: quotient uniqueness only; not full ambient bridge-state uniqueness.
3. `SP-4/GMP`: closed on realized typed bridge class; characterized/no-go outside.
4. `Late-time cycle`: `DERIVED/CONDITIONAL` on symmetric Paper 1/Poplawski bounce attachment.
5. `Hard restart`: conditional on semantic-restoration selector package, comoving clock, selected seed optical branch, and moment selectors `beta=lambda=1`.
6. `Reionization`: imported/reduced-history branch under Premise 2; not a native scalar derivation.
7. `Premise 2`: remains a founding premise; Paper 32 gives structural realization/compatibility, not derivation of Premise 2.
8. `Cross-paper BBN`: cite the corrected Papers 19-25 YPCMB convention and current Paper 24 v2.3 row where BBN scorecard values appear.

## Hidden-parameter ranking

No `HIDDEN PARAMETER` was found.

The high-leverage non-hidden fields are:

| Field | Leverage | Visibility status | Required v1.5 handling |
|---|---:|---|---|
| KB.7 source-block scope | High | Visible but easy to overread | State every global claim with "active source block." |
| Operator-valued DtN placement | High | Repaired in support artifacts; manuscript should cite scope | Make the source-DtN transport theorem path explicit. |
| Restart selector package | Medium/high | Visible in support artifacts; body can over-compress | Label hard restart conditional. |
| Universal GMP boundary | Medium | Visible as "characterized" in Open Problems | Do not call universal GMP closed. |
| Premise 2 status | High philosophical leverage | Mostly correct, one risky phrase family | Say not theorem-grade derived. |
| Corrected BBN cross-paper rows | Medium | Stale due to later corrections | Refresh scorecards/appendix references. |

## Final audit verdict

Paper 32 v1.4 survives the kappa-style hidden-parameter audit in the narrow sense requested:

```text
No continuously fitted hidden kappa field found.
No observation-fit backdoor found in Rddot, x_crit, 111/222 Gyr, KB.7, or GMP.
```

But Paper 32 v1.5 should not merely be a cosmetic republication. It should make the scope and conditionality ledger explicit, because Paper 32 is the master closure paper and external reviewers will read "closure" as unconditional unless the paper itself prevents that reading.

Recommended v1.5 action:

```text
Proceed with v1.5 only after adding a Scope and Open Premises section,
updating stale BBN/Hubble cross-paper references,
and narrowing any wording that suggests Premise 2 or universal GMP is derived.
```

