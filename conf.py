# Sphinx configuration file.
#
#  - import original configurations from cpython/Doc/conf.py
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

# Import all the Sphinx settings from cpython
sys.path.append(os.path.abspath('cpython/Doc'))
from conf import *

version = '3.7'
release = '3.7.7'

project = 'Python en Español'
copyright = '2001-%s, Python Software Foundation' % time.strftime('%Y')

html_theme_path = ['cpython/Doc/tools']
templates_path = ['cpython/Doc/tools/templates']
html_static_path = ['cpython/Doc/tools/static']

os.system('mkdir -p cpython/locales/es/')
os.system('ln -nfs `pwd` cpython/locales/es/LC_MESSAGES')

gettext_compact = False
locale_dirs = ['../locales', 'cpython/locales']  # relative to the sourcedir

def setup(app):
    # Change the sourcedir programmatically because Read the Docs always call it with `.`
    app.srcdir = 'cpython/Doc'
