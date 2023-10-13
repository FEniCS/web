"""Test that the code on the front page runs."""
import os
import pytest

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

with open(os.path.join(root_dir, "index.md")) as f:
    content = f.read()
codes = [i.split("```")[0]
         for i in content.split("```python")[1:]]

imports = [
    "import ufl\n"
    "import dolfinx\n"
    "import dolfinx.fem\n"
    "import dolfinx.fem.petsc\n"
    "import dolfinx.mesh\n"
    "from mpi4py import MPI\n"
    "from ufl import inner, grad, dx, div, dot\n"
    "\n"
    "mesh = dolfinx.mesh.create_unit_cube(MPI.COMM_WORLD, 2, 3, 4)\n"
    "f = ufl.grad(ufl.SpatialCoordinate(mesh)[1])\n"
    "bcs = []"
]

assert len(codes) == len(imports)


@pytest.mark.parametrize("code, preamble", zip(codes, imports))
def test_index_code(code, preamble, has_fenicsx):
    if not has_fenicsx:
        try:
            import dolfinx  # noqa: F401
        except ImportError:
            pytest.skip("DOLFINx must be installed to run this test.")

    exec(preamble + "\n\n" + code)
