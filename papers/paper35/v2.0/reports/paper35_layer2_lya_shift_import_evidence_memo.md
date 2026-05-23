# Paper 35 §4 Layer 2 Lyα Shift Import Evidence Memo

## Purpose

Cosmo placed Layer 2 of the Paper 35 §4 DESI correction on HOLD because the
RCA report did not include enough evidence that the Lyα shift
`alpha = 0.9905 +/- 0.0027` was:

1. banked upstream in Paper 29 / Paper 31 theorem artifacts,
2. imported from a specific external publication,
3. banked before the Paper 35 raw DESI GCcomb residual was used.

This memo gathers those three evidence classes in one file.

## Executive Verdict

The Lyα shift is an honest P2 import banked before the public Paper 35 raw
GCcomb BAO confrontation.

Narrow discipline statement:

- The external Lyα shift value is not internally derived by IO.
- Layer 2 is therefore `DERIVED/CONDITIONAL_VERIFIED` at most: conditional on
  Premise 2 and the accepted exterior Lyα redshift-space flux-correlation
  shift class.
- The timeline supports non-fitted use relative to the Paper 35 raw GCcomb BAO
  residual: Paper 31 banked the shift on 2026-04-03, Paper 29 banked the full
  current-DESI imported-Lyα closure on 2026-04-12, and Paper 35 v1.1 first
  archived the raw GCcomb `chi2 = 69.4848` result on 2026-05-03. Paper 35
  v2.0 was still pre-publication during the present replacement.
- There were earlier Paper 35 DESI-dark-energy exploratory artifacts in April
  2026, but those are not the Paper 35 raw GCcomb BAO confrontation used in
  the Layer 1/Layer 2 correction. The relevant fitted-parameter question for
  Layer 2 is whether `alpha = 0.9905 +/- 0.0027` was selected after seeing the
  Paper 35 raw GCcomb BAO residual. The file timestamps and public-git history
  indicate no.

Final summary statement:

**The Lyα shift is an honest P2 import banked before Paper 35's raw DESI GCcomb
BAO confrontation.**

## 1. Theorem Text Quotations

### 1.1 Paper 29 full current-DESI imported-Lyα closure report

Source path:

`/opt/cosmology-lab/results/paper29/paper29_full_desi_imported_lya_closure_report.md`

File timestamp:

`2026-04-12 10:39:59.441270795 -0400`

Version/status:

- Lab/MCP result artifact for Paper 29.
- The public Paper 29 v2.0 reproducibility bundle does not currently include
  this report; it is banked in the lab result/MCP store.
- Claim label in artifact: `derived / conditional / scoped under Premise 2`.

Relevant theorem/status quotation:

> `derived / conditional / scoped under Premise 2`:
> the current i.i.d. DESI DR2 GCcomb route strengthens to a full
> current-observable closure by combining
> 1. hybrid isolated pre-drag ruler
> 2. promoted galaxy/quasar kernel
> 3. inherited exterior Lyalpha flux-shift class

Relevant imported-source quotation:

> `verified`:
> the strongest published Lyalpha class on the current i.i.d. route is still
> the redshift-space negative-shift class of `arXiv:2407.03918`

Relevant alpha and numerical-output quotation:

> Best published class on the current i.i.d. route:
> - `Sinigaglia 2024 redshift-space isotropic shift` from `arXiv:2407.03918`
> - `alpha_parallel = 0.9905`
> - `alpha_perp = 0.9905`
> - `BAO chi2 = 26.296479748359552`
> - `combined chi2 = 40.998003712340335`
> - `Lyalpha block chi2 = 0.30139501794264395`

Relevant boundary quotation:

> `derived / conditional / scoped`:
> the current full DESI DR2 route closes if
> - the promoted i.i.d. galaxy/quasar kernel is accepted, and
> - the Lyalpha late-time readout belongs to the inherited redshift-space
>   negative-shift class of `arXiv:2407.03918`

Negative-boundary quotation:

> `not derived`:
> the non-identity Lyalpha shift is still not an internal IO theorem.

Chain visibility:

