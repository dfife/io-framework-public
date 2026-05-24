# Paper 1 v4.1 Theorem Memo - Schwarzschild Mass Measure Theorem

Date: 2026-05-24  
Prepared for: Paper 1 v4.1 placement review  
Companion calculation: `results/paper1/paper1_total_energy_calculation_round1.md`

## Theorem 1.Y - Schwarzschild Mass Measure Theorem

Status: `DERIVED/THEOREM` for the OS dust/Misner-Sharp measure statement; `DERIVED/CONDITIONAL_VERIFIED` for the IO typed-density guard, conditional on the current Paper 19/Paper 32/Paper 35 active density-slot architecture.

### Statement

Under Premise 1, the observable universe is the interior of a Schwarzschild black hole with exterior Schwarzschild mass \(M_U\). Under Premise 2, the interior collapse/expansion geometry is governed by standard general relativity. In the Oppenheimer-Snyder closed \(K=+1\) interior, the exterior Schwarzschild mass is the quasi-local Misner-Sharp mass of the matched spherical boundary, not the proper-volume integral of every observer-side or support-side density slot over the full closed \(S^3\) support slice.

Let the closed FRW/OS interior metric be

\[
ds^2=-c^2d\tau^2+a(\tau)^2\left(d\chi^2+\sin^2\chi\,d\Omega_2^2\right),
\]

with areal radius

\[
R_A(\tau,\chi)=a(\tau)\sin\chi .
\]

The gravitational mass measured by the exterior Schwarzschild geometry is

\[
M_{\rm MS}(\chi)
=\frac{4\pi}{3}\rho_{\rm mass}(\tau)a(\tau)^3\sin^3\chi ,
\]

equivalently the Misner-Sharp mass associated with the two-sphere \(R_A=a\sin\chi\). The proper-volume integral of a homogeneous density over a closed spatial region is instead

\[
M_{\rm prop}(\chi)
=4\pi\rho_{\rm mass}(\tau)a(\tau)^3
  \int_0^\chi \sin^2u\,du
=2\pi\rho_{\rm mass}(\tau)a(\tau)^3
  \left(\chi-\frac{1}{2}\sin 2\chi\right).
\]

These are not the same functional except in the local flat/small-\(\chi\) limit. Therefore the equality

\[
M_U \stackrel{?}{=}\int_{\Sigma_\tau}\rho_{\rm total}\,dV_{S^3}
\]

is not a theorem of the IO framework and is generally false on the closed \(K=+1\) OS support geometry.

For the full closed \(S^3\) support slice, the mismatch is explicit. The OS dust equation gives

\[
\rho_{\rm dust}(\tau)=\frac{3c^2r_s}{8\pi G a(\tau)^3}.
\]

Using the full support volume

\[
V_{S^3}(a)=2\pi^2a^3,
\]

the proper-volume dust integral is

\[
M_{\rm prop}^{S^3}
=\rho_{\rm dust}V_{S^3}
=\frac{3\pi c^2r_s}{4G}
=\frac{3\pi}{2}M_U,
\]

where \(r_s=2GM_U/c^2\). Thus even the pure OS dust sector over the full closed \(S^3\) support slice overcounts the exterior Schwarzschild mass by the exact factor

\[
\frac{M_{\rm prop}^{S^3}}{M_U}=\frac{3\pi}{2}=4.71238898038469.
\]

Consequently, local density slots such as \(\omega_{b,\rm geom}\), observer-side thermal densities, geometric dark-sector inventory densities, and the Paper 1 torsion-\(\Lambda\) slot may be used in their typed observer/support equations, but they may not be added and integrated over \(2\pi^2R_U^3\) to reconstruct \(M_U\) unless a separate theorem supplies:

1. the quasi-local mass functional being evaluated;
2. the matched boundary \(\chi_b\) or equivalent areal-radius surface;
3. the frame map converting each typed density slot into that same quasi-local mass measure;
4. the gravitational binding/curvature contribution implicit in the Hamiltonian constraint.

No current Paper 1-35 theorem supplies all four objects for the mixed slot sum

\[
\rho_{\rm rad}+\rho_b+\rho_{\rm geom.dark}+\rho_\Lambda .
\]

Therefore the Round 1 direct full-\(S^3\) proper-volume route is a `DERIVED/NO-GO` reconstruction route for \(M_Uc^2\), not a valid second derivation of \(M_Uc^2\).

