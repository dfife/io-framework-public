# Paper 17 R4 FIRAS Uniqueness Consensus Outcome

Date: 2026-05-05

## Purpose

Record the multi-AI consensus on the revised R4 claim boundary after the
independent IO CMB-temperature prediction was retired.

## Consensus Verdict

All reviewers agree with the revised direction.

The active boundary is:

```text
IO no longer claims an independent prediction of the observed CMB temperature.
FIRAS supplies the empirical observer-side thermal datum.
Given the IO readout family, FIRAS fixes a unique R4.
```

This replaces the failed target:

```text
derive R4 = 1 internally without empirical input
```

with the theorem-grade target:

```text
prove uniqueness of R4 given FIRAS and the IO readout family.
```

## Retired Claim

Retired:

```text
IO independently predicts T_CMB = 2.7253 K with zero fitted parameters.
```

This statement should not appear as an active claim in Paper 17, overview
documents, scorecards, website tables, or downstream paper summaries.

## Active Theorem

### Theorem: Uniqueness of the FIRAS-Fixed Readout Normalization

Given:

```text
T_obs(R4) = T_IO x^(R4 K_gauge),
```

with:

```text
T_IO > 0,
T_FIRAS > 0,
x > 0,
x != 1,
K_gauge != 0,
```

there exists exactly one `R4` such that:

```text
T_FIRAS = T_IO x^(R4 K_gauge).
```

The unique solution is:

```text
R4_FIRAS = ln(T_FIRAS/T_IO) / (K_gauge ln x).
```

Proof:

Taking logarithms gives:

```text
ln(T_FIRAS/T_IO) = R4 K_gauge ln x.
```

Since `K_gauge ln x != 0`, division gives the unique solution. Injectivity of
the logarithm on positive reals gives uniqueness.

## Status Label

Primary manuscript-facing label:

```text
FIRAS-FIXED UNIQUE READOUT NORMALIZATION
```

or theorem heading:

```text
Theorem: Uniqueness of the Empirical Readout Normalization
```

Internal taxonomy:

```text
DERIVED uniqueness theorem + VERIFIED FIRAS empirical input
```

Acceptable internal dependency label:

```text
DERIVED / CONDITIONAL_VERIFIED on FIRAS empirical thermal datum
```

but avoid leading manuscript text with `CONDITIONAL_VERIFIED`, because hostile
readers may misread it as an arbitrary assumption.

## Referee-Safe Wording

Recommended wording:

```text
The observed CMB temperature is not treated here as an independent theoretical
prediction of the framework. Instead, the FIRAS measurement serves as the
empirical anchor for the observer-side thermal datum. Given the framework's
generalized readout family, T_obs(R4)=T_IO x^(R4 K_gauge), the FIRAS blackbody
temperature uniquely fixes the optical readout normalization,

R4_FIRAS = ln(T_FIRAS/T_IO)/(K_gauge ln x).

This empirical normalization is executed exactly once. Once R4_FIRAS is fixed
by the CMB temperature, it is frozen and propagated rigidly through downstream
cosmological and nucleosynthetic calculations. It is not retuned against D/H,
Y_p, Li-7, H_0, n_s, A_s, DESI, JWST timing, or any other downstream
observable.
```

## Load-Bearing Inheritance

R4 remains load-bearing.

Any downstream result using:

```text
T_obs,
T_CMB,
x^(K_gauge),
full GTTP readout
```

inherits the FIRAS-fixed R4 dependency.

Results using only the base interior Hawking scale:

```text
T_IO
```

do not inherit R4.

## Hidden-Fitting Guardrail

There is no hidden downstream fitting if this rule is enforced:

```text
R4 is fixed once by FIRAS, frozen, and never adjusted against downstream
observables.
```

Forbidden:

```text
adjust R4 against D/H, Y_p, Li-7, H_0, n_s, A_s, DESI, JWST, or any downstream
observable.
```

Required:

```text
If the empirical CMB temperature datum changes, recompute R4 by the same
formula and propagate the change through all R4-dependent calculations.
```

This is the falsifiability commitment.

## Consensus Action Items

1. Update Paper 17 claim language to remove independent CMB-temperature
   prediction status.
2. Add the FIRAS-fixed uniqueness theorem.
3. Add an R4 dependency ledger listing downstream claims that inherit R4.
4. Update framework conventions or paper status notes to include
   `FIRAS-FIXED UNIQUE READOUT NORMALIZATION` as manuscript-facing wording.
5. Update public-facing scorecards / overview language to avoid listing
   `T_CMB` as an independent IO prediction.

