# Paper 34 v2.0 Planck CMB Classification Strengthening Memo

Date: 2026-05-22

## Verdict

**PROMOTE / SCOPED CLOSURE.**

The Planck row should not be assigned a derived single effective alpha-class.
The current IO stack instead supports a theorem-grade classification as a
**compound CMB inference**: Planck's published `H0` is a model-inferred
background parameter constrained by the acoustic angle, thermodynamic acoustic
ruler, angular-diameter distance, and full CMB transfer hierarchy. Those pieces
live on different typed blocks of the IO boundary-to-bulk architecture, so a
single primitive alpha assignment would be a category error.

This is stronger than the current prose exception. It makes Planck a uniform
scorecard row with its own row type:

```text
compound CMB inference; baseline projected background; no additional f_Gamma dressing
```

The result is not an OPEN/PREMISE_GAP. The open object is the stronger and
different problem of deriving a native CMB-side `H0` calculator from the full
acoustic/recombination observable. Paper 34 does not need that stronger object
to classify the published Planck `H0` row.

## Theorem 34.PC0 - Scoped Planck Scorecard Row Closure

**Status:** `DERIVED/CONDITIONAL_VERIFIED`.

**Scope.** This theorem closes only the Planck row as it is used in the Paper
34 six-method `H0` scorecard. It does not close the native IO CMB acoustic
calculator, does not derive the full CMB `C_l` hierarchy, and does not assign a
universal alpha-class to arbitrary CMB observables.

**Condition package.**

1. The active Paper 34 baseline is the Paper 10 legacy projected observer
   branch, `H0 = 67.57585653582628 km/s/Mpc`.
2. The Planck row uses the Planck 2018 base-Lambda-CDM posterior value
   `H0 = 67.4 +/- 0.5 km/s/Mpc` as an imported external CMB model inference,
   not as a direct local `H0` measurement.
3. The only Paper 34 question being closed is whether this imported Planck
   row receives an additional `f_Gamma` inverse-estimator dressing or
   stellar-photometric half-leg dressing inside the `H_ext(alpha,n)`
   scorecard.

**Statement.** Under the condition package above, the Planck row is completely
classified for the needs of Paper 34: it is a compound CMB-inference row whose
IO comparison value is the active projected baseline
`H0 = 67.58 km/s/Mpc`, with no additional `f_Gamma` dressing and no
photometric `x^{K_gauge/2}` leg. The scorecard pull is therefore
`+0.35 sigma`.

**Proof.** The Planck 2018 `H0` value is a posterior parameter inferred from
the CMB likelihood under base Lambda-CDM. Its dominant geometric handle is the
acoustic angular scale, reported by Planck as `100 theta_* = 1.0411 +/- 0.0003`,
and the same external source reports the model-inferred
`H0 = 67.4 +/- 0.5 km/s/Mpc`. Thus the Planck row is not a direct local
estimator of `H0`; it is an imported compound CMB model inference.

The Paper 34 inverse-estimator dressing law acts only after a measurement
method is assigned to a primitive late-time observable class. The
stellar-photometric half-leg factor acts only on uncancelled luminosity
calibrator legs in standard-candle chains. Planck has neither structure: it has
no local late-time distance-ladder primitive and no stellar-photometric
calibrator leg. Its acoustic and transfer ingredients are typed separately in
the Paper 32 boundary-to-bulk architecture, so adding a single extra
`f_Gamma` or photometric factor would mix blocks rather than follow from the
method definition.

Therefore the Planck scorecard row is closed by identity dressing relative to
the active projected baseline:

```text
H_IO,Planck-row = H0,baseline = 67.57585653582628 km/s/Mpc.
```

Rounded to the table precision, this is `67.58 km/s/Mpc`. The residual against
the imported Planck value is

```text
(67.57585653582628 - 67.4) / 0.5 = 0.3517,
```

reported in the manuscript as `+0.35 sigma` using the unrounded baseline
convention already used in the Paper 34 bundle.

**Chain.**

```text
Theorem 34.PC0
<- Paper 34 v2.0 §10.1 active Paper 10 legacy projected observer baseline
   H0 = 67.57585653582628 km/s/Mpc
<- Paper 34 v2.0 scoped inverse-estimator law
   H_eff(alpha) = H0 * f_Gamma^(1-alpha), valid only after primitive
   late-time observable-class assignment
<- Paper 34 v2.0 stellar-photometric extension, valid only for uncancelled
   standard-candle luminosity calibrator legs
<- Paper 32 v2.0 Theorem 32.B typed boundary-to-bulk architecture:
   CMB acoustic/thermodynamic history, projected geometry, and perturbation
   transfer are distinct typed blocks, not one primitive scalar slot
<- Paper 19 alpha-ladder observable-class taxonomy for primitive
   geometric/inventory, clustering, and Weyl/slice-curvature observables
<- Planck Collaboration 2020, Planck 2018 results VI:
   base-Lambda-CDM CMB posterior reports H0 = 67.4 +/- 0.5 km/s/Mpc and
   100 theta_* = 1.0411 +/- 0.0003
<- P1
<- P2
```

