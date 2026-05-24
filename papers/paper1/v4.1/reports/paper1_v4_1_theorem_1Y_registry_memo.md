# Paper 1 v4.1 Theorem 1.Y Registry Memo

Date: 2026-05-24  
Theorem: `Theorem 1.Y`  
Title: Total Energy / Density Accounting Separation  
Source of truth: Paper 1 v4.1 §2.12 manuscript text

## Theorem Statement

### Theorem 1.Y - Total Energy / Density Accounting Separation

Under P1, the observable universe exists inside a Schwarzschild black hole whose exterior mass parameter is \(M_U\). Under P2, the standard mass-energy relation applies to that exterior Schwarzschild mass charge. Therefore the exterior Schwarzschild mass charge, treated as the global/quasi-local mass-energy parameter of the matched IO geometry, has energy

\[
E_{\rm total}=M_Uc^2.
\]

For a closed \(K=+1\) spatial slice with curvature scale \(R\), the full \(S^3\) volume is

\[
V_{S^3}(R)=2\pi^2R^3.
\]

This licenses a coarse average density at a specified epoch/scale:

\[
\rho_{\rm avg}(R)=\frac{M_U}{V_{S^3}(R)}
=\frac{M_U}{2\pi^2R^3}.
\]

This average is a bookkeeping definition on a specified closed slice. It is not a component budget and it is not a local quantum-mechanical input. Any later calculation that wants to decompose \(M_U\) into radiation, baryon, geometric-dark, and vacuum slots must first prove a typed-measure theorem placing those slots on the same extensive measure.

Nor does \(\rho_{\rm avg}(R)\) identify a local stress-energy component, Friedmann density slot, or observer-frame density parameter without a theorem specifying the frame and measure.

The two objects have different status:

1. \(E_{\rm total}=M_Uc^2\) is the exterior Schwarzschild mass charge, treated as the global/quasi-local mass-energy parameter of the matched IO geometry.
2. \(\rho_{\rm avg}(R)\) is an epoch-indexed coarse geometric average. It changes with \(R\) and is not a fixed framework constant.

Consequently, component-density slots such as

\[
\rho_{\rm radiation},\quad
\rho_{\rm baryon},\quad
\rho_{\rm geometric\ dark},\quad
\rho_\Lambda
\]

may not be summed and integrated over the full \(S^3\) spatial volume to recover \(M_U\) unless a separate typed-measure theorem first defines all of those slots on a common extensive mass-energy measure.

### Status

`DERIVED/THEOREM` within the Paper 1 P1/P2 Schwarzschild-interior mass-accounting and closed-\(S^3\) geometry setting.

The theorem is unconditional inside Paper 1's P1/P2 Schwarzschild-interior mass-accounting setting. It imports only standard Schwarzschild/GR mass-energy usage and the standard volume formula for the closed \(S^3\) spatial slice.

## Proof

### Step 1 - P1 supplies the exterior mass parameter

P1 states that the observable universe exists inside a Schwarzschild black hole. A Schwarzschild black hole is characterized by an exterior mass parameter \(M_U\). Paper 1 v4.1 §2.2 identifies this parameter as the total mass-energy content of the interior cosmology viewed from the exterior Schwarzschild side.

### Step 2 - P2 supplies the mass-energy relation for the exterior Schwarzschild charge

P2 states that physics inside the horizon is the same physics outside the horizon. Standard relativistic physics assigns energy

\[
E=Mc^2
\]

to a mass \(M\) when read as an exterior Schwarzschild/quasi-local mass parameter. Applying this to the Schwarzschild mass parameter \(M_U\) gives

\[
E_{\rm total}=M_Uc^2.
\]

Using Paper 1 v4.1 §2.2,

\[
M_U=4.50\times10^{53}\ {\rm kg},
\]

so

\[
E_{\rm total}
=(4.50\times10^{53})(299792458)^2
=4.0443983043156795\times10^{70}\ {\rm J}.
\]

