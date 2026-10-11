# Notes for coding agents

This repository is the FEniCS Project website: a [Hugo](https://gohugo.io)
static site using the [Hextra](https://imfing.github.io/hextra/) theme. It is
mostly prose. Changes here are read by the public, so accuracy of the content
matters more than cleverness of the templates.

Read `README.md` first — it is written for human contributors and explains
page settings, shortcodes and how to build. This file covers what that one
does not: the things that will otherwise cost you an hour.

## Checking your work

Hugo (the *extended* edition) and Go are required; `hugo version` must report
`+extended`. The first build downloads the theme, so it needs a network.

```bash
hugo --minify --printPathWarnings --panicOnWarning   # what CI runs; must be silent
python3 -m pytest _test/test_links.py _test/test_citations.py   # offline, fast
python3 -m flake8 _test/ _tools/
```

`hugo server` serves <http://localhost:1313>. Prefer `--renderToMemory`: a
server left running in the background writes into `public/`, which will
quietly corrupt any comparison you make against a build.

To prove a refactor changed nothing, build before and after and diff the two
`public/` trees. Normalise first — fingerprinted filenames (`*.HASH.css`) and
`integrity="…"` attributes change whenever any asset changes, and nothing
else will differ.

## Rules

**Never edit the theme.** Hextra is a Go module pinned in `go.mod`. To read
it, `hugo mod vendor`, inspect `_vendor/github.com/imfing/hextra/`, then
`rm -rf _vendor` — it must never be committed. `hugo mod verify` checks the
cached copy is untouched.

**Do not override theme templates.** There are no copies of Hextra's layouts
here any more and it should stay that way: a copy silently stops tracking the
theme and nothing fails when it goes stale. Extend through the documented
hooks in `layouts/_partials/custom/` instead (`page-begin`, `content-begin`,
`content-end`, `page-end`, `head-end`, `footer`, `banner`, `navbar-title`).
`layouts/404.html` is the single exception — Hextra's 404 is a standalone
document that runs through no hooks, and this one carries the redirect for
legacy `/pub/`, `/olddocs/` and `/qa/` addresses.

**Every page sets `url:`**, which is the address it is published at; only
`content/_index.md` does not. These are inherited from the Jekyll site and
are load-bearing — changing one breaks inbound links. If a page must move,
list the old address under `aliases:`.

**A page that introduces a folder** (`_index.md`) also needs `layout: single`.
Without it Hextra lays it out as a documentation index, with a left sidebar
and a left-aligned title, which matches nothing else on the site.

**Links between pages are written as full addresses** — `[the download
page](/download/)`, not a relative path to a `.md` file.

**Prefer a shortcode to raw HTML.** The site defines `image`, `paper`,
`person`, `quote` and `buttons`/`button`; Hextra adds `cards`, `callout`,
`gallery`, `details`, `icon` and more. Each file in `layouts/_shortcodes/`
documents its own parameters.

## Traps

**Maths.** Inline is `\( … \)`; block is `$$ … $$` or `\[ … \]`. A lone `$`
is deliberately not a delimiter, so `$500` is safe. In a block spanning
several lines, **no line may begin with `+` or `-`** — Markdown claims it as
a list before the maths extension sees it, and the equation renders as
bullets with the backslashes stripped. Put operators at the end of the
previous line.

**`_tools/make_bibtex.py` will damage `static/assets/citations.bib`.** The
committed file is hand-curated — fuller author names, a legacy section — and
the tool regenerates a reduced version from `content/citing/_index.md`. Do
not run it casually. `_test/test_citations.py` only compares citation *keys*,
so it will not notice.

**The full test suite is slow and flaky locally.** `_test/test_version_numbers.py`
queries the GitHub API, which rate-limits unauthenticated callers; it will
hang once you have made a few calls. Run the two offline test files instead,
and let CI run the rest with a token.

**HTML comments do not reach the published site.** `--minify` strips them, so
commented-out draft sections in `content/` are not visible in page source.
Anything inside one is also skipped by the link test.

**The footer sits just below the fold in a headless screenshot.** Hextra
gives the article a `min-height` of `100vh - navbar`, so the footer is always
one pixel past whatever window size you choose. To photograph it, inject
`[class*="min-h"]{min-height:0 !important}` temporarily, and remove it after.

## Deployment

Pushing to `main` runs `.github/workflows/deploy.yml`, which publishes to
GitHub Pages. This needs Settings → Pages → Source set to "GitHub Actions".
The Hugo version is pinned once, in `.github/actions/setup-hugo/action.yml`.

`.github/workflows/run-tests.yml` is currently **disabled by GitHub** for
inactivity, so the Python tests do not run in CI until someone re-enables it.
It also still runs in a DOLFINx container that nothing under `_test/` needs.
