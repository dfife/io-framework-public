# External Dependencies

The validation entry point only requires Python 3 from the standard library.

The full CMB reproduction scripts require external packages and data that are
not redistributed inside this repository:

- `classy`, the Python wrapper for CLASS.
- `PlanckLitePy` and the Planck 2018 lite likelihood data.
- A local CLASS/PlanckLite environment equivalent to the lab path used when the
  frozen outputs were generated.

These dependencies are external because the bundle preserves frozen numerical
outputs and scripts, not third-party likelihood data. The archived JSON/CSV/PNG
files are enough to validate the public v2.0 bundle state with
`scripts/08_validate_expected_outputs.py`.
