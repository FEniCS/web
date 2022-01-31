---
title: FEniCSx
subtitle: fenicsxversion
image: assets/img/headers/design.jpg
layout: with_twitter_sidebar
---

## The FEniCSx computing platform

FEniCSx is a popular open-source 
([LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.en.html)) computing 
platform for solving partial differential equations (PDEs). FEniCSx 
enables users to quickly translate scientific models into efficient 
finite element code. With the high-level Python and C++ interfaces to 
FEniCSx, it is easy to get started, but FEniCSx offers also powerful 
capabilities for more experienced programmers. FEniCSx runs on a 
multitude of platforms ranging from laptops to high-performance 
clusters.

## Solving a PDE in FEniCSx

As an illustration of how to program a simple PDE model with FEniCSx, consider the Stokes 
equations in variational form:

$$
\int_{\Omega} \mathrm{grad} \, u : \mathrm{grad} \, v \,\mathrm{d}x \, -
\int_{\Omega} p \, \mathrm{div} \, v \,\mathrm{d}x +
\int_{\Omega} \mathrm{div} \, u \, q \,\mathrm{d}x =
\int_{\Omega} f \cdot v \,\mathrm{d}x.
$$

The variational problem is easily transcribed into Python using mathematical operators in FEniCSx:

```python
# Define function space
P2 = ufl.VectorElement("CG", ufl.tetrahedron, 2)
P1 = ufl.FiniteElement("CG", ufl.tetrahedron, 1)
TH = ufl.MixedElement([P2, P1])
W = dolfinx.fem.FunctionSpace(mesh, TH)

# Define variational problem
(u, p) = ufl.TrialFunctions(W)
(v, q) = ufl.TestFunctions(W)
a = inner(grad(u), grad(v))*dx - p*div(v)*dx + div(u)*q*dx
L = dot(f, v)*dx

# Compute solution
solver = dolfinx.fem.LinearProblem(
    a, L, bcs, petsc_options={"ksp_type": "preonly", "pc_type": "lu",
                              "pc_factor_mat_solver_type": "mumps"})
solver.solve()
```

The above code snippet also shows how to define a suitable finite element
function space, using continuous piecewise quadratic vector-valued functions
for the velocity and continuous piecewise linear functions for the pressure
(Taylor-Hood). The computational domain and mesh are also easily created with
[gmsh](https://gmsh.info/), here defined by three spheres immersed in a 3D
channel.

![Stokes example](/assets/img/stokesexample.png){: .image-center }

```python
h = 0.25
r = 0.3*h
box = model.occ.addBox(0, 0, 0, 1, h, h)
s0 = model.occ.addSphere(0.3, 0.50*h, 0.50*h, r)
s1 = model.occ.addSphere(0.5, 0.65*h, 0.65*h, r)
s2 = model.occ.addSphere(0.7, 0.35*h, 0.35*h, r)

domain = model.occ.cut([(3, box)], [(3, s0), (3, s1), (3, s2)])

model.occ.synchronize()
model.mesh.generate(3)
```

## High-performance computing

![An example image](/assets/img/tc_vm.png){: .image-left }
Each component of the FEniCSx platform has been fundamentally designed for parallel processing. 
Executing a FEniCSx script in parallel is as simple as calling `mpirun -np 64 python script.py`. 
This framework allows for rapid prototyping of finite element formulations and solvers on 
laptops and workstations, and the same code may then be deployed on large high-performance 
computers.

The figure shows the von Mises stresses computed from a nonlinear thermomechanical FEniCSx 
simulation of a turbocharger. The finite element system of linear equations comprises more 
than \\(3.3 \times 10^9\\) degrees of freedom. The solver was initially developed on a desktop computer 
for a small scale problem, and the same code was then deployed on a supercomputer using over 
24,000 parallel processes.

## Installation and documentation

FEniCSx is available for a range of platforms (Linux, Mac, Windows). Choose between Docker 
containers, binary packages, Spack packages and source code. Visit our [installation page](download/index.md) to get the latest 
version of FEniCSx. FEniCSx comes with [extensive documentation](documentation/index.md) and numerous examples. A good 
starting point is the [FEniCSx Tutorial](https://jorgensd.github.io/dolfinx-tutorial/).

## About
The FEniCSx Project is developed and maintained as a freely available, open-source project by a 
global community of scientists and software developers. The project is developed by the FEniCS 
Community, is [governed](governance/index.md) by the [FEniCS Steering Council](governance/steering-council.md) and is overseen by the
[FEniCS Advisory Board](governance/advisory-board.md).

FEniCS is a [NumFOCUS](https://www.numfocus.org/) fiscally supported project. If you like FEniCS and want to support our 
mission to produce the best possible platform for open-source computing, consider making a 
donation to our project.

[![NumFOCUS](/assets/img/numfocus.png){: .image-center }](https://www.numfocus.org/)
