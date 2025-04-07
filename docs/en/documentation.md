# Contribute to documentation

NOTE: New translations, editing, more visuals or examples, and any fixes are welcome!

## How it works

Documentation is written in Markdown and the website is statically built using [Mkdocs material](https://squidfunk.github.io/mkdocs-material/) (see: [Getting Started](https://squidfunk.github.io/mkdocs-material/getting-started/)). It is served by GitHub Pages via [this workflow](https://github.com/agorakit/documentation/actions/workflows/ci.yml).
Each commit to `main` [rebuilds the docs](https://github.com/mhausenblas/mkdocs-deploy-gh-pages) via GitHub Action, publishing it to the special `gh-pages` branch.

## Editing docs
- Create a GitHub account
- Edit the docs directly in your browser, creating a new branch and submitting a PR (against `main`) with the GitHub.com UI.

For more advanced editing, fork it like you would a code repository and submit pull requests to `main`. You'll find the Markdown files under `/docs`.

## Build the docs

NOTE: This is an advanced setup NOT required to contribute to the docs!

Install mkdocs material and a few plugins:

    pip install -r requirements.txt

Start the built-in webserver to preview your work on the documentation:

    mkdocs serve

That should get you started.