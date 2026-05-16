Paper 26
Thomson-Kernel Identity Audit
=============================

Question
--------

Can the class-membership premise

    AV1: Thomson-gated scalar CMB observables belong to the acoustic baryon class

be replaced by a theorem derived directly from the scalar perturbation equations?


Executive result
----------------

Short answer:

- `derived`: yes, for a **Thomson-kernel identity lemma**.
- `not derived`: no, for the full conclusion

      omega_b,vis = omega_b,eff

  from the perturbation equations alone.

The perturbation equations do prove that the same differential Thomson opacity

    kappa' = a n_e sigma_T

controls both:

1. the visibility function, and
2. the photon-baryon momentum-transfer terms.

But they do **not** prove that the baryon-loading observable

    R = 3 rho_b / (4 rho_gamma)

must use the same baryon slot as `kappa'`.


==================================================
I. Derived lemma from the equations
==================================================

Lemma 26.TK1 (unique Thomson-kernel lemma)
------------------------------------------

Status:

    derived

Statement
---------

In the scalar CMB perturbation system, the differential Thomson opacity

    kappa' = a n_e sigma_T

is the unique local photon-baryon interaction kernel appearing both:

1. in the visibility function

       g = kappa' e^{-kappa},

2. and in the photon-baryon momentum-transfer terms of the tightly coupled Euler system.


Proof
-----

1. In the thermodynamics module, CLASS computes

       dkappa/dtau = a n_e sigma_T

   and then builds

       g = (d kappa / d tau) exp(-kappa).

   See:
   - [thermodynamics.c](/opt/cosmology-lab/src/class_public/source/thermodynamics.c#L3019)
   - [thermodynamics.c](/opt/cosmology-lab/src/class_public/source/thermodynamics.c#L3457)

2. In the same codebase, the baryon drag rate is defined from the same opacity as

       -dkappa_b/dtau = -(1/R) kappa',
       R = 3 rho_b / 4 rho_gamma.

   See:
   - [thermodynamics.c](/opt/cosmology-lab/src/class_public/source/thermodynamics.c#L3185)

3. In the perturbation equations, the tight-coupling slip and Euler-system evolution use
   `tau_c = 1/kappa'` and the same `R`.

   See:
   - [perturbations.c](/opt/cosmology-lab/src/class_public/source/perturbations.c#L10136)

Therefore the same local kernel `kappa'` governs both the visibility construction and the
photon-baryon momentum exchange.

QED.


Corollary 26.TK2
----------------

Status:

    derived

Statement
---------

Any reassignment of the baryon slot used in the Thomson interaction kernel `kappa'` must be shared
simultaneously by:

1. the visibility function, and
2. the tight-coupling drag terms built from `kappa'`.

So visibility and Thomson drag cannot be typed independently once the `kappa'` slot is fixed.


==================================================
II. What the equations do NOT prove
==================================================

No-go theorem 26.TK3
--------------------

Status:

    derived / no-go

Statement
---------

The Thomson-kernel identity does **not** by itself prove

    omega_b,vis = omega_b,eff.


Reason
------

Because the acoustic dynamics do not depend on `kappa'` alone.
They depend on the pair

    (kappa', R),
    R = 3 rho_b / (4 rho_gamma).

The equations show that:

- `kappa'` is the local scattering / opacity kernel,
- `R` is the baryon inertia loading.

These are different observables, even though they appear in the same coupled system.

So from the equations alone one can prove

    visibility and drag share the same Thomson kernel,

but not

    visibility and acoustic loading are the same baryon observable.


Framework-side obstruction
--------------------------

This is exactly consistent with the existing Paper 20 boundary:

    local Thomson operator commutes with Z_g,

so the reduced-core gauge dressing does not enter directly through the local Thomson contact term.

See:
- [paper20_acoustic_bridge_theorem_report.txt](/opt/cosmology-lab/results/paper20/paper20_acoustic_bridge_theorem_report.txt)

Theorem AB5:

    the factor sqrt(1+gamma^2) does not follow directly from the local Thomson operator.

And Paper 21 AC1 preserves the same boundary:

    local plasma insertion is ruled out;
    the surviving gauge-sensitive correction is in the optical readout stage, not in the local
    Thomson kernel itself.

See:
- [paper21_ac1_opening_investigation_report.txt](/opt/cosmology-lab/results/paper21/paper21_ac1_opening_investigation_report.txt)


==================================================
III. Strongest honest replacement
==================================================

What *is* now theorem-grade is:

Theorem 26.TK4 (shared Thomson-sector theorem)
----------------------------------------------

Status:

    derived

Statement
---------

The CMB visibility function and the tight-coupling drag terms belong to the same **Thomson
interaction sector**, because they are built from the same kernel `kappa' = a n_e sigma_T`.

What remains open is the next step:

    which IO baryon class is assigned to that Thomson sector?

That question is not answered by the perturbation equations alone.


==================================================
IV. Bottom line
==================================================

The user's core observation is correct and should be kept:

    visibility and acoustic momentum exchange are not merely analogous;
    they share the same Thomson kernel.

But the stronger conclusion

    therefore omega_b,vis = omega_b,eff

still needs one extra theorem:

    that the Thomson sector as a whole is typed by the acoustic baryon class rather than by raw
    inventory.

So AV1 can be narrowed, but not eliminated entirely.
