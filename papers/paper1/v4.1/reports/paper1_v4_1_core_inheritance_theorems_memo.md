# Paper 1 v4.1 Core Inheritance Theorems Memo

Date: 2026-05-24  
Purpose: Full theorem memo for the compact Paper 1 inheritance principles to be added after the existing structural-consequence section without turning Paper 1 into a theorem dump.

## Executive Placement Recommendation

Paper 1 should not insert five long theorem sections into the body. The manuscript should add a compact "Core Inheritance Rules for Later Papers" table, while this memo supplies the full theorem statements and dependency chains for the audit trail.

The six proposed additions covered by the complete registry package are:

| Working label | Title | Status |
|---|---|---|
| Theorem 1.Y | Total Energy / Density Accounting Separation | `DERIVED/THEOREM` |
| Theorem 1.Z | Closed \(K=+1\) Interior Geometry | `DERIVED/THEOREM` |
| Theorem 1.W | Horizon-Contained Dynamics / No Asymptotic-Infinity Readout | `DERIVED/THEOREM` |
| Theorem 1.V | Typed Observable / No Cross-Class Substitution | `DERIVED/CONDITIONAL_VERIFIED` |
| Theorem 1.U | Native Closed-\(S^3\) Spatial Mode Reduction Principle | `DERIVED/THEOREM` |
| Theorem 1.T | Schwarzschild Parent Neutrality | `DERIVED/THEOREM` |

Theorem 1.Y has its own registry memo at `results/paper1/paper1_v4_1_theorem_1Y_registry_memo.md` because it appears as a full manuscript theorem in Paper 1 v4.1 §2.12. Theorems 1.Z and 1.W are already present in Paper 1 v4.0 in prose. Theorems 1.V, 1.U, and 1.T are the genuinely new explicit inheritance rules.

### Post-Cosmo Terminology Guardrail

Cosmo approved the closed-space reduction package on the explicit condition that it not be cited as a standalone universal "closed curve space" theorem. The approved reduction chain is Theorem 1.Z plus Theorem 1.U, guarded by Theorem 1.V.

The approved statement is:

> The primitive IO spatial geometry is closed \(K=+1\), with compact \(S^3\) spatial slices. Therefore native global IO spatial modes are compact \(S^3\) modes with discrete spectrum. Flat-space continuum \(k\)-modes and curve-space approximations are valid only as local, large-mode, observational, or dictionary limits after the relevant map is stated.

This package does not prove that all local physics must be computed on full \(S^3\) without tangent-space approximations; it does not invalidate continuum quantum field theory; it does not reduce every curve/path-integral object by Theorem 1.U; and it does not allow closed-\(S^3\) mode reduction to move automatically across typed observable classes.

---

## Theorem 1.Z - Closed \(K=+1\) Interior Geometry

### Statement

Under P1, the observable universe exists inside a Schwarzschild black hole produced by gravitational collapse. Under P2, the interior collapse/expansion geometry is governed by standard general relativity. For the homogeneous dust interior used by the IO framework, the relevant standard solution is the Oppenheimer-Snyder interior, whose spatial slices are closed \(K=+1\) Friedmann-Robertson-Walker slices with topology \(S^3\).

Therefore the native IO geometric chassis is closed \(K=+1\), not flat \(K=0\), and later calculations must use closed-space geometry unless they explicitly prove a local or asymptotic approximation.

### Status

`DERIVED/THEOREM` within the IO homogeneous Oppenheimer-Snyder interior chassis.

### Proof

P1 identifies the observable universe with the interior of a Schwarzschild black hole. P2 imports the standard GR treatment of a homogeneous pressureless collapse interior. The Oppenheimer-Snyder construction matches a closed FRW dust interior to an exterior Schwarzschild solution across a spherical boundary. The interior metric can be written

\[
ds^2=-c^2d\tau^2+a(\tau)^2\left(d\chi^2+\sin^2\chi\,d\Omega_2^2\right),
\]

