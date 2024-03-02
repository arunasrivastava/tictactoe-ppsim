# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# -- Project information -----------------------------------------------------

project = 'ppsim'
copyright = '2021, Eric Severson and David Doty'
author = 'Eric Severson and David Doty'

# to get this to work on readthedocs, following the advice here in how to configure readthedocs
# (briefly, we have to enable a virtualenv for readthe docs so it can compile the Cython extension
# to be able to import it, to be able to create the docs):
# https://stackoverflow.com/questions/13238736/how-to-document-cython-function-on-readthedocs


# this is ugly, but appears to be standard practice:
# https://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package/17626524#17626524
def extract_version(filename: str):
    with open(filename) as f:
        lines = f.readlines()
    version_comment = '# version line; WARNING: do not remove or change this line or comment'
    for line in lines:
        if version_comment in line:
            idx = line.index(version_comment)
            line_prefix = line[:idx]
            parts = line_prefix.split('=')
            parts = [part.strip() for part in parts]
            version_str = parts[-1]
            version_str = version_str.replace('"', '')
            version_str = version_str.replace("'", '')
            version_str = version_str.strip()
            return version_str
    raise AssertionError(f'could not find version in {filename}')

version = extract_version('../ppsim/__version__.py')
print(f'ppsim version = {version}')

# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# next line puts type of each function parameter next to description of parameter
autodoc_typehints = "description"

# make sure __init__ constructor gets documented
autoclass_content = 'both'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# This line was causing a warning
# html_static_path = ['_static']

# sort by order methods appear in source code
# https://stackoverflow.com/questions/37209921/python-how-not-to-sort-sphinx-output-in-alphabetical-order
autodoc_member_order = 'bysource'