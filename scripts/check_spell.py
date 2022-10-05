"""
Script to check the spelling of one, many or all .po files based
on the custom dictionaries under the 'dictionaries/' directory.
"""

from pathlib import Path
import sys
import tempfile

import pospell

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
        f.write('\n')

# Run pospell either against all files or the file given on the command line
po_files = sys.argv[1:]
if not po_files:
    po_files = Path(".").glob("*/*.po")

errors = pospell.spell_check(po_files, personal_dict=output_filename, language="es_ES")
sys.exit(0 if errors == 0 else -1)