which has positive spatial curvature and \(S^3\) spatial sections. This is exactly the geometry Paper 1 v4.0 §2.1 states as the framework chassis, and Paper 32 v2.0 later uses as the closed support geometry.

Thus the primitive IO geometry is \(K=+1\) closed \(S^3\). Flat-space tools may still be used as controlled approximations, but they are not primitive IO geometry. QED.

### Dependency Chain

Theorem 1.Z (Closed \(K=+1\) Interior Geometry)

<- P1: observable universe exists inside a Schwarzschild black hole  
<- P2: physics inside the horizon follows standard GR dynamics  
<- `IMPORTED/STANDARD`: Oppenheimer-Snyder collapse, Schwarzschild exterior matched to closed FRW dust interior  
<- Paper 1 v4.0 §2.1: closed \(K=+1\) spatial geometry stated as the framework chassis  
-> Native IO spatial geometry is closed \(S^3\), not infinite flat space

### What It Does Not Cover

This theorem does not assert that every local calculation must retain global curvature terms at all scales. Local tangent-space and high-\(n\) approximations remain valid when explicitly justified. This theorem fixes the background chassis. It does not exclude perturbations, local anisotropies, inhomogeneous matter distributions, or non-dust microphysics inside that chassis.

---

## Theorem 1.W - Horizon-Contained Dynamics / No Asymptotic-Infinity Readout

### Statement

Under P1, the interior observer lives inside a Schwarzschild event horizon. Standard Schwarzschild causal structure implies that no future-directed causal signal from the interior reaches exterior asymptotic infinity. IO observables may not be treated as operationally measured at exterior asymptotic infinity. Asymptotic-infinity or S-matrix constructions may be used as imported mathematical tools only after a theorem or explicit approximation maps them to horizon-readable, local, or interior-readable data.

The horizon is the physical containment boundary for IO dynamics.

### Status

`DERIVED/THEOREM`.

### Proof

P1 places the observable universe inside a Schwarzschild black hole. In the Schwarzschild spacetime, the event horizon is the boundary of the causal past of future null infinity. Once a worldline is inside the horizon, every future-directed causal curve remains inside the black-hole region and cannot reach exterior future null infinity.

An interior observer therefore has no operational access to exterior asymptotic-infinity readout. A calculation that uses exterior \(r\to\infty\) normalization, scattering data, or asymptotic flat boundary conditions may still be used as imported mathematics under P2, but it is not automatically an IO observable. To become an IO observable, it must be mapped to horizon-readable, local, or interior-readable data through a theorem or explicit approximation.

Paper 1 v4.0 §2.6-§2.7 already uses this principle physically: the formation-event energy cannot escape, the first-cycle boundary state is horizon-contained, and the future is bounded by the horizon/Hawking structure. This theorem states the general rule explicitly. QED.

### Dependency Chain

Theorem 1.W (Horizon-Contained Dynamics / No Asymptotic-Infinity Readout)

<- P1: observable universe exists inside a Schwarzschild black hole  
<- P2: standard Schwarzschild causal structure applies  
<- `IMPORTED/STANDARD`: event horizon as boundary of causal access to future null infinity  
<- Paper 1 v4.0 §2.6-§2.7: horizon containment of formation-event energy and bounded future  
-> Interior IO observables require horizon/interior readout, not exterior asymptotic-infinity readout

### What It Does Not Cover

This theorem does not deny that the mathematical exterior Schwarzschild solution has an asymptotic region. It says that exterior asymptotic infinity is not an operational readout surface for interior observers. Asymptotic-infinity or S-matrix constructions may be used as imported mathematical tools only after a theorem or explicit approximation maps them to horizon-readable, local, or interior-readable data.

---

## Theorem 1.V - Typed Observable / No Cross-Class Substitution

### Statement

