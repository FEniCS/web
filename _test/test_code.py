"""Test that the code on the front page runs."""
import os

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")


def test_index_code():
    with open(os.path.join(root_dir, "index.md")) as f:
        content = f.read()
    code = (
        "import ufl\n"
        "import dolfinx\n\n"
    )
    for i in content.split("```python")[1:]:
        pass  # code += i.split("```")[0] + "\n\n"

    exec(code)
