FEniCS website
==============
This repository contains the (new, not-yet finished) FEniCS website.

Website pages
-------------
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
default style page) or `with_twitter_sidebar` (for a page with a twitter sidebar). If no `layout`
is set, then `default` will be used.

Assets
------
Files in the `assets` folder will be included as part of the website. Images and other files can
be included in this folder.

Navigation bar
--------------
The links included in the navigation bar are defined in [`_data/navbar.yml`](https://github.com/FEniCS/web/blob/main/_data/navbar.yml).
Each link is given a `name`, which will be displayed in the navigation bar; and a `page` which is
the name of a `.md` file (without the `.md` file) relative to the root folder of the repository.
