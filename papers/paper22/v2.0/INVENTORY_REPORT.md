# Paper 22 v2.0 Inventory Report

## Existing Scripts Reused

The v1.6 public bundle already contained compact scripts for the live Paper 22
mathematics and scorecard values. Those scripts were retained, renumbered, and
updated for v2.0 documentation:

- spatial Hodge complex and Peter-Weyl bridge;
- transverse-traceless tensor channel floor;
- homogeneous gauge placement;
- no-go and rate-paradigm ledger;
- amplitude scorecard and comparator arithmetic;
- kappa-audit summary.

## New Script Added

`01_r4_firas_dependency_audit.py` was added for v2.0. It records the Paper 17
v1.5 thermal-readout repair and verifies that Paper 22's active scorecard does
not depend on the optical readout normalization.

## R4 / CMB Review

R4 appears in the v2.0 manuscript as inherited Paper 17 context. The active
Paper 22 BBN scorecard does not call the CMB-temperature readout. Therefore no
Paper 22 numerical scorecard values changed when `R4 = 1.0031014644` replaced
the retired `R4 = 1` convention.

The audit report flags stale manuscript language that should be removed before
v2.0 publication:

- old `T_obs = T_IO x^K_gauge` readout;
- old `T_obs = T_IO exp(K_gauge/2)` readout;
- FIRAS inversion language that reads as a `gamma_BI` prediction;
- historical/superseded appendix scorecards that are not active theorem support.

## Gaps

No live Paper 22 v2.0 number with a public-script expectation was found missing
from the bundle. The open bridge premises `GMP` and `TBS` are not back-filled by
scripts; they remain `OPEN/PREMISE_GAP` fields.

## Documentation Status

All public scripts now include reader-facing docstrings and command examples.
The bundle avoids private IO shorthand where practical, but the manuscript
itself still needs abbreviation and terminology cleanup as listed in the audit.
