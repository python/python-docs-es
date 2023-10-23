"""
Script to identify and complete general index entries with original content.
"""

import glob
import sys

import polib


def complete_index(po_files=None):
    """
    Identifies general index entries based on source order and completes them
    with original content.

    args:
        po_files: List of .po files to process. If not provided, it processes
        all .po files in the current directory and immediate subdirectories.

    returns:
        str: Files and entries modified.
    """

    # Read .po files
    if not po_files:
        po_files = [f for f in glob.glob("**/*.po", recursive=True)]

    modified_texts = []
    po_entries = []
    for file in po_files:
        try:
            po_file = polib.pofile(file)
            po_entries = [entry for entry in po_file if not entry.obsolete]
            val_max = 0
            marks = []

            # Compare source index with file order and create marks
            for i, entry in enumerate(po_entries):

                source_index = int(entry.occurrences[0][1])
                if source_index <= val_max:
                    marks.append(i)
                val_max = val_max if source_index <= val_max else source_index

            # We only keep the entries that are marked
            po_entries = [j for i, j in enumerate(po_entries) if i in marks]

            # Complete translation with original text
            for entry in po_entries:
                user_input = input(f"\n{entry}\nIs this a index entry? (y/N):")
                if user_input.lower() == "y":
                        entry.msgstr = entry.msgid
                        modified_texts.append(f"Adjusted: {file}\n{entry}")
            po_file.save()

        except Exception as e:
            print(f"{len(modified_texts)} text(s) adjusted.",
                  f"Error! file {file}: {e}\n")
            return 1

    print(f"\n{len(modified_texts)} text(s) adjusted",
          f"{len(po_files)} file(s) processed.")


if __name__ == "__main__":
    po_files = sys.argv[1:]
    results = complete_index(po_files)
    sys.exit(0 if results != 1 else -1)