### Scope

This theorem does **not** say that the published density slots are meaningless. It says they are not all densities with respect to one common extensive full-\(S^3\) mass measure.

The theorem preserves:

- Paper 1's identification of \(M_U\) with the exterior Schwarzschild mass;
- Paper 19's dust-current/Radon-Nikodym reconstruction of the homogeneous matter slot;
- Paper 32's use of \(V_{S^3}(R)=2\pi^2R^3\) for support-branch coarse-graining;
- Paper 35's observer-side baryon and geometric dark-sector inventory slots.

The theorem blocks only the unproved cross-frame operation:

\[
\text{observer/support density slots}
\quad\longrightarrow\quad
\text{single additive full-}S^3\text{ proper-volume mass integral}.
\]

## Proof

### Step 1 - OS interior and areal radius

By P1, the object is a Schwarzschild black hole. By P2, the interior dynamics of a homogeneous dust collapse/expansion region are the standard Oppenheimer-Snyder solution: a closed \(K=+1\) FRW interior matched to a Schwarzschild exterior across a spherical boundary. Paper 1 v4.1 §2.1-§2.3 uses this closed \(S^3\) OS chassis, and Paper 32 v2.0 keeps the closed \(S^3\) support branch.

In a closed FRW chart, the areal radius of a two-sphere labelled by \(\chi\) is

\[
R_A=a(\tau)\sin\chi .
\]

The full spatial proper-volume element is

\[
dV=a^3\sin^2\chi\,d\chi\,d\Omega_2 .
\]

### Step 2 - Misner-Sharp mass is the Schwarzschild matching mass

In spherical symmetry, the standard quasi-local mass is the Misner-Sharp mass. For a perfect-fluid FRW interior it reduces to

\[
M_{\rm MS}(\chi)
=\frac{4\pi}{3}\rho_{\rm mass}R_A^3
=\frac{4\pi}{3}\rho_{\rm mass}a^3\sin^3\chi .
\]

At the OS matching boundary \(\chi=\chi_b\), the exterior Schwarzschild mass is this quasi-local mass:

\[
M_U=M_{\rm MS}(\chi_b).
\]

This is the general-relativistic mass charge seen by the exterior Schwarzschild geometry.

### Step 3 - Proper-volume integral is a different object

The proper-volume integral over the same homogeneous density out to \(\chi\) is

\[
M_{\rm prop}(\chi)
=\int_0^\chi \rho_{\rm mass}\,dV
=4\pi\rho_{\rm mass}a^3\int_0^\chi\sin^2u\,du .
\]

Since

\[
\int_0^\chi\sin^2u\,du
=\frac{\chi}{2}-\frac{\sin2\chi}{4},
\]

we get

\[
M_{\rm prop}(\chi)
=2\pi\rho_{\rm mass}a^3
\left(\chi-\frac{1}{2}\sin2\chi\right).
\]

This is not equal to

\[
M_{\rm MS}(\chi)=\frac{4\pi}{3}\rho_{\rm mass}a^3\sin^3\chi
\]

except in the small-\(\chi\) limit where the closed geometry is locally flat.

### Step 4 - Full \(S^3\) overcount is exact

Paper 32 uses the support-branch full-\(S^3\) volume

\[
V_{S^3}(a)=2\pi^2a^3.
\]

For OS dust, Paper 19's background matter source theorem gives the same dust scaling as the Einstein-dust equation:

\[
\rho_{\rm dust}a^3={\rm constant}.
\]

In the Paper 32 support-branch notation this is equivalently

\[
\rho_{\rm dust}(\tau)=\frac{3c^2r_s}{8\pi G a(\tau)^3}.
\]

Therefore

\[
\rho_{\rm dust}V_{S^3}
=\frac{3c^2r_s}{8\pi G a^3}\,2\pi^2a^3
=\frac{3\pi c^2r_s}{4G}
=\frac{3\pi}{2}M_U.
\]

Thus the full-\(S^3\) proper-volume integral is not the Schwarzschild mass even before adding radiation, Lambda, or typed observer-side projection slots.

### Step 5 - Typed IO density slots do not share one automatic extensive measure

Paper 19 establishes that the homogeneous matter density is the Radon-Nikodym derivative of the conserved dust measure with respect to the flow-orthogonal 3-volume measure. It also warns that the full observer Friedmann assembly remains separate.