This is the total-energy statement licensed by Paper 1.

### Step 3 - closed \(S^3\) geometry supplies a coarse average density formula

Paper 1 v4.1 §2.1 fixes the native interior geometry as closed \(K=+1\), with \(S^3\) spatial slices. The volume of a full closed \(S^3\) slice with curvature scale \(R\) is

\[
V_{S^3}(R)=2\pi^2R^3.
\]

Therefore one may define the coarse average density

\[
\rho_{\rm avg}(R)=\frac{M_U}{2\pi^2R^3}.
\]

This is a definition of a global average over a specified closed slice.

This average is a bookkeeping definition on a specified closed slice. It is not a component budget and it is not a local quantum-mechanical input. Any later calculation that wants to decompose \(M_U\) into radiation, baryon, geometric-dark, and vacuum slots must first prove a typed-measure theorem placing those slots on the same extensive measure.

Nor does \(\rho_{\rm avg}(R)\) identify a local stress-energy component, Friedmann density slot, or observer-frame density parameter without a theorem specifying the frame and measure.

### Step 4 - \(\rho_{\rm avg}(R)\) is not a conserved invariant

The IO interior evolves through an \(R\)-dependent cycle. Since

\[
\rho_{\rm avg}(R)\propto R^{-3},
\]

the numerical value of \(\rho_{\rm avg}\) changes with the chosen epoch/scale. A density statement therefore requires an epoch, frame, radius convention, and uncertainty convention.

This is unlike

\[
E_{\rm total}=M_Uc^2,
\]

which is the exterior Schwarzschild mass charge, treated as the global/quasi-local mass-energy parameter of the matched IO geometry.

### Step 5 - component-density summation requires a separate typed-measure theorem

Later IO papers use density-like quantities in typed observable classes: radiation slots, baryon physical-density slots, geometric dark-sector inventory slots, and torsion/vacuum slots. These are not automatically elements of one common extensive full-\(S^3\) mass measure.

To reconstruct \(M_U\) from component densities, one would need a theorem proving at least:

1. all component slots are defined at the same epoch;
2. all component slots are expressed in the same frame;
3. all component slots are densities with respect to the same spatial measure;
4. the gravitational/quasi-local mass convention equals the proposed proper-volume integral;
5. the vacuum/torsion slot is being counted by the same extensive rule as conserved matter.

No such theorem is part of Paper 1 v4.1 §2.12. Therefore the component-density integral

\[
\int_{\Sigma_R}
(\rho_{\rm radiation}+\rho_{\rm baryon}
+\rho_{\rm geometric\ dark}+\rho_\Lambda)\,dV
\]

is not licensed as an independent derivation of \(M_U\).

### Step 6 - local quantum processes cannot use the coarse average by default

\(\rho_{\rm avg}(R)\) is a global geometric average. Local quantum-mechanical processes require local state data: local carrier, local Hamiltonian, local temperature, local covariance/state selection, chemical potentials, interaction rates, and fluctuations. A global average density does not supply those data.

Therefore no downstream quantum calculation may use \(\rho_{\rm avg}(R)\) as a local microphysical input unless a separate local-sampling theorem proves that the relevant carrier samples this average.

The theorem follows. QED.

## Dependency Chain

Theorem 1.Y (Total Energy / Density Accounting Separation)

