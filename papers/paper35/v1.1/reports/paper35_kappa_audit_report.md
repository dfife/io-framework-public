# Paper 35 Formal Kappa-Style Field-Redefinition Audit

Status: `forensic structural audit / no manuscript edits`

Manuscript audited: `/opt/cosmology-lab/results/Full Papers/Interior_Observer_Paper35_v1_0.docx`

Primary local support reviewed:

- `paper35_eta_io_theorem_chain_report.md`
- `paper35_eta_bbn_temperature_assignment_report.md`
- `paper35_eta_io_gap_closure_report.md`
- `paper35_baryogenesis_from_chiral_boundary_report.md`
- `paper35_external_leptogenesis_target_theorem_report.md`
- `paper35_external_casas_ibarra_source_manifold_theorem_report.md`
- `paper35_transfer_operator_class_theorem_report.md`
- `paper35_cp_asymmetry_boundary_nogo_theorem_report.md`
- `paper35_q5_topological_spectral_nogo_theorem_report.md`
- `paper35_q5_route_exhaustion_theorem_report.md`
- `paper35_spin_c_residual_class_exhaustion_theorem_report.md`
- `paper35_final_residual_irreducibility_theorem_report.md`
- `paper35_desi_dark_energy_investigation_report.md`
- `paper35_three_confrontations_report.md`
- `paper35_conditional_verified_audit_results.md`

## Executive Verdict

No unlabelled continuous fitted parameter was found in Paper 35's load-bearing
calculation chain.

The numerical claims are mostly reproducible from existing scripts and theorem
artifacts. The serious issues are claim-label and scope-hygiene issues:

1. Paper 35 v1.0 overstates the theorem status of the baryogenesis obstruction
   package. The manuscript's phrase "30+ theorem-grade artifacts" is not
   compatible with the current status registry, which audits 48 theorem surfaces
   as 15 `CLEAN` and 33 `CONDITIONAL_VERIFIED`.
2. The dark-matter null section overstates the framework status. The geometric
   dark-matter reading is a scoped/conditional interpretation, not a derived
   no-particle theorem. The forecast of future null results must be labelled a
   conditional forecast, not an unconditional prediction.
3. The JWST section is numerically defensible as timing-pressure relief, but
   "impossible galaxies are expected" is too strong unless explicitly scoped to
   the master-clock timing window and not to full galaxy-formation physics.
4. The eta calculation is structurally clean, but the manuscript should say
   "plus standard particle/thermodynamic constants and a mean-baryon-mass
   convention" instead of implying it uses only `f_b` and the IO temperature.
5. The chiral source-era route is a conditional constructed diagnostic. It
   should not be described as an independent theorem-grade derivation of eta.
6. The final baryogenesis frontier is exact only on the current-stack/admitted
   carrier package. The two future routes are exact frontier objects, not
   existing derived mechanisms.

Recommendation: Paper 35 v1.0 should receive a v1.1 republication/errata-level
scope cleanup before a public reproducibility bundle is used as a credibility
artifact. No numerical recomputation is required by this audit.

## Method

For each load-bearing Paper 35 choice, I applied the standard kappa-audit test:

1. Replace the numerical or structural choice by a free variable.
2. Ask whether an existing theorem, scoped premise, symmetry, standard external
   identity, or published measurement forces the value used in the manuscript.
3. Classify the result as `DERIVED`, `DERIVED/SCOPED`,
   `DERIVED/CONDITIONAL on [premise]`, `CONDITIONAL/CONSTRUCTED`, `FITTED`,
   `scope-creep`, or `no-issue-found`.

The audit does not judge whether the IO framework premises are true. It tests
whether Paper 35 correctly reports what is forced given the active framework
stack and stated assumptions.

## Target 1: `gamma_BI = 0.2375` and the Zero-Fitted-Parameter Claim

Candidate kappa field: replace `gamma_BI` by an adjustable scalar `g`.

