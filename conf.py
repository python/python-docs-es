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

import sys, os, time
sys.path.append(os.path.abspath('cpython/Doc/tools/extensions'))
sys.path.append(os.path.abspath('cpython/Doc/includes'))

# Import all the Sphinx settings from cpython
sys.path.append(os.path.abspath('cpython/Doc'))
from conf import *

# Call patchlevel with the proper path to get the version from
# instead of hardcoding it
import patchlevel
version, release = patchlevel.get_header_version_info(os.path.abspath('cpython/Doc'))

project = 'Python en Español'
copyright = '2001-%s, Python Software Foundation' % time.strftime('%Y')

html_theme_path = ['cpython/Doc/tools']
templates_path = ['cpython/Doc/tools/templates']
html_static_path = ['cpython/Doc/tools/static']

os.system('mkdir -p cpython/locales/es/')
os.system('ln -nfs `pwd` cpython/locales/es/LC_MESSAGES')

html_short_title = f'Documentación {release}'
html_title = f'Documentación de Python en Español -- {release}'

exclude_patterns = [
    # This file is not included and it not marked as :orphan:
    'distutils/_setuptools_disclaimer.rst',
    'README.rst',
]

if not os.environ.get('SPHINX_GETTEXT') == 'True':
    # Override all the files from ``.overrides`` directory
    import glob
    for root, dirs, files in os.walk('.overrides'):
        for fname in files:
            if fname == 'README.rst' and root == '.overrides':
                continue
            destroot = root.replace('.overrides', '').lstrip('/')
            outputdir = os.path.join(
                'cpython',
                'Doc',
                destroot,
                fname,
            )
            os.system(f'ln -nfs `pwd`/{root}/{fname} {outputdir}')

gettext_compact = False
locale_dirs = ['../locales', 'cpython/locales']  # relative to the sourcedir


# NOTE: Read the Docs does not support "multi document output".
# So, we put all the documentation as a single file for now.
_stdauthor = r'Guido van Rossum\\and the Python development team'
latex_documents = [
    ('contents', 'python-docs-es.tex', u'Documentación de Python en Español',
     _stdauthor, 'manual'),
]

extensions.extend([
    'sphinx_tabs.tabs',
    'sphinxemoji.sphinxemoji',
])


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

        message = '¡Ayúdanos a traducir la documentación oficial de Python al Español! ' \
        f'Puedes encontrar más información en `Como contribuir </es/{version}/CONTRIBUTING.html>`_.  ' \
        'Ayuda a acercar Python a más personas de habla hispana.'

        paragraph = core.publish_doctree(message)[0]
        banner = nodes.warning(ids=['contributing-banner'])
        banner.append(paragraph)

        for document in doctree.traverse(nodes.document):
            document.insert(0, banner)

    # Change the sourcedir programmatically because Read the Docs always call it with `.`
    app.srcdir = 'cpython/Doc'

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
