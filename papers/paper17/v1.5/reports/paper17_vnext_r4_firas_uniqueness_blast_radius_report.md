# Paper 17 vNext R4 / FIRAS uniqueness blast-radius report

Date: May 2026

## Executive verdict

The update is structurally necessary and non-local.

The old active claim

```text
IO independently predicts the observed CMB temperature:
T_obs = T_IO x^K_gauge = 2.7253 K, 0.3 sigma from FIRAS.
```

must be retired. The existing Paper 17 modular-projection stack identifies the optical readout carrier and explains why the gauge payload is the relevant one-slot thermal readout, but it does not force the unit optical readout normalization. A continuous `R4` family remains:

```text
T_obs(R4) = T_IO x^(R4 K_gauge).
```

The replacement claim is:

```text
FIRAS supplies the empirical observer-side thermal datum. Given the IO readout
family, FIRAS fixes a unique R4:

R4_FIRAS = ln(T_FIRAS/T_IO) / (K_gauge ln x).
```

This is theorem-grade as a uniqueness theorem inside an empirical-normalized readout family. It is not an independent CMB-temperature prediction. R4 remains load-bearing for every downstream result using observer-side thermal readout.

## Immediate Paper 17 vNext action

Paper 17 should become the canonical correction point. It should not present `R4 = 1` as derived. It should present:

* `T_IO` as the base interior Hawking thermal scale.
* `K_gauge` as the derived gauge payload.
* the readout family `T_obs(R4) = T_IO x^(R4 K_gauge)`.
* FIRAS as the empirical observer-side thermal datum.
* the uniqueness theorem fixing `R4_FIRAS`.
* the frozen-use rule forbidding retuning against downstream observables.

The vNext version history should explicitly say that the prior independent CMB-temperature prediction has been retired and replaced by a FIRAS-fixed unique readout normalization theorem.

## Proposed theorem text

Use the theorem text in:

```text
results/paper17/paper17_vnext_r4_firas_uniqueness_theorem_text.md
```

Short insert form:

```text
Theorem 17.X (Uniqueness of the Empirical Readout Normalization).
Let T_IO > 0, T_FIRAS > 0, x > 0 with x != 1, and K_gauge != 0. For
R4 in R define T_obs(R4) = T_IO x^(R4 K_gauge). Then there exists a
unique R4 such that T_obs(R4) = T_FIRAS, namely

    R4_FIRAS = ln(T_FIRAS/T_IO) / (K_gauge ln x).

The proof is immediate after taking logarithms: ln T_obs is affine in
R4 with nonzero slope K_gauge ln x, hence injective. Therefore FIRAS
fixes a unique observer-side thermal readout normalization inside the
IO readout family. This is not an independent prediction of T_FIRAS.
```

## Numerical reference

Using the active Paper 17 constants:

```text
T_IO = 2.6635 K
T_FIRAS = 2.7255 K
sigma_FIRAS = 0.0006 K
x = 1.519
gamma_BI = 0.2375
K_gauge = ln(1 + gamma_BI^2) = 0.05487281774291466
```

the theorem gives:

```text
R4_FIRAS = 1.0031014644105183
sigma(R4)_FIRAS-only = 0.009596597151571828
T_obs(R4=1) = 2.725306096638128 K
```

The historical unit choice `R4 = 1` is close to the FIRAS-fixed value, but closeness is not derivation.

## Directly affected claim surfaces

### Paper 17 v1.4

Priority: P0. Must be updated first.

Representative affected locations from the text extraction:

