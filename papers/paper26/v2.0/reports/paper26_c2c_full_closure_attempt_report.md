# Paper 26 C2c Full-Closure Attempt

Date: 2026-05-16

## Executive Verdict

Full C2c closure does not go through.

The external mathematical-physics literature gives a stronger partial theorem
than the internal Paper 1--25 stack alone: on a static spacetime with a
bifurcate Killing horizon, wedge reflection, and a regular quasifree Hadamard
state, the Kay--Wald / Sewell / Hartle-Hawking-Israel machinery forces
Hawking-temperature KMS behavior on the relevant exterior wedge algebra. That is
a real state-selection theorem under its hypotheses.

Those hypotheses are not the Paper 26 geometry. Paper 26 works with a closed
`K=+1` Oppenheimer-Snyder interior and a boundary carrier reduced to the
`S^2 ell=1` coexact shell. The Oppenheimer-Snyder interior is dynamical, not a
stationary spacetime with a global bifurcate Killing horizon. In addition, the
standard black-hole KMS theorems thermalize with respect to the horizon Killing
flow / Killing frequency. They do not by themselves select a thermal ensemble
over the angular `S^2` coexact Laplacian with one-particle Hamiltonian
`h = hbar c sqrt(Delta_{S^2,coex})`.

Therefore C2c reduces to a sharper single missing theorem:

> IO horizon coexact state-selection theorem: the scalar bridge source algebra
> on the Paper 26 Lemma C2.2 `S^2 ell=1` coexact carrier is the restriction of
> the regular Hartle-Hawking/KMS horizon state, and its physical one-particle
> Hamiltonian is `hbar c sqrt(Delta_{S^2,coex})`.

That theorem is not supplied by standard Kay--Wald, Sewell, Tomita--Takesaki, or
Bisognano--Wichmann results without adding an equilibrium/bifurcate-horizon
identification and an angular-Hamiltonian identification. C2c remains
`OPEN/PREMISE_GAP` on the bare stack. The fixed-carrier covariance theorem
remains `DERIVED/THEOREM`.

## External Theorem Audit

### Hawking 1975

Hawking's original result supplies the Schwarzschild black-hole temperature:
black holes emit thermally with temperature proportional to surface gravity,
`T = hbar kappa/(2 pi k_B)`. For Schwarzschild,
`kappa = c^2/(2 r_s)`, hence `T_H = hbar c/(4 pi k_B r_s)`.

This is a valid imported standard-physics input. It fixes the temperature, not
the Paper 26 state-selection map from that temperature to an angular coexact
boundary covariance.

Status contribution: `IMPORTED/EMPIRICAL` standard physics for `T_H`.

### Sewell 1982

Sewell proves a generalized Hawking-Unruh/KMS result for fields on manifolds
with event-horizon boundaries, using a Bisognano-Wichmann-type argument. This
supports the claim that a regular horizon-restricted field state can have KMS
thermal behavior.

It does not prove C2c by itself, because it does not identify the Paper 26
`S^2 ell=1` coexact bridge carrier as the horizon field algebra, nor does it
replace the horizon Killing-flow frequency by the angular coexact Laplacian
frequency.

Status contribution: supports Hawking/KMS behavior under regular horizon
conditions; does not close C2c.

### Kay--Wald 1991

Kay and Wald consider quasifree states of a linear scalar field on globally
hyperbolic spacetimes with a one-parameter isometry and a bifurcate Killing
horizon. Under stationarity, vanishing one-point function, and Hadamard
nonsingularity near the horizon, they prove uniqueness on a large horizon
subalgebra; with wedge reflection, the state restricts to a KMS state at the
Hawking temperature in the exterior wedge. They also note that existence can
fail in some black-hole spacetimes.

This is the closest external theorem. It would close the Hartle-Hawking/KMS
state selection if Paper 26's setting satisfied the hypotheses and if the
Paper 26 coexact carrier were a subalgebra of the Kay--Wald horizon algebra.
But Paper 26's Oppenheimer-Snyder interior is not stationary and does not
provide the full bifurcate Killing-horizon structure required by the theorem.
Using the maximally extended static Schwarzschild/Kruskal geometry instead
would import an equilibrium eternal-horizon extension not contained in P1+P2 as
used by Paper 26.

Status contribution: conditional closure on a different equilibrium geometry;
not a closure of C2c on the Paper 26 geometry.

### Hartle-Hawking-Israel construction results

Modern constructions such as Sanders 2015 and Gerard 2018 prove existence /
Hadamard properties of Hartle-Hawking-Israel states on static or stationary
bifurcate-Killing-horizon spacetimes, complementing Kay--Wald uniqueness.

