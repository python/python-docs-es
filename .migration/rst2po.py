# rst2po.py
# Script to migrate the Python official tutorial that we have already translated in PyAr
# (https://github.com/PyAr/tutorial) from reStructuredText to the new official translation format (.po)
#
# It parses the .rst and compare sentence/paragraph by sentence/paragraph and if the match is exact,
# and there is no translation for that sentence/paragraph it updates the .po file with the translated text
# from the .rst file.

import polib  # fades
