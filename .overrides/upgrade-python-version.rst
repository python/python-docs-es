=======================================
 How to update to a new Python version
=======================================

We are currently in branch 3.7, and we want to update the strings from 3.8.


#. Fetch the `lastet commit of 3.8 branch <https://github.com/python/cpython/commit/70fe95cdc9ac1b00d4f86b7525dca80caf7003e1>`_::

   git fetch --depth 1 origin 70fe95cdc9ac1b00d4f86b7525dca80caf7003e1

#. Checkout that commit locally::

   git checkout 70fe95cdc9ac1b00d4f86b7525dca80caf7003e1

#. Create the .po files from the new source code. This will generate all the .po files for version 3.8::

   SPHINX_GETTEXT=True sphinx-build -j auto -b gettext -d _build/doctrees . ../pot

#. Now we have to merge our current translation .po files with the new .po files that come from upstream::

   pomerge --from-files **/*.po --to-files ../pot/**/*.pot

   .. note::

      In ../pot, we will have the new .pot files with new strings from 3.8 branch,
      with all the translations from our current 3.7 branch.
      If there wasn't a translation found, it is left unstranlated.

#. Remove `python-docs-cpython/` prefix::

   sed -i **/*.pot -e "s|python-docs-es/cpython/||g"

#. Rename all the .pot files to .po files::

#. Move all the newly pot files created to our repository::
