# Agorakit documentation
This is the documentation for [Agorakit](https://github.com/agorakit/agorakit) (which you can [help with](./docs/en/documentation.md)!)
written in [Markdown](https://www.markdownguide.org/cheat-sheet/) and built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Each commit to `main` [rebuilds the docs](https://github.com/mhausenblas/mkdocs-deploy-gh-pages) via GitHub Action, publishing it to the special `gh-pages` branch.

## Build the docs locally
This is an advanced setup NOT required to contribute to the docs. It simply lets you run the documentation website on your localhost.

Install MkDocs Material and necessary plugins. On MacOS, use `pip3` instead of `pip`:

    pip install -r requirements.txt

From the root of this repo, start the built-in webserver to preview your work on the documentation:

    mkdocs serve

You should now be able to view the docs at: `http://127.0.0.1:8000/` (paste it in your browser).

To stop serving, use `Ctrl + C` or close the Terminal window. To restart, just use `mkdocs serve` again.

### Troubleshooting

#### command not found: mkdocs
If you get this on MacOS, it's likely not in your `PATH`. Take the output of `python3 -m site --user-base` and add `/bin` to it (ex: `/Users/linc/Library/Python/3.9/bin`), add that as a new line in `/etc/paths` (requires `sudo`), and **restart Terminal**.

#### Error: Config file 'mkdocs.yml' does not exist.
You are not in the root of this repo. Use the `cd` command to move there.
