"""Test that the code on the front page runs."""
import os
import re


def test_citation_list():
    root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

    papers = set()
    for file in ["citing/index.md", "citing/legacy.md"]:
        with open(os.path.join(root_dir, file)) as f:
            content = f.read()
        for id in re.findall(r'id\s*=\s*"([^"]+)"', content):
            papers.add(id)

    papers2 = set()
    for file in ["assets/citations.bib"]:
        with open(os.path.join(root_dir, file)) as f:
            content = f.read()
        for ptype, id in re.findall(r'@([^\{]+)\{\s*([^,\}]+)\s*(?:,|\})', content):
            if ptype != "comment":
                papers2.add(id)

    assert papers == papers2