* Line 11: abstract/summary claims `T_obs = T_IO x^K_gauge = 2.7253 K` and states Paper 17 promotes GTTP to theorem-grade.
* Line 20: "Framework-Constructible Uniqueness Result" treats FIRAS-band enumeration as selecting `K_gauge`.
* Line 22: classifies the old result as `DERIVED/THEOREM`.
* Line 25: calls the 0.3 sigma FIRAS agreement "the tightest agreement of any IO prediction".
* Lines 112-113: theorem proof ends with `T_obs = T_IO x^K_gauge` and numerical FIRAS verification.
* Lines 116-127: framework-constructible uniqueness is presented as a CMB-temperature closure route.
* Lines 139-140: self-consistency sweep says FIRAS alone determines the allowed band, but this is treated as support for the old selection.
* Lines 162, 184-185: results and conclusion repeat the old theorem-grade CMB prediction.
* Appendix lines 434-443 and 493-530: inherited step table labels the old GTTP and FIRAS inversion claims as `DERIVED`.

Required Paper 17 changes:

* Retire "IO independently predicts observed CMB temperature."
* Replace "GTTP theorem proves `T_obs = T_IO x^K_gauge`" with "Paper 17 constructs the optical readout family and FIRAS fixes the unique readout normalization."
* Reclassify the old framework-constructible FIRAS-band enumeration as a historical reconstruction / near-hit, not proof.
* Remove or reframe "gamma_BI from FIRAS inversion" as a consistency diagnostic, not a derived prediction.
* Add an inheritance ledger for every downstream use of `T_obs` or `x^(R4 K_gauge)`.

### Paper 13 v1.7

Priority: P1 after Paper 17 vNext. Paper 13 is the historical source of GTTP and contains the most explicit overclaim language.

Representative locations:

* Title line: "Closing the 230 sigma T_CMB Gap with Zero New Parameters."
* Lines 11-13: claims the CMB gap is reduced to 0.3 sigma and inverting the correction predicts `gamma_BI`.
* Lines 35-38: bounded search over framework constants against `T_CMB/T_IO`.
* Lines 66-77: source selector and transfer theorem use FIRAS as the sole survivor.
* Lines 111-119: FIRAS inversion presented as a falsifiable structural prediction for `gamma_BI`.
* Lines 142-147: conclusion says GTTP independently predicts `gamma_BI` from FIRAS and closes the CMB gap.
* Appendix lines 1104-1220: repeats Paper 13/32 promotion of GTTP to theorem and FIRAS inversion as derived.

Recommended handling:

* Do not rewrite Paper 13 first. Let Paper 17 vNext become the correction authority.
* If Paper 13 is republished later, mark it as a historical pre-R4-normalization paper whose FIRAS-band reconstruction motivated the readout family but did not prove `R4 = 1`.

### Papers 20, 21, 22, 25, 26 and inherited appendix stacks

Priority: P1/P2 depending on republication order. These papers repeatedly inherit Paper 13/17 GTTP steps.

Representative scanned examples:

* Paper 20 v1.7 line 67: `T_CMB: x^K_gauge ... T_obs = 2.7253 K vs FIRAS`.
* Paper 20 v1.7 line 121: already lists "R4 normalization (Paper 17): load-bearing for GTTP. [Pending verification]".
* Paper 20 v1.7 lines 373-382, 431, 450, 520-523: appendix labels old GTTP and Bogoliubov readout as derived while also retaining the R4 premise.
* Paper 22 v1.5 line 399: same R4 open problem.
* Paper 22 v1.5 lines 650-659, 711, 744: inherited GTTP and gamma-inversion steps need FIRAS-fixed status.
* Paper 25 v1.2 line 215: same R4 open problem.
* Paper 25 v1.2 lines 469-478, 530, 563: inherited GTTP, temperature transfer, gamma inversion, and Bogoliubov readout need update.

Recommended handling:

* Replace "R4 normalization pending" with "R4 fixed uniquely by FIRAS in Paper 17 vNext; downstream `T_obs` results inherit the FIRAS-fixed readout normalization."
* Replace old `DERIVED/THEOREM` labels on `T_obs = T_IO x^K_gauge` with `FIRAS-FIXED UNIQUE READOUT NORMALIZATION` or `DERIVED uniqueness theorem + VERIFIED FIRAS empirical input`, depending on context.
* Retain BBN branch-assignment results that say local nuclear microphysics uses `T_IO`, not `T_obs`; those are not weakened by the R4 update.

