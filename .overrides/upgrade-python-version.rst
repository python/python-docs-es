:orphan:

How to update to a new Python version
=====================================

We are currently in branch 3.10, and we want to update the strings from 3.11.


#. Make sure you are in a clean state of the branch 3.10

#. Create a new branch called ``3.11``

#. Initialize the submodules::

     git submodule init
     git submodule update

#. Fetch the `latest commit of 3.11 branch <https://github.com/python/cpython/commit/69b6b56d857440183e227ca0b10c84bca4239985>`_::

     cd cpython/
     git fetch --depth 1 origin b3cafb60afeb2300002af9982d43703435b8302d

   .. note:: you could also base the hash on the 'git tag' from the desired
             version: ``git checkout tags/v3.11.0 -b 3.11`` considering that
             ``3.11`` doesn't exist locally.

#. Checkout that commit locally::

     git checkout 69b6b56d857440183e227ca0b10c84bca4239985

#. Update the branch on the ``Makefile`` and check the ``requirements.txt`` from
   the cpython repository, to see if upgrades on the modules like sphinx is
   needed.

#. Commit the update of the submodule change::

     git add cpython
     git commit -m "Update the cpython submodule"

   .. note:: This is important, so the later ``make build`` step will not reset
             the cpython submodule to the previous hash on the old branch.

#. Verify that the docs build with the new versions you changed from
   ``requirements.txt`` mainly the sphinx version::

     make html

   .. note::

      It may fail the build because there may be files
      that don't exist anymore in the new branch.
      If that's the case, just continue with the steps
      and verify the build later.

#. Clean possible garbage (form previous builds)::

     rm -rf _build ../python-docs-es-pot cpython/Doc/CONTRIBUTING.rst cpython/Doc/upgrade-python-version.rst

   .. note::

      The 'python-docs-es-pot' is a temporary directory that is created
      in the next step. It's included here because it might be a leftover
      from previous attempts on your machine.

#. Create a virtual environment and install the dependencies of the project::

     python -m venv env
     source env/bin/activate  # Windows: env\Scripts\activate.bat
     pip install -r requirements.txt


#. Create the .po files from the new source code. This will generate all the .po files for version 3.11::

     SPHINX_GETTEXT=True sphinx-build -j auto -b gettext -d _build/doctrees . ../python-docs-es-pot

   .. note::

      In ``../python-docs-es-pot`` directory, we will have the new .pot files with new strings from 3.11 branch.
      All these strings will be *untranslated* at this point.

#. Now, we update our translated files form the source language (English) with new strings::

     sphinx-intl update --language es --pot-dir ../python-docs-es-pot --locale-dir cpython/locales/

#. At this point, all the ``.po`` files will have a different comment on each translation phrase,
   for example::

     -#: ../python-docs-es/cpython/Doc/whatsnew/3.11.rst:3
     +#: ../Doc/whatsnew/3.11.rst:3

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


Once the process is completely and you are happy with the results,
there are a few extra steps to finish the process::

#. Upgrade GitHub Actions to use Python 3.11

#. Update Read the Docs project to use 3.11 in the build and also as default branch/version
