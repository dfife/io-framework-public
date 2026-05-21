# Paper 31 v2.0 Reproducibility Bundle

The Paper 31 v2.0 public bundle is available at:

- Reproducibility directory:
  `papers/paper31/v2.0/`
- Release tag expected by the manuscript:
  `paper31-v2.0`
- Release asset filename:
  `paper31-v2.0.tar.gz`
- SHA256:
  `52381e0abe3fcfb2a3087b403ef569ef733b8976ccefaffa5f0db934ad2fe454`

Current validation entry point:

```bash
cd papers/paper31/v2.0
python3 scripts/08_validate_expected_outputs.py
```

Expected output:

```text
Paper 31 v2.0 validation passed: 62/62 checks
```

Scope note: this bundle archives the active Paper 31 v2.0 numerical and
theorem-support artifacts, including the pre-Zenodo manuscript reconciliation
audit. The chronometer + DESI `chi2 = 42.48` cross-paper value is exposed for
traceability, but the available upstream source labels it as legacy
Schur-context material rather than as an active-branch reproducer.
