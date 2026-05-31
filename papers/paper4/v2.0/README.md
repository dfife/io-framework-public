# Paper 4 v2.0 Reproducibility Bundle

This bundle supports the Paper 4 v2.0 storytelling rebuild:

`Evidence for a Black Hole Interior - Four Horizon Connections, the Light-Element Abundances, and Early-Galaxy Timing`

It recomputes the Paper 4-specific active-branch quantities and freezes inherited
outputs from the upstream bundles that Paper 4 reports rather than rederives.

## Validate

```bash
python scripts/04_validate_expected_outputs.py
```

Expected result:

```text
SUMMARY total_checks=27 pass_count=27 fail_count=0
```

## Scope

This bundle validates:

- four horizon-connection constants and dark-energy bridge numbers;
- projected optical-age table at `z = 6, 10, 14, 20`;
- Paper 35 active dark-energy/flat-CPL curvature signature values;
- Paper 28 homogeneous OS JWST formation-clock values;
- Paper 32 `sigma_8` and `S_8` values;
- Paper 24 v3.0 BBN scorecard values reported by Paper 4;
- Paper 20 v2.0 acoustic-scale tension value reported by Paper 4.

The bundle does not rerun PRyMordial, CLASS, DESI likelihood scripts, or the
Paper 28 full theorem suite. It uses frozen upstream public-bundle outputs for
those inherited results.
