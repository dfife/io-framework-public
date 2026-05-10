# External Data and Code Sources

This Paper 22 v2.0 bundle does not redistribute external observational
datasets or PRyMordial.

## IO Framework Conventions

- URL: https://dfife.github.io/data/conventions_v2.md
- Use: observational denominators, labeling conventions, and versioning conventions.
- Redistributed: no; values are recorded in `data/imported_constants.json`.

## FIRAS CMB Temperature

- Source: COBE/FIRAS blackbody temperature measurement as imported by Paper 17 v1.5.
- Use: fixes the observer-side optical readout normalization `R4_FIRAS`.
- Redistributed: no; the scalar value and uncertainty used by the framework are
  recorded in `data/imported_constants.json`.

## PRyMordial

- Source: separate PRyMordial repository / local checkout used in the private lab.
- Use: original BBN abundance rows for the v1.4/v1.5/v2.0 correction sweep.
- Redistributed: no.
- Public bundle treatment: corrected output rows are frozen in
  `data/imported_constants.json`; scripts validate arithmetic and wrapper
  conventions but do not ship PRyMordial.

## Zenodo Manuscript

- Paper 22 DOI: https://doi.org/10.5281/zenodo.19198706
- Use: associated manuscript citation.
- Redistributed: no.