In the IO framework, an observable is not just a scalar number; it is a typed readout object defined by a carrier, a physical process, and a readout map. If two observables belong to different typed classes, a factor, Jacobian, state, temperature, density slot, or transfer operator derived for one class may not be substituted into the other class unless a theorem supplies an explicit class map, intertwiner, or natural transformation between the two readouts.

Equivalently: no cross-class substitution is valid by notation alone.

### Status

`DERIVED/CONDITIONAL_VERIFIED` on the typed observable architecture banked in Papers 19, 21, 32, 33, and 35.

This is not a universal claim about all mathematical representations of physics. It is a framework rule for IO calculations once the relevant observable classes are typed.

### Proof

Let an IO observable class \(\mathcal O\) be represented by a tuple

\[
(\mathcal H_{\mathcal O},\mathcal A_{\mathcal O},T_{\mathcal O},R_{\mathcal O}),
\]

where \(\mathcal H_{\mathcal O}\) is the carrier, \(\mathcal A_{\mathcal O}\) is the relevant algebra or operator family, \(T_{\mathcal O}\) is the physical transfer/readout map, and \(R_{\mathcal O}\) is the resulting observer-readable datum.

Suppose a factor \(J_A\) is derived for class \(A\). This means \(J_A\) is a statement about the readout map \(T_A\), the carrier \(\mathcal H_A\), or the algebra \(\mathcal A_A\). For another class \(B\), inserting \(J_A\) into \(T_B\) changes the \(B\)-class readout unless there exists a class map

\[
F_{A\to B}:\mathcal O_A\to\mathcal O_B
\]

that preserves the relevant structure and transports \(J_A\) to a well-defined \(J_B\). Without such a map, the substitution is not a theorem but a new premise.

This is exactly the pattern already enforced in the current stack:

- Paper 21/Paper 35 temperature assignment: \(T_{\rm obs}\) belongs to observer-side optical readout, while BBN nuclear rates are local bulk thermodynamics; inserting \(T_{\rm obs}\) into BBN rates is a class error.
- Paper 35 DESI dark-energy repair: the support-coordinate \(\rho_\Lambda(R)\propto R^{-2}\) law does not directly become an observer-frame \(w=-1/3\) statement; the observer branch needs its own projection.
- Paper 19/Paper 35 baryon-density repair: the killed projected route \(\Omega_b=f_b\Omega_{m,\rm active}\) is not the surviving physical-density slot \(\omega_{b,\rm geom}\).
- Paper 32 typed boundary-to-bulk projection: source/readout, thermodynamic-history, and closed-\(S^3\) perturbation blocks are separate typed blocks.

Therefore cross-class substitution without a map theorem is invalid inside IO. QED.

### Dependency Chain

Theorem 1.V (Typed Observable / No Cross-Class Substitution)

<- P1: Schwarzschild interior with horizon/interior readout boundary  
<- P2: local physics and observable processes retain their standard process typing unless mapped  
<- Paper 19: density and observable-class/Jacobian audits; background matter slot is not freely dressed by another class projector  
<- Paper 21 Theorem 21.L: local BBN thermodynamics uses \(T_{\rm IO}\), not optical \(T_{\rm obs}\)  
<- Paper 32 typed boundary-to-bulk projection architecture: distinct typed source/readout, thermodynamic-history, and perturbation blocks  
<- Paper 35 BBN temperature-assignment audit and DESI dark-energy scope repair  
-> No factor may migrate across typed observable classes without an explicit map theorem

### What It Does Not Cover

This theorem does not say that different observable classes can never be related. It says the relation must be proved. A valid class map, intertwiner, functor, or projection theorem can transport data between classes. The theorem blocks silent substitution, not theorem-grade transfer.

This theorem does not license post-hoc class definitions. In any application, the observable class, carrier, and readout map must be fixed from the measurement structure before comparison with the target value. A class boundary chosen because it improves a residual is a fitted selector, not a theorem.

---

