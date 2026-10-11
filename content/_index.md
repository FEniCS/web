---
title: FEniCS
headerLogo: true
toc: false
description: FEniCS is an open-source computing platform for solving partial differential equations with the finite element method, from laptops to high-performance computers.
---

FEniCS is a popular open-source computing platform for solving partial
differential equations (PDEs) with the finite element method (FEM).
FEniCS enables users to quickly translate scientific models into
efficient finite element code. With the high-level Python and C++
interfaces to FEniCS, it is easy to get started, but FEniCS offers also
powerful capabilities for advanced users. FEniCS runs on a multitude of
platforms, ranging from laptops to leadership-class supercomputers.

{{< buttons >}}
  {{< button icon="download" label="Download" href="/download/" >}}
  {{< button icon="book-open" label="Documentation" href="/documentation/" >}}
  {{< button icon="github" label="Source code" href="https://github.com/FEniCS" >}}
{{< /buttons >}}

## Solving a PDE in FEniCS

A finite element problem is written in FEniCS much as it is written on
paper. Take the Stokes equations, which describe slow viscous flow, in
variational form: find a velocity \(u\) and a pressure \(p\) such that

$$
\int_{\Omega} \nabla u : \nabla v \,\mathrm{d}x +
\int_{\Omega} p \, (\nabla \cdot v) \,\mathrm{d}x +
\int_{\Omega} (\nabla \cdot u) \, q \,\mathrm{d}x =
\int_{\Omega} f \cdot v \,\mathrm{d}x
$$

for all test functions \(v\) and \(q\). The heart of the
[Stokes demo](https://docs.fenicsproject.org/dolfinx/v{{< param dolfinxversion >}}/python/demos/demo_stokes.html)
transcribes that almost line for line:

```python
# A Taylor-Hood element: quadratic velocity, linear pressure
P2 = element("Lagrange", msh.basix_cell(), degree=2, shape=(msh.geometry.dim,))
P1 = element("Lagrange", msh.basix_cell(), degree=1)
W = functionspace(msh, mixed_element([P2, P1]))

# The variational problem
(u, p) = ufl.TrialFunctions(W)
(v, q) = ufl.TestFunctions(W)
a = (ufl.inner(ufl.grad(u), ufl.grad(v))
     + ufl.inner(p, ufl.div(v))
     + ufl.inner(ufl.div(u), q)) * ufl.dx
L = ufl.inner(f, v) * ufl.dx

# Solve it
problem = LinearProblem(a, L, bcs=bcs, petsc_options_prefix="stokes_")
wh = problem.solve()
```

You choose the elements, and FEniCS generates and compiles the finite
element code for them. The figure below shows the flow computed for
spheres held in a channel.

{{< image src="/assets/img/stokesexample.png" alt="Streamlines of Stokes flow past three spheres held in a rectangular channel" >}}

<!-- ## Running in parallel

{{< image src="/assets/img/tc_vm.png" alt="Von Mises stresses in a turbocharger, computed with FEniCS" align="right" >}}
Every component of FEniCS is designed for parallel computing. Running a
FEniCS script across 64 processes is no more than
`mpirun -np 64 python script.py`, so a formulation worked out on a
laptop can be taken to a cluster without rewriting it.

The figure shows von Mises stresses from a nonlinear thermomechanical
simulation of a turbocharger, a system of more than
\(3.3 \times 10^{9}\) degrees of freedom. The solver was developed on a
desktop at small scale and then run on a supercomputer across more than
24,000 processes. -->

<!-- ## Support FEniCS -->

FEniCS is a [NumFOCUS](https://www.numfocus.org/) fiscally supported
project. If you like FEniCS and want to support our mission to produce
the best possible platform for open-source finite element computing,
consider making [a donation](https://numfocus.org/donate-to-fenics) to
support FEniCS.

{{< image src="/assets/img/numfocus.png" alt="NumFOCUS" link="https://www.numfocus.org/" width="260px" >}}
