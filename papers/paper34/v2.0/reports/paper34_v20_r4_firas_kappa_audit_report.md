# Paper 34 v2.0 R4/FIRAS repair and kappa-style impact audit

Status: verified / structural-audit / v2.0 bundle support

Date: 2026-05-06

Target: Paper 34 Hubble observable-class formula

```text
H_ext(alpha,n) = H0_active * f_Gamma^(1-alpha) * x^((n/2)*K_gauge)
```

## Executive conclusion

No R4 damage was found in the Paper 34 Hubble calculation scripts.

The Paper 17 v1.5 repair changes the optical thermal readout normalization from the retired implicit value `R4 = 1` to the FIRAS-fixed value

```text
R4_FIRAS = 1.0031014644105183.
```

That repair does not change Paper 34's Hubble scorecard because Paper 34 does not use the optical thermal readout law

```text
T_obs(R4) = T_IO * x^(R4*K_gauge).
```

Paper 34 uses a different carrier:

```text
x^((n/2)*K_gauge),
```

which is the stellar-photometric half-leg payload in the H0 observable-class ladder. Inserting `R4` into that exponent would be a new error, not a correction.

The only v1.1 damage found was wording hygiene: the Planck row used the phrase `geometric CMB readout`, which could be misread as a CMB-temperature prediction. In v2.0 this was replaced with:

```text
projected-observer H0 baseline / Planck CMB-inferred H0 class; no optical R4 thermal-readout dependence
```

## What changed in v2.0

The v2.0 public bundle:

- keeps all Paper 34 H0 predictions unchanged;
- records `R4_FIRAS` as a framework constant for cross-paper provenance;
- adds `04_r4_firas_impact_audit.py`;
- renumbers the validator to `05_validate_expected_outputs.py`;
- adds an explicit rejected-counterfactual check showing what would happen if `R4` were wrongly inserted into the photometric exponent;
- removes the ambiguous Planck `geometric CMB readout` wording from the bundled JSON outputs.

## R4-use inventory

| Surface | Uses R4? | v2.0 action |
|---|---:|---|
| `01_compute_hext_grid.py` | No | Added claim-boundary note and `x_half_leg` consistency check. |
| `02_compare_to_published_measurements.py` | No | Clarified Planck CMB row as H0 method class, not CMB-temperature prediction. |
| `03_run_anti_fit_check.py` | No | Added `R4_times_K_gauge` only as rejected counterfactual payload. |
| `04_r4_firas_impact_audit.py` | Audit only | New script proving no Paper 34 scorecard dependency on R4. |
| `05_validate_expected_outputs.py` | Validation only | Validates unchanged H0 outputs and no active R4 dependency. |
| `data/imported_constants.json` | Provenance only | Records `R4_FIRAS` and the non-dependency boundary. |
| `results/*.json` | Provenance/audit only | No active H0 row changes. |

No active Paper 34 script computes or reports `T_obs`, `T_CMB`, FIRAS temperature, or an IO CMB-temperature prediction.

## Numerical impact

The v2.0 scorecard is unchanged from v1.1:

| Method | alpha | n | H_ext | Residual |
|---|---:|---:|---:|---:|
| Planck CMB class | 1 | 0 | 67.575856535826 | +0.351713 sigma |
| GW sirens | 1 | 0 | 67.575856535826 | -0.566864 sigma |
| TRGB direct | 3/2 | 1 | 70.256778814438 | -0.068671 sigma |
| TDCOSMO | 2 | 0 | 71.387557193550 | -0.059012 sigma |
| SH0ES | 2 | 2 | 73.044060740302 | +0.044061 sigma |
| TRGB+SN | 2 | 2 | 73.044060740302 | -0.154476 sigma |

The six-method maximum residual remains:

```text
max |sigma| = 0.5668642595545683.
```

## Rejected counterfactual

The v2.0 audit script intentionally computes the rejected diagnostic:

```text
H_wrong(alpha,n) = H0_active * f_Gamma^(1-alpha) * x^((n/2)*R4_FIRAS*K_gauge).
```

This is not the active Paper 34 formula. It is included only to prove that applying the Paper 17 R4 repair to the wrong carrier would change the H0 grid artificially.

The maximum counterfactual H0 shift over the Paper 34 grid is:

```text
0.005196923130114328 km/s/Mpc.
```

That small size does not make the substitution acceptable. The substitution is structurally wrong because `R4` normalizes the optical thermal readout, while `n/2` counts uncancelled stellar-photometric calibrator legs in the Hubble observable-class ladder.

## Kappa-style field audit

### Candidate 1: optical `R4`

Candidate field: replace the thermal readout normalization by `rho` in

```text
T_obs(rho) = T_IO * x^(rho*K_gauge).
```

Rigidity result: Paper 17 v1.5 fixes `rho = R4_FIRAS` from FIRAS in the optical thermal readout family. This is load-bearing for GTTP thermal readouts but not part of Paper 34's H0 formula.

Classification: `DERIVED uniqueness theorem + VERIFIED FIRAS empirical input` in Paper 17; `not used` in Paper 34 H_ext.

Hidden-parameter verdict: no Paper 34 hidden parameter.

### Candidate 2: photometric payload `K_gauge`

Candidate field: replace `K_gauge` by `k` in

```text
x^((n/2)*k).
```

Rigidity result: unchanged from the Paper 34 v1.1 audit. Within the stellar-photometric extension, the centered boundary/KMS action on the photometric log-frequency carrier uses `K_gauge`. The payload is scoped to that extension package, not fitted to the H0 measurements.

Classification: `DERIVED/SCOPED` within the stellar-photometric extension.

Hidden-parameter verdict: no new R4 issue.

### Candidate 3: leg count `n/2`

Candidate field: replace `n/2` by a continuous coefficient.

Rigidity result: unchanged from the Paper 34 v1.1 audit. `n` is a discrete count of uncancelled photometric calibrator legs. The factor `1/2` is the luminosity-to-distance half-leg relation. It is not the optical thermal `R4` normalization.

Classification: `DERIVED/SCOPED` within the leg-counting extension.

Hidden-parameter verdict: no new R4 issue.

### Candidate 4: Planck CMB row

Candidate field: treat the Planck row as a CMB-temperature prediction.

Rigidity result: rejected. The Paper 34 Planck row is an H0 method-class comparison against Planck's CMB-inferred H0 value. It does not compute the observed CMB temperature.

Classification: `DERIVED/SCOPED` baseline H0 class; not a CMB-temperature claim.

Hidden-parameter verdict: wording hygiene only.

## CMB-temperature claim removal

The active Paper 34 bundle contains no CMB-temperature prediction. The only occurrence of `CMB` is the method name `Planck CMB`, which is retained because it identifies the external H0 measurement class.

Future manuscript wording should avoid:

```text
geometric CMB readout
CMB readout prediction
IO predicts the CMB temperature
```

Use instead:

```text
Planck CMB-inferred H0 class
projected-observer H0 baseline
no optical R4 thermal-readout dependence
```

## Final verdict

Paper 34 v2.0 does not require a numerical Hubble-scorecard update from the R4/FIRAS repair.

The correct repair is documentation and reproducibility hygiene:

```text
No R4 in H_ext.
No CMB-temperature prediction in Paper 34.
Planck CMB row is an H0 method-class row.
All six H0 residuals remain unchanged.
```
