"""
Script to check the spelling of one, many or all .po files based
on the custom dictionaries under the 'dictionaries/' directory.
"""

from pathlib import Path
import shutil
import sys
import tempfile

import polib
import pospell


def check_spell(po_files=None):
    """
    Check spell in the given list of po_files and log the spell errors details.

    If no po_files are given, check spell in all files.

    args:
        po_files: list of po_files paths.

    returns:
        - int: spell errors count.

    """
    # Read custom dictionaries
    entries = set()
    for filename in Path("dictionaries").glob("*.txt"):
        with open(filename, "r") as f:
            entries.update(
                stripped_line
                for stripped_line in (line.strip() for line in f.readlines())
                if stripped_line
            )

    # Write merged dictionary file
    output_filename = tempfile.mktemp(suffix="_merged_dict.txt")
    with open(output_filename, "w") as f:
        for e in entries:
            f.write(e)
            f.write("\n")

    # Run pospell either against all files or the file given on the command line
    if not po_files:
        po_files = list(Path(".").glob("*/*.po"))

    # Workaround issue #3324 FIXME
    # It seems that all code snippets have line breaks '\n'. This causes the
    # currently indentation issues.

    # Create temporary copies of the original files.
    po_files_tmp = []
    for po_file in po_files:
        with open(tempfile.mktemp(), "wb") as temp_file:
            with open(po_file, "rb") as original_file:
                shutil.copyfileobj(original_file, temp_file)
                po_files_tmp.append(temp_file.name)

        # Don't translate probably code entries
        polib_temp_file = polib.pofile(temp_file.name)
        for entry in polib_temp_file:
            if "\n" in entry.msgid:
                entry.msgstr = ""
        polib_temp_file.save()

    detected_errors = pospell.spell_check(po_files_tmp, personal_dict=output_filename, language="es_ES")
    if detected_errors:
        for tmp, orig in zip(po_files_tmp, po_files):
            print(tmp, " == ", orig)
    return detected_errors


if __name__ == "__main__":
    po_files = sys.argv[1:]
    errors = check_spell(po_files)
    sys.exit(0 if errors == 0 else -1)