## Theorem 1.U - Native Closed-\(S^3\) Spatial Mode Reduction Principle

### Statement

Because the IO spatial geometry is closed \(K=+1\) with compact \(S^3\) spatial slices, the native spatial spectral theory is discrete. Scalar, vector, tensor, and Hodge-decomposed perturbative carriers should be formulated on the compact \(S^3\) spectrum. Continuous flat-space \(k\)-modes are approximation/dictionary objects, not the primitive IO mode basis.

### Status

`DERIVED/THEOREM`.

### Proof

By Theorem 1.Z, IO spatial slices are compact \(S^3\) slices. Standard spectral theory for elliptic operators on compact Riemannian manifolds gives a discrete spectrum with finite multiplicities and no continuous spatial momentum spectrum.

For the scalar Laplacian on unit \(S^3\),

\[
\lambda_n=n(n+2),\qquad {\rm mult}(\lambda_n)=(n+1)^2,
\]

with analogous discrete exact/coexact Hodge spectra for differential forms. Paper 22 and Paper 32 already use these spectra: the closed-\(S^3\) solver grammar uses a discrete \(q\)-ladder and hyperspherical support rather than a primitive infinite-flat \(k\)-basis.

Therefore the native IO mode principle is compact/discrete. Continuous \(k\) is allowed only as a large-\(n\), local, observational, or dictionary limit after proving the mapping from the \(S^3\) ladder. QED.

### Dependency Chain

Theorem 1.U (Native Closed-\(S^3\) Spatial Mode Reduction Principle)

<- Theorem 1.Z: closed \(K=+1\) \(S^3\) interior geometry  
<- `IMPORTED/STANDARD`: spectral theorem for elliptic operators on compact Riemannian manifolds  
<- Paper 22 Hodge Spectrum Theorem: scalar/exact/coexact spectra on \(S^3\) are discrete with finite multiplicity  
<- Paper 32 S^3-native solver specification: admissible IO-native solver uses closed \(S^3\) mode grammar  
-> Native IO spatial modes are compact \(S^3\) modes; flat continuum \(k\) is derived/approximate

### What It Does Not Cover

This theorem does not ban continuum notation. It bans treating infinite flat-space mode structure as primitive IO geometry. Continuum \(k\)-space may be used as a controlled approximation, a high-mode limit, or an observational dictionary when the mapping is explicitly stated. Local tangent-space Fourier transforms remain valid for local physics under P2; what is not valid is treating the infinite flat-space continuum as the primitive global IO spectrum.

This theorem is not a standalone universal "closed curve space" theorem. It does not prove that all local physics must be computed on full \(S^3\) without tangent-space approximations; it does not invalidate continuum quantum field theory; it does not reduce every curve/path-integral object; and, by Theorem 1.V, it does not automatically apply across typed observable classes without a map theorem.

---

## Theorem 1.T - Schwarzschild Parent Neutrality

### Statement

Under P1 as stated, the containing black hole is Schwarzschild. A Schwarzschild black hole has no Kerr angular-momentum parameter and no Reissner-Nordstrom charge parameter:

\[
a=J/(M_Uc)=0,\qquad Q=0.
\]

Therefore parent black-hole spin or parent black-hole charge cannot be used as an IO mechanism, sign selector, CP-odd datum, baryogenesis source, or observational adjustment unless P1 is amended from Schwarzschild to Kerr, Reissner-Nordstrom, or Kerr-Newman and the downstream framework is rebuilt accordingly.

### Status

`DERIVED/THEOREM` from exact P1.

### Proof

P1 states that the observable universe exists inside a Schwarzschild black hole. In the standard black-hole family, the Schwarzschild solution is the unique stationary, spherically symmetric, uncharged, non-rotating vacuum black-hole solution. It is characterized by mass \(M_U\) alone. Its angular momentum and electromagnetic charge parameters vanish:

\[
J=0,\qquad Q=0.
\]