### Paper 32 v1.5

Priority: P1 because Paper 32 is the closure paper and public synthesis source.

Representative locations:

* Line 27: says GTTP is elevated to `DERIVED/THEOREM`.
* Line 306: says the same derivation already produced zero-free-parameter predictions for `T_CMB`.
* Line 351: constants block lists `T_obs = T_IO x^K_gauge = 2.7253 K (Paper 13/17)`.
* Line 430: framework-zero-fitted-parameters summary is not directly false, but must no longer count observed CMB temperature as an independent prediction.
* Line 443: Paper 32 bundle description says it reproduces `T_IO, T_obs`; this remains valid only with the FIRAS-fixed R4 dependency noted.
* Appendix lines 704-718, 766, 792: inherited GTTP, FIRAS inversion, and Bogoliubov readout steps need status update.

Recommended handling:

* Paper 32 vNext should cite Paper 17 vNext for FIRAS-fixed readout normalization.
* It should not list observed CMB temperature as an independent zero-parameter prediction.
* It may still list base `T_IO` and the FIRAS-fixed `T_obs` readout, but the dependency must be explicit.

### Paper 33 v1.1

Priority: P1 if Paper 33 remains a public synthesis / architecture paper.

Representative locations:

* Line 12: Channel 2 includes "the CMB temperature" among bridge-active results.
* Line 20: claims the framework derives all major observables including "the CMB temperature (Paper 1)".
* Line 21: says the Hawking temperature becomes the CMB temperature.
* Line 24: lists CMB temperature among expansion-era derived observables.
* Lines 294 and 303: treat GTTP optical thermometry / CMB temperature as an active dynamic-thermal prediction.

Recommended handling:

* Replace "CMB temperature derived" with "base interior Hawking scale derived; observer-side CMB readout FIRAS-fixed by Paper 17 vNext."
* Keep dynamic-thermal channel architecture, but do not cite observed CMB temperature as an independent output.

### Paper 35 v1.1

Priority: P0/P1 because it uses `T_obs` in a live headline result.

Representative locations:

* Version history line 13: `eta_late` derived from `omega_b,geom + T_obs`.
* Line 16: says the derivation uses the IO CMB temperature and that the baryon count is a geometric prediction.
* Line 27: says `T_obs = T_IO x^K_gauge = 2.7253 K` is `DERIVED/SCOPED`.
* Line 30: uses `x^(3K_gauge)` conversion for `eta_BBN`.
* Line 31: says the two-temperature split is itself an IO prediction and the ratio is derived.
* Line 40: lists CMB temperature as one independent observable produced without adjustment.
* Line 42: says `gamma_BI` cannot be adjusted without moving `T_CMB`.
* Line 97: says IO predicts eta_late from `omega_b,geom + T_obs`.

Recommended handling:

* `eta_late` remains computationally reproducible but inherits the FIRAS-fixed `T_obs` dependency.
* `eta_BBN` on the local `T_IO` branch remains independent of R4.
* The two-temperature split should be reframed: the local-vs-observer thermal typing is structural; the observer-side normalization is FIRAS-fixed.
* Remove CMB temperature from the list of independent observables produced without adjustment.

## Numerical scorecard impact

Immediate numerical recomputation is not required for every downstream paper if the historical value `R4 = 1` remains within the FIRAS-fixed uncertainty and if existing scripts used the unit approximation. However, the status/wording impact is mandatory.

Cases:

* Results using `T_IO` only: no R4 numerical impact.
* Results using `T_obs = T_IO x^K_gauge` with implicit `R4 = 1`: should be treated as using the unit approximation to the FIRAS-fixed normalization. For exact vNext work, replace with `T_obs = T_IO x^(R4_FIRAS K_gauge) = T_FIRAS` by construction.
* Results depending on powers of `T_obs`, especially `eta_late ~ T_obs^-3`: if exact FIRAS-fixed `R4_FIRAS` is used, the change from `T_obs(1) = 2.7253060966 K` to `T_FIRAS = 2.7255 K` is tiny:

