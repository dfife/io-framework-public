# Paper 1 v4.0 Theorem Memo: Finite Horizon-Readable Quotient

Date: 2026-05-24

Target paper: Paper 1 v4.1 §2.11

Purpose: provide a framework-level theorem for the Paper 1 rebuild establishing that physically distinguishable IO claims must pass through finite horizon-readable boundary data. This is the general foundation later used by finite-grid class-screen programs such as baryogenesis, dark-sector mechanism exclusion, CMB state-selection, and boundary-to-bulk observable classification.

Status label: `DERIVED/CONDITIONAL_VERIFIED`

Cosmo audit: approved. Bank as IO core principle `IO.CORE.FHRQ.1`.

Reason for conditional label: the proof is derived from `P1` and `P2` plus standard imported black-hole entropy/holographic-bound physics. The finite-quotient statement is theorem-grade inside IO once those standard imports are admitted. It is not a claim that all mathematical Hilbert spaces are finite-dimensional.

## Manuscript-Ready Theorem

### Theorem 1.X — Finite Horizon-Readable Quotient

Under Premise 1, the observable universe is the interior of a Schwarzschild black hole. Its boundary is therefore a finite-area horizon,
\[
A_H = 4\pi r_s^2.
\]
Under Premise 2, standard black-hole thermodynamics applies to that horizon. The horizon carries Bekenstein-Hawking entropy
\[
S_H = \frac{k_B A_H}{4\ell_P^2},
\]
so the number of mutually distinguishable horizon-readable information states is bounded by
\[
N_{\rm read} \le \exp(S_H/k_B).
\]

Therefore, within the Interior Observer framework, physically distinct interior explanations are not distinguished by arbitrary continuum microstructure. They are distinguished only by the finite horizon-readable data that survive the IO boundary/readout quotient. If two interior constructions induce the same horizon-readable typed data, IO treats them as the same physical explanation for observable purposes.

Equivalently, for any IO observable class \(\mathcal O\), the physically relevant mechanism space is the quotient
\[
\mathcal M_{\mathcal O}^{\rm IO,read}
=
\mathcal M_{\mathcal O}^{\rm admissible}/\!\sim_{\rm read},
\]
where
\[
M_1 \sim_{\rm read} M_2
\quad\Longleftrightarrow\quad
T_{\rm IO}^{\mathcal O}(M_1)
=
T_{\rm IO}^{\mathcal O}(M_2).
\]
The quotient is bounded by the finite horizon-readable information capacity:
\[
|\mathcal M_{\mathcal O}^{\rm IO,read}|
\le
\exp(S_H/k_B).
\]

This is the finite-quotient rule of the framework. Infinite model-building freedom in flat-space quantum field theory does not by itself create infinitely many IO-distinct physical explanations. It creates new IO-distinct explanations only when it changes the finite boundary-readable data.

Status: `DERIVED/CONDITIONAL_VERIFIED` from `P1`, `P2`, Bekenstein-Hawking entropy, holographic entropy bounds, and the IO boundary/readout architecture.

## Proof

### Step 1 — P1 Gives A Finite Horizon

Premise 1 states that the observable universe exists inside a Schwarzschild black hole. A Schwarzschild horizon has radius \(r_s\) and area
\[
A_H = 4\pi r_s^2.
\]
For the IO universe \(r_s\) is finite. Therefore the framework boundary is a finite-area \(S^2\) horizon, not an infinite flat-space boundary.

### Step 2 — P2 Imports Standard Horizon Entropy

Premise 2 states that physics inside the horizon is the same physics that operates outside. Standard black-hole thermodynamics assigns a Schwarzschild horizon the Bekenstein-Hawking entropy
\[
S_H = \frac{k_B A_H}{4\ell_P^2}.
\]
The entropy is finite whenever \(A_H\) is finite. The entropy bound means the horizon cannot encode an unlimited number of mutually distinguishable physical states. The maximum number of distinguishable horizon-readable states is bounded by
\[
N_{\rm read} \le \exp(S_H/k_B).
\]
This number is enormous for a universe-scale black hole, but it is finite.

### Step 3 — IO Observables Are Readout Classes, Not Raw Microstate Labels

The IO framework never observes arbitrary microscopic labels directly. Observables are readout classes: interior physics is projected through the horizon/boundary architecture into quantities that an interior observer can measure.

Define the readout map for an observable class \(\mathcal O\):
\[
T_{\rm IO}^{\mathcal O}:
\mathcal M_{\mathcal O}^{\rm admissible}
\rightarrow
\mathcal H_{\rm read}^{\mathcal O}.
\]
Here \(\mathcal M_{\mathcal O}^{\rm admissible}\) is the class of candidate mechanisms relevant to observable \(\mathcal O\), and \(\mathcal H_{\rm read}^{\mathcal O}\) is the horizon-readable data sector for that observable.

Two mechanisms are IO-equivalent if they induce the same readout:
\[
M_1 \sim_{\rm read} M_2
\quad\Longleftrightarrow\quad
T_{\rm IO}^{\mathcal O}(M_1)
=
T_{\rm IO}^{\mathcal O}(M_2).
\]
This is not a convenience definition. It is the framework's physical equivalence relation: if no boundary-readable datum changes, no IO observable changes.

### Step 4 — The Readout Image Is Entropy-Bounded

