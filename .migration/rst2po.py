# rst2po.py
# Script to migrate the Python official tutorial that we have already translated in PyAr
# (https://github.com/PyAr/tutorial) from reStructuredText to the new official translation format (.po)
#
# It parses the .rst and compare sentence/paragraph by sentence/paragraph and if the match is exact,
# and there is no translation for that sentence/paragraph it updates the .po file with the translated text
# from the .rst file.

import glob
import os
import polib  # fades


PO_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ))

RST_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'tutorialpyar',
    ))



def get_rst_file(pofilename):
    """Given a .po filename returns the corresponding .rst filename"""
    pass


def get_rst_translation_text(rstfilename, text):
    """Given an rstfilename an a text returns the corresponding translated text if exists"""
    pass


def update_po_translation(pofilename, english, spanish):
    """Update the pofilename with the translated spanish text"""
    pass



for pofilename in glob.glob(PO_DIR + '**/*.po'):
    rstfilename = get_rst_file(pofilename)
    if rst is None:
        continue

    po = polib.pofile(pofilename)
    for entry in po:
        english_text = entry.msgid
        spanish_text = entry.msgstr
        if spanish_text:
            # Do not override already translated text
            continue

        translated_text = get_rst_translation_text(rstfilename, english_text)
        if translated_text is None:
            continue

        update_po_translation(po, english_text, translated_text)
