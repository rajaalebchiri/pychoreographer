"""Sphinx configuration."""
from datetime import datetime


project = "Pychoreographer"
author = "Rajaa Lechiri"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.intersphinx", "myst_parser"]
intersphinx_mapping = {"mypy": ("https://mypy.readthedocs.io/en/stable/", None)}  # noqa
language = "en"
html_theme = "furo"
linkcheck_ignore = [
    "codeofconduct.html",
    "https://github.com/PyCQA/flake8-bugbear#",
    "https://github.com/peterjc/flake8-rst-docstrings#",
    "https://github.com/pre-commit/pre-commit-hooks#",
    "https://github.com/pycqa/pep8-naming#",
    "https://github.com/terrencepreilly/darglint#",
    "https://github.com/PyCQA/mccabe#",
    "https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases/tag/",  # noqa
    "https://cookiecutter-hypermodern-python.readthedocs.io",
    "https://badgen.net/badge/status/alpha/d8624d",
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]