These results strengthen the static-equilibrium route but keep the same
hypothesis boundary: static or stationary bifurcate horizon, appropriate wedge
reflection or related analytic structure, and a free field class. They do not
turn the Oppenheimer-Snyder interior into a stationary bifurcate-horizon
spacetime.

Status contribution: validates the equilibrium Hartle-Hawking route when its
hypotheses are met; does not prove they are met here.

### Tomita--Takesaki / Bisognano--Wichmann

Tomita--Takesaki modular theory gives a modular flow for a von Neumann algebra
and a faithful normal state. Bisognano--Wichmann identifies modular flow with
geometric boost flow for wedge algebras in relativistic quantum field theory.
Sewell and Kay--Wald are black-hole-horizon analogues of this logic.

The obstruction is the same: modular theory identifies the flow after the
state/algebra pair is supplied. It does not by itself select the physical state
on the Paper 26 coexact bridge carrier. A claim that Tomita--Takesaki alone
selects C2c would be a hidden state-selection premise.

Status contribution: supports KMS uniqueness once state and algebra are fixed;
does not close state selection.

### General curved-spacetime state-selection no-go boundary

Hollands--Wald and Fewster--Verch emphasize a basic fact of curved-spacetime
quantum field theory: one should not assume a preferred state in a general
globally hyperbolic spacetime. Fewster--Verch further give a model-independent
no-go against a covariant preferred-state choice in all spacetimes for
dynamically local theories under typical assumptions.

This does not forbid special states in special stationary spacetimes. It does
rule out the move "P1+P2+QFT in curved spacetime automatically selects a unique
state" as a general theorem.

Status contribution: supports the obstacle report.

## Theorem-Grade Partial Result

### Theorem 26.C2c.KW (Equilibrium-Horizon Conditional Closure)

Let `(M,g)` be a static or stationary spacetime with a nonextremal bifurcate
Killing horizon, a horizon Killing field `xi`, surface gravity `kappa`, and the
reflection/analytic structure required by the Kay--Wald / Hartle-Hawking-Israel
theorems. Let `A_H` be a horizon-localized bosonic field algebra whose
restriction to the Paper 26 coexact carrier is a gauge-invariant quasifree CCR
subalgebra. Assume the state is quasifree, invariant under the Killing flow,
has vanishing one-point function, and is Hadamard/nonsingular in a neighborhood
of the horizon.

Then the restriction of that state to the exterior wedge algebra is KMS at
inverse Hawking temperature

```text
beta_H = 2 pi / kappa.
```

If the Paper 26 coexact carrier Hamiltonian is additionally

```text
h_coex = hbar c sqrt(Delta_{S^2,coex}),
```

then on the `ell=1` coexact shell of `S^2(r_s)`,

```text
lambda_1 = 2/r_s^2,
omega_1 = c sqrt(lambda_1) = sqrt(2)c/r_s,
beta_H hbar omega_1 = 4 pi sqrt(2),
G_H^(1)|_{ell=1} = [exp(4 pi sqrt(2)) - 1]^-1 I.
```

Proof. The first paragraph is Kay--Wald/Sewell/Hartle-Hawking-Israel under the
listed equilibrium-horizon hypotheses. For Schwarzschild, `kappa=c^2/(2r_s)`,
so `beta_H=4 pi r_s/(hbar c)` after restoring units. The coexact `S^2` spectral
calculation is standard Hodge theory: `lambda_1=2/r_s^2`. The massless
one-particle energy assignment gives `hbar omega_1 = hbar c sqrt(lambda_1)`.
Substitution gives `4 pi sqrt(2)`. CCR/KMS quasifree uniqueness then gives the
Bose covariance.

Chain: P1 only if P1 is strengthened to an equilibrium/static bifurcate
Schwarzschild horizon; P2; Hawking 1975; Sewell 1982; Kay--Wald 1991; Sanders
2015 / Gerard 2018 for existence of Hartle-Hawking-Israel states under static or
stationary hypotheses; standard Hodge spectrum on `S^2`; standard bosonic CCR
KMS uniqueness.

Status: `DERIVED/THEOREM` under equilibrium-horizon and coexact-Hamiltonian
hypotheses. Not an unconditional closure of Paper 26 C2c.

## Why This Does Not Fully Close C2c

### Obstacle 1: Oppenheimer-Snyder interior is not Kay--Wald geometry

Paper 26 is explicitly in the closed `K=+1` Oppenheimer-Snyder interior branch.
That interior is a dynamical Friedmann-type region. It does not supply a global
stationary Killing flow whose orbits define the Kay--Wald state-selection
problem, nor does it supply the past/future pair of null horizons intersecting
on a bifurcation two-sphere used by the Hartle-Hawking-Israel construction.

