# Paper 26 `tau` Routes A/B/C Audit

Date: 2026-03-28

## Scope

Audit three candidate late-time damping routes using the current Paper 26
conditional scalar amplitude

`A_s = 2.0072459972737343e-9`

derived on the angular-Hawking branch.

Candidate routes:

1. Route A: `tau = f_K = gamma^2 / (1 + gamma^2)`
2. Route B: inverse-operator / propagator route from the tangential
   Ashtekar-Barbero quadratic operator
3. Route C: optical-reduction semigroup / visibility theorem

## Live constants

With `gamma = 0.2375`:

`Q := 1 + gamma^2 = 1.05640625`

`K_gauge = ln(Q) = 0.05487281774291466`

`f_K = gamma^2 / (1 + gamma^2) = 0.053394468273923974`

`exp(-K_gauge) = 1 / Q = 0.9466055317260761`

`exp(-2 K_gauge) = 1 / Q^2 = 0.8960620326944071`

TT-only effective-amplitude ridges already on file:

- `A_eff^(TT,1) = 1.97808e-9`
- `A_eff^(TT,2) = 1.97963e-9`

## Route A. `tau = f_K`

### Standard-physics reading

Optical depth is a mean scattering probability / integrated interaction number.
So one can test whether the relevant IO late-time parameter is not the modular
log-weight `K_gauge`, but the gauge-active fraction already isolated by the
Rosetta partition:

`tau_eff = f_K`.

Then standard exponential survival gives

`A_eff = A_s exp(-2 f_K)`.

### Exact number

`A_eff^(A) = 2.0072459972737343e-9 * exp(-2 * 0.053394468273923974)`

`A_eff^(A) = 1.8039427667673209e-9`.

Comparison:

- versus `1.97808e-9`: `-8.803346337492869%`
- versus `1.97963e-9`: `-8.87475100057481%`

### Double-counting status

`f_K` already appears at the source stage in the conditional `A_s` derivation,
because the bridge reads the extrinsic `K` channel only.

That does **not** automatically kill Route A. The same scalar may enter two
different observable classes at two different stages:

- source-selection fraction at the primordial bridge stage,
- late visibility/scattering probability at the readout stage.

But this requires a separate theorem identifying the late-time attenuation class
with the same `f_K`. No such theorem exists yet.

### Status

- `verified`: numerical consequence is fixed.
- `reconstruction`: physically coherent, no theorem-grade observable-class
  identification yet.

## Route B. Inverse-Operator / Propagator Route

### Operator datum already present

The current stack does support the reduced tangential quadratic identity

`A_tan^T A_tan = (1 + gamma^2) I / r_s^2`

from the Paper 9 / Paper 16 tangential operator package.

At the determinant / free-energy level this is exactly the origin of

`K_gauge = ln(1 + gamma^2)`.

### Critical standard-physics point

For a Gaussian field with quadratic action

`S[phi] = (1/2) <phi, O phi>`,

the two-point function is

`<phi phi> = O^(-1)`,

that is, **one inverse operator**, not one inverse factor per field leg.

So if one conditionally identifies the observed CMB covariance with the
propagator of the gauge-dressed tangential operator, then

`O_A = Q O_Gamma`

would imply

`<delta A delta A>_A = Q^(-1) <delta A delta A>_Gamma = exp(-K_gauge) <...>`.

That corresponds to

`exp(-2 tau_eff) = exp(-K_gauge)`

and therefore

`tau_eff = K_gauge / 2`.

### Exact number

`A_eff^(B,std) = A_s exp(-K_gauge)`

`A_eff^(B,std) = 1.900070164554341e-9`.

Comparison:

- versus `1.97808e-9`: `-3.94371488744939%`
- versus `1.97963e-9`: `-4.018924518503919%`

### What Route B does NOT derive

The often-suggested per-leg argument

`[(1 + gamma^2)^(-1)]^2 = exp(-2 K_gauge)`

is **not** the standard Gaussian propagator rule by itself. It would require an
additional theorem that the observed field is first mapped by a separate inverse
one-slot readout operator on each leg before the covariance is formed.

No such theorem is currently in the stack.

### Theorem status

- `conditional`: the reduced tangential quadratic scaling by `Q = 1 + gamma^2`
  is supported by the Paper 9 / 16 operator package.
- `not derived`: the observed CMB field has not been proved to be the
  propagator of that operator.
- `killed as standard Gaussian proof of tau = K_gauge`: standard Gaussian field
  theory gives `tau = K_gauge / 2`, not `K_gauge`.

## Route C. Optical-Reduction Semigroup

### Proposed structure

Build a positive contraction semigroup on the observed sky field

`R_opt(s) = exp(-s L_opt)`

and prove that on the central gauge line

`L_opt = K_hat_g`.

Then each field leg gets `exp(-K_gauge)` and the power gets

`exp(-2 K_gauge)`.

### Existing support

Papers 17-21 already provide:

- an observer/readout stage,
- an optical reduced class,
- an A-vacuum / modular gauge scalar `K_hat_g`,
- and a reduction/filtration architecture.

### What is missing

The stack does **not** yet provide:

- the explicit optical reduction semigroup,
- the generator `L_opt`,
- or a theorem identifying `L_opt` with `K_hat_g`.

So Route C currently gives no numeric prediction beyond the previously tested
candidate

`A_eff = A_s exp(-2 K_gauge) = 1.7986169284348148e-9`

which remains only `reconstruction`.

### Status

- `reconstruction`: strongest remaining theorem target.
- `not yet constructible` from existing theorems alone.

## Verdict

### Best current numbers

- Route A (`tau = f_K`): `A_eff = 1.8039427667673209e-9`
- Route B (standard Gaussian inverse operator): `A_eff = 1.900070164554341e-9`
- Route C (`tau = K_gauge` semigroup/readout reconstruction):
  `A_eff = 1.7986169284348148e-9`

### Strongest legal statuses

- Route A: numerically viable, theorem missing
- Route B: standard physics does **not** give `tau = K_gauge`; it gives at most
  `tau = K_gauge/2`
- Route C: best remaining theorem target, but still open

### Immediate frontier

The operator route sharpens the problem:

- if one wants `tau = K_gauge` from operator inversion, one needs a **second**
  inverse/readout insertion theorem beyond the standard Gaussian propagator.
- if one wants a direct late-time number from existing framework data, `f_K`
  is the cleaner surviving candidate than `K_gauge`.
