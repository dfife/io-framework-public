# External Data Sources

The public Paper 25 v2.0 validation path does not fetch or redistribute
external observational data files. It uses the IO Framework observational
denominators frozen in `data/imported_constants.json` and cited from:

- IO Framework Observational Conventions v1:
  https://dfife.github.io/data/observational_conventions_v1.md

PRyMordial is not redistributed. The PRyMordial output rows used by Paper 25
are frozen as JSON values with provenance to the local Paper 25 correction
audit and the Paper 24 v3.0 public bundle.

The active BBN scorecard imports the Paper 24 v3.0 Pastore `Q_GS` / Henderson
primary lithium branch:

- Pastore et al. (2013), Phys. Rev. C 87, 035503, Table II,
  doi:10.1103/PhysRevC.87.035503.
- Henderson et al. (2019), Phys. Rev. C 99, 064320,
  doi:10.1103/PhysRevC.99.064320.

External observational denominators used by the conventions document:

- D/H: Cooke et al. primordial deuterium convention.
- Y_p: helium mass-fraction convention used by the IO sweep.
- Li-7/H: Spite-plateau lithium convention used by the IO sweep.

R4/FIRAS is not an active data dependency for Paper 25 v2.0 scripts. The value
`R4_FIRAS = 1.0031014644` is recorded only as framework-state metadata.

If a future bundle reruns PRyMordial directly, it should document the
PRyMordial repository/version and any nuclear-data files separately rather than
vendoring PRyMordial into this repository.