The exterior Schwarzschild solution has a Killing horizon. The maximally
extended Kruskal solution has a bifurcate Killing horizon. A collapse/OS
spacetime does not generally have the full bifurcate horizon; it has a future
event horizon and a physically different vacuum choice, usually the Unruh
state, for collapse radiation.

Therefore importing Kay--Wald as a direct C2c closure silently imports an
eternal-equilibrium horizon not supplied by the stated Paper 26 geometry.

### Obstacle 2: standard Hawking thermality is frequency thermality, not angular-mode thermality

Hawking/KMS theorems thermalize with respect to the horizon Killing flow. The
thermal label is the Killing frequency. Angular momentum labels are degeneracy
and scattering/greybody labels in the usual black-hole mode expansion; they are
not automatically energies `hbar c sqrt(ell(ell+1))/r_s`.

Paper 26 C2c needs the stronger statement that the physical boundary source is
a compact `S^2` coexact oscillator with Hamiltonian
`hbar c sqrt(Delta_{S^2,coex})`. That is not the Kay--Wald or Sewell theorem.
It is an additional horizon coexact dynamics theorem.

### Obstacle 3: Tomita--Takesaki is state-relative

Tomita--Takesaki modular flow is determined by a chosen algebra/state pair.
It cannot choose the physical state without already being given a state or a
state-selection criterion. Using it as a C2c closure without a separate
selection theorem would hide the premise.

### Obstacle 4: H1/H2 do not fully close from external QFT

H2 can be strengthened: once the physical perturbation sector is specified as a
linear coexact bosonic field on the compact spatial slice, the minimal CCR lift
is standard canonical quantization. But this does not prove that this is the
physical sector for every Paper 26 scalar source; Paper 26 Lemma C2.2 already
does the carrier work needed for C2c.

H1 remains the real issue. Standard QFT can construct and sometimes uniquely
characterize a Hartle-Hawking-Israel state under stationary bifurcate-horizon
hypotheses. It does not prove that the Paper 26 OS-interior scalar bridge source
must be that state.

## A_s Forward Check

Using only the forward Paper 26 body formula:

```text
gamma_BI = 0.2375
Q = 1 + gamma_BI^2 = 1.05640625
f_K = gamma_BI^2 / Q = 0.053394468273923974
beta_H hbar omega_1 = 4 pi sqrt(2) = 17.771531752633464
g_H = [exp(4 pi sqrt(2)) - 1]^-1 = 1.9139114172056972e-08
canonical source = g_H / sqrt(2) = 1.353339741696504e-08
A_s = (25/9) f_K g_H/sqrt(2)
    = 2.0072459972737347e-09
```

Against the Planck reference `A_s = 2.100e-9 +/- 0.030e-9`, this is
`-4.4168572726793066%`, or `-3.0918000908755148 sigma`.

The reproducible check is banked at:

```text
/opt/cosmology-lab/tmp/io-framework-public/papers/paper26/v2.0/scripts/c2c_analysis/01_c2c_as_forward_check.py
```

Generated output:

```text
/opt/cosmology-lab/tmp/io-framework-public/papers/paper26/v2.0/results/c2c_analysis/c2c_as_forward_check_results.json
```

Manuscript hygiene note: the extracted Paper 26 v2.0 appendix Step 387 contains
an expression proportional to `[2/(exp(4*pi*sqrt(2))-1)]^2`. That expression
does not reproduce `2.007e-9`. The active body formula is the single-occupation
formula above. If the squared expression remains in the manuscript, it should be
corrected or removed.

## Final Classification

Deeper partial closure, not full closure.

- `G_H^(1)|_{ell=1} = [exp(4 pi sqrt(2))-1]^-1 I` on the selected
  fixed-carrier Hawking/KMS state class: `DERIVED/THEOREM`.
- Kay--Wald/Sewell/Hartle-Hawking-Israel state selection on a static
  bifurcate-horizon equilibrium spacetime: `IMPORTED/EMPIRICAL` standard
  physics plus `DERIVED/THEOREM` under those hypotheses.
- Application of that state-selection theorem to the Paper 26
  Oppenheimer-Snyder interior and to the angular `S^2` coexact Hamiltonian:
  not proved.
- C2c on the actual Paper 26 stack: remains `OPEN/PREMISE_GAP`.
- `A_s = 2.0072459972737347e-9`: remains `DERIVED/CONDITIONAL_VERIFIED` only
  if C1 and the C2c physical-state-selection package are admitted; otherwise it
  is a forward conditional calculation, not a closed prediction.

Proof incomplete for full C2c closure -- gap: an IO-specific horizon coexact
state-selection theorem connecting the OS-interior boundary carrier to the
regular Hartle-Hawking/KMS horizon state with Hamiltonian
`hbar c sqrt(Delta_{S^2,coex})`.
