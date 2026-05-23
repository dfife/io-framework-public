# Paper 35 external washout-selector no-go theorem

## Discipline label

- label state: `CONDITIONAL_VERIFIED`
- registry check: Vectors 1-4 reviewed. No unresolved load-bearing circularity-vector hit remains on this surface after the present audit.
- chain verification: verified through the stated external washout/source class; the remaining conditionality is exactly the surfaced external class within which the counterexample and no-go are proved.
- admitted inputs surfaced here: `ADMITTED_EXTERNAL_CLASS(standard thermal-leptogenesis washout/initial-condition class)`.
- usage rule: this theorem may be cited as a premise because it is `CONDITIONAL_VERIFIED`.
## Headline

- `verified / explicit external counterexample`: same source equations, same `K`, different admissible initial abundances, different final `kappa_f`.
- `derived / exact external no-go`: no universal washout theorem can fix `kappa_f` from source data alone in the standard thermal-leptogenesis class.
- `verified / scoped`: strong washout suppresses this ambiguity numerically, but does not erase the selector debt logically.

## Theorem 1: Initial-Condition Counterexample

- status: `verified / explicit external counterexample`
- `K = 1`
  - thermal initial `kappa_f = 5.525132041886168e-01`
  - zero initial `kappa_f = 1.377691257523194e-01`
  - `delta = 4.147440784362974e-01`
  - ratio `thermal/zero = 4.010428324717122e+00`
- `K = 3`
  - thermal initial `kappa_f = 1.737380124978479e-01`
  - zero initial `kappa_f = 1.294258877907043e-01`
  - `delta = 4.431212470714360e-02`
  - ratio `thermal/zero = 1.342374508404386e+00`
- `K = 10`
  - thermal initial `kappa_f = 3.161204281976033e-02`
  - zero initial `kappa_f = 3.159908361744947e-02`
  - `delta = 1.295920231085546e-05`
  - ratio `thermal/zero = 1.000410113232008e+00`
- `K = 30`
  - thermal initial `kappa_f = 8.221391738088722e-03`
  - zero initial `kappa_f = 8.221391737145960e-03`
  - `delta = 9.427614938717355e-13`
  - ratio `thermal/zero = 1.000000000114672e+00`
- For fixed K and fixed source equations, changing only the admissible initial heavy-neutrino abundance changes the final efficiency factor kappa_f. Therefore kappa_f is not a unique function of source data alone.

## Theorem 2: Universal Washout No-Go

- status: `derived / exact external no-go`
- A universal washout selector theorem is false in the standard thermal-leptogenesis class unless extra selectors are supplied. At minimum one must specify the initial abundance / reheating history; in the full theory one must also specify flavor regime and thermal-spectator package.
- exact missing selectors:
  - `initial heavy-neutrino abundance or reheating theorem`
  - `flavor-regime selector`
  - `thermal / spectator / scattering package selector`

## Theorem 3: Strong-Washout Boundary

- status: `verified / scoped`
- `K=10` thermal-vs-zero difference: `delta = 1.295920231085546e-05`
- `K=30` thermal-vs-zero difference: `delta = 9.427614938717355e-13`
- The same counterexample family shows that strong washout suppresses but does not logically remove the need for selectors: the initial-condition dependence becomes tiny for large K, but this is an attractor behavior, not a universal theorem of source uniqueness.

## Sources

- https://arxiv.org/abs/hep-ph/0310123
- https://arxiv.org/abs/hep-ph/0502169
- https://arxiv.org/abs/hep-ph/0601084

