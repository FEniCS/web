# FEniCS website

This repository contains the FEniCS website. It is built with
[Hugo](https://gohugo.io) using the [Hextra](https://imfing.github.io/hextra/)
theme.

## Editing this website

To edit this website:

1. Make a new branch (if you have access to push to this repo) or a new fork.
2. Make your changes in your branch/fork.
3. Open a pull request.

If you think something on the website should be changed, but you're not sure
how to do it, please [open an issue](https://github.com/FEniCS/web/issues)
describing the change you would like to suggest.

When a pull request is opened, the website will be built and an artifact of
this build will be uploaded. To see what the website will look like after the
pull request is merged, you can:

1. Download the artifact.
2. Unzip the artifact.
3. Run `python3 -m http.server` in the unzipped folder, and open
   <http://localhost:8000> in a browser.

## Code of conduct

When interacting with others (eg when discussing issues or pull requests), you
are expected to follow the FEniCS project
[code of conduct](https://fenicsproject.org/code-of-conduct/).

## Structure of this repo

### Website pages

The website is generated from the `.md` files in the `content` folder. The
folders inside `content` are there to keep related pages together: they do not
affect the address of a page, which is set by `url` (see below). The page that
introduces a folder is called `_index.md`; the rest are named after their
contents, for example `content/conference/2027.md`.

Markdown and HTML can be included in these files. LaTeX-style maths can be
included between `\(` and `\)` for inline maths; or between `$$` and `$$` (or
`\[` and `\]`) for a block of maths. A lone `$` is not a maths delimiter, so
dollar amounts such as `$500` can be written as they are.

A block of maths may run over several lines, but no line of it may begin with
a character that starts a Markdown block, such as `+` or `-`: Markdown claims
the line before the maths is recognised, and the equation comes out as a
bullet list. Put such operators at the end of the previous line instead.

At the start of each `.md` file, page settings can be given between two lines
containing only `---`. For example, `content/conference/2027.md` starts with:

```yaml
---
title: FEniCS 2027
subtitle: "BAM, Berlin, Germany,<br>30 June-2 July 2027"
image: /assets/img/fenics2027/bam2.jpg
imageFit: cover
url: /fenics-2027/
---
```

The `title` is displayed at the top of the page, with the `subtitle` (optional)
below it. The `subtitle` may contain HTML, so `<br>` can be used to break it
over several lines.

The `image` will be used as the background of the header; if no image is given,
a default image will be used. `imageFit` controls how that image is sized:

- `cover` fills the header and crops the image: use this for photographs;
- `auto` (the default when an `image` is given) scales the image to the height
  of the header: use this for logos and maps;
- `tile` repeats the image at its own size.

`url` sets the address of the page: for example, if set to `/fenics/`, the page
would be available at `https://fenicsproject.org/fenics/`. Every page must set
a `url`, except the front page (`content/_index.md`). If a page is moved to a
new address, list the old one under `aliases` so that the old address redirects
to the new one.

Two further settings are occasionally useful: `headerLogo: true` puts the
FEniCS logo above the title (used on the front page), and `hideHeader: true`
leaves the header off altogether.

Links from one page to another are written as the full address of the target
page, for example `[the download page](/download/)`.

### Shortcodes

Pieces of markup that appear on several pages are written as *shortcodes*,
which live in `layouts/_shortcodes`. They are used like this:

```text
{{< image src="/assets/img/numfocus.png" alt="NumFOCUS"
          link="https://www.numfocus.org/" >}}
```

A shortcode may be written on one line or, as above, spread over several.

The shortcodes defined by this website are:

- `image`, an image placed to the centre, left or right of the page;
- `paper`, a cited publication;
- `person`, a member of the FEniCS community, as used on the "People of FEniCS"
  page;
- `quote`, a pull quote;
- `buttons` and `button`, the large icon links on the front page.

Each file in `layouts/_shortcodes` documents the settings it takes. The
[Hextra shortcodes](https://imfing.github.io/hextra/docs/guide/shortcodes/) are
also available, including `gallery`, `callout`, `cards` and `details`.

The `person` shortcode shows a flag next to the person's name. The country
names it understands are listed in `data/flags.yaml`.

Icons are referred to by name, for example `{{< icon "github" >}}`. The
[available icons](https://imfing.github.io/hextra/docs/guide/shortcodes/icon/)
come from the theme.

### Assets

Files in the `static` folder are copied to the website as they are: a file at
`static/assets/img/example.png` is served at
`https://fenicsproject.org/assets/img/example.png`. Images and other files such
as PDFs can be put in this folder.

Files in the `assets` folder are processed by Hugo before being included. This
is where the website's stylesheet (`assets/css/custom.css`) lives.

The website is set in [Inter](https://github.com/rsms/inter), which is served
from `static/assets/fonts` rather than from a font service, so that opening a
page makes no third-party request. See the README in that folder.

### Navigation bar

The links included in the navigation bar are defined under `menu.main` in
[`hugo.yaml`](https://github.com/FEniCS/web/blob/main/hugo.yaml). Each link is
given a `name`, which will be displayed in the navigation bar; a `weight`,
which sets the order the links appear in; and either a `url` (for an external
link) or a `pageRef` (the `url` of a page of this website).

### Latest versions

The latest released version of FEniCS and FEniCSx (and their release dates) can
be set in [`hugo.yaml`](https://github.com/FEniCS/web/blob/main/hugo.yaml). If
you want to display the latest version on the website, you can write
`{{< param fenicsversion >}}` or `{{< param fenicsxversion >}}` so that the
values are automatically updated. (If you don't want a version number to
update, do not use these and write the version number.) In a page's `subtitle`,
write `{fenicsversion}` or `{fenicsxversion}` instead.

## Building the website

The prerequisites for building the website are
[Hugo](https://gohugo.io/installation/) and [Go](https://go.dev/doc/install),
which Hugo uses to download the theme. Hugo must be the *extended* edition: the
packages below are all extended, as is any download whose name contains
`extended`. Running `hugo version` will tell you which edition you have.

On macOS, using [Homebrew](https://brew.sh):

```bash
brew install hugo go
```

On Ubuntu:

```bash
sudo snap install hugo
sudo apt-get install -y golang-go
```

### Viewing the website locally

To build the website and serve it on your own machine, run:

```bash
hugo server
```

from the folder you cloned this repository into, then open
<http://localhost:1313> in a browser. The pages in the browser update as you
edit and save files, so you can leave this running while you work. Press Ctrl+C
to stop it.

The first run downloads the theme, so it needs a network connection and takes a
little longer than later ones.

### Building the website to a folder

To write the website to the `public` folder instead of serving it, run:

```bash
hugo
```

Opening the files in `public` directly will not work, because the pages link to
each other by absolute address. To look at them, serve the folder:

```bash
python3 -m http.server --directory public
```

and open <http://localhost:8000>. This is also how to view the artifact that is
built for a pull request.

### Updating the theme

The version of the Hextra theme that the website is built with is recorded in
`go.mod` and `go.sum`. To move to a newer version of the theme, run:

```bash
hugo mod get -u github.com/imfing/hextra
```

and commit the changes to those two files.

## Tests

The tests in `_test` check that every page sets a `url`, that no two pages
share one, that links point at pages and files that exist, and that the version
numbers in `hugo.yaml` match the latest DOLFINx release. They are run by the
[test workflow](https://github.com/FEniCS/web/blob/main/.github/workflows/run-tests.yml),
and can be run locally with:

```bash
python3 -m pip install pytest -r _test/requirements.txt
python3 -m pytest _test/
```

If you add a page, the link test will fail until the page sets a `url`. Links
inside HTML comments are not checked, so a draft that is commented out may
contain placeholder addresses.

## Deployment

The website is deployed to GitHub Pages by the
[deploy workflow](https://github.com/FEniCS/web/blob/main/.github/workflows/deploy.yml)
when a change is pushed to `main`. This requires the "Source" setting under
Settings → Pages to be set to "GitHub Actions".