Rigidity test: The manuscript treats `gamma_BI = 0.2375` as an imported LQG
constant, not a Paper 35 fitted parameter. On this audit, that is legitimate.
Changing `g` would move the CMB temperature, baryon fraction, BBN dressing,
spectral index, scalar amplitude, slip, Hubble-rung predictions, and the Paper
35 eta calculation simultaneously.

Verdict: `no-issue-found / imported external constant`.

Boundary: This does not make `gamma_BI` derived inside IO. It means Paper 35
does not hide a new Paper 35 fit in `gamma_BI`.

Recommendation: No action beyond retaining the "one external constant" wording.

## Target 2: Late-Time Eta Route `eta_IO,late`

Manuscript claim: `eta_late = 5.75e-10` from `omega_b,geom + T_obs`,
`DERIVED/SCOPED`, 5.7% from Planck.

Candidate kappa fields:

- `omega_b,geom`
- `f_b = 2 gamma / x`
- `T_obs = T_IO x^K_gauge`
- `m_bar`
- the blackbody photon-number prefactor
- the choice not to use `Omega_b = f_b Omega_m,active`

Rigidity test:

- `omega_b,geom` is forced by the active geometric physical-density route in
  the Paper 10/19/29 chain.
- `f_b = 2 gamma / x` is upstream `DERIVED/SCOPED`.
- `T_obs = T_IO x^K_gauge` is upstream `DERIVED/SCOPED`.
- The dead projected-density route is explicitly killed by
  `paper35_eta_io_theorem_chain_report.md`; it gives `eta = 1.36e-9`, so the
  surviving route is not a free choice.
- `m_bar` and the photon-number formula are standard imported physical
  conventions, not IO-derived constants.

Evidence:

- Exact proton-mass value: `eta_IO,late = 5.741795864304530e-10`.
- Composition-corrected value: `eta_IO,late = 5.748778515173695e-10`.
- Manuscript headline: `5.75e-10`.

Verdict: `DERIVED/SCOPED plus imported standard constants`.

Field-redefinition result: no hidden fit. Replacing `omega_b,geom` or `T_obs`
breaks upstream theorem assignments. Replacing `m_bar` changes eta at the
`~0.1%` level and is a standard convention, not a cosmological fit.

Recommendation: v1.1 should explicitly say the eta number also imports standard
particle/thermodynamic constants and the mean-baryon-mass convention.

## Target 3: `T_BBN = T_IO` Temperature Assignment

Manuscript claim: BBN nuclear reactions see `T_IO = 2.6635 K`, not
`T_obs = 2.7253 K`.

Candidate kappa field: replace the BBN temperature by
`T_BBN = T_IO x^(lambda K_gauge)` with free `lambda`.

Rigidity test:

- `lambda = 0` is forced if BBN rates are local bulk microphysics.
- `lambda = 1` would treat BBN nuclear reactions as observer-side optical
  readout objects, which conflicts with the Paper 17/21 GTTP typing and the
  local-reaction nature of standard BBN microphysics.

Evidence:

- `paper35_eta_bbn_temperature_assignment_report.md` closes the temperature
  gate as `DERIVED/SCOPED`.
- The conversion factor is `x^(3 K_gauge) = 1.071240943860573`.

Verdict: `DERIVED/SCOPED`.

Recommendation: No numerical action. Preserve the statement that the Planck eta
comparison is cross-typed, not same-observable.

## Target 4: `eta_BBN = 6.151e-10` and 0.8% Planck Agreement

Candidate kappa fields:

- raw equality between `eta_BBN` and Planck `eta_CMB`
- the conversion map `eta_BBN = eta_obs x^(3 K_gauge)`
- the Planck comparison denominator

Rigidity test: The raw equality is not forced. The typed conversion is forced
once `T_BBN = T_IO` and `T_obs = T_IO x^K_gauge` are accepted. The 0.8% number
is a numerical cross-typed consistency observation, not a same-observable
chi-square.