```text
delta_T / T ~= 7.12e-5
delta_eta / eta ~= -3 delta_T/T ~= -2.14e-4
```

This is a numerical non-event for most current scorecards, but it is not a claim-status non-event.

## Not directly affected

The following remain structurally intact, subject only to reference hygiene if they cite old GTTP wording:

* The base interior Hawking scale `T_IO`.
* The derivation/import of `gamma_BI` as an external LQG constant.
* The definition `K_gauge = ln(1 + gamma_BI^2)`.
* Local BBN thermal branch assignment: BBN microphysics uses `T_IO`, not observer-side `T_obs`.
* Paper 24 v2.3 lithium scorecard, insofar as it is a BBN/local nuclear computation and not a CMB-temperature prediction.
* Paper 34 Hubble scorecard formula unless the photometric `x^((n/2)K_gauge)` legs are explicitly tied to the same R4-normalized optical readout. This should be checked in a later Paper 34 hygiene pass.
* R4 no-go artifacts: they remain valid and now motivate the FIRAS-fixed route.

## Public site and calculator blast radius

The public-facing surfaces need a cleanup after Paper 17 vNext is accepted.

Known affected local files:

* `tmp/dfife.github.io/data/observational_conventions_v1.md`: states `T_0,CMB` used as PRyMordial input is `2.6635 K` because the framework has its own CMB derivation. This needs a vNext conventions clarification; do not mutate v1 if published papers cite it without adding a successor.
* `tmp/dfife.github.io/data/crossings.json`: CMB Temperature and GTTP Optical Transfer cards present `2.7253 K` as a prediction / CMB gap closure.
* `tmp/dfife.github.io/index.html`: confrontation table includes `T_CMB | 2.7253 K | FIRAS`.
* `tmp/dfife.github.io/data/papers.json` and `calculator/data/papers.json`: Paper 1, 13, 17, 33 summaries call observed CMB temperature a zero-parameter prediction.
* `calculator/calculator-theorems.html`: theorem nodes include `T_CMB (0.3 sigma from FIRAS)` and `T_obs = T_IO x^K_gauge`.

Recommended public wording:

```text
Base interior thermal scale: T_IO = 2.6635 K (derived).
Observer-side CMB readout: FIRAS-fixed unique normalization within the IO
thermal readout family (Paper 17 vNext).
```

## Version-history template for Paper 17 vNext

```text
vNext (May 2026): R4 / FIRAS readout-normalization correction.
Paper 17 v1.4 promoted the Gauge Thermal Transfer Principle as an
independent prediction of the observed CMB temperature,
T_obs = T_IO x^K_gauge = 2.7253 K. Subsequent field-redefinition audit
found that the Paper 17 modular-projection stack identifies the optical
thermal readout carrier and gauge payload but does not force the unit
optical normalization R4 = 1. The observed CMB temperature is therefore
no longer counted as an independent IO prediction. The corrected vNext
form defines the readout family T_obs(R4) = T_IO x^(R4 K_gauge) and
proves that the FIRAS empirical thermal datum fixes a unique normalization,
R4_FIRAS = ln(T_FIRAS/T_IO)/(K_gauge ln x). R4 is fixed once, frozen, and
not retuned against downstream observables. Downstream results using
T_obs or full GTTP readout inherit the FIRAS-fixed normalization; local
T_IO-only results are unaffected.
```

## Recommendation

Proceed in this order:

1. Paper 17 vNext: apply theorem replacement and dependency ledger.
2. Public conventions / calculator: stop displaying observed CMB temperature as an independent IO prediction.
3. Active synthesis papers: update Paper 32, Paper 33, and Paper 35 language when next republished.
4. Inherited appendix papers: update Papers 20-26 as they receive future hygiene releases.

Do not continue to defend `R4 = 1` as internally derived. The defensible position is the FIRAS-fixed uniqueness theorem plus a strict no-retuning rule.
