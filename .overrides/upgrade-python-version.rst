:orphan:

How to update to a new Python version
=====================================

We are currently in branch 3.11, and we want to update the strings from 3.12.

#. Make sure you are in a clean state of the branch 3.11

#. Create a new branch called ``3.12``

#. Initialize the submodules::

     git submodule init
     git submodule update

#. Fetch the `latest commit of 3.12 branch <https://github.com/python/cpython/commit/0fb18b02c8ad56299d6a2910be0bab8ad601ef24>`_::

     cd cpython/
     git fetch --depth 1 origin 0fb18b02c8ad56299d6a2910be0bab8ad601ef24

   .. note:: you could also base the hash on the 'git tag' from the desired
             version: ``git checkout tags/v3.12.0 -b 3.12`` considering that
             ``3.12`` doesn't exist locally.

#. Checkout that commit locally::

     git checkout 0fb18b02c8ad56299d6a2910be0bab8ad601ef24

#. Update the branch on the ``Makefile`` and check the ``requirements.txt`` from
   ``./cpython/Doc`` directory, to see if upgrades on the modules like sphinx is
   needed.

#. Commit the update of the submodule change::

     git add cpython
     git commit -m "Update the cpython submodule"

   .. note:: This is important, so the later ``make build`` step will not reset
             the cpython submodule to the previous hash on the old branch.

#. Create a virtual environment and install the dependencies of the project::

     python -m venv env
     source env/bin/activate  # Windows: env\Scripts\activate.bat
     pip install -r requirements.txt
     
#. Verify that the docs build with the new versions you changed from
   ``requirements.txt`` mainly the sphinx version::

     make build

   .. note::

      It may fail the build because there may be files
      that don't exist anymore in the new branch.
      If that's the case, just continue with the steps
      and verify the build later.

#. Clean possible garbage (form previous builds)::

     rm -rf _build ../python-docs-es-pot cpython/Doc/CONTRIBUTING.rst cpython/Doc/upgrade-python-version.rst reviewers-guide.rst

   .. note::

      The 'python-docs-es-pot' is a temporary directory that is created
      in the next step. It's included here because it might be a leftover
      from previous attempts on your machine.

#. Create the .po files from the new source code. This will generate all the .po files for version 3.11::

     SPHINX_GETTEXT=True sphinx-build -j auto -b gettext -d _build/doctrees . ../python-docs-es-pot

   .. note::

      In ``../python-docs-es-pot`` directory, we will have the new .pot files with new strings from 3.12 branch.
      All these strings will be *untranslated* at this point.

#. Now, we update our translated files form the source language (English) with new strings::

     sphinx-intl update --language es --pot-dir ../python-docs-es-pot --locale-dir cpython/locales/

#. At this point, all the ``.po`` files will have a different comment on each translation phrase,
   for example::

     -#: ../python-docs-es/cpython/Doc/whatsnew/3.12.rst:3
     +#: ../Doc/whatsnew/3.12.rst:3

   As you can see, it added the path of the local repository, but you can
   remove it from it with this regular expression::

     sed -i **/*.po -e "s|python-docs-es/cpython/||g"

   .. note::

      If you have your local repository cloned with a different name,
      please make sure to adapt the expression.

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

#. Upgrade GitHub Actions to use Python 3.12, by updating Python version to 3.12 in the ``.github/workflows/main.yml`` file.

#. Update the *Read the Docs* project to use 3.12 in the build and also as default branch/version.
	
#. Commit all the newly created files locally.
	
#. Create branch 3.12 in the repository in order to merge changes there.
	
#. Inside the github project settings, set 3.12 branch as the default branch for the repository.

