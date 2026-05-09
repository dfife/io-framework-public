# Paper 21 v2.0 Inventory Report

Status: `VERIFIED / bundle-scope-inventory`

## Existing Local Script Inventory

The private Paper 21 folder contains many Python scripts from the original
AC1, puncture-load, and radiation-response investigations. Under the v2.0 scope
reduction, those scripts fall into three groups:

1. Live theorem/number support scripts suitable for the public bundle.
2. Retired radiation-response or `P_resp` route scripts that no longer support
   active v2.0 claims.
3. Exploratory support scripts whose theorem labels or intermediate route
   numbers are not live public bundle targets.

## Included

The public v2.0 bundle includes distilled scripts for:

- `R4_FIRAS = 1.0031014644` inheritance from Paper 17 v1.5 and the statement
  that R4 does not enter the active Paper 21 Big Bang nucleosynthesis scorecard.
- `L_1 = 0.22416889162576648`
- `L_2 = 0.13805247907094412`
- `J_theta = 0.8339461798286282`
- YPCMB / `PRyMresults()[3]` wrapper convention
- corrected Big Bang nucleosynthesis scorecard pulls and chi-square
- live operator-algebra theorem artifacts

## Excluded

The following private route families are intentionally excluded from the
runnable public bundle:

- assembly-gap radiation reruns,
- stiff `a^-8` reruns,
- local expansion variance reruns,
- local interaction dressing reruns,
- nonseparable weak-sector reruns,
- chemical-potential / ultraviolet-tail / sterile-depletion reruns,
- broad `P_resp` exploratory route scans,
- the old `F_abs / Delta N_eff` response-map program.

Reason: the Paper 21 v2.0 manuscript is scope-reduced. The appendix is not a
historical record; superseded or invalid routes should not be re-presented as
active support.

## Gap Assessment

No active Paper 21 v2.0 number identified in the bundle scope lacks script
support.

The two boundaries are:

- PRyMordial is external. This bundle validates frozen output values and wrapper
  convention but does not redistribute or reimplement PRyMordial.
- The Paper 22/Paper 25 rate-dressing bridge is external to Paper 21. Paper 21
  derives `L_1` and `L_2`; downstream delivery into weak and nuclear rate
  dressing is not claimed by this bundle.
