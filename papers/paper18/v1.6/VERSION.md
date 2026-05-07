# Paper 18 Bundle Version

Paper: 18

Bundle version: v1.6

Release tag: `paper18-v1.6`

Build date: May 2026

Primary repair:

- Replace implicit `R4 = 1` observer-side thermal readout with Paper 17 v1.5
  FIRAS-fixed `R4_FIRAS = 1.0031014644`.
- Remove independent CMB-temperature prediction status from Paper 18 support
  artifacts.
- Preserve R4-independent CMP, BDP, and `V(alpha)` theorem claims.
- Keep `N_eff = Delta` as a math-only entropy-rank theorem and withdrawn
  Friedmann-radiation physical identification.

Immutable release policy:

Once tagged as `paper18-v1.6`, this bundle should not be retagged. Any
post-release correction should be made as `paper18-v1.7`.
