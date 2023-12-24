"""
Script to identify and complete general index entries with original content.

This script processes .po files, identifies out-of-order entries based on the
source order, and completes them with original content.

Usage:
    python script_name.py [list of .po files]

If no list of .po files is provided, the script processes all .po files in the
current directory and its immediate subdirectories.
"""

from pathlib import Path
import sys

import polib


def out_of_order_entries(po_file):
    """
    Compare the order of source lines against the order in which they appear in
    the file, and return a generator with entries that are out of order.
    """
    po_entries = [entry for entry in po_file if not entry.obsolete]
    val_max = 0

    for entry in po_entries:
        source_index = int(entry.occurrences[0][1])

        if source_index <= val_max:
            yield entry

        val_max = max(val_max, source_index)


def complete_index(po_files=None):
    """
    Identifies general index entries based on source order and completes them
    with original content.

    args:
        po_files: List of .po files to process. If not provided, it processes
        all .po files in the current directory and immediate subdirectories.
   """

    # Read .po files
    if not po_files:
        po_files = Path(".").glob("**/*.po")

    for po_file_path in po_files:

        try:
            po_file = polib.pofile(po_file_path, wrapwidth=79)

            # Ask to complete entries out of order with original text
            needs_save = False
            for entry in out_of_order_entries(po_file):
                user_input = input(f"\n{entry}\nIs this a index entry? (y/N):")
                if user_input.lower() == "y":
                    entry.msgstr = entry.msgid
                    needs_save = True
            if needs_save:
                po_file.save()

        except KeyboardInterrupt:
            break

        except Exception as e:
            print(f"Error! file {po_file_path}: {e}\n")

        else:
            print(f"\n---\n{po_file_path} processed!\n---")


if __name__ == "__main__":
    po_files = sys.argv[1:]
    complete_index(po_files)