- Direct chain endpoint visible in the quoted status: Premise 2.
- External endpoint visible in the quoted source: `arXiv:2407.03918`.
- Scope boundary visible: imported exterior Lyα flux-shift class, not internal
  IO derivation.

### 1.2 Paper 29 full current-DESI imported-Lyα closure results JSON

Source path:

`/opt/cosmology-lab/results/paper29/paper29_full_desi_imported_lya_closure_results.json`

File timestamp:

`2026-04-12 10:39:59.441270795 -0400`

Relevant JSON quotation:

```json
"headline": {
  "status": "derived_conditional_scoped_full_current_desi_with_imported_lya_shift",
  "summary": "On the promoted i.i.d. galaxy/quasar route, importing the published Lyalpha redshift-space negative-shift class from arXiv:2407.03918 gives the strongest current full-DESI conditional closure. The literature central value remains within half a sigma of the current i.i.d. isotropic Lyalpha optimum."
}
```

Input quotation:

```json
"inputs": {
  "hybrid_r_d_mpc": 144.01351425392883,
  "eta": 0.036124605346983495,
  "f_perp_gal": 1.036785027400527,
  "f_par_gal": 1.0182264126413767,
  "sinigaglia_redshift_alpha": 0.9905,
  "sinigaglia_redshift_alpha_sigma": 0.0027
}
```

Best-literature-case quotation:

```json
"best_literature_case": {
  "name": "sinigaglia2024_redshift_iso",
  "label": "Sinigaglia 2024 redshift-space isotropic shift",
  "source": "arXiv:2407.03918",
  "alpha_parallel": 0.9905,
  "alpha_perp": 0.9905,
  "alpha_iso": 0.9905,
  "alpha_iso_sigma": 0.0027,
  "bao_chi2": 26.296479748359552,
  "combined_chi2": 40.998003712340335,
  "lya_block_chi2": 0.30139501794264395,
  "galaxy_quasar_block_chi2": 25.995084730416906
}
```

Boundary quotation:

```json
"not_established": [
  "Internal theorem-grade derivation of the non-identity Lyalpha shift.",
  "Universal BAO closure across all tracers, estimators, and Lyalpha modelling classes.",
  "Unique external Lyalpha class selection independent of late-time modelling assumptions."
]
```

Chain visibility:

- Status names the closure as conditional/scoped.
- Source field points to the external import.
- Boundary field explicitly prevents treating the shift as an internal theorem.

### 1.3 Paper 31 Ly-alpha BAO Shift Inheritance Theorem

Source path:

`/opt/cosmology-lab/results/paper31/paper31_lya_bao_shift_inheritance_theorem.md`

File timestamp:

`2026-04-03 10:40:09.157412796 -0400`

Relevant theorem question:

> Can the open Ly-alpha half of Seam 2 be closed by importing the exterior
> Ly-alpha nonlinear flux-correlation shift class under Premise 2, without
> introducing a new free fit parameter?

Relevant imported-shift-law quotation:

> Under Premise 2, the late-time Ly-alpha forest flux-correlation kernel is an
> inherited exterior physics object. The primitive sound horizon is not
> tracer-specific, but the late-time readout operator is.

Relevant imported primary-source class quotation:

> The audit used only published primary-source Ly-alpha shift classes:
>
> 1. `arXiv:2407.03918` redshift-space isotropic shift:
>    \[
>    \alpha = 0.9905 \pm 0.0027
>    \]

Relevant status quotation:

> `derived / conditional`:
> under Premise 2, exterior Ly-alpha nonlinear flux-shift classes are
> admissible imports on the Schur raw ruler.

Relevant verified statement:

> `verified`:
> the redshift-space negative-shift class of `arXiv:2407.03918` moves the Schur
> Ly-alpha block inside current DR2 precision and improves the 2-row block
> chi-square from `6.1764` to `1.5033`.

Relevant conditional-boundary quotation:

> `conditional`:
> the Ly-alpha half of Seam 2 closes if the admissible inherited Ly-alpha
> readout kernel is that redshift-space negative-shift class.

Negative-boundary quotation:

> This is not an internal derivation of the Ly-alpha kernel.
> It is a conditional closure via imported exterior late-time flux physics under
> Premise 2.

Chain visibility:

- Premise 2 is explicit.
- External source `arXiv:2407.03918` is explicit.
- No-free-fit language is explicit in the question.

### 1.4 Paper 31 Ly-alpha BAO End-to-End Inheritance Theorem

Source path:

`/opt/cosmology-lab/results/paper31/paper31_lya_bao_end_to_end_inheritance_theorem.md`

Public bundle path:

`/opt/cosmology-lab/tmp/io-framework-public/papers/paper31/v2.0/reports/paper31_lya_bao_end_to_end_inheritance_theorem.md`

File timestamp:

`2026-04-03 11:52:50.774128286 -0400`

Relevant claim quotation:

> Yes, but only conditionally.
>
> The strongest honest upgrade is:
>
> \[
> \boxed{
> \text{same raw Schur ruler}
> \;\;+\;\;
> \text{inherited exterior Ly}\alpha\text{ flux observable class}
> \;\;+\;\;
> \text{inherited redshift-space negative Ly}\alpha\text{ shift class}
> \;\Rightarrow\;
> \text{Ly}\alpha\text{ BAO closure at current DR2 precision.}
> }
> \]

Relevant Premise 2 chain quotation:

> Under Premise 2, these are admissible inherited late-time Ly-alpha kernel
> classes on the Schur raw ruler.

Relevant external-source quotation:

> strong negative redshift-space shift:
> `arXiv:2407.03918`
> \[
> \alpha = 0.9905 \pm 0.0027
> \]

Relevant theorem statement quotation:

> Assume:
>
> 1. Premise 2: exterior late-time Ly-alpha forest physics is admissible inside
>    the hole.
> 2. The primitive early-time Schur pre-drag ruler is the same object for all BAO
>    tracers.
> 3. The Ly-alpha BAO observable belongs to the accepted continuous
>    redshift-space flux-correlation class.
> 4. The physical late-time Ly-alpha nonlinear readout kernel belongs to the
>    redshift-space negative-shift class measured in `arXiv:2407.03918`.

Relevant status quotation:

> `derived / conditional`:
> the end-to-end theorem chain exists under Premise 2 and accepted exterior
> Ly-alpha forest physics.

Relevant verification quotation:

> `verified`:
> the imported redshift-space negative shift class of `arXiv:2407.03918`
> closes the DESI DR2 Ly-alpha block on the Schur raw ruler.

Negative-boundary quotation:

> It does **not** upgrade the Ly-alpha sector to a purely internal derivation.

Chain visibility:

- Premise 2 is explicit in the theorem assumptions.
- External source `arXiv:2407.03918` is explicit in the theorem assumptions.
- The result is conditional, not universal or internally derived.

## 2. External Source Citation

External source:

Sinigaglia, F., Kitaura, F.-S., Nagamine, K., and Oku, Y. (2024).
*The negative BAO shift in the Lyα forest from cosmological simulations*.
arXiv:2407.03918 [astro-ph.CO], v3 revised 2024-07-24.
The arXiv record states the paper was accepted for publication in *ApJ Letters*.
arXiv DOI: `10.48550/arXiv.2407.03918`.

Public source URL:

`https://arxiv.org/abs/2407.03918`

Source location for the value:

- arXiv abstract reports the real-space and redshift-space BAO shift values.
- The PDF text places the same result in Section 5, "Results and Discussion",
  immediately after discussing Figs. 4 and 5 posterior distributions.
- The result is also repeated in the paper conclusion.

Specific value:

- real space: `alpha = 0.9969^{+0.0014}_{-0.0014}`;
- redshift space: `alpha = 0.9905^{+0.0027}_{-0.0027}`.

External-source quote kept short for copyright discipline:

> "in real and redshift space, respectively."

The full arXiv abstract line reports the two values in that order; the
redshift-space value is the second value, `0.9905 +/- 0.0027`.

From local PDF text extraction, Section 5 says:

```text
5. RESULTS AND DISCUSSION
...
We find the following BAO shift parameters: alpha =
0.9969... in real space, alpha = 0.9905... in redshift space.
```

Publication role:

- This is the original derivation/measurement used by the IO import, not a
  downstream citation.
- It is a Lyα forest redshift-space flux-correlation BAO shift from
  cosmological simulations.
- Physics class: Lyα redshift-space nonlinear BAO-shift / RSD-including
  flux-correlation systematic.

No combination of multiple external sources is needed for the Layer 2 central
value. Paper 29 compared other external classes, but the Layer 2 value itself
is imported from Sinigaglia et al. 2024 / arXiv:2407.03918.

## 3. Banking Timeline and Fitted-Parameter Discipline Check

### 3.1 Paper 31 banking

Paper 31 shift-inheritance theorem file:

`/opt/cosmology-lab/results/paper31/paper31_lya_bao_shift_inheritance_theorem.md`

Timestamp:

`2026-04-03 10:40:09.157412796 -0400`

Paper 31 end-to-end inheritance theorem file:

`/opt/cosmology-lab/results/paper31/paper31_lya_bao_end_to_end_inheritance_theorem.md`

Timestamp:

`2026-04-03 11:52:50.774128286 -0400`

Public bundle copy:

`/opt/cosmology-lab/tmp/io-framework-public/papers/paper31/v2.0/reports/paper31_lya_bao_end_to_end_inheritance_theorem.md`

Public repo commits:

```text
8967c46 2026-05-21T07:02:35-04:00 Add Paper 31 v2.0 reproducibility bundle
13b7e50 2026-05-21T08:08:27-04:00 Publish Paper 31 v2.0 reproducibility bundle
```

The local theorem artifact predates the public Paper 31 v2.0 bundle commit.
The public bundle preserves the same theorem text.

### 3.2 Paper 29 banking

Paper 29 full-DESI imported-Lyα closure report:

`/opt/cosmology-lab/results/paper29/paper29_full_desi_imported_lya_closure_report.md`

Timestamp:

`2026-04-12 10:39:59.441270795 -0400`

Paper 29 full-DESI imported-Lyα closure results:

`/opt/cosmology-lab/results/paper29/paper29_full_desi_imported_lya_closure_results.json`

Timestamp:

`2026-04-12 10:39:59.441270795 -0400`

Public repo commit for Paper 29 v2.0 bundle:

```text
216e29a 2026-05-18T19:46:02-04:00 Add Paper 29 v2.0 reproducibility bundle
```

Important limitation:

- The Paper 29 imported-Lyα closure report appears in the lab/MCP result store,
  not in the public Paper 29 v2.0 bundle files currently checked under
  `tmp/io-framework-public/papers/paper29/v2.0`.
- Therefore, for Cosmo's audit, the Paper 29 evidence should be treated as a
  banked lab/MCP result artifact rather than a public-bundle artifact unless it
  is separately added to a Paper 29 bundle revision.

### 3.3 Paper 35 first raw GCcomb BAO confrontation

First public Paper 35 version with the raw DESI DR2 GCcomb confrontation:

`Paper 35 v1.1`

Script path:

`/opt/cosmology-lab/tmp/io-framework-public/papers/paper35/v1.1/scripts/07_desi_confrontation.py`

Script timestamp:

`2026-05-03 19:18:47.084750259 -0400`

Result path:

`/opt/cosmology-lab/tmp/io-framework-public/papers/paper35/v1.1/results/desi_confrontation_results.json`

Result timestamp:

`2026-05-03 19:18:47.202750403 -0400`

Result quotation:

```json
"raw_gccomb": {
  "active_branch_chi2": 69.48480893315653
}
```

Public repo commit:

```text
8518720 2026-05-03T19:23:12-04:00 Add Paper 35 v1.1 reproducibility bundle
```

Paper 35 v1.2 preserved the same raw GCcomb result on 2026-05-06.
Paper 35 v2.0 was staged in the public repository on 2026-05-23 and later
repaired to Layer 1 before manuscript publication.