The readout image is a subset of the horizon-readable information sector:
\[
\operatorname{im} T_{\rm IO}^{\mathcal O}
\subseteq
\mathcal H_{\rm read}^{\mathcal O}.
\]
The total number of mutually distinguishable horizon-readable states is bounded by \(\exp(S_H/k_B)\). Therefore
\[
|\operatorname{im} T_{\rm IO}^{\mathcal O}|
\le
\exp(S_H/k_B).
\]
But the quotient \(\mathcal M_{\mathcal O}^{\rm IO,read}\) is isomorphic to the image of the readout map:
\[
\mathcal M_{\mathcal O}^{\rm IO,read}
\cong
\operatorname{im}T_{\rm IO}^{\mathcal O}.
\]
Thus
\[
|\mathcal M_{\mathcal O}^{\rm IO,read}|
\le
\exp(S_H/k_B)
<\infty.
\]
So the physically distinguishable IO mechanism space is finite after the horizon-readable quotient.

### Step 5 — The Lower Boundary Is Quantized Horizon Readout

The upper boundary is the finite entropy cap. The lower boundary is that a difference must be physically readable. In the loop/isolated-horizon construction used to fix \(\gamma_{\rm BI}\), the horizon degrees of freedom are quantized and represented by puncture/Chern-Simons boundary data. Therefore an admissible IO distinction is not an arbitrary continuum label; it must survive as a distinguishable boundary-readable datum after gauge, diffeomorphism, and non-readable redundancies are quotient out.

This gives the theorem its operational content: IO searches finite readout classes, not all formal ways of writing a microscopic model.

## Scope Boundary

This theorem does not say:

- that every mathematical Hilbert space in quantum theory is finite-dimensional;
- that continuum QFT is invalid as a calculational language;
- that all possible BSM Lagrangians have been enumerated;
- that a specific mechanism, such as baryogenesis, has already been selected;
- that entropy counting alone fixes amplitudes, couplings, signs, or rates.

It says:

- the IO boundary has finite entropy;
- physically distinguishable IO claims must change boundary-readable data;
- infinitely many microscopic presentations collapse to one IO class if they induce the same readout;
- finite-grid elimination is legitimate only after passing to this finite readout quotient.

## Dependency Chain

Theorem 1.X Finite Horizon-Readable Quotient

<- `P1`: the observable universe exists inside a Schwarzschild black hole

<- Schwarzschild geometry: finite horizon area \(A_H = 4\pi r_s^2\)

<- `P2`: physics inside the horizon is the same physics that operates outside

<- `IMPORTED/EMPIRICAL/STANDARD`: Bekenstein-Hawking black-hole entropy \(S_H = k_B A_H/(4\ell_P^2)\)

<- `IMPORTED/STANDARD`: holographic/covariant entropy-bound principle for finite-area horizons

<- `IMPORTED/STANDARD_QG`: quantized isolated-horizon readout structure in the Ashtekar-Baez-Corichi-Krasnov horizon construction used to fix \(\gamma_{\rm BI}\)

<- IO observable/readout discipline: interior mechanisms are physically distinguished only by their boundary-readable typed data

<- quotient definition \(M_1\sim_{\rm read}M_2\) iff their IO readout images agree

-> finite IO-readable mechanism quotient for any observable class

## External Source Citations

Use these references in Paper 1's bibliography if not already present:

1. Bekenstein, J. D. (1973). "Black Holes and Entropy." *Physical Review D* 7, 2333-2346. DOI: `10.1103/PhysRevD.7.2333`.
2. Hawking, S. W. (1975). "Particle Creation by Black Holes." *Communications in Mathematical Physics* 43, 199-220.
3. Bousso, R. (2002). "The Holographic Principle." *Reviews of Modern Physics* 74, 825-874. DOI: `10.1103/RevModPhys.74.825`.
4. Ashtekar, A., Baez, J., Corichi, A., and Krasnov, K. (1998). "Quantum Geometry and Black Hole Entropy." *Physical Review Letters* 80, 904-907. DOI: `10.1103/PhysRevLett.80.904`.

## Recommended Placement In Paper 1

Best location: Section 2, after the finite total mass / bounded geometry consequences and before later-paper forward references.

Suggested subsection title:

`2.x Finite Horizon-Readable Quotient`

This placement makes the theorem a framework rule before Paper 1 discusses downstream observables.

## Manuscript-Ready Explanatory Paragraph

The framework also has a finite information boundary. This matters because it prevents the usual infinite-flat-space objection from entering IO unchanged. In ordinary model-building one can always write another hidden field, another EFT operator, another microscopic presentation. But an interior observer does not measure arbitrary microscopic presentations. The observer measures the finite horizon-readable data that survive the boundary projection. The Schwarzschild horizon has finite area, and by the Bekenstein-Hawking entropy law it has finite information capacity. Therefore IO treats two constructions as physically distinct only if they induce different boundary-readable data. Infinite formal microphysics collapses to a finite readout quotient. This is why later class-screen arguments can work like elimination problems: not because all mathematical possibilities are finite, but because IO-visible physical distinctions are finite after the horizon-readable quotient.

## Downstream Uses

This theorem should be cited whenever a later paper uses finite-grid or Sudoku-style elimination:

- baryogenesis mechanism class-screening;
- dark-sector carrier no-go arguments;
- CMB state-selection residual classification;
- boundary-to-bulk observable class audits;
- no-hidden-fit audits where infinite BSM freedom is not allowed to count as physical freedom unless it changes an IO-readable datum.

## Conservative Audit Note

The theorem is strongest if written as a finite **readout quotient** theorem, not as "the full physical Hilbert space is finite." Existing IO work still uses infinite-dimensional Hilbert spaces, continuous fields, and operator algebras as calculational structures. The finite claim attaches to physically distinguishable IO-readable data, not to every auxiliary mathematical representation.
