import collections
import os
import glob

from pprint import pprint

import polib  # fades

PO_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ))


def main():
    files_with_differences = collections.defaultdict(list)

    for i, pofilename in enumerate(glob.glob(PO_DIR + '**/**/*.po')):
        po = polib.pofile(pofilename)
        if po.percent_translated() < 85:
            continue

        for entry in po:
            words = []
            wordsid = wordsstr = list()

            if '*' in entry.msgid or '``' in entry.msgid:
                wordsid = [word for word in entry.msgid.split() if '*' in word or '``' in word]

            if '*' in entry.msgstr or '``' in entry.msgstr:
                wordsstr = [word for word in entry.msgstr.split() if '*' in word or '``' in word]

            if len(wordsid) != len(wordsstr):
                key = pofilename.replace(PO_DIR, '')
                files_with_differences[key].append({
                    'occurrences': entry.occurrences,
                    'words': {
                        'original': wordsid,
                        'translated': wordsstr,
                    },
                })

    return files_with_differences


pprint(main())
