import collections
import re
import sys
from pathlib import Path
from pprint import pprint
from typing import List

import polib

_patterns = [
    ":c:func:`[^`]+`",
    ":c:type:`[^`]+`",
    ":c:macro:`[^`]+`",
    ":c:member:`[^`]+`",
    ":c:data:`[^`]+`",
    ":py:data:`[^`]+`",
    ":py:mod:`[^`]+`",
    ":func:`[^`]+`",
    ":mod:`[^`]+`",
    ":ref:`[^`]+`",
    ":class:`[^`]+`",
    ":pep:`[^`]+`",
    ":data:`[^`]+`",
    ":exc:`[^`]+`",
    ":term:`[^`]+`",
    ":meth:`[^`]+`",
    ":envvar:`[^`]+`",
    ":file:`[^`]+`",
    ":attr:`[^`]+`",
    ":const:`[^`]+`",
    ":issue:`[^`]+`",
    ":opcode:`[^`]+`",
    ":option:`[^`]+`",
    ":program:`[^`]+`",
    ":keyword:`[^`]+`",
    ":RFC:`[^`]+`",
    ":rfc:`[^`]+`",
    ":doc:`[^`]+`",
    "``[^`]+``",
    "`[^`]+`__",
    "`[^`]+`_",
    "\*\*[^\*]+\*\*",  # bold text between **
    "\*[^\*]+\*",  # italic text between *
]

_exps = [re.compile(e) for e in _patterns]


def get_sphinx_directives(s: str) -> List[str]:
    """
    Parameters:
        string containing the text to translate

    Returns:
        dictionary containing all the placeholder text as keys
        and the correct value.
    """

    output: List[str] = []
    for exp in _exps:
        matches = exp.findall(s)
        for match in matches:
            output.append(match)
            # remove the found pattern from the original string
            s = s.replace(match, "")
    return output

def ind(level=0):
    return f"{' ' * 4 * level}"

if __name__ == "__main__":
    PO_DIR = Path(__file__).resolve().parent.parent
    VENV_DIR = PO_DIR / "venv"

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        files = []
        if filename:
            if Path(filename).is_dir():
                files = [i for i in PO_DIR.glob(f"{filename}/*.po") if not i.is_relative_to(VENV_DIR)]
            elif not Path(filename).is_file():
                print(f"File not found: '{filename}'")
                sys.exit(-1)
            else:
                files = [filename]
    else:
        files = [i for i in PO_DIR.glob("**/**/*.po") if not i.is_relative_to(VENV_DIR)]

    for i, pofilename in enumerate(files):
        print(f"\n> Processing {pofilename}")
        po = polib.pofile(pofilename)

        for entry in po:

            directives_id = get_sphinx_directives(entry.msgid)
            directives_str = get_sphinx_directives(entry.msgstr)

            # Check if any of them is not empty
            if directives_id or directives_str:

                # Check if the directives are the same
                for ori, dst in zip(directives_id, directives_str):
                    if ori == dst:
                        continue

                    if ori != dst:
                        occs = [f"{ind(2)}{t[0]}:{t[1]}" for t in entry.occurrences]
                        print(f"\n{ind(1)}{pofilename}:{entry.linenum}")
                        print(f"\n".join(occs))
                        print(f"{ind(3)}{ori}")
                        print(f"{ind(3)}{dst}")
