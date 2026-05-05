# Paper 17 R4 Impossibility Theorem

## Result

- status: `derived`
- theorem: Within the Paper 17 reduced thermal-plus-gauge construction, if one removes R4 and keeps only the derived operator data plus the geometric conformal coordinate λ, then the bridge from λ to modular time is underdetermined by a constant c. Consequently c = 1 cannot be derived from the current premise package.

## Assumptions

- A1. Paper 17 fixes the reduced physical modular flow on each gauge fiber as exp(i t κ D).
- A2. On the physical Schwarzschild tangential sector, κ = K_gauge = ln(1+γ^2).
- A3. The conformal depth λ = ln(r/R_U) is a continuous additive coordinate on the radial line.
- A4. The physical thermal transfer must be read out by a continuous additive embedding ι: λ -> t(λ) into the modular flow parameter.
- A5. No extra normalization premise equivalent to R4 is supplied.

## Proof

- Because λ is additive and t(λ) must compose additively under concatenation, t: (R,+) -> (R,+) is a continuous group homomorphism.
- Every continuous endomorphism of (R,+) has the form t(λ) = c λ for some real constant c.
- Substituting into the derived fiber modular flow gives α_λ = Ad(exp(i c λ κ D)).
- On the physical sector κ = K_gauge, so d(ln ω)/dλ = c K_gauge and therefore σ = c K_gauge.
- For every c, the resulting λ-parameterized transfer remains Planck-preserving, additive in λ, gauge-central, and γ -> 0 decoupling.
- Hence the non-R4 premise package admits a continuum of admissible completions.
- A theorem selecting c = 1 from that premise package would contradict existence of the family c != 1 with the same premises.
- Therefore c = 1 is underivable from the current package; equivalently, R4 is irreducible on the current foundation.

## Explicit c-Family

| c | sigma = c K_gauge | T_obs = T_IO x^(sigma) |
|---:|---:|---:|
| `0.5` | `0.02743640887145733` | `2.6942252068932158` |
| `0.8` | `0.04389825419433173` | `2.712830199335826` |
| `1.0` | `0.05487281774291466` | `2.7253048490553007` |
| `1.2` | `0.06584738129149759` | `2.7378368620722138` |

Each row above preserves every non-R4 ingredient of the Paper 17 construction. The only changed object is the bridge embedding `t = c λ`.

## Corollary

Any future derivation of R4 must add new structure that destroys the c-family, e.g. a theorem identifying the radial geometric action with the modular action at unit normalization.

## Boundary

- Half-sided modular inclusion / BW theorems can fix normalization in settings where a geometric one-parameter symmetry is proved to be the modular group. No such IO radial net theorem exists yet.
- Paper 17 itself introduces R4 as a premise and Paper 18 Step 62 proves independent channel rescaling can preserve all other local consistency checks while changing λ-calibration.

## Final Claim Discipline

- `derived`: R4 cannot be derived from the current Paper 17 package without adding new structure.
- `derived`: the headline target is impossible on the present foundation.
- `open`: a future BW/Wiesbrock-style radial modular theorem could change this, but that would be a new theorem, not a consequence of the current stack.
