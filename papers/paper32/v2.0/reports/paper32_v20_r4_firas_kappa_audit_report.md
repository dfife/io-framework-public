# Paper 32 v2.0 R4/FIRAS Kappa-Style Audit and Damage Report

Date: 2026-05-06

Status: `verified / kappa-style structural audit / manuscript-impact report`

## Executive Verdict

Paper 32 v1.5 contains real R4 damage in its temperature-readout language.
The damaged claim is narrow:

- `T_obs = T_IO * x^K_gauge = 2.7253 K` must not be presented as an
  independent CMB-temperature prediction.
- Paper 32 Theorem 32.KB.7 must not be read as deriving Paper 17 optical
  thermal `R4`.
- `R4/P4 normalization` must be split into two different objects.

The repair is:

- `P4` source-block fixed-point normalization remains `DERIVED/CONDITIONAL_VERIFIED` by
  Paper 32 KB7 on the active reduced scalar source block.
- Optical thermal `R4` is not derived by Paper 32. It is fixed by Paper 17
  v1.5's FIRAS uniqueness theorem:

```text
T_obs(R4) = T_IO * x^(R4*K_gauge)
R4_FIRAS = ln(T_FIRAS/T_IO) / (K_gauge * ln x)
         = 1.0031014644105183
```

The observed CMB temperature is therefore a FIRAS-normalized readout datum, not
an IO prediction. Once fixed, `R4_FIRAS` is frozen and cannot be retuned against
BBN, Hubble, DESI, JWST, `n_s`, `A_s`, or any other downstream observable.

No Paper 32 core closure number changes under this repair. Recollapse,
`x_crit`, the 111/222 Gyr timescale arithmetic, KB7 source-block validation,
`n_s`, `A_s`, and universal-GMP characterization do not numerically depend on
optical `R4`.

## Numerical Repair

Constants:

```text
gamma_BI = 0.2375
x = 1.519
K_gauge = ln(1 + gamma_BI^2) = 0.05487281774291466
ln x = 0.41805222361363575
T_IO = 2.6635 K
T_FIRAS = 2.7255 K
sigma(T_FIRAS) = 0.0006 K
```

Derived FIRAS-fixed readout:

```text
K_gauge * ln x = 0.022939703473371237
R4_FIRAS = 1.0031014644105183
sigma_R4(FIRAS only) = 0.009596597151571828
R4_FIRAS * K_gauge = 0.05504300383424916
T_obs(R4_FIRAS) = 2.7255 K
```

Historical diagnostic:

```text
T_obs(R4=1) = T_IO * x^K_gauge = 2.725306096638128 K
T_obs(R4=1) - T_FIRAS = -0.00019390336187186108 K
offset = -0.32317226978643515 sigma(FIRAS)
```

This near agreement is not a prediction. It is now only a diagnostic showing
that the original unit-readout assumption landed close to FIRAS.

## Kappa-Style Field-Redefinition Audit

The audit replaces each relevant normalization by a candidate free field and
asks whether Paper 32 or later accepted theorem-grade work forces the original
value.

| Candidate field | Rigidity test | Classification | v2.0 handling |
|---|---|---|---|
| `R4` optical thermal readout coefficient | Replace `R4` by arbitrary positive real `kappa_R4` in `T_obs = T_IO*x^(kappa_R4*K_gauge)`. The modular/gauge stack remains algebraically consistent for a continuous family. Paper 32 KB7 does not constrain this optical coefficient. | `FIRAS-FIXED / CONDITIONAL_VERIFIED on FIRAS empirical thermal datum` | Set `R4 = 1.0031014644105183`; do not call CMB an independent prediction. |
| `P4` source-block fixed-point normalization | Replace active-source character `Z(s)=s^(K_gauge/x)` by an arbitrary character. KB7/P4 source-class lock and alpha-class repair force `Z(e^x)=Q` only on the active reduced scalar source block. | `DERIVED/CONDITIONAL_VERIFIED` | Keep Paper 32 KB7 result; explicitly say it is not optical `R4`. |
| `K_gauge` payload | Replace `K_gauge=ln(1+gamma_BI^2)` by another modular scalar. Gauge-side determinant and Ashtekar-Barbero bridge fix `Q=1+gamma_BI^2`; logarithm fixes `K_gauge`. | `DERIVED/CONDITIONAL_VERIFIED` | Unchanged. |
| `T_IO` interior thermal scale | Replace `T_IO=2.6635 K` by arbitrary scale. In the Paper 1/Paper 32 branch this is the interior Hawking-scale input used by the readout family. | `DERIVED/CONDITIONAL_VERIFIED within branch` | Unchanged. |
| Observed CMB temperature | Treat as predicted output instead of empirical input. This creates circularity once `R4` is FIRAS-fixed. | `VERIFIED empirical datum` | Remove prediction language. |
| `n_s = 1 - K_gauge/x` | Insert optical `R4` into the scalar-source exponent. The derivation uses source-block `K_gauge/x`, not optical thermal readout. | `DERIVED/CONDITIONAL_VERIFIED` | Unchanged; no R4 dependence. |
| `A_s` Hawking boundary-state amplitude | Insert optical `R4` into the lowest-shell amplitude. Formula uses the Hawking boundary state and `gamma_BI`; no optical temperature normalization. | `DERIVED/CONDITIONAL_VERIFIED` | Unchanged. |
| `x_crit = Q^(-1/4)` | Insert optical `R4` into the Delta boundary identity. The identity uses `Delta=x^4 Q`; no temperature readout. | `DERIVED/CONDITIONAL_VERIFIED` | Unchanged. |
| Recollapse and 111/222 Gyr cycle arithmetic | Insert optical `R4` into OS acceleration/time equations. Equations use `r_s`, `c`, and bounce/restart packages; no temperature readout. | `DERIVED` / `DERIVED/CONDITIONAL_VERIFIED` | Unchanged. |

