"""
Script to generate the 'dict.txt' dictionary based
on the custom dictionaries under the 'dictionaries/' directory.
"""

from pathlib import Path

entries = set()

# Read custom dictionaries
for filename in Path("dictionaries").glob("*.txt"):
    with open(filename, "r") as f:
        entries.update(
            stripped_line
            for stripped_line in (line.strip() for line in f.readlines())
            if stripped_line
        )

# Write the 'dict.txt' file
with open("dict.txt", "w") as f:
    for e in entries:
        f.write(e)
        f.write("\n")
print("Created 'dict.txt'")
