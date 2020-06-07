#!/usr/bin/env python3

import argparse
from glob import glob
import os
from textwrap import fill

import regex  # fades
import polib  # fades
from tabulate import tabulate   # fades


def find_in_po(pattern):
    table = []
    try:
        _, columns = os.popen("stty size", "r").read().split()
        available_width = int(columns) // 2 - 3
    except:
        available_width = 80 // 2 - 3

    for file in glob("**/*.po"):
        pofile = polib.pofile(file)
        for entry in pofile:
            if entry.msgstr and regex.search(pattern, entry.msgid):
                add_str = entry.msgid + " ·filename: " + file + "·"
                table.append(
                    [
                        fill(add_str, width=available_width),
                        fill(entry.msgstr, width=available_width),
                    ]
                )
    print(tabulate(table, tablefmt="fancy_grid"))


def parse_args():
    parser = argparse.ArgumentParser(description="Find translated words.")
    parser.add_argument("pattern")
    return parser.parse_args()


def main():
    args = parse_args()
    find_in_po(args.pattern)


if __name__ == "__main__":
    main()