### 3.4 Earlier Paper 35 DESI awareness distinction

There is an earlier Paper 35 exploratory report:

`/opt/cosmology-lab/results/paper35/paper35_three_confrontations_report.md`

It discusses DESI evolving-dark-energy `w0-wa` / constant-`w` confrontations,
not the raw GCcomb BAO `chi2 = 69.4848` residual that Layer 1/Layer 2 repairs.

The Paper 35 three-confrontations report existed after the downloaded DESI DR2
source material and around the April 2026 Paper 35 exploration cycle. Its DESI
section tested `w_IO = -1/3` against DESI dark-energy parameter fits, and
states:

> `verified`: the CPL image `(-1/3, 0)` does **not** lie in DESI DR2's
> preferred region

This is not the same residual as the Paper 35 raw GCcomb BAO confrontation.
For the Layer 2 fitted-parameter audit, the relevant sequence is:

1. 2026-04-03: Paper 31 banks the Lyα shift inheritance theorem.
2. 2026-04-12: Paper 29 banks the full current-DESI imported-Lyα closure.
3. 2026-05-03: Paper 35 v1.1 first archives raw GCcomb `chi2 = 69.4848`.
4. 2026-05-23: Paper 35 v2.0 Layer 1 repair identifies raw GCcomb as the wrong
   live observable.
5. 2026-05-23: Paper 35 v2.0 Layer 2 candidate archives the conditional
   P2-imported Lyα shift branch.

### 3.5 Timeline verdict

The file and git timestamps show that the Lyα shift import was banked before
the Paper 35 raw GCcomb BAO confrontation:

| Event | Date/time | Evidence |
|---|---:|---|
| Paper 31 Lyα shift inheritance theorem | 2026-04-03 10:40:09 -0400 | local/MCP artifact timestamp |
| Paper 31 Lyα end-to-end theorem | 2026-04-03 11:52:50 -0400 | local artifact and public bundle copy |
| Paper 29 full-DESI imported-Lyα closure | 2026-04-12 10:39:59 -0400 | local/MCP artifact timestamp |
| Paper 35 v1.1 raw GCcomb result | 2026-05-03 19:18:47 -0400 | public-bundle result timestamp |
| Paper 35 v1.1 public commit | 2026-05-03 19:23:12 -0400 | git commit `8518720` |
| Paper 35 v2.0 pre-publication public-repo commit | 2026-05-23 07:09:14 -0400 | git commit `ff4198b` |

Discipline conclusion:

The evidence supports using Layer 2 as a conditional P2 import without treating
it as a fitted parameter selected after Paper 35 saw the raw GCcomb BAO
residual.

## 4. What Cosmo Can and Cannot Approve From This Evidence

Cosmo can approve:

- The external source of `alpha = 0.9905 +/- 0.0027` is identified:
  Sinigaglia et al. 2024, arXiv:2407.03918.
- Paper 31 explicitly banks the import under Premise 2 and labels it
  conditional, not internal.
- Paper 29 explicitly applies the imported class to the full current-DESI route
  and records `BAO chi2 = 26.296479748359552`.
- The Paper 35 v2.0 Layer 2 number is a recalculation of that already-banked
  class on the Paper 35 active script and covariance, with uncertainty
  propagation added.

Cosmo should not approve:

- Any statement that the Lyα shift is internally derived from IO geometry.
- Any statement that Layer 2 is universal BAO closure.
- Any statement that external Lyα literature uniquely proves this shift class
  independent of late-time modelling assumptions.

Correct status for Paper 35 Layer 2:

`DERIVED/CONDITIONAL_VERIFIED` for the P2-imported exterior redshift-space
Lyα flux-shift class, with `alpha = 0.9905 +/- 0.0027` imported from
Sinigaglia et al. 2024.

Correct short manuscript wording:

> Layer 2 uses the exterior Lyα redshift-space flux-correlation shift class
> imported under Premise 2, `alpha = 0.9905 +/- 0.0027` from Sinigaglia et al.
> (2024). This branch is conditional on that external Lyα class and does not
> constitute an internal IO derivation of the Lyα shift.