## Theorem 34.PC1 - Planck Compound CMB-Inference Classification

**Status:** `DERIVED/CONDITIONAL_VERIFIED`.

**Statement.** In the Paper 34 Hubble-scorecard setting, the Planck 2018
`H0` entry is not a primitive late-time expansion-rate observable and is not a
primitive member of one Paper 19 alpha-ladder rung. It is a compound CMB
inference whose likelihood constrains a baseline background parameter through
the joint CMB acoustic and transfer hierarchy. Under the IO typed
boundary-to-bulk architecture, its ingredients occupy at least three distinct
typed blocks:

1. the thermodynamic/acoustic history block carrying the sound-horizon and
   recombination/drag history,
2. the projected geometric background block carrying `D_M(z_*)` and the
   baseline `H0` branch,
3. the perturbation/transfer block carrying the full CMB temperature and
   polarization hierarchy.

Therefore the Planck row receives no additional late-time `f_Gamma`
inverse-estimator dressing and no stellar-photometric half-leg dressing. Its
Paper 34 classification is:

```text
compound CMB inference / baseline projected background / no single alpha
```

with the numerical comparison made against the inherited active baseline
`H0 = 67.57585653582628 km/s/Mpc`, rounded to `67.58 km/s/Mpc`.

**Proof.** Planck's quoted `H0` is obtained by fitting the CMB acoustic and
transfer data within a cosmological model, not by directly measuring a local
distance ladder, a standard siren amplitude, a time-delay distance, or a
differential-age expansion rate. The primary acoustic handle is the angular
scale

```text
theta_* = r_d / D_M(z_*)
```

together with the full TT/TE/EE transfer hierarchy. The numerator is an
early-time thermodynamic/acoustic object; the denominator is a geometric
projected-distance object; the full CMB spectrum adds perturbation and
visibility-transfer structure.

Paper 32 Theorem 32.B states that the complete boundary-to-bulk map exists only
as a typed extended-carrier projection theorem. Its diagonal blocks include the
source/readout block, thermodynamic history block, and closed-`S^3`
perturbation block. Paper 32 also records that the perturbation hierarchy
receives typed inputs from both the primordial source block and the
thermodynamic history block. Therefore the Planck likelihood is not a single
one-slot scalar readout of the kind to which a primitive Paper 19 alpha-rung can
be assigned.

The Paper 19 alpha-ladder applies to identified observable classes: geometric
or inventory observables at `alpha = 1`, continuity/clustering descendants at
`alpha = 3/2`, and Weyl/slice-curvature descendants at `alpha = 2`. A compound
CMB likelihood formed from thermodynamic, geometric, and perturbative pieces
does not become one of these primitive classes merely because the fit reports a
posterior value for `H0`. Assigning a single effective alpha would require an
additional theorem showing that the compound likelihood functor collapses to one
primitive alpha-rung. The current stack proves the opposite structural
separation: the CMB acoustic angle and full CMB spectrum remain composite typed
objects rather than a single scalar slot.

The Paper 34 late-time inverse-estimator formula

```text
H_eff(alpha) = H0 * f_Gamma^(1-alpha)
```

is scoped to measurement methods that infer `H0` through one identified
late-time observable class. The stellar-photometric extension further adds
`x^((n/2) K_gauge)` only for standard-candle luminosity calibration legs.
Planck has neither structure. It is not a late-time local inverse-estimator
measurement with one primitive alpha-class, and it has no Cepheid, TRGB,
supernova, or other uncancelled stellar-photometric calibration leg. Hence the
additional factors are identity for the Planck scorecard row.

What remains is the inherited active projected baseline branch. Paper 34 v2.0
uses the Paper 10 legacy projected observer baseline
`H0 = 67.57585653582628 km/s/Mpc`; the Planck row compares the published
Planck 2018 `H0 = 67.4 +/- 0.5 km/s/Mpc` against this baseline. The residual is

```text
(67.58 - 67.4) / 0.5 = +0.35 sigma
```

after rounding. This completes the classification.

**Chain.**

```text
Theorem 34.PC1
<- Paper 34 v2.0 §10.1 active Paper 10 legacy projected baseline
   H0 = 67.57585653582628 km/s/Mpc
<- Paper 34 v2.0 inverse-estimator scope statement for H_eff(alpha)
   and stellar-photometric no-leakage statement
<- Paper 32 v2.0 Theorem 32.B (Typed Boundary-to-Bulk Projection Theorem:
   complete field-level map exists only as typed extended-carrier projection;
   thermodynamic history and perturbation blocks do not collapse to the
   one-slot source/readout block)
<- Paper 32 v2.0 Corollary 32.B.2 (thermodynamic/reionization history is a
   local-history theorem, not a scalar source theorem)
<- Paper 19 alpha-ladder observable-class assignments
   (alpha = 1 geometric/inventory, alpha = 3/2 continuity/clustering,
   alpha = 2 Weyl/slice-curvature)
<- Planck Collaboration 2020, Planck 2018 results VI:
   Planck CMB `H0` is a Lambda-CDM parameter inference from the CMB acoustic
   and transfer likelihood, not a direct local `H0` measurement
<- P1 (the observable universe is inside a Schwarzschild black hole)
<- P2 (physics inside the horizon equals physics outside)
```