Paper 35 uses \(\omega_{b,\rm geom}\) as a physical-density slot for the baryon-to-photon and BBN calculations, and uses \(f_b=2\gamma_{\rm BI}/x\) to split the geometric matter inventory into gauge-charged and gauge-neutral sectors.

Paper 1/Paper 10/Paper 35 treat the torsion-\(\Lambda\) slot as a support/observer projected vacuum slot, not as an ordinary dust count. Paper 35 explicitly separates the support-coordinate \(\rho_\Lambda\propto1/R^2\) statement from the active observer-frame constant-vacuum \(w=-1\) statement.

Therefore the operation

\[
\left(\rho_{\rm rad}+\rho_b+\rho_{\rm geom.dark}+\rho_\Lambda\right)
2\pi^2R_U^3
\]

mixes density slots from different typed measures and treats them as if they were one common extensive proper-volume mass density. That common-measure identification has not been derived.

### Step 6 - Conclusion

Because exterior Schwarzschild mass is the matched Misner-Sharp charge, and because the full-\(S^3\) proper-volume integral already fails for pure OS dust by the exact factor \(3\pi/2\), the direct extensive full-support integral cannot be used as an independent derivation of \(M_Uc^2\).

The correct closure is a measure theorem:

\[
M_Uc^2
\quad\text{is the exterior/quasi-local Schwarzschild charge,}
\]

not

\[
c^2\int_{\text{full current }S^3}
\left(\rho_{\rm rad}+\rho_b+\rho_{\rm geom.dark}+\rho_\Lambda\right)dV.
\]

QED.

## Dependency Chain

Theorem 1.Y (Schwarzschild Mass Measure Theorem)

<- P1: observable universe is inside a Schwarzschild black hole  
<- P2: interior physics obeys the same GR dynamics as exterior physics  
<- `IMPORTED/STANDARD`: Oppenheimer-Snyder closed-FRW dust interior matched to Schwarzschild exterior (Oppenheimer and Snyder 1939)  
<- `IMPORTED/STANDARD`: Misner-Sharp quasi-local mass in spherical symmetry (Misner and Sharp 1964)  
<- Paper 1 v4.1 §2.1-§2.3: closed \(K=+1\) OS chassis, \(M_U\), \(r_s=2GM_U/c^2\), \(x=r_s/R_U\)  
<- Paper 19 background matter source theorem: homogeneous matter density is a conserved dust-measure/Radon-Nikodym source slot on the flow-orthogonal 3-volume measure  
<- Paper 32 support-branch volume convention: \(V_{S^3}(R)=2\pi^2R^3\)  
<- Paper 35 typed inventory: \(\omega_{b,\rm geom}\), \(f_b=2\gamma_{\rm BI}/x\), and active observer/support separation for the dark-sector and vacuum slots  
-> exterior Schwarzschild mass is the matched Misner-Sharp charge  
-> full-support proper-volume density integral is not an equivalent mass-energy route  
-> direct Round 1 Route 2 reconstruction is `DERIVED/NO-GO` as an \(M_Uc^2\) derivation

## Placement Recommendation

Paper 1 should not claim that the current observer-frame density budget, integrated over the full current \(S^3\) support volume, independently reproduces \(M_Uc^2\).

The clean statement is:

> The total mass-energy \(M_Uc^2\) is the exterior Schwarzschild/Misner-Sharp charge of the matched OS interior. Local density slots inside the IO framework are typed observer/support quantities. They enter Friedmann, BBN, CMB, and dark-sector calculations through their own measures and readout maps; they are not automatically additive over the full closed \(S^3\) support volume. A direct full-\(S^3\) proper-volume integral is therefore not the mass definition. In fact, for pure OS dust it overcounts the Schwarzschild mass by the exact factor \(3\pi/2\), before any vacuum or projection-sector terms are added.

## External References

- Oppenheimer, J. R., and Snyder, H. (1939). "On Continued Gravitational Contraction." *Physical Review* 56, 455.
- Misner, C. W., and Sharp, D. H. (1964). "Relativistic Equations for Adiabatic, Spherically Symmetric Gravitational Collapse." *Physical Review* 136, B571.
- Hernandez, W. C., and Misner, C. W. (1966). "Observer Time as a Coordinate in Relativistic Spherical Hydrodynamics." *Astrophysical Journal* 143, 452.