Verdict: `DERIVED/SCOPED for IO eta_BBN; cross-typed verified comparison`.

Recommendation: No hidden parameter. Keep the cross-typed language prominent.

## Target 5: Eta Anti-Fit Argument

Candidate kappa field: allow `gamma_BI` to vary only for the eta target.

Rigidity test: Not allowed under the framework. `gamma_BI` is a shared external
constant imported before Paper 35. A one-off eta fit would require changing the
same scalar in many already-published predictions.

Verdict: `no-issue-found`.

Recommendation: No action.

## Target 6: Sakharov Structural Ingredients

Manuscript claim: IO provides departure from equilibrium and structural
chirality/CP ingredients, but not a full generated baryogenesis mechanism.

Candidate kappa fields:

- bounce density / departure-from-equilibrium gate
- chiral projection `Pi_chi`
- sign/chirality selector
- baryon-number transfer operator

Rigidity test:

- Departure from equilibrium is `DERIVED/SCOPED` inside the Paper 32 extended
  fermionic/chiral IO-EC theory.
- Structural chirality is present, but the sign/chirality selector is not
  derived.
- Baryon-number transfer is not derived.

Verdict: `DERIVED/SCOPED` for departure from equilibrium;
`CONDITIONAL/CONSTRUCTED` for structural CP ingredient; no full mechanism.

Recommendation: No action if the manuscript keeps the mechanism explicitly
open. Avoid wording that implies Sakharov closure.

## Target 7: Chiral Source-Era Route

Manuscript claim: a conditional source-era route gives
`g_chi = K_gauge^4`, `T_f = K_gauge^4 M_Pl,reduced`, and
`eta_chiral = 7.04 K_gauge^8 = 5.787e-10`.

Candidate kappa fields:

- exponent `4` in `K_gauge^4`
- exponent `8` in `K_gauge^8`
- factor `7.04`
- freeze-out law imported from Poplawski
- freeze-out dynamics
- baryon-separation operator
- chirality/sign selector

Rigidity test: The current stack does not force `K_gauge^4` as the physical
freeze-out selector. Poplawski supplies an external map from a freeze-out scale
to an asymmetry; it does not derive the freeze-out selector from IO. The route
is a coherent constructed diagnostic, not theorem-grade closure.

Verdict: `CONDITIONAL/CONSTRUCTED`.

Field-redefinition result: the route would be a hidden parameter only if the
manuscript presented the exponent/slice as unconditionally forced. It does not
fully do that, but the phrase "independent derivation" is too strong.

Recommendation: v1.1 should call this a "conditional constructed source-era
diagnostic" rather than an independent derivation.

## Target 8: Leptogenesis Target Reduction

Manuscript claim: the closed late-time eta fixes
`epsilon_1 kappa_f = 5.905e-8`, the Davidson-Ibarra floor, and the admissible
source region.

Candidate kappa fields:

- sphaleron conversion factor
- equilibrium `N1` abundance
- Davidson-Ibarra coefficient
- `M1 = T_f` Poplawski slice
- washout efficiency `kappa_f`

Rigidity test: The numerical target is forced inside the stated external
standard hierarchical thermal-leptogenesis reduction class. It is not an
internal IO source theorem. `M1 = T_f` is an admitted slice.

Verdict: `DERIVED/CONDITIONAL on standard external leptogenesis class and
Poplawski target slice`.

Recommendation: v1.1 should surface "external-class conditional" where these
numbers are quoted.

## Target 9: Source-Manifold Uniqueness No-Go

Manuscript claim: type-I seesaw source space remains positive-dimensional after
imposing eta; residual dimension is 3 real.

Candidate kappa fields:

- Casas-Ibarra source class
- fixed `M1`
- fixed `epsilon1`
- washout initial conditions

