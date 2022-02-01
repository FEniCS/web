"""Test that the code on the front page runs."""
import os
import pytest

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")


def test_index_code(has_fenicsx):
    if not has_fenicsx:
        try:
            import dolfinx  # noaq: F401
        except ImportError:
            pytest.skip("DOLFINx must be installed to run this test.")

    with open(os.path.join(root_dir, "index.md")) as f:
        content = f.read()
    code = (
        "import ufl\n"
        "import dolfinx\n\n"
    )
    for i in content.split("```python")[1:]:
        code += i.split("```")[0] + "\n\n"

    exec(code)
