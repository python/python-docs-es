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
    for pofilename in glob.glob(PO_DIR + '**/tutorial/*.po'):
        po = polib.pofile(pofilename)
        file_per = po.percent_translated()
        print(f"{pofilename} ::: {file_per}%")


if __name__ == "__main__":
    main()