Rigidity test: The no-go is forced within the external Casas-Ibarra hierarchical
type-I source manifold. It does not claim all conceivable baryogenesis
frameworks are non-unique.

Verdict: `DERIVED/CONDITIONAL on Casas-Ibarra hierarchical type-I class`.

Recommendation: No numerical action; label explicitly as external-class no-go.

## Target 10: Portal Classification and Local Thermal No-Go

Manuscript claim: visible `Delta(B-L)=2` transfer closes to the Weinberg
operator; the compatible renormalizable UV completion is type-I neutrino portal;
the naive local thermal implementation is dead.

Candidate kappa fields:

- visible operator dimension
- mediator representation
- current IO neutral singlet fermionic carrier
- support-crossing slice `M1 = T_f,target`
- local equality `Gamma_D = H_support(R_eta)`

Rigidity test:

- Weinberg-operator uniqueness is standard EFT reasoning.
- Type-I portal uniqueness is forced only after fixing the admitted neutral
  singlet source carrier.
- The local thermal no-go is forced on the support-crossing slice, not as a
  universal no-go for all nonthermal source production.

Verdict: `DERIVED/CONDITIONAL on current carrier and support-crossing slice`.

Recommendation: Add conditional-visibility wording around "unique" and "dead"
in v1.1.

## Target 11: Single-Operator Reduction to `V_tr`

Manuscript claim: the remaining internal debt reduces to a charged transfer
interaction generator `V_tr`.

Candidate kappa fields:

- visible charge `Q_vis`
- free Hamiltonian `H0`
- allowed transfer class
- coefficient/rate data

Rigidity test: If the visible charge commutes with the current free Hamiltonian,
then no visible charge is produced without an interaction generator. The
operator-class reduction is forced on the admitted carrier/portal class. The
coefficient/rate theorem remains open.

Verdict: `DERIVED/CONDITIONAL on admitted carrier and portal class`.

Recommendation: Surface the carrier/portal conditionality.

## Target 12: CP-Odd Pseudoscalar Factorization and `Q5 = 0`

Manuscript claim:

`Y_{B-L}^source = Q5 F(M1, mtilde1, theta(R))`, and current-stack `Q5 = 0`
kills baryogenesis multiplicatively.

Candidate kappa fields:

- factorization into `Q5` times CP-even source function
- `Q5 = N_+ - N_-`
- current horizon carrier
- chirality seed
- spin-c residual class `n`
- APS/inflow contribution

Rigidity test: The multiplicative kill is forced if the scalar-map theorem and
admitted current carrier are accepted. `Q5 = 0` is rigid on the admitted
untwisted closed-sphere carrier: zero index, zero eta-invariant, no chirality
selector, no puncture-resolved twist, and no APS term. It is not a statement
about all possible future extensions.

Verdict: `DERIVED/CONDITIONAL on Paper 32 extended fermionic/chiral carrier and
current-stack no-extra-twist conditions`.

Recommendation: v1.1 should qualify "topologically and spectrally rigid" with
"on the admitted current carrier/current stack."

## Target 13: Topological Obstruction Routes

Manuscript claim: SU(2) puncture route, neutral `Z_k` lift, divisor route,
punctured-connection compactification, equivariant selector, canonical ball
inflow, global bulk inflow, and bare surface selector are killed.

Candidate kappa fields:

- nonzero U(1) determinant line
- puncture-resolved line-bundle degree
- nontracial surface state
- boundary-local inflow hypothesis
- relative/singular inflow extension

Rigidity test: Many route kills are clean current-stack no-gos. Some are
conditional on the Paper 32 carrier, boundary-locality hypothesis, or
relative/singular inflow extension. The route family is not a monolithic
unconditional theorem package.

Verdict: mixed `DERIVED`, `DERIVED/SCOPED`, and
`DERIVED/CONDITIONAL`.

