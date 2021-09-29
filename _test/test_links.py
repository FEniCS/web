"""Test links."""

import pytest
import os
import yaml
import re


def load_page_list(dir):
    """Load a list of md files."""
    files = []
    for f in os.listdir(dir):
        if f[0] not in [".", "_"]:
            if os.path.isdir(f):
                files += load_page_list(os.path.join(dir, f))
            if f.endswith(".md") and f != "README.md":
                files.append((dir, f))
    return files


root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
pagelist = load_page_list(root_dir)

permalinks = []
for dir, p in pagelist:
    with open(os.path.join(dir, p)) as f:
        content = f.read()
    if "---\n" in content:
        data = content.split("---\n")[1]
        if "permalink:" in data:
            permalinks.append(
                data.split("permalink:")[1].split("\n")[0].strip())


@pytest.mark.parametrize("page", [
    "code-of-conduct",
    "fenics17",
    "fenics18",
    "fenics19",
    "fenics-2021",
    "google-summer-of-code-2017",
    "google-summer-of-code-2018",
    "people-of-fenics",
])
def test_permalinks(page):
    """Test that permalink exists."""
    assert page in permalinks


@pytest.mark.parametrize("dir, file", pagelist)
def test_permalink_is_set(dir, file):
    """Check that page has a permalink defined."""
    if (dir != root_dir or file != "index.md") and file != "404.md":
        with open(os.path.join(dir, file)) as f:
            page = f.read()
        assert "---\n" in page
        assert "permalink:" in page.split("---\n")[1]


@pytest.mark.parametrize("dir, file", pagelist)
def test_links(dir, file):
    """Test that links on a page point to pages that exists."""
    with open(os.path.join(dir, file)) as f:
        page = f.read()
    links = re.findall(r"\[[^\]]+\]\(([^\]\n]+)\)", page)

    external_links = [
        i for i in links
        if i.startswith("http:") or i.startswith("https:")]
    for i in external_links:
        if "fenicsproject.org" in i:
            assert "/pub/" in i or "/olddocs/" in i

    links = [i for i in links if not i.startswith("http:")]
    links = [i for i in links if not i.startswith("https:")]
    links = [i for i in links if not i.startswith("mailto:")]

    assets = [i[1:] for i in links if i.startswith("/assets/")]
    links = [i for i in links if not i.startswith("/assets/")]

    # Check that links within the website point to pages that exists
    for i in links:
        print(f"Checking for {i}")
        if i[0] == "/":
            d = root_dir
            i = i[1:]
        else:
            d = dir

        assert i.endswith(".md")

        f = os.path.join(d, i)
        assert os.path.isfile(f)

    # Check that assets exist
    for i in assets:
        f = os.path.join(root_dir, i)
        assert os.path.isfile(f)


def test_header_links():
    """Test that links in header point to pages that exist."""
    with open(os.path.join(root_dir, "_data/navbar.yml")) as f:
        nav = yaml.load(f, Loader=yaml.FullLoader)

    for i in nav:
        page = i["page"]
        print(f"Checking {page}")
        if page.startswith("http:"):
            continue
        if page.startswith("https:"):
            continue
        if page.startswith("mailto:"):
            continue

        assert page[0] == "/"
        assert page[1:] in permalinks
