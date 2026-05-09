# Paper 21 v2.0 R4 and Kappa-Style Structural Audit

Date: May 9, 2026

Scope: Paper 21 v2.0 draft in `results/Full Papers/Interior_Observer_Paper21_v2_0.docx`, extracted to `/tmp/paper21_v20_text.txt` for line references. This audit checks active Paper 21 v2.0 claims, R4/FIRAS damage, hidden fitted parameters, status-label compliance, abbreviation/slang hygiene, and appendix cleanup requirements.

## Executive Verdict

No hidden continuous fitted parameter was found in the active Paper 21 v2.0 claim set.

The active Paper 21 v2.0 calculations survive the R4 update because the active Big Bang nucleosynthesis branch assignment uses `T_IO`, not the observer-side optical readout temperature. Updating `R4 = 1` to `R4_FIRAS = 1.0031014644` changes the optical readout bookkeeping but does not enter the active Paper 21 Big Bang nucleosynthesis scorecard.

The manuscript draft still has significant hygiene issues:

- The appendix still contains stale `R4 = 1` / independent cosmic microwave background temperature prediction language.
- The appendix still functions as a historical record, despite the new rule that superseded or no-longer-valid entries should be removed rather than preserved.
- Several labels use retired forms (`CONDITIONAL/THEOREM`, `DERIVED/SCOPED`, `CONDITIONAL/BRIDGE THEOREM`, plain `DERIVED` where a premise package is explicit).
- The Code and Data Availability section still points to `paper21-v1.7`.
- Multiple abbreviations and IO-specific slang terms appear without enough standard-physics explanation for a reader arriving cold.

## Active Claims Audited

### 1. R4/FIRAS Dependency

Candidate field: the optical readout normalization multiplying `K_gauge` in `T_obs(R4) = T_IO x^(R4 K_gauge)`.

Rigidity test: Paper 17 v1.5 no longer treats `R4 = 1` as internally derived. It fixes a unique `R4_FIRAS = 1.0031014644` using the FIRAS empirical thermal datum. Paper 21's active Big Bang nucleosynthesis branch assignment does not use `T_obs`; it uses `T_IO`.

Classification: `IMPORTED/EMPIRICAL` for `R4_FIRAS`; `VERIFIED` for Paper 21 inheritance audit.

Impact on Paper 21 active calculations: none for `L_1`, `L_2`, AC1 closure, YPCMB wrapper convention, or active Big Bang nucleosynthesis scorecard.

Bundle action: `scripts/01_r4_firas_dependency_audit.py` added. The public bundle now records `R4_FIRAS = 1.0031014644`, `T_obs(R4) = 2.725499012374763 K`, and `R4_enters_active_BBN_scorecard = false`.

### 2. AC1 Acoustic Closure

Candidate fields: the numerator readout class, the denominator gauge neutrality, the `sqrt(1 + gamma_BI^2)` factor, the `x^(-1/2)` acoustic-history factor, and the reduced scalar/longitudinal acoustic-sector scope.

Rigidity test: Given the Paper 15-20 theorem stack and the A4 bridge theorem, the script-level arithmetic for `J_theta = x^(-1/2) sqrt(1 + gamma_BI^2) = 0.8339461798286282` is fixed. The sector restriction is load-bearing and must be visibly stated.

Classification: `DERIVED/CONDITIONAL_VERIFIED`, unless the manuscript explicitly expands the whole AH1-AH7 + P1-P6 + RT/BY + B1-B5 chain back to the founding premises in the local theorem text.

Hidden parameter finding: none.

Label issue: paragraph 68 says `DERIVED/THEOREM under AH1-AH7 + P1-P6 + RT/BY + B1-B5. Scope: reduced scalar/longitudinal acoustic sector.` Under the current claim discipline, this should be `DERIVED/CONDITIONAL_VERIFIED` unless all dependencies are restated locally as closed theorem dependencies.

### 3. Puncture Loads `L_1` and `L_2`

Candidate fields: isolated-horizon puncture Hamiltonian, local Unruh temperature pairing, physical spin spectrum `j in {1/2, 1, 3/2, ...}`, degeneracy `(2j + 1)`, energy weighting, denominator range, and channel selection `j = 1`, `j = 2`.

Rigidity test: Given the stated isolated-horizon Hamiltonian and Barbero-Immirzi input, the local scale cancels and the numerical loads are fixed:

- `L_1 = 0.22416889162576648`
- `L_2 = 0.13805247907094412`
- `L_1 + L_2 = 0.36222137069671057`

