# External Dependencies

The Paper 34 v2.0 public scripts require only Python 3 and the standard
library.

No external numerical package, cosmology solver, or private lab database is
required.

The bundle references published H0 measurements in
`data/imported_constants.json`. Those measurements are imported comparison
values only. They are not fit by the scripts.

The bundle also records the Paper 17 v1.5 FIRAS-fixed `R4_FIRAS` value for
provenance. No FIRAS data product is redistributed or required to run the Paper
34 H0 scripts, because Paper 34 does not compute the observed CMB temperature.
