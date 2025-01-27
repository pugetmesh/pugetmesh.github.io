# Contributing

## Install requirements

- Python 3.11 or newer
- VENV is highly recommended
- Linux-based host highly recommended

## Setup

```sh
# create a venv at project root with name of {path}
python3 -m venv {path} # will be gitignored or untracked
source {path}/bin/activate # prompt prefix changes to named venv

# install prereqs
pip install mkdocs
pip install -r requirements.txt
pip install mkdocs-material
```

## Dev Interactively

```sh
mkdocs serve
```

Changes made to files in `docs/` will be reflected in the browser session.

## References

- [MKDocs Installation](https://www.mkdocs.org/getting-started/)
- [Mkdocs-material Installation](https://squidfunk.github.io/mkdocs-material/getting-started/)
