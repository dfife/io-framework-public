# Paper 20 v1.8 Abbreviation and IO-Slang Audit

Source reviewed: `Interior_Observer_Paper20_v1_7.docx`

Purpose: flag terms that should be expanded or rewritten for a reader who has
not read the previous IO papers.

## High-Priority Expansion Required

- `IO`: expand as "Interior Observer" on first use in the abstract/body and
  avoid using it as a noun where "the framework" is clearer.
- `GTTP`: replace or expand as "geometric temperature-transfer principle" only
  when historically needed; active CMB-temperature prediction language is
  retired.
- `CMP`: expand as "Conformal Modular Principle" on first use.
- `BDP`: expand as "Baryon Dictionary Principle" on first use.
- `H_IO`: replace with "Interior Observer Hilbert/operator algebra" or define
  before use.
- `M_red`, `Z_g`, `M_big`: define as operator algebras before use.
- `CCR`, `CAR`, `KMS`: standard to mathematical physics, but still expand on
  first use for cross-disciplinary readers.
- `OS`, `FRW`: standard but should be expanded on first use as
  Oppenheimer-Snyder and Friedmann-Robertson-Walker.
- `BBN`, `CMB`, `BAO`, `BOSS`: standard cosmology abbreviations, but expand on
  first use.
- `AC1`, `AH1-AH7`, `P1-P6`, `B1-B5`, `RT/BY`: define locally or cite the exact
  theorem package. Do not assume the reader knows the IO shorthand.

## IO-Specific Terms To Rewrite

- `slot`: replace with "sector", "term", "contribution", or "operator
  component" depending on context.
- `rung`: replace with "observable class", "exponent level", or "classification
  level".
- `branch`: acceptable in cosmology if defined, but avoid unexplained IO branch
  shorthand.
- `scorecard`: replace with "comparison table" or "observational comparison"
  in manuscript prose.
- `kill`, `kill shot`, `dead route`: replace with "excluded", "ruled out", or
  "no-go result".
- `fossil`: replace with "historical artifact" or "retired computation".
- `Rosetta`: use only as a title/proper-name reference; otherwise define the
  mathematical object directly.

## Manuscript Locations Flagged

- Paragraph 14: "IO framework" in the abstract should expand first use.
- Paragraphs 15, 24, 83, 99, 111, 116, 609: `H_IO`, reduced algebra, and
  operator shorthand need first-use definitions.
- Paragraphs 17, 34, 37, 40: `AC1`, `AH1-AH7`, `P1-P6`, `RT/BY`, and `B1-B5`
  need local definitions or an explicit upstream theorem-package citation.
- Paragraphs 24, 47-50, 67, 78, 83, 87-89, 92-107: dense abbreviation blocks
  should be rewritten as standard physics prose.
- Paragraphs 121, 145-155, 215, 233, 248, 250, 272, 278: master-reference table
  abbreviations require a legend.
- Appendix Steps 31-41, 76-82, 84-96, 97-118: inherited shorthand should be
  either expanded or clearly marked as inherited appendix notation.
- Appendix A.6: "universal transport", "BDP alpha-ladder", and "GTTP
  significance" need standard-terminology replacements in v1.8.

## Recommendation

Paper 20 v1.8 should add a short notation paragraph near the start and should
not use IO shorthand in theorem statements unless the term is expanded in the
same paragraph. The most important readability fix is to remove active
temperature-prediction language before doing abbreviation cleanup; otherwise the
abbreviation cleanup can preserve a stale claim.
