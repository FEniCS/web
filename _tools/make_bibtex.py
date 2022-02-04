"""Running this file updates the bibtex file from the citations page."""

import os
import re


def parse_paper(content):
    return {i: j for i, j in re.findall(r'([a-zA-Z0-9]+)\s*=\s*"([^\\\"]*)"', content)}


def cap_wrap(text):
    return " ".join(
        "{" + i + "}" if re.search(r"[A-Z]", i[1:]) else i
        for i in text.split(" ")
    )

def bibline(name, value, caps=True):
    assert len(name) < 10
    return f"  {(name + ' ' * 10)[:11]} = {{{cap_wrap(value) if caps else value}}},\n"


def generate_bib(paper):
    if paper["bibtype"] == "article" and "submitted" in paper:
        paper["bibtype"] = "unpublished"
    out = f"@{paper['bibtype']}{{{paper['id']}\n"
    for a in ["title", "author", "journal", "year", "volume", "number"]:
        if a in paper:
            out += bibline(a, paper[a])
    for a in ["doi", "url"]:
        if a in paper:
            out += bibline(a, paper[a], caps=False)
    for a, b in [
        ("booktitle", "book"), ("publisher", "bookpublisher"),
        ("series", "bookseries"), ("volume", "bookvolume"),
        ("chapter", "bookchapter"), ("editor", "bookeditor")
    ]:
        if b in paper:
            out += bibline(a, paper[b])
    if "submitted" in paper:
        out += bibline("note", f"submitted to {paper['submitted']}")
    if "pagestart" in paper:
        if "pageend" in paper:
            out += bibline("pages", f"{{{paper['pagestart']}--{paper['pageend']}}}")
        else:
            out += bibline("pages", f"{{{paper['pagestart']}}}")
    out += "}"

    return out

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../citing/index.md")
    output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets/citations.bib")

    with open(input_file) as f:
        content = f.read()
    bibs = []
    for paper in content.split("{% include _paper.html")[1:]:
        paper = parse_paper(paper.split("%}")[0])
        bibs.append(generate_bib(paper))

    with open(output_file, "w") as f:
        f.write("\n\n".join(bibs) + "\n")
