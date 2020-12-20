#!/usr/bin/env python

import glob
import os

import polib  # fades

PO_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ))


def main():
    for pofilename in sorted(glob.glob(PO_DIR + '**/*/*.po')):
        po = polib.pofile(pofilename)
        percent_translated = po.percent_translated()
        if percent_translated > 90:
            pofilename = pofilename.replace(PO_DIR + os.sep, '')
            print(f"{pofilename:<30} :: {percent_translated}%")


if __name__ == "__main__":
    main()
