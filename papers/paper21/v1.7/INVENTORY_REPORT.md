# Paper 21 v1.7 Inventory Report

Status: `verified / bundle-scope-inventory`

## Existing Local Script Inventory

The private Paper 21 folder contains 27 Python scripts. They fall into three
groups:

1. Live theorem/number support scripts suitable for the public bundle.
2. Historical `P_resp` no-go route scripts that remain manuscript provenance but
   are not rerun publicly under the v1.7 inclusion rule.
3. Exploratory support scripts whose theorem labels or intermediate route
   numbers are not live public bundle targets.

## Included

The public bundle includes distilled scripts for:

- `L_1 = 0.22416889162576648`
- `L_2 = 0.13805247907094412`
- `J_theta = 0.8339461798286282`
- YPCMB / `PRyMresults()[3]` wrapper convention
- corrected BBN scorecard pulls and chi-square
- live operator-algebra theorem artifacts

## Excluded

The following private route families are intentionally excluded from the
runnable public bundle:

- assembly-gap radiation reruns,
- stiff `a^-8` reruns,
- local expansion variance reruns,
- local interaction dressing reruns,
- nonseparable weak-sector reruns,
- chemical-potential / UV-tail / sterile-depletion reruns,
- broad `P_resp` exploratory route scans.

Reason: the PI inclusion rule says no-go demonstrations stay in the manuscript;
the bundle does not rerun dead routes to re-prove they are dead.

## Gap Assessment

No live Paper 21 v1.6/v1.7 number identified in the bundle scope lacks script
support.

The only boundary is PRyMordial: this bundle validates frozen PRyMordial output
values and wrapper convention but does not redistribute or reimplement
PRyMordial.
