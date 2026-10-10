# FEniCS website
This repository contains the FEniCS website. It is built with
[Hugo](https://gohugo.io) using the [Hextra](https://imfing.github.io/hextra/)
theme.

## Editing this website
To edit this website:

1) Make a new branch (if you have access to push to this repo) or a new fork.

2) Make your changes in your branch/fork.

3) Open a pull request.

If you think something on the website should be change, but you're not sure how to do it,
please [open an issue](https://github.com/FEniCS/web/issues) describing the change you
would like to suggest.

When a pull request is opened, the website will be build and an artifact of this build will be uploaded.
To see what the website will look look like after the pull request is merged, you can:

1) Download the artifact

2) unzip the artifact

3) Run `python -m http.server` in the unzipped folder

## Code of conduct

When interacting with others (eg when discussing issues or pull requests), you
are expected to follow the FEniCS project [code of conduct](https://fenicsproject.org/code-of-conduct/).

## Structure of this repo

### Website pages
The website is generated from the `.md` files in the `content` folder.
Markdown and HTML can be included in these files. LaTeX-style maths can be
included between `\\(` and `\\)` for inline maths; or `$$` and `$$` for a
block of maths. A page that contains maths must set `math: true` in its page
settings. (A lone `$` is not a maths delimiter, so dollar amounts such as
`$500` can be written as they are.)

At the start of each `.md` file, page settings can be given between two lines containing only `---`.
For example, `content/conference/2027.md` starts with:

```
---
title: FEniCS 2027
subtitle: "BAM, Berlin, Germany,<br>30 June-2 July 2027"
image: /assets/img/fenics2027/bam2.jpg
imageFit: cover
url: /fenics-2027/
---
```

The `title` is displayed at the top of the page, with the `subtitle` (optional) below it. The
`image` will be used as the background of the header; if no image is given, a default image will
be used. `imageFit` controls how that image is sized: `cover` fills the header
and crops the image (use this for photographs), while the default scales the
image to the height of the header (use this for logos and maps). `url` sets the
address of the page: for example, if set to `/fenics/`, the page would be
available at `https://fenicsproject.org/fenics/`. Every page must set a `url`,
except the front page (`content/_index.md`).

Links from one page to another are written as the full address of the target
page, for example `[the download page](/download/)`.

### Shortcodes
Pieces of markup that appear on several pages are written as *shortcodes*,
which live in `layouts/_shortcodes`. They are used like this:

```
{{< image src="/assets/img/numfocus.png" alt="NumFOCUS" link="https://www.numfocus.org/" >}}
```

The shortcodes defined by this website are `image` (an image placed to the
centre, left or right of the page), `paper` (a cited publication), `person` (a
member of the FEniCS community, as used on the "People of FEniCS" page),
`quote` (a pull quote), and `buttons`/`button` (the large icon links on the
front page). Each file in `layouts/_shortcodes` documents the settings it
takes. The [Hextra
shortcodes](https://imfing.github.io/hextra/docs/guide/shortcodes/) are also
available, including `gallery`, `callout`, `cards` and `details`.

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

### Navigation bar
The links included in the navigation bar are defined under `menu.main` in
[`hugo.yaml`](https://github.com/FEniCS/web/blob/main/hugo.yaml).
Each link is given a `name`, which will be displayed in the navigation bar; and either a
`url` (for an external link) or a `pageRef` (the `url` of a page of this website).

### Latest versions
The latest released version of FEniCS and FEniCSx (and their release dates) can be set in
[`hugo.yaml`](https://github.com/FEniCS/web/blob/main/hugo.yaml).
If you want to display the latest version on the website, you can write `{{< param fenicsversion >}}`
or `{{< param fenicsxversion >}}` so that the values are automatically updated. (If you don't want a
version number to update, do not use these and write the version number.) In a
page's `subtitle`, write `{fenicsversion}` or `{fenicsxversion}` instead.

## Building the website
The prerequisites for building the website are
[Hugo](https://gohugo.io/installation/) (the *extended* edition) and
[Go](https://go.dev/doc/install), which Hugo uses to download the theme. On
Ubuntu these can be installed by running:

```bash
sudo snap install hugo
sudo apt-get install -y golang-go
```

The website can then be built by running:

```bash
hugo
```

which writes the website to the `public` folder. The website can be served
locally (so it can then be opened in a browser) by running:

```bash
hugo server
```

## Deployment
The website is deployed to GitHub Pages by the
[deploy workflow](https://github.com/FEniCS/web/blob/main/.github/workflows/deploy.yml)
when a change is pushed to `main`. This requires the "Source" setting under
Settings &rarr; Pages to be set to "GitHub Actions".