<- P1: observable universe exists inside a Schwarzschild black hole  
<- Schwarzschild exterior has mass parameter \(M_U\)  
<- Paper 1 v4.1 §2.2: \(M_U=4.50\times10^{53}\ {\rm kg}\)  
<- P2: standard physics applies inside/outside the horizon  
<- `IMPORTED/STANDARD`: relativistic mass-energy relation \(E=Mc^2\) for the exterior Schwarzschild/quasi-local mass parameter  
-> \(E_{\rm total}=M_Uc^2=4.0443983043156795\times10^{70}\ {\rm J}\)  
<- Paper 1 v4.1 §2.1: closed \(K=+1\) \(S^3\) spatial geometry  
<- `IMPORTED/STANDARD`: full closed-\(S^3\) volume \(V_{S^3}(R)=2\pi^2R^3\)  
-> \(\rho_{\rm avg}(R)=M_U/(2\pi^2R^3)\) as an epoch-indexed coarse average  
-> separation rule: total energy is tied to the exterior Schwarzschild mass charge; density is epoch/frame/measure indexed  
-> accounting guard: mixed component-density slots cannot be summed over full \(S^3\) to recover \(M_U\) without a separate common typed-measure theorem  
-> local-QM guard: \(\rho_{\rm avg}(R)\) is not a default local microphysical input

## Scope Boundary

### What Theorem 1.Y Establishes

1. The exterior Schwarzschild mass charge, treated as the global/quasi-local mass-energy parameter of the matched IO geometry, gives \(E_{\rm total}=M_Uc^2\).
2. The full closed-\(S^3\) coarse average density formula is \(\rho_{\rm avg}(R)=M_U/(2\pi^2R^3)\).
3. \(\rho_{\rm avg}(R)\) is not a fixed framework constant; it is epoch/scale indexed.
4. Component-density decomposition is a separate accounting problem requiring a typed-measure theorem.
5. Local quantum-mechanical rates and carrier states cannot use \(\rho_{\rm avg}(R)\) by default.

### What Theorem 1.Y Does Not Establish

1. It does not define the radiation, baryon, geometric-dark, or \(\Lambda\) component budget.
2. It does not prove

\[
\rho_{\rm avg}=\rho_{\rm radiation}+\rho_{\rm baryon}
+\rho_{\rm geometric\ dark}+\rho_\Lambda.
\]

3. It does not say the later component slots are wrong; it says they are not automatically one common extensive density budget.
4. It does not license local quantum calculations from global average density.
5. It does not solve baryogenesis, BBN, CMB covariance, dark-sector accounting, or vacuum-energy accounting.
6. It does not require Paper 1 to provide an independent density-integral derivation of \(M_Uc^2\).

## Downstream Uses

### Paper 1

Paper 1 §2.2 uses \(M_U\) as the finite exterior Schwarzschild mass parameter. Theorem 1.Y licenses the clean Schwarzschild mass-accounting statement

\[
E_{\rm total}=M_Uc^2.
\]

Paper 1 §2.12 uses the theorem to prevent a false second route based on current-epoch component-density summation.

### Later Papers

The theorem supplies a guardrail for later density and local-microphysics calculations:

- BBN and baryogenesis may not use \(\rho_{\rm avg}(R)\) as a local quantum input without a local-sampling theorem.
- Dark-sector accounting may not sum typed density slots as one full-\(S^3\) extensive budget without a common-measure theorem.
- Reproducibility/audit work should treat density values as epoch/frame/measure indexed, not as fixed total-energy identities.
- Automated baryogenesis class-screen research should not treat global mean density as a local source-rate substitute.

## Manuscript Tightening Recommendation

If Paper 1 v4.1 §2.12 does not already contain the following scope sentence, add it after the \(\rho_{\rm avg}(R)\) formula:

> This average is a bookkeeping definition on a specified closed slice. It is not a component budget and it is not a local quantum-mechanical input. Any later calculation that wants to decompose \(M_U\) into radiation, baryon, geometric-dark, and vacuum slots must first prove a typed-measure theorem placing those slots on the same extensive measure.

This edit makes the theorem's overclaim boundary reviewer-extractable.

## Registry Status

Registry memo complete. Suitable for downstream citation as:

> Theorem 1.Y (Total Energy / Density Accounting Separation), Paper 1 v4.1 registry memo, `DERIVED/THEOREM` within the Paper 1 P1/P2 Schwarzschild-interior mass-accounting and closed-\(S^3\) geometry setting.