Classification: `DERIVED/THEOREM` for Paper 21's puncture-load arithmetic and temperature-independence theorem. `gamma_BI` remains an external physics input from loop quantum gravity black-hole entropy.

Hidden parameter finding: none.

Boundary: Paper 21 derives the loads. Paper 22/Paper 25 own the later claim that these loads enter the weak and nuclear rate-dressing channels.

### 4. Optical Filtration Theorem 21.J

Candidate fields: reduced RT/BY optical class, compact SU(2) averaging, fixed-point algebra, and blindness to noncentral puncture data.

Rigidity test: Within the reduced optical readout class, the averaging map is fixed. Outside that class, the theorem does not apply.

Classification: `DERIVED/CONDITIONAL_VERIFIED`, because the reduced optical class is load-bearing and must trace through the bridge-map theorem stack.

Hidden parameter finding: none.

Label issue: paragraph 121 says `DERIVED/THEOREM within reduced RT/BY optical class`. That should either include the dependency chain locally or migrate to `DERIVED/CONDITIONAL_VERIFIED`.

### 5. Local Nontraciality Theorem 21.O

Candidate fields: bipartite puncture split, multiplicities `m_A^J`, `m_B^J`, invariant-state projection, and the physical interpretation connecting local nontraciality to the Big Bang nucleosynthesis sector.

Rigidity test: The mathematical nontraciality result is rigid: the reduced local state is invariant but generically nontracial unless `m_B^J/(2J+1)` is independent of `J`.

Classification:

- Mathematical theorem: `DERIVED/THEOREM`.
- Physical interpretation as a bridge substrate: `DERIVED/CONDITIONAL_VERIFIED` only if the paper states the physical partition and coupling path back to P1/P2 or imported physics. Otherwise label as `OPEN/PREMISE_GAP`.

Hidden parameter finding: none in the mathematical theorem. The physical delivery path is conditional and must not be hidden inside a theorem label.

Label issue: paragraph 130 uses `CONDITIONAL/BRIDGE THEOREM`, which is not in the current public claim-discipline list.

### 6. Conformal Transparency Theorem 21.Ba

Candidate fields: exact homogeneous OS interior, source-free Maxwell equations, and homogeneous-level restriction.

Rigidity test: Standard 3+1 Maxwell conformal invariance fixes the result on the stated background. Dynamic backscattering remains outside the theorem.

Classification: `DERIVED/THEOREM` for the homogeneous source-free result.

Hidden parameter finding: none.

### 7. Big Bang Nucleosynthesis Branch Assignment 21.L

Candidate fields: classify Big Bang nucleosynthesis as local bulk thermodynamics or RT/BY optical readout; use `T_IO` or `T_obs`; minimal premise TIO1.

Rigidity test: Once TIO1 is admitted, the class assignment is fixed: the optical readout map has no primitive leg on which to act in the Big Bang nucleosynthesis abundance/rate calculation. The active scorecard uses `T_IO`.

Classification: `DERIVED/CONDITIONAL_VERIFIED`, with TIO1 stated explicitly. It should not remain `CONDITIONAL/THEOREM at reduced scope`.

Hidden parameter finding: none. The risk is label opacity, not numerical fitting.

R4 impact: none on the active scorecard. The class-mismatched `T_obs` demonstration should use updated `T_obs(R4)` if retained with exact numerics, or be described only qualitatively as a class-error check.

## R4/CMB Damage Inventory

The following v2.0 draft locations need update or removal:

- Paragraph 22: says Papers 1-21 derived all major cosmological observables including cosmic microwave background data from `M_U` and `gamma_BI`. This should not imply an independent cosmic microwave background temperature prediction after Paper 17 v1.5.
- Paragraph 24: says zero fitted parameters means zero parameters fitted to `CMB, BBN, supernovae, BAO`. This needs qualification because FIRAS fixes the observer-side optical thermal readout normalization.
- Paragraph 33: old status taxonomy includes `OBSERVATIONALLY SELECTED CLOSURE`, `CONDITIONAL/THEOREM`, `SCOPE-BOUNDARY`, and other retired labels.
- Paragraph 155: says `R4 normalization (Paper 17): load-bearing for GTTP. [Pending verification]`. This is stale. Paper 17 v1.5 fixes `R4_FIRAS`; remove from active open problems or relabel as an imported empirical dependency.
- Paragraphs 159-164: Code and Data Availability still points to `paper21-v1.7`; update to `paper21-v2.0` after bundle release.
- Appendix paragraphs 165-647: the appendix still acts as a historical master record. Under the new rule, superseded or invalid entries should be removed rather than preserved.
- Appendix paragraphs 193-196, 316-339, 364-367, 413-426, 472-474, 491-492, 551-552, 579-580, 591-647: stale `T_obs = T_IO x^K_gauge`, `R4 = 1`, `gamma_required from FIRAS`, `a = dim(S2)/2 = 1`, and independent CMB-temperature prediction surfaces. These should be removed or rewritten to cite Paper 17 v1.5's `R4_FIRAS` theorem.

