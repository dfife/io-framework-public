# Paper 18 v1.6 Scripts

Run the default validator:

```bash
python3 scripts/17_validate_expected_outputs.py
```

The validator reruns the core theorem scripts and validates frozen outputs from
the optional external-data scripts.

Optional external reruns:

```bash
python3 scripts/08_legacy_observables_recalculation.py
python3 scripts/10_matter_power_shape_test.py
```

These require external data and dependencies described in
`../data/external_data_sources.md` and `../environment/external_dependencies.md`.
