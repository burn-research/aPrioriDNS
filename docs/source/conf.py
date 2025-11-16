# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project source code
import os
import sys

# Make sure src is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "src")))

# AutoAPI config
autoapi_type = "python"
autoapi_dirs = [os.path.abspath(os.path.join("..", "..", "src"))]

autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]

# Optional but nice:
autoapi_root = "autoapi"
autoapi_add_toctree_entry = False   # If false, must link it manually from index.rst
autoapi_keep_files = True           # keep generated .rst files in docs/source/autoapi
autoapi_own_page_level = "function"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'aPriori'
copyright = '2025, Lorenzo Piu, Heinz Pitsch, Alessandro Parente'
author = 'Lorenzo Piu'
release = '1.1.10'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",        # Google/Numpy style docstrings
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_autodoc_typehints",
    "autoapi.extension",
]

autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# Allow markdown via MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "smartquotes",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
