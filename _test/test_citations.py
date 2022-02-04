"""Test that the code on the front page runs."""
import os
import re


def test_citation_list():
    root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

    with open(os.path.join(root_dir, "citing/index.md")) as f:
        content = f.read()
    papers = set(re.findall(r'id\s*=\s*"([^"]+)"', content))

    with open(os.path.join(root_dir, "assets/citations.bib")) as f:
        content = f.read()
    papers2 = set(re.findall(r'@[^\{]+\{\s*([^,]+)\s*,', content))

    assert papers == papers2
