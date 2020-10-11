import os
import sys

"""
Script to generate the 'dict.txt' dictionary based
on the custom dictionaries under the 'dictionaries/' directory,
but also considering the old words from the 'dict' file.

This was done with:
    awk 1 dict dictionaries/*.txt > dict.txt
but the problem was that windows users, not using Git bash
have the problem that 'awk' is not a valid command, so this
enable them to use the script instead.
"""

entries = set()

# Read custom dictionaries
for name in os.listdir("dictionaries"):
    if name.endswith(".txt"):
        filename = os.path.join("dictionaries", name)
        with open(filename, "r") as f:
            lines = [i.rstrip() for i in f.readlines()]
            if lines:
                entries.update(set(lines))
                del lines

# Remove empty string, from empty lines
entries.remove("")

# Read main 'dict'
with open("dict", "r") as f:
    entries.update(set(i.rstrip() for i in f.readlines()))

# Write the 'dict.txt' file
with open("dict.txt", "w") as f:
    for e in entries:
        f.write(e)
        f.write("\n")
print("Created 'dict.txt'")
