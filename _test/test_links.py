import pytest
import os
import re


def load_page_list(dir):
    files = []
    for f in os.listdir(dir):
        if f[0] not in [".", "_"]:
            if os.path.isdir(f):
                files += load_page_list(os.path.join(dir, f))
            if f.endswith(".md"):
                files.append((dir, f))
    return files


root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
pagelist = load_page_list(root_dir)


@pytest.mark.parametrize("dir, file", pagelist)
def test_links(dir, file):
    with open(os.path.join(dir, file)) as f:
        page = f.read()
    links = re.findall(r"\[[^\]]+\]\(([^\]\n]+)\)", page)
    links = [i for i in links if not i.startswith("http:")]
    links = [i for i in links if not i.startswith("https:")]
    links = [i for i in links if not i.startswith("mailto:")]
    links = [i for i in links if not i.startswith("/assets/")]

    for i in links:
        print(f"Checking for {i}")
        if i[0] == "/":
            d = root_dir
            i = i[1:]
        else:
            d = dir
        if i.endswith(".html"):
            i = i[:-3] + ".html"

        if i.endswith(".md"):
            f = os.path.join(d, i)
            print(f"    Checking for {f}")
            assert os.path.isfile(f)
        else:
            f = os.path.join(d, i + ".md")
            f2 = os.path.join(d, os.path.join(i, "index.md"))
            print(f"    Checking for {f} or {f2}")
            assert os.path.isfile(f) or os.path.isfile(f2)
