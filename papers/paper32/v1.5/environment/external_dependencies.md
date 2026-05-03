# External Dependencies

The Paper 32 v1.5 public scripts require only Python standard-library modules.

No external numerical package, database, CLASS installation, PRyMordial checkout,
or private lab artifact is required to run the bundle validator.

## External Inputs and Provenance

The bundle uses the following public/framework inputs:

- `gamma_BI = 0.2375`, imported from LQG black-hole entropy counting as used
  throughout the IO framework.
- `M_U = 4.50e53 kg`, the rounded measured universe mass input used in the IO
  framework.
- `r_s = 6.685e26 m`, the Paper 32 harmonized Schwarzschild radius used for
  the late-time recollapse arithmetic.
- `x = 1.519`, the IO horizon/support ratio.
- `T_IO = 2.6635 K`, the IO interior CMB-temperature branch input.

The bundle includes cross-paper reference values for Papers 24 and 34 only as
version-alignment metadata. Those values are not recomputed here.

