# Paper 31 v2.0 Scripts

This directory contains the public reproducibility scripts selected for Paper 31
v2.0. The computational scripts are copied from the active lab run directory and
preserve their original absolute lab paths in comments and output settings so
that provenance remains auditable.

The scripts that call `classy` and `PlanckLitePy` require an external CLASS /
PlanckLite environment. The public validator,
`08_validate_expected_outputs.py`, does not rerun those expensive external
calculations; it validates the frozen JSON outputs committed in `../results/`.

Use:

```bash
cd papers/paper31/v2.0
python3 scripts/08_validate_expected_outputs.py
```

The validator is the supported quick reproducibility entry point for archive
integrity. Re-running the full PlanckLite/CLASS scripts is an optional extended
check documented in `../environment/external_dependencies.md`.
