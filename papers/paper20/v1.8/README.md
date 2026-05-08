# Paper 20 v1.8 Reproducibility Bundle

Classification: `verified / public-reproducibility-support`

This bundle supports Paper 20 v1.8 of the Interior Observer framework. It
documents the R4/FIRAS repair, the acoustic phase-calibration arithmetic, the
corrected BBN wrapper scorecard, the torsion-Lambda branch diagnostics, and the
radiation-sector theorem/no-go audit.

The bundle is not a mirror of the private research lab. Scratch routes and
dead-route automation are excluded unless they are necessary to audit a live
number, theorem, or no-go claim.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper20/v1.8
python3 scripts/08_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=14 pass_count=14 fail_count=0
```

The quick validator uses only Python standard-library modules and the frozen
JSON outputs included in this bundle.

## What Changed In v1.8

Paper 20 inherits the Paper 17 v1.5 R4/FIRAS correction:

```text
T_obs(R4) = T_IO * x^(R4*K_gauge)
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255 K
```

The observed CMB temperature is not counted as an independent Paper 20
prediction. FIRAS is an `IMPORTED/EMPIRICAL` observer-side thermal datum. Paper
17 v1.5 supplies the uniqueness theorem fixing R4 inside the readout family.

## Headline Reproduced Values

```text
J_theta = x^(-1/2) * sqrt(1 + gamma^2) = 0.8339461798286282

Corrected BBN wrapper row:
D/H   = 2.510410594954571e-5  (-0.5529801682 sigma)
Y_p   = 0.24781814417284279   (+0.7045360432 sigma)
Li7/H = 5.363335812718549e-10 (+12.2043090733 sigma)
chi2(D/H + Y_p) = 0.8021581025844415

Torsion-Lambda branch:
H0_obs = 61.05967054543954 km/s/Mpc
Omega_m = 0.4270807367909129
Omega_k = -0.2811609930222799
age_obs = 15.063539536645377 Gyr
```

## Claim Boundary

- `IMPORTED/EMPIRICAL`: FIRAS observer-side thermal datum.
- `DERIVED/THEOREM`: uniqueness of R4 inside the Paper 17 v1.5 readout family.
- `DERIVED/CONDITIONAL_VERIFIED`: Theorem 20.2 only if Paper 21's AC1 closure
  chain is cited explicitly.
- `OPEN/PREMISE_GAP`: Theorem 20.2 if AC1 is not routed through Paper 21, and
  the torsion-Lambda branch-selection/observational adequacy status.
- `DERIVED/NO-GO`: radiation-sector no-go results and retired DeltaN_eff target
  route.

## Full Reproduction Notes

Scripts 01-07 are documented, lightweight, and read the frozen JSON outputs.
They are intended to make the bundle legible to non-IO readers. Full
heavyweight reruns require external packages and datasets listed under
`environment/` and `data/`; those dependencies are not redistributed here.

## Citation

If you use this bundle, cite the Paper 20 v1.8 manuscript and this GitHub
release:

```text
David Fife, Paper 20 v1.8 Reproducibility Bundle,
Interior Observer Framework public reproducibility repository,
GitHub release paper20-v1.8, May 2026.
https://github.com/dfife/io-framework-public/releases/tag/paper20-v1.8
```

Machine-readable citation metadata is provided in `CITATION.cff`.
