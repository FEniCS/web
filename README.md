# FEniCS website
This repository contains the (new, not-yet finished) FEniCS website.

## Editing this website
To edit this website:

1) Make a new branch (if you have access to push to this repo) or a new fork.

2) Make your changes in your branch/fork.

3) Open a pull request.

If you think something on the website should be change, but you're not sure how to do it,
please [open an issue](https://github.com/FEniCS/web/issues) describing the change you
would like to suggest.

## Code of conduct

When interacting with others (eg when discussing issues or pull requests), you
are expected to follow the FEniCS project [code of conduct](https://fenicsproject.org/code-of-conduct/).

## Structure of this repo

### Website pages
The website is generated from of the content of `.md` files in the main folder and
subfolders (excluding `README.md`). Markdown and HTML can be included in these files.
LaTeX-style maths can be included between `\\(` and `\\)` for inline maths; or `$$` and `$$`
for a block of maths.

At the start of each `.md` file, page setting can be given between two lines containing only `---`.
For example, `index.md` starts with:

```
---
title: FEniCSx
subtitle: fenicsxversion
image: assets/img/headers/design.jpg
layout: with_twitter_sidebar
---
```

The `title` is displayed at the top of the page, with the `subtitle` (optional) below it. The
`image` will be used as the background of the header; if no image is given, a default image will
be used. The `layout` is used to select which layout the page uses: this can be `default` (for a
default style page) or `with_twitter_sidebar` (for a page with a twitter sidebar). If `layout`
is not set, then `default` will be used.

### Assets
Files in the `assets` folder will be included as part of the website. Images and other files can
be included in this folder.

### Navigation bar
The links included in the navigation bar are defined in [`_data/navbar.yml`](https://github.com/FEniCS/web/blob/main/_data/navbar.yml).
Each link is given a `title`, which will be displayed in the navigation bar; and a `page` which will be linked to.
When linking to a `.md` file from the navigation bar, the `.md` should be changed to `.html`.

### Latest versions
The latest released version of FEniCS and FEniCSx (and their release dates) can be set in
[`_config.yml`](https://github.com/FEniCS/web/blob/main/_config.yml).
If you want to display the latest version on the website, you can write `{{ site.fenicsversion }}`
or `{{ site.fenicsxversion }}` so that the values are automatically updated. (If you don't want a
version number to update, do not use these and write the version number.)