## Corollary 34.PC2 - No Single Effective Alpha for Planck

**Status:** `DERIVED/NO-GO` for single-alpha promotion on the current stack.

**Statement.** The current IO theorem stack does not derive a single effective
`alpha_Planck` for the Planck `H0` row. Any such assignment would require an
additional collapse theorem showing that the compound CMB likelihood reduces to
one primitive alpha-rung without double-counting thermodynamic, geometric, and
perturbation contributions.

**Proof.** A single alpha assignment would mean the full Planck CMB inference
transforms under the same one-parameter inverse-estimator law as a primitive
late-time observable class. But the CMB likelihood includes at least
`r_d`, `D_M(z_*)`, and transfer-function information. Paper 32 Theorem 32.B
places these in different typed blocks. Paper 31's observable-class map marks
`theta_*` and the full CMB `C_l` spectrum as composite/open class objects, not
closed primitive alpha slots. Therefore no existing theorem collapses the
Planck likelihood to one alpha-rung. Choosing an alpha because it reproduces
Planck's published `H0` would be observational selection and is not allowed.

**Chain.**

```text
Corollary 34.PC2
<- Theorem 34.PC1
<- Paper 32 v2.0 Theorem 32.B
<- Paper 31 complete observable-class map entries for theta_* and full CMB C_l
   spectrum: composite/open, not primitive single alpha slots
<- Paper 19 alpha-ladder observable-class assignments
<- P1
<- P2
```

## Recommended §4.1 Replacement Text

```text
4.1 Planck CMB

The Planck H0 value is not a direct local measurement of H0. It is a
Lambda-CDM parameter inference from the CMB acoustic and transfer likelihood,
with the acoustic scale theta_* = r_d / D_M(z_*) tying together an early-time
thermodynamic sound horizon, a projected geometric angular-diameter distance,
and the full temperature/polarization transfer spectrum. By the Paper 32 typed
boundary-to-bulk projection theorem, these factors live on distinct typed
blocks of the IO architecture: thermodynamic history, projected geometry, and
closed-S^3 perturbation transfer. Therefore the Planck row is not assigned a
single primitive alpha-rung. Its scorecard classification is instead
compound CMB inference / baseline projected background: it receives no
additional late-time f_Gamma inverse-estimator dressing and no
stellar-photometric half-leg dressing. IO prediction: 67.58 km/s/Mpc. Planck
measurement: 67.4 +/- 0.5 km/s/Mpc. Deviation: +0.35 sigma. Status:
DERIVED/CONDITIONAL_VERIFIED as a compound CMB-inference classification;
DERIVED/NO-GO for promotion to a single effective alpha on the current stack.
```

## Recommended §5 Table Row

Replace the `alpha` cell for Planck:

```text
baseline
```

with:

```text
compound CMB / baseline
```

If the table can support a wider label, use:

```text
compound CMB inference; baseline, no single alpha
```

## Recommended §10 Addition

This is not an open-premise entry. It is a scope clarification / promoted row
classification. Add after §10.1 or fold into §10.5:

```text
Planck CMB row. The Planck row is classified as a compound CMB inference, not
as a primitive alpha-rung. The Planck H0 posterior is inferred from a model fit
to theta_* and the full CMB transfer hierarchy, whose components occupy
thermodynamic-history, projected-geometric, and perturbation-transfer blocks in
the Paper 32 typed boundary-to-bulk architecture. No existing theorem collapses
that compound likelihood to a single effective alpha, and this paper does not
claim one. The row is therefore compared to the active projected baseline
H0 = 67.58 km/s/Mpc with no additional f_Gamma or photometric dressing.
```

## Why DERIVED Is Not Recommended

The DERIVED single-alpha route would require proving that the compound CMB
likelihood has an effective primitive class with a unique alpha. The current
stack does not prove that. Existing audits say the stronger native CMB-side
`H0` calculator is not finished because the primitive acoustic/recombination
observable remains open. Promoting Planck to a single alpha would therefore
overclaim.

## Why OPEN PREMISE Is Not Recommended

The row does not need an additional open premise to be used in Paper 34. The
published Planck `H0` is already an imported external CMB model inference, and
the IO classification needed for Paper 34 is only whether it receives the
Paper 34 late-time inverse-estimator or stellar-photometric dressings. The typed
architecture and method definition answer that: it does not. The unresolved
native CMB calculator is a separate stronger problem, not a blocker for the
Paper 34 scorecard classification.
