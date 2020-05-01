# Sphinx configuration file.
#
# Most of the content of this file comes from cpython/Doc/conf.py
# It's modified to:
#  - append the path considering the cpython submodule is at ./cpython
#  - create the symbolic links under ./cpython/locale/es/LC_MESSAGES
#  - make the build to work under Read the Docs
#
# The git submodule was created using this Stack Overflow answer
# to fetch only the commit that I needed and avoid clonning the whole history
# https://stackoverflow.com/a/27445058
#
# This can be built locally using `sphinx-build` by running
#
#   $ sphinx-build -b html -n -d _build/doctrees -D language=es . _build/html

import sys, os, time
sys.path.append(os.path.abspath('cpython/Doc/tools/extensions'))
sys.path.append(os.path.abspath('cpython/Doc/includes'))

# General configuration
# ---------------------

extensions = ['sphinx.ext.coverage', 'sphinx.ext.doctest',
              'pyspecific', 'c_annotations', 'escape4chm']


project = 'Python en Español'
copyright = '2001-%s, Python Software Foundation' % time.strftime('%Y')

release = version = '3.7'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# By default, highlight as Python 3.
highlight_language = 'python3'

# Minimum version of sphinx required
needs_sphinx = '1.8'

# Ignore any .rst files in the venv/ directory.
exclude_patterns = ['venv/*', 'README.rst']

# Avoid a warning with Sphinx >= 2.0
master_doc = 'contents'

# Use our custom theme.
html_theme = 'python_docs_theme'
html_theme_path = ['cpython/Doc/tools']
html_theme_options = {
    'collapsiblesidebar': True,
    'issues_url': 'https://docs.python.org/3/bugs.html',
    'root_include_title': False   # We use the version switcher instead.
}

# Short title used e.g. for <title> HTML tags.
html_short_title = '%s Documentation' % release

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# Path to find HTML templates.
templates_path = ['cpython/Doc/tools/templates']

# Custom sidebar templates, filenames relative to this file.
html_sidebars = {
    # Defaults taken from http://www.sphinx-doc.org/en/stable/config.html#confval-html_sidebars
    # Removes the quick search block
    '**': ['localtoc.html', 'relations.html', 'customsourcelink.html'],
    'index': ['indexsidebar.html'],
}

# Additional templates that should be rendered to pages.
html_additional_pages = {
    'download': 'download.html',
    'index': 'indexcontent.html',
}

# Output an OpenSearch description file.
html_use_opensearch = 'https://docs.python.org/' + version

# Additional static files.
html_static_path = ['cpython/Doc/tools/static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'python' + release.replace('.', '')

# Split the index
html_split_index = True

# Relative filename of the reference count data file.
refcount_file = 'data/refcounts.dat'


os.system('mkdir -p cpython/locales/es/')
os.system('ln -nfs `pwd` cpython/locales/es/LC_MESSAGES')


gettext_compact = False
locale_dirs = ['cpython/locales']


def setup(app):
    # Change the sourcedir programmatically because Read the Docs always call it with `.`
    app.srcdir = 'cpython/Doc'