## Script Review

| Script | R4 impact | v2.0 action |
|---|---|---|
| `01_compute_framework_constants.py` | Damaged in v1.5: computed `T_obs=T_IO*x^K_gauge` as active observed CMB value. | Repaired. Now computes `R4_FIRAS`, `T_obs(R4_FIRAS)`, and historical `T_obs(R4=1)` diagnostic. |
| `02_recollapse_acceleration.py` | None. | No numerical change. |
| `03_x_crit_identity.py` | None. | No numerical change. |
| `04_recollapse_cycle_timescales.py` | None. | No numerical change. |
| `05_kb7_source_block_validation.py` | Wording boundary only. | Updated docstring and gate text to say KB7 closes P4 source-block only, not optical R4. |
| `06_n_s_derivation_chain.py` | None. | No numerical change. |
| `07_a_s_derivation_chain.py` | None. | No numerical change. |
| `08_universal_gmp_classification.py` | None. | No numerical change. |
| `09_r4_firas_impact_audit.py` | New. | Added to freeze this damage ledger. |
| `10_validate_expected_outputs.py` | Expected-value change. | Validator now checks `R4_FIRAS`, `T_obs(R4_FIRAS)`, and the R4 impact audit. |

## Manuscript Damage Locations

The following locations were identified in the extracted Paper 32 v1.5 text.
These are manuscript-edit targets for v2.0. The current task does not edit the
DOCX.

| Paragraph | Damage | Required v2.0 handling |
|---|---|---|
| 305 | Says the derivation already produced zero-free-parameter predictions for `T_CMB`. | Retire independent `T_CMB` prediction wording. Say `T_IO` is derived and observed CMB is FIRAS-normalized through Paper 17 v1.5. |
| 350 | States `T_obs = T_IO*x^K_gauge = 2.7253 K`. | Replace with `T_obs(R4)=T_IO*x^(R4*K_gauge)` and `R4_FIRAS=1.0031014644105183`. |
| 442 | Code/Data section points to v1.5 bundle and unqualified `T_obs` reproduction. | Update to v2.0 bundle/hash and describe `T_obs` as FIRAS-fixed readout. |
| 446 | Open Problems list merges `R4/P4 normalization` and marks it closed by KB7. | Split: `P4` source-block closure is closed by KB7; optical `R4` is FIRAS-fixed by Paper 17 v1.5 and not closed by KB7. |
| 703 | States `T_obs = T_IO*exp(K_gauge/2) = T_IO*sqrt(1+gamma^2) = 2.7253 K`. | Retire as erroneous/historical. Use Paper 17 v1.5 readout family. |
| 704 | Temperature Transfer Theorem says structural pieces force `T_obs = T_IO*x^K_gauge`. | Reframe as forcing the readout family and gauge payload; R4 fixed separately by FIRAS. |
| 713, 715, 791 | Use `ln(T_obs/T_IO)=K_gauge*ln x` or equivalent. | Replace with `ln(T_obs/T_IO)=R4*K_gauge*ln x`. |
| 717 | Treats `gamma_BI` prediction from FIRAS inversion as `DERIVED`. | Reframe as consistency diagnostic, not a derivation of `gamma_BI` from FIRAS. |
| 764, 765, 766 | `R1-R4` / one-e-fold normalization wording implies optical R4 is forced by modular stack. | Separate R1-R3/gauge payload from FIRAS-fixed optical R4. |

## Impact on Paper 32 Core Claims

Unaffected:

- `Rddot = -c^2 r_s/(2R^2)` and local clamp value
  `Rddot(r_s) = -6.722177851434687e-11 m/s^2`.
- `x_crit = Q^(-1/4) = 0.9863754613328337`.
- `Delta tau_recollapse = 110.9932628887098 Gyr`.
- `Delta tau_cycle = 221.9865257774196 Gyr`, with the same conditional
  bounce/restart scope.
- KB7/P4 source-block validation: `Z(e^x)=Q`.
- `n_s = 0.963875696021781`.
- `A_s = 2.0072459972737347e-9`.
- Universal-GMP characterization.

Changed:

- CMB-temperature status only. The observed CMB temperature is no longer an
  independent prediction. It is a FIRAS-fixed normalization datum.
- The bundle URL and hash must update from v1.5 to v2.0.
- Any phrase "R4/P4 closed" must be split into optical `R4` and source-block
  `P4`.

## Final Classification

No new hidden fitted parameter is introduced by v2.0 if the discipline is
enforced:

1. FIRAS fixes `R4` once.
2. `R4` is frozen globally.
3. `R4` is not retuned against any downstream observable.
4. The CMB temperature is not counted as an independent IO prediction.

The v1.5 damage was not that the recollapse, scalar-index, scalar-amplitude, or
KB7 calculations were numerically wrong. The damage was overclaim language:
Paper 32 compressed `R4` and `P4` into one normalization line and carried the
retired CMB-prediction wording forward. Paper 32 v2.0 must repair that
distinction explicitly.
