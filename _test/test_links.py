"""Test links."""

import collections
import os
import re

import pytest
import yaml

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
content_dir = os.path.join(root_dir, "content")
static_dir = os.path.join(root_dir, "static")


def load_page_list(dir):
    """Load a list of the markdown files that make up the website."""
    files = []
    for f in sorted(os.listdir(dir)):
        path = os.path.join(dir, f)
        if os.path.isdir(path):
            files += load_page_list(path)
        elif f.endswith(".md"):
            files.append((dir, f))
    return files


def front_matter(content):
    """Return the front matter of a page as a dictionary."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.S)
    assert match is not None
    return yaml.load(match.group(1), Loader=yaml.FullLoader)


def page_url(dir, file):
    """Return the URL that a page is published at."""
    with open(os.path.join(dir, file)) as f:
        data = front_matter(f.read())
    if "url" in data:
        return data["url"]
    # Only the home page is allowed to fall back to its position on disk.
    assert (dir, file) == (content_dir, "_index.md")
    return "/"


pagelist = load_page_list(content_dir)
url_of = {(dir, file): page_url(dir, file) for dir, file in pagelist}
urls = list(url_of.values())


@pytest.mark.parametrize("page", [
    "/",
    "/code-of-conduct/",
    "/fenics17/",
    "/fenics18/",
    "/fenics19/",
    "/fenics-2021/",
    "/fenics-2022/",
    "/google-summer-of-code-2017/",
    "/google-summer-of-code-2018/",
    "/people-of-fenics/",
    "/gsoc/",
])
def test_urls(page):
    """Test that a URL that the website has always had still exists."""
    assert page in urls


@pytest.mark.parametrize("dir, file", pagelist)
def test_url_is_set(dir, file):
    """Check that a page sets the URL it is published at."""
    url = url_of[dir, file]
    assert url.startswith("/") and url.endswith("/")


def test_no_duplicate_urls():
    """Check that no two pages are published at the same URL."""
    repeated = [u for u, n in collections.Counter(urls).items() if n > 1]
    assert repeated == []


@pytest.mark.parametrize("dir, file", pagelist)
def test_links(dir, file):
    """Test that links on a page point to pages that exist."""
    with open(os.path.join(dir, file)) as f:
        page = f.read()
    # Links in commented-out draft content are not checked.
    page = re.sub(r"<!--.*?-->", "", page, flags=re.S)
    links = re.findall(r"\[[^\]]+\]\(([^\)\n]+)\)", page)
    links += re.findall(r'(?:href|src|link)\s*=\s*"([^"]+)"', page)

    external_links = [
        i for i in links
        if i.startswith("http:") or i.startswith("https:")]
    for i in external_links:
        print(f"Checking {i}")
        if "fenicsproject.org" in i and "docs.fenicsproject.org" not in i:
            assert "/pub/" in i or "/olddocs/" in i

    links = [i for i in links if not re.match(r"(https?|mailto|data):", i)]
    links = [i for i in links if not i.startswith("//")]
    links = [i.split("#")[0] for i in links]
    links = [i for i in links if i != ""]

    for i in links:
        print(f"Checking for {i}")
        # Links within the website are absolute.
        assert i.startswith("/"), f"{i} is not an absolute link"
        if i in urls:
            continue
        # Otherwise it must be a file in static/.
        assert os.path.isfile(os.path.join(static_dir, i[1:])), \
            f"{i} is neither a page nor a file in static/"


def test_header_links():
    """Test that links in the navigation bar point to pages that exist."""
    with open(os.path.join(root_dir, "hugo.yaml")) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    for i in config["menu"]["main"]:
        if "pageRef" not in i:
            continue
        page = i["pageRef"]
        print(f"Checking {page}")
        assert page in urls
