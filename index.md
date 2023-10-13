---
title: FEniCSx
image: assets/img/headers/design.jpg
---

## The FEniCSx computing platform

FEniCSx is a popular open-source computing platform for solving partial
differential equations (PDEs). FEniCSx enables users to quickly
translate scientific models into efficient finite element code. With the
high-level Python and C++ interfaces to FEniCSx, it is easy to get
started, but FEniCSx offers also powerful capabilities for more
experienced programmers. FEniCSx runs on a multitude of platforms
ranging from laptops to high-performance clusters.

## Solving a PDE in FEniCSx

As an illustration of how to program a simple PDE model with FEniCSx,
consider the Stokes equations in variational form:

$$
\int_{\Omega} \mathrm{grad} \, u : \mathrm{grad} \, v \,\mathrm{d}x \, -
\int_{\Omega} p \, \mathrm{div} \, v \,\mathrm{d}x +
\int_{\Omega} \mathrm{div} \, u \, q \,\mathrm{d}x =
\int_{\Omega} f \cdot v \,\mathrm{d}x.
$$

The variational problem is easily transcribed into Python using
mathematical operators in FEniCSx:

```python
# Define function space
P2 = ufl.VectorElement("Lagrange", ufl.tetrahedron, 2)
P1 = ufl.FiniteElement("Lagrange", ufl.tetrahedron, 1)
TH = ufl.MixedElement([P2, P1])
W = dolfinx.fem.FunctionSpace(mesh, TH)

# Define variational problem
(u, p) = ufl.TrialFunctions(W)
(v, q) = ufl.TestFunctions(W)
a = inner(grad(u), grad(v)) * dx - p * div(v) * dx + div(u) * q * dx
L = inner(f, v) * dx

# Compute solution
solver = dolfinx.fem.petsc.LinearProblem(
    a, L, bcs, petsc_options={"ksp_type": "preonly", "pc_type": "lu",
                              "pc_factor_mat_solver_type": "mumps"})
solver.solve()
```

The above code snippet also shows how to define a suitable finite
element function space, using continuous piecewise quadratic
vector-valued functions for the velocity and continuous piecewise linear
functions for the pressure (Taylor-Hood). The computational domain and
mesh are also easily created with [gmsh](https://gmsh.info/), here
defined by three spheres immersed in a 3D channel.

![Stokes example](/assets/img/stokesexample.png){: .image-center }


## High-performance computing

![An example image](/assets/img/tc_vm.png){: .image-left }
Each component of the FEniCSx platform has been fundamentally designed
for parallel processing. Executing a FEniCSx script in parallel is as
simple as calling `mpirun -np 64 python script.py`. This framework
allows for rapid prototyping of finite element formulations and solvers
on laptops and workstations, and the same code may then be deployed on
large high-performance computers.

The figure shows the von Mises stresses computed from a nonlinear
thermomechanical FEniCSx simulation of a turbocharger. The finite
element system of linear equations comprises more than \\(3.3 \times
10^9\\) degrees of freedom. The solver was initially developed on a
desktop computer for a small scale problem, and the same code was then
deployed on a supercomputer using over 24,000 parallel processes.

## Installation and documentation

FEniCSx is available for a range of platforms (Linux, Mac, Windows).
Choose between Docker containers, binary packages, Spack packages and
source code. Visit our [installation page](download/index.md) to get the
latest version of FEniCSx. FEniCSx comes with
[extensive documentation](documentation/index.md) and numerous examples.

## FEniCSx vs legacy FEniCS

In 2018, work started on FEniCSx: the new version of the FEniCS library.
FEniCSx has a number of major improvements over the legacy library,
including support for a wide range of cell types and elements, memory
parallelisation, and complex number support, as well as a large number
of improvements to the overall library design. FEniCSx is comprised of
the libraries UFL, Basix, FFCx and DOLFINx. The latest version of
FEniCSx ({{ site.fenicsxversion }}) was released in
{{ site.fenicsxversiondate }}.

Now that development is focussed on FEniCSx, updates are made very
rarely to the legacy FEniCS library. We recommend that users consider
using FEniCSx instead of the legacy library. Lecacy FEniCS is comprised
of the libraries UFL, FIAT, FFC and DOLFIN. The latest version of legacy
FEniCS ({{ site.fenicsversion }}) was released in
{{ site.fenicsversiondate }}.

## About

FEniCS is a [NumFOCUS](https://www.numfocus.org/) fiscally supported
project. If you like FEniCS and want to support our mission to produce
the best possible platform for open-source computing, consider making a
donation to our project.

[![NumFOCUS](/assets/img/numfocus.png){: .image-center }](https://www.numfocus.org/)
