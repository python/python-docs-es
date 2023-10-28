#!/usr/bin/env python3

import argparse
import functools
from glob import glob
import multiprocessing
from shutil import get_terminal_size
from textwrap import fill

import regex  # fades
import polib  # fades
from tabulate import tabulate   # fades


REVERSE = '\033[7m'
NORMAL = '\033[m'

def _get_file_entries(pattern, width, filename):
    entries = []
    for entry in (entry for entry in polib.pofile(filename) if entry.msgstr):
        match = pattern.search(entry.msgid)
        if match:
            add_str = entry.msgid + " ·filename: " + filename + "·"
            entries.append(
                [
                    fill(add_str, width=width),
                    fill(entry.msgstr, width=width),
                ]
            )
    return entries

def find_in_po(pattern):
    pattern = regex.compile(pattern)
    columns = get_terminal_size().columns
    available_width = columns // 2 - 3

    # Find entries in parallel
    get_file_entries = functools.partial(_get_file_entries, pattern, available_width)
    pool = multiprocessing.Pool()
    all_entries = pool.map(get_file_entries, glob("**/*.po"))
    table = [entry for file_entries in all_entries for entry in file_entries]

    # Create table and highlight results
    table = tabulate(table, tablefmt="fancy_grid")
    for line in table.splitlines():
        match = pattern.search(line)
        if match:
            span = match.span()
            line = (line[:span[0]] + REVERSE + line[span[0]:span[1]] + NORMAL +
                    line[span[1]:])
        print(line)


def parse_args():
    parser = argparse.ArgumentParser(description="Find translated words.")
    parser.add_argument("pattern")
    return parser.parse_args()


def main():
    args = parse_args()
    find_in_po(args.pattern)


if __name__ == "__main__":
    main()