The Kerr family introduces \(J\neq0\). The Reissner-Nordstrom family introduces \(Q\neq0\). Kerr-Newman introduces both. Those are different parent geometries, not hidden degrees of freedom inside the Schwarzschild premise.

Therefore any later argument that uses parent spin, parent charge, frame dragging, an electromagnetic horizon charge, or a Kerr/RN sign datum has changed P1. Such a route is not an allowed IO route unless the premise is explicitly amended and all dependent geometry, horizon thermodynamics, mode structure, and observable maps are revalidated. QED.

### Dependency Chain

Theorem 1.T (Schwarzschild Parent Neutrality)

<- P1: observable universe exists inside a Schwarzschild black hole  
<- `IMPORTED/STANDARD`: Schwarzschild solution is mass-only, static, uncharged, non-rotating  
<- definitions \(a=J/(M_Uc)\), \(Q\) electromagnetic charge  
-> \(a=0\), \(Q=0\) for the parent geometry  
-> parent Kerr/RN spin-charge mechanisms are excluded unless P1 is amended

### What It Does Not Cover

This theorem does not say no local angular momentum, magnetic field, charge separation, or vorticity can exist inside the universe. It says the parent black-hole geometry itself supplies no Kerr or Reissner-Nordstrom parameter. Local internal processes require their own carriers and cannot borrow a parent spin/charge datum from P1.

Parent neutrality does not prohibit internal charged sectors, local electromagnetic fields, chiral matter, or CP-odd internal operators. It only says those cannot be borrowed from a Kerr or Reissner-Nordstrom parent parameter.

---

## Compact Manuscript Table

Claude can use this table in Paper 1 body text, with the full memo remaining in the bundle/audit trail:

| Inheritance rule | Body statement |
|---|---|
| Closed \(K=+1\) interior geometry | The native IO geometry is the closed \(S^3\) OS interior, not infinite flat space. Flat-space formulas require a local/dictionary justification. |
| Horizon-contained dynamics | Interior observers do not have asymptotic-infinity readout. IO observables must be horizon-readable or interior-readable. |
| Typed observables | A factor derived for one observable class cannot be inserted into another class without a map theorem. |
| Native closed-\(S^3\) mode reduction | Closed-space hyperspherical modes are primitive; continuum \(k\)-space is approximate or dictionary-level, with local tangent-space Fourier transforms still valid under P2. |
| Schwarzschild parent neutrality | The parent geometry has no Kerr spin or Reissner-Nordstrom charge. Spin/charge mechanisms require a premise amendment or an internal carrier theorem. |

## Research Impact

These five rules materially affect future work:

1. Baryogenesis searches cannot use Kerr/RN parent spin or charge as a hidden sign selector under current P1.
2. Automated finite-grid research must enumerate readout-distinct IO classes on compact \(S^3\)/horizon-readable architecture, not arbitrary flat-space continuum mechanisms.
3. Local quantum processes cannot use global averages, optical readout factors, or support-coordinate densities without a typed map theorem.
4. Any external P2 physics imported from flat-space QFT must be checked for compatibility with the closed \(S^3\) support and no-asymptotic-infinity readout boundary.
5. Future no-hidden-fit audits can reject a proposed calculation when it silently moves a factor across observable classes.

## External References

- Oppenheimer, J. R., and Snyder, H. (1939). "On Continued Gravitational Contraction." *Physical Review* 56, 455. DOI: `10.1103/PhysRev.56.455`.
- Schwarzschild, K. (1916). "Uber das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie." *Sitzungsberichte der Koniglich Preussischen Akademie der Wissenschaften*.
- Weyl, H. (1911). "Uber die asymptotische Verteilung der Eigenwerte." *Nachrichten der Koniglichen Gesellschaft der Wissenschaften zu Gottingen*.
- O'Neill, B. (1983). *Semi-Riemannian Geometry with Applications to Relativity*. Academic Press.