## Status-Label Noncompliance

Canonical labels currently expected by the public claim discipline:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `RECONSTRUCTION`
- `RECONSTRUCTION/RESEARCH_ONLY`
- `OPEN/PREMISE_GAP`
- `SUPERSEDED`
- `Historical/SUPERSEDED`

Observed noncanonical or retired forms in the v2.0 draft:

- `CONDITIONAL/THEOREM`: paragraphs 16, 25, 33, 149.
- `CONDITIONAL/BRIDGE THEOREM`: paragraph 130.
- `DERIVED/THEOREM under ... Scope ...`: paragraph 68 should be reviewed for `DERIVED/CONDITIONAL_VERIFIED`.
- `DERIVED/THEOREM within reduced ... class`: paragraph 121 should be reviewed for `DERIVED/CONDITIONAL_VERIFIED`.
- `CONDITIONAL/THEOREM at reduced scope`: paragraph 146 should be `DERIVED/CONDITIONAL_VERIFIED` if TIO1 is accepted and traceable; otherwise `OPEN/PREMISE_GAP`.
- Plain `DERIVED` in appendix scorecards: paragraph 413 labels the BBN scorecard `DERIVED`; it is better labeled `VERIFIED` cross-paper scorecard arithmetic, with the underlying physics claim owned by Paper 22/Paper 24.
- Appendix uses `THEOREM`, `DERIVED`, and `CONDITIONAL` without the canonical prefixes throughout paragraphs 371-647.

## Abbreviation, Slang, and Nonstandard-Term Flags

The following terms should be defined on first use or replaced with standard physics language:

- `IO`: define as Interior Observer framework at first use.
- `AC1`: expand as acoustic-ruler class membership premise or replace with a descriptive phrase.
- `BBN`: spell out Big Bang nucleosynthesis at first use.
- `CMB`: spell out cosmic microwave background at first use.
- `RT/BY`: define Regge-Teitelboim / Brown-York boundary readout if retained.
- `AH1-AH7`, `P1-P6`, `B1-B5`, `TIO1`: list the premises or move to a named premise package table.
- `CMP`, `BDP`, `GTTP`: define the principles and current status before abbreviating.
- `OS`: define Oppenheimer-Snyder interior before using OS.
- `YPCMB`, `YPBBN`, `PRyMresults()[3]`, `PRyMresults()[4]`: define as PRyMordial output components.
- `one-slot`, `A-slot`, `A-action`, `sky-slot`: IO-specific internal language; define operationally or replace with standard observable-factor language.
- `dead routes`, `hunt`, `kill shot`, `private-lab`, `theorem-grade`, `survivor`: informal or internal-pipeline language; avoid in the manuscript body.
- `P_resp`, `F_abs`, `Delta N_eff hunt`: retired internal program names; remove from active v2.0 body except in version history if necessary.

## Bundle Impact

The public v2.0 bundle was updated to match the active v2.0 scope:

- Added `scripts/01_r4_firas_dependency_audit.py`.
- Updated `scripts/07_operator_algebra_live_theorem_artifacts.py` to compute `T_obs(R4)` using `R4_FIRAS`.
- Updated validator to 16 checks.
- Retired labels removed from public script outputs.
- Historical route rerunners remain excluded.

## Recommendation

Proceed with the Paper 21 v2.0 reproducibility bundle as built. Before publishing the v2.0 manuscript, revise the draft to:

1. Replace the old status-label taxonomy in paragraph 33 with the canonical claim-discipline labels.
2. Update Code and Data Availability to `paper21-v2.0` and the new SHA256.
3. Remove the appendix historical catalog entries that are superseded or no longer valid.
4. Replace all independent cosmic microwave background temperature prediction wording with Paper 17 v1.5's FIRAS-fixed optical readout dependency.
5. Relabel reduced-scope or conditional theorem statements as `DERIVED/CONDITIONAL_VERIFIED` where they trace to P1/P2 or imported empirical physics; otherwise mark them `OPEN/PREMISE_GAP`.
