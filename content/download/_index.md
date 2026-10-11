---
title: Download
url: /download/
# Use the same layout as an ordinary page, rather than Hextra's docs list.
layout: single
aliases:
  # The legacy FEniCS install instructions used to live here.
  - /download/archive/
description: How to install FEniCSx with conda or apt, build it from source, and where to find the source code for UFL, Basix, FFCx and DOLFINx.
---
## Getting started

The latest release of FEniCSx is version {{< param fenicsxversion
>}}, which was released in {{< param fenicsxversiondate >}}. The easiest
way to start using FEniCSx is to install it using
[conda](https://conda.io):
```shell
conda create -n fenicsx-env
conda activate fenicsx-env
conda install -c conda-forge fenics-dolfinx mpich pyvista
```

On Debian or Ubuntu, FEniCSx can be installed via apt:
```shell
sudo add-apt-repository ppa:fenics-packages/fenics
sudo apt update
sudo apt install fenicsx
```


## Other installation options

The source code of all the components of FEniCSx is hosted on
[GitHub](https://github.com/FEniCS/):
- [UFL](https://github.com/FEniCS/ufl)
- [Basix](https://github.com/FEniCS/basix)
- [FFCx](https://github.com/FEniCS/ffcx)
- [DOLFINx](https://github.com/FEniCS/dolfinx)

Detailed instructions for installing FEniCSx from source, or using some
binary distributions can be found [in the installation page of the
DOLFINx docs](https://github.com/FEniCS/dolfinx#installation).


## Complex number support with Debian/Ubuntu

On Debian/Ubuntu, complex number support with PETSc is provided via the
`python3-dolfinx-complex` package:
```shell
sudo apt install python3-dolfinx-complex
```

The Debian/Ubuntu standard installation uses the real number build of
PETSc and SLEPc. To access other builds, set the environment variable
`PETSC_DIR` to point at the required PETSc, and likewise for SLEPc using
`SLEPC_DIR`:
```shell
PETSC_DIR=/usr/lib/petscdir/petsc-complex python3 demo_dolfinx.py
```
```shell
PETSC_DIR=/usr/lib/petscdir/petsc-complex SLEPC_DIR=/usr/lib/slepcdir/slepc-complex python3 demo_dolfinx.py
```
