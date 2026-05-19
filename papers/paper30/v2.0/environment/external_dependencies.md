# External Dependencies

The bundle does not redistribute large third-party likelihood files. The validation script fetches the public Pantheon+SH0ES data products from the official PantheonPlusSH0ES GitHub DataRelease repository when they are not already cached under `data/external_cache/`.

Fetched files:

- `Pantheon+SH0ES.dat`
- `Pantheon+SH0ES_STAT+SYS.cov`

Other external inputs are represented by frozen upstream JSON outputs from Paper 29 v2.0 and frozen Paper 30 legacy-context JSON files used only for comparison columns in the recomputation report.
