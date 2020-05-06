#!/usr/bin/env python

import glob
import os
import sys

import polib  # fades

PO_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ))


def get_percent_translated(pofilename):
    po = polib.pofile(pofilename)
    file_per = po.percent_translated()
    return file_per


def main():
    pofilename = None
    if len(sys.argv) == 2:
        pofilename = sys.argv[1]

    if pofilename:
        file_per = get_percent_translated(pofilename)
        print(f"{pofilename} ::: {file_per}%")

    else:
        for pofilename in glob.glob(PO_DIR + '**/tutorial/*.po'):
            file_per = get_percent_translated(pofilename)
            print(f"{pofilename} ::: {file_per}%")


if __name__ == "__main__":
    main()
