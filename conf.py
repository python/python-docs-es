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
#   $ sphinx-build -b html -d _build/doctrees -D language=es . _build/html

import sys
import os
import time
from pathlib import Path

sys.path.append(os.path.abspath('cpython/Doc/tools/extensions'))
sys.path.append(os.path.abspath('cpython/Doc/includes'))

# Import all the Sphinx settings from cpython
# This import will trigger warnings on the 'Include/patchlevel.h'
# not being found, because it execute the content of the whole file,
# and there there is a local call to 'get_header_version' like the one
# we have in a few lines.
sys.path.insert(0, os.path.abspath('cpython/Doc'))
from conf import *

# Call patchlevel with the proper path to get the version from
# instead of hardcoding it
from patchlevel import get_header_version_info
version, release = get_header_version_info(os.path.abspath('cpython/Doc'))

project = 'Python en Español'
year = time.strftime("%Y")
copyright = f'2001-{year}, Python Software Foundation'

html_theme_path = ['cpython/Doc/tools']
templates_path = ['cpython/Doc/tools/templates']
html_static_path = ['cpython/Doc/tools/static']

os.system('mkdir -p cpython/locales/es/')
os.system('ln -nfs `pwd` cpython/locales/es/LC_MESSAGES')

html_short_title = f'Documentación {release}'
html_title = f'Documentación de Python en Español -- {release}'


# Extend settings from upstream
_exclude_patterns = [
    # This file is not included and it's not marked as :orphan:
    'distutils/_setuptools_disclaimer.rst',
    'includes/wasm-notavail.rst',
]
if 'exclude_patterns' in globals():
    exclude_patterns += _exclude_patterns
else:
    exclude_patterns  = _exclude_patterns

_extensions = [
    'sphinx_tabs.tabs',
    'sphinxemoji.sphinxemoji',
]
if 'extensions' in globals():
    extensions += _extensions
else:
    extensions = _extensions


if os.environ.get('SPHINX_GETTEXT') is None:
    # Override all the files from ``.overrides`` directory
    overrides_paths = Path('.overrides')

    for path in overrides_paths.glob('**/*.*'):
        if path.name == 'README.rst' and path.parent == '.overrides':
            continue
        # Skip the files in the .overrides/logo directory
        # to avoid ln issues.
        if str(path.parent).endswith("logo"):
            continue
        destroot = str(path.parent).replace('.overrides', '').lstrip('/')
        outputdir = Path('cpython/Doc') / destroot / path.name
        os.system(f'ln -nfs `pwd`/{path.parent}/{path.name} {outputdir}')

gettext_compact = False
locale_dirs = ['../locales', 'cpython/locales']  # relative to the sourcedir


# NOTE: Read the Docs does not support "multi document output".
# So, we put all the documentation as a single file for now.
_stdauthor = r'Guido van Rossum\\and the Python development team'
latex_documents = [
    ('contents', 'python-docs-es.tex', u'Documentación de Python en Español',
     _stdauthor, 'manual'),
]


def setup(app):

    def add_contributing_banner(app, doctree):
        """
        Insert a banner at the top of the index.

        This way, we can easily communicate people to help with the translation,
        pointing them to different resources.
        """

        if app.builder.format != 'html':
            # Do not include the banner when building with other formats
            # (this is useful when using -b gettext)
            return

        from docutils import nodes, core
        from textwrap import dedent

        message = dedent(f"""\
        ¡Ayúdanos a traducir la documentación oficial de Python al Español!
        Puedes encontrar más información en `Como contribuir </es/{version}/CONTRIBUTING.html>`_.
        Ayuda a acercar Python a más personas de habla hispana.
        """)

        paragraph = core.publish_doctree(message)[0]
        banner = nodes.note(ids=['contributing-banner'])
        banner.append(paragraph)

        for document in doctree.traverse(nodes.document):
            document.insert(0, banner)

    # Change the sourcedir programmatically because Read the Docs always call it with `.`
    app.srcdir = Path(os.getcwd() + '/cpython/Doc')

    app.connect('doctree-read', add_contributing_banner)

    # Import the sphinx-autorun manually to avoid this warning
    # TODO: Remove this code and use just ``extensions.append('sphinx_autorun')`` when
    # that issue gets fixed
    # See https://github.com/WhyNotHugo/sphinx-autorun/issues/17

    # WARNING: the sphinx_autorun extension does not declare if it is safe for
    # parallel reading, assuming it isn't - please ask the extension author to
    # check and make it explicit
    # WARNING: doing serial read
    from sphinx_autorun import RunBlock, AutoRun
    app.add_directive('runblock', RunBlock)
    app.connect('builder-inited', AutoRun.builder_init)
    app.add_config_value('autorun_languages', AutoRun.config, 'env')
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
