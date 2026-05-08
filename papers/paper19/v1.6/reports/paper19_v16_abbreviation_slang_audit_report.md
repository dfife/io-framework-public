# Paper 19 v1.6 Abbreviation and IO-Slang Audit

Date: May 2026

Purpose: flag terms in Paper 19 v1.5 that are likely unclear to a reader who has not read the prior Interior Observer papers. This is a manuscript-hygiene report, not a physics audit.

## High-Priority Replacements

| Term in v1.5 | Problem | Recommended v1.6 handling |
| --- | --- | --- |
| `IO` | Framework shorthand appears before reader has context. | Expand as "Interior Observer" at first use and use the full name in section openings. |
| `CMP` | Internal principle acronym. | Expand as "Conformal Modular Principle" and state current status. |
| `BDP` | Internal principle acronym. | Expand as "Baryon Dictionary Principle" and state its observable type. |
| `GTTP` | Internal theorem acronym and now R4-sensitive. | Replace with "gauge thermal transfer/readout theorem" or expand every use. |
| `Schur N-slot` | IO shorthand for a specific open curvature/radiation mode issue. | Use "Schur-complement curvature mode parameter" and define once. |
| `slot` | Nonstandard unless defined as a source component in the Hamiltonian constraint. | Replace with "sector", "source term", "observable class", or define precisely. |
| `rung` | Internal alpha-ladder metaphor. | Use "observable-class exponent" or define the alpha ladder before use. |
| `branch` | Acceptable only if defined as a model branch; otherwise vague. | Use "calculation branch" or "diagnostic branch" with status label. |
| `scorecard` | Informal. | Use "comparison table", "observable comparison", or "diagnostic table" in main text. |
| `fossil` | Informal cosmology metaphor. | Use "observable imprinted at epoch..." |
| `kill shot` | Slang. | Replace with "no-go result", "falsifying check", or "exclusion test." |
| `dead path` | Informal. | Replace with "retired route" or "no-go route." |
| `foundation punch list` | Internal project-management term. | Replace with "remaining open problems" or "closure ledger." |

## Standard Physics Acronyms That Still Need First-Use Expansion

The following are standard enough to keep after first use, but v1.6 should expand them once:

- `CMB`: cosmic microwave background.
- `BBN`: big-bang nucleosynthesis.
- `BAO`: baryon acoustic oscillations.
- `BOSS DR12`: Baryon Oscillation Spectroscopic Survey Data Release 12.
- `DESI`: Dark Energy Spectroscopic Instrument.
- `CLASS` and `CAMB`: Boltzmann solvers; name as external computational tools.
- `FIRAS`: Far Infrared Absolute Spectrophotometer; the COBE instrument supplying the blackbody temperature datum.
- `N_eff`: effective number of relativistic species.
- `P(k)`: matter power spectrum.

## Notation That Needs a Local Ledger

Paper 19 v1.6 should define these before use, even if prior papers already defined them:

- `H_IO`
- `M_red`
- `Z_g`
- `K_hat_g`
- `Q_hat`
- `M_th`
- `M_dust^geom`
- `A-vacuum`
- `K_gauge`
- `Delta`
- `sqrt(Delta)`
- `P_k`

## R4-Specific Language Rule

Do not write:

```text
IO predicts T_CMB = 2.7253 K.
T_obs = T_IO*x^K_gauge is DERIVED.
```

Use:

```text
The observed CMB temperature is the FIRAS empirical datum. Paper 17 v1.5 proves
that, within the readout family T_obs(R4)=T_IO*x^(R4*K_gauge), FIRAS fixes a
unique normalization R4_FIRAS=1.0031014644. Paper 19 propagates that frozen
observer-side thermal datum.
```

