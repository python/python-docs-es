:orphan:

How to upgrade to a new Python version
======================================

We are currently in branch 3.13, and we want to update the strings from 3.14.

#. Make sure you are in a clean state of the branch 3.13

#. Create a new branch called ``3.14``

#. Initialize the submodules::

     git submodule init
     git submodule update

#. Fetch the `latest release tag of 3.14  <https://github.com/python/cpython/releases/tag/v3.14.0>`_::

     cd cpython/
     git fetch --depth 1 origin refs/tags/v3.14.0:refs/tags/v3.14.0

#. Checkout that commit locally::

     git checkout tags/v3.14.0 -b 3.14.0

#. Update the branch on the ``Makefile``

#. Commit the update of the submodule change::

     git add cpython
     git commit -m "Update the cpython submodule"

   .. note:: This is important, so the later ``make build`` step will not reset
             the cpython submodule to the previous hash on the old branch.

#. Create a virtual environment and install the dependencies of the project::

     python -m venv env
     source env/bin/activate  # Windows: env\Scripts\activate.bat
     pip install -r requirements.txt

   .. note::
      This might fail if some of our own requirements
      conflict with cpython's. If so, find a way to fix
      *our* requirements.

#. Verify that the docs build with the new versions of the build requirements,
   mainly the sphinx version::

     make build

   .. note::

      The underlying ``sphinx-build`` command uses all available cores by default.
      Use the ``SPHINX_JOBS`` ``make`` variable (defaults to ``auto``)
      to specify an explicit amount, e.g. ``make build SPHINX_JOBS=10``.

   .. note::
      It may fail the build because there may be files
      that don't exist anymore in the new branch.
      If that's the case, just continue with the steps
      and verify the build later.

#. Clean possible garbage (form previous builds)::

     rm -rf _build cpython/python-docs-es-pot cpython/Doc/CONTRIBUTING.rst cpython/Doc/upgrade-python-version.rst reviewers-guide.rst

   .. note::

      The 'python-docs-es-pot' is a temporary directory that is created
      in the next step. It's included here because it might be a leftover
      from previous attempts on your machine.

#. Create the .po files from the new source code. This will generate all the .po files for version 3.14::

     SPHINX_GETTEXT=True sphinx-build -j auto -b gettext -d _build/doctrees . cpython/python-docs-es-pot

   .. note::

      In ``cpython/python-docs-es-pot`` directory, we will have the new .pot files with new strings from 3.14 branch.
      All these strings will be *untranslated* at this point.

#. Now, we update our translated files form the source language (English) with new strings::

     sphinx-intl update --language es --pot-dir cpython/python-docs-es-pot --locale-dir cpython/locales/

#. Pass ``powrap`` to make the column widths consistent::

     powrap --modified

   .. note::

      Make sure you have installed ``gettext``,
      since it's required for the previous command.

#. Prepare for fireworks! Now it's time for an initial build::

     make build

   you will find many warnings that needs to be fixed before the push
   of the new branch is done. So prepare a cup of any hot beverage
   and fix them.

**Once the process is completely and you are happy with the results,
there are a few extra steps to finish the process**

#. Upgrade GitHub Actions to use Python 3.14, by updating Python version to 3.14 in the ``.github/workflows/main.yml`` file.

#. Update the *Read the Docs* project to use 3.14 in the build and also as default branch/version.
	
#. Commit all the newly created files locally.
	
#. Create branch 3.14 in the repository in order to merge changes there.
	
#. Inside the github project settings, set 3.14 branch as the default branch for the repository.

#. Create GitHub issues with [the script](../scripts/create_issue.py) 