Recommendation: Replace "every route ... theorem grade" with "every route on
the stated current-stack scopes is either killed or reduced to the two surfaced
future objects."

## Target 14: "Single Topological Datum" and Two Future Routes

Manuscript claim: the obstruction traces to spin-c residual class `n`, current
value `n = 0`, and two exact future routes: surface state or relative inflow.

Candidate kappa fields:

- residual spin-c class `n`
- surface-state datum `(omega_sb, q)`
- inflow datum `(A_rel, m_odd)`
- map identifying surface and inflow residuals

Rigidity test: The reduction to the residual pair is forced on the current
stack. The compression to a single inflow object is conditional on a quantized
relative/singular inflow extension. No current-stack map identifies the two
residual categories.

Verdict: `DERIVED/SCOPED current-stack frontier`; partial
`DERIVED/CONDITIONAL` inside relative/singular inflow extension.

Recommendation: State "future route/frontier object," not "derived mechanism."

## Target 15: Theorem-Surface Status Claim

Manuscript claim: "30+ theorem-grade artifacts" support the baryogenesis
obstruction investigation.

Candidate kappa field: replace `theorem-grade` by actual registry status.

Rigidity test: The existing Paper 35 status audit reports:

- total theorem surfaces: `48`
- `CLEAN`: `15`
- `CONDITIONAL_VERIFIED`: `33`
- `NEEDS_REVIEW`: `0`
- `CIRCULAR`: `0`

Verdict: `scope-creep`.

Recommendation: v1.1 should replace "30+ theorem-grade artifacts" with a
registry-accurate phrase such as "48 audited theorem surfaces, 15 clean and 33
conditional-verified." This is the most important republication hygiene fix.

## Target 16: JWST Timing Claim

Manuscript claim: IO gives 46-48% more time at `z > 10`; JWST massive galaxies
are expected under IO.

Candidate kappa fields:

- Paper 28/30 master clock selection
- `t_bare(0) = 19.181 Gyr`
- redshift-age formula
- star-formation onset assumption
- comparison to LCDM

Rigidity test: The timing numbers are reproducible from the master-clock
confrontation. The claim does not derive full galaxy formation, stellar
feedback, dust, seed black holes, or mass assembly histories. The manuscript
does say the objects are not literally impossible from clock time alone, which
is correct.

Verdict: `DERIVED/SCOPED timing relief; verified confrontation; not full galaxy
formation resolution`.

Recommendation: The abstract should avoid "impossible galaxies are expected"
unless immediately scoped to timing relief. Use "IO materially eases the timing
pressure."

## Target 17: DESI Dark-Energy Correction

Manuscript claim: old observer-side `w = -1/3` is retired; active observer-side
vacuum is `w = -1`; active branch gives `chi2 = 69.48`; IO does not predict the
DESI evolving-dark-energy signal.

Candidate kappa fields:

- support variable `R` versus observer scale factor `a`
- old `K_Lambda`
- constant projector/alpha-ladder dressing
- ratio-lock carryover
- flat-CPL reinterpretation
- active branch selection

Rigidity test: The active result is forced by the Paper 10 legacy branch and
Paper 32 support/observer distinction. `rho_Lambda proportional to 1/R^2` is a
hidden-support law, not an observer-side fluid law. A constant projector cannot
generate evolving `w(z)`.

Evidence:

- active branch public DR2 GCcomb crosscheck: `chi2 = 69.484809`.
- retired old observer-side `a^-2` carryover: `chi2 = 3343.470545`.
- flat CPL image of active IO background: `w0 = -1.030263`, `wa = -0.111508`.

Verdict: `DERIVED/SCOPED plus verified data confrontation`.

Recommendation: No structural action. If v1.1 is made, preserve the correction
framing and do not cite the older `paper35_three_confrontations_report.md` DESI
`w=-1/3` result as the active Paper 35 conclusion.

## Target 18: Dark-Matter Null Prediction

