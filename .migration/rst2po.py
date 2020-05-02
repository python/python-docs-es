# rst2po.py
# Script to migrate the Python official tutorial that we have already translated in PyAr
# (https://github.com/PyAr/tutorial) from reStructuredText to the new official translation format (.po)
#
# It parses the .rst and compare sentence/paragraph by sentence/paragraph and if the match is exact,
# and there is no translation for that sentence/paragraph it updates the .po file with the translated text
# from the .rst file.

import re
import glob
import os
import polib  # fades


PO_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ))

RST_TRADUCIDOS_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'tutorialpyar',
        'traducidos',
    ))

RST_ORIGINAL_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'tutorialpyar',
        'original',
    ))



def get_rst_file(pofilename):
    """Given a .po filename returns the corresponding .rst filename"""
    basename = os.path.basename(pofilename)
    basename, ext = basename.split('.')
    rstfilename = os.path.join(RST_TRADUCIDOS_DIR, f'{basename}.rst')
    if os.path.exists(rstfilename):
        return rstfilename


def get_rst_original_filename(rstfilename):
    if rstfilename.endswith('real-index.rst'):
        rst_original_filename = 'index.rst'

    rst_original_filename = os.path.join(RST_ORIGINAL_DIR, rst_original_filename)
    if os.path.exists(rst_original_filename):
        return rst_original_filename


def create_english_spanish_sentences(rstfilename):
    """Create a tuple of (english, spanish) sentences for rstfilename"""

    # NOTE: we could use docutils and parse the rst in the correct way, but
    # that will probably take more time

    with open(rstfilename) as fd:
        lines = []
        for line in fd.read().splitlines():
            if re.match('^[a-zA-Z] ', line):
                # keep text lines only
                lines.append(line)
        # make the document just one line so we can split it in sentences
        document = ' '.join(lines)
        import pdb; pdb.set_trace()


def get_rst_translation_text(rstfilename, text):
    """Given an rstfilename an a text returns the corresponding translated text if exists"""
    pass


def update_po_translation(pofilename, english, spanish):
    """Update the pofilename with the translated spanish text"""
    pass


for pofilename in glob.glob(PO_DIR + '**/*/*.po'):
    rstfilename = get_rst_file(pofilename)
    if rstfilename is None:
        continue

    create_english_spanish_sentences(rstfilename)

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

        entry.msgstr = translated_text
        # update_po_translation(po, english_text, translated_text)
    po.save(pofilename)