Manuscript claim: the IO geometric alternative accounts for the gauge-coupled
matter inventory without a dark-matter particle; future direct-detection
experiments will continue to find nothing.

Candidate kappa fields:

- `f_b = 2 gamma / x`
- missing mass-budget interpretation as boundary geometry
- no-particle theorem
- xenon-coupled WIMP forecast
- next-generation null forecast

Rigidity test: The baryon fraction is upstream `DERIVED/SCOPED`. But Paper 33
already records that the geometric dark-sector interpretation is not a derived
no-particle theorem. A primitive typed dark-sector carrier remains
conditionally open. Therefore "there is no particle to find" is not forced by
the current theorem stack.

Verdict: `scope-creep / label downgrade required`.

Recommendation: v1.1 should downgrade this section to
`CONDITIONAL FORECAST / geometric-DM sector`. Suggested wording:
"If the IO geometric dark-sector interpretation is correct, xenon WIMP searches
should remain null; a clean WIMP detection would falsify that sector." Do not
state an unconditional no-particle theorem.

## Target 19: "Four Problems Resolved or Constrained"

Manuscript claim: four problems are addressed by the same boundary-to-bulk
projection; where LCDM fits a parameter, IO derives a number.

Candidate kappa fields:

- "resolved" versus "constrained"
- "same boundary-to-bulk projection" across four heterogeneous problems
- scope of baryogenesis no-go
- scope of dark matter forecast

Rigidity test: Eta and DESI are strong. JWST is timing relief, not full
formation physics. Baryogenesis mechanism is not derived; it is obstructed and
reduced to future objects. Dark matter is a conditional forecast. The umbrella
claim is acceptable only if "resolved or constrained" is interpreted
heterogeneously and scoped.

Verdict: `scope correction recommended`.

Recommendation: Use "addressed, constrained, or reduced" rather than implying
all four are solved at the same level.

## Target 20: Overall Hidden-Parameter Audit

Candidate kappa fields:

- all scalar numerical constants used in Paper 35
- external observational anchors
- external standard-theory maps
- admitted support/portal/inflow slices

Rigidity test: I found external constants, standard-theory maps, admitted
slices, and conditional extensions. I did not find a continuous fitted scalar
introduced silently to match Paper 35 outputs. The target-guided external
baryogenesis reductions are inverse constraints, not fitted framework
parameters, provided they remain labelled as external reductions.

Verdict: `no hidden continuous fitted parameter found`.

Recommendation: The paper can keep "zero fitted cosmological parameters" if it
also surfaces the conditional/constructed/external status of the relevant
baryogenesis and dark-sector claims.

## Action Summary

Recommended v1.1 changes:

1. Replace "30+ theorem-grade artifacts" with registry-accurate status:
   "48 audited theorem surfaces: 15 clean and 33 conditional-verified."
2. In the eta derivation, state that the calculation imports standard
   particle/thermodynamic constants and a mean-baryon-mass convention.
3. Label the chiral source-era eta route as `CONDITIONAL/CONSTRUCTED`, not an
   independent theorem-grade derivation.
4. Label the leptogenesis target reductions as conditional on the standard
   external hierarchical thermal-leptogenesis class and admitted Poplawski
   target slice.
5. Qualify `Q5 = 0` and the topological obstruction as current-stack/admitted
   carrier statements.
6. Reword JWST claims as timing-pressure relief, not full galaxy-formation
   resolution.
7. Preserve the DESI correction as an active-branch result; do not reuse the
   older `w=-1/3` confrontation as the live conclusion.
8. Downgrade the dark-matter null section to a conditional forecast of the IO
   geometric-DM sector.
9. Replace broad "resolved" language with "resolved, constrained, or reduced"
   where the four problems are grouped together.

Republication recommendation: yes, v1.1 is recommended for label/scope hygiene.
This is not a numerical invalidation and not evidence of a hidden fitted
parameter.
