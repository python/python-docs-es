import os
import re
import sys
from typing import Dict, Tuple

import polib

VERBOSE = False
DEBUG = False
SKIP_TRANSLATED_ENTRIES = True

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("Error: This util script needs `deep_translator` to be installed")
    sys.exit(1)

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
    ":source:`[^`]+`",
    ":manpage:`[^`]+`",
    ":sup:`[^`]+`",
    "``[^`]+``",
    "`[^`]+`__",
    "`[^`]+`_",
    "\*\*[^\*]+\*\*",  # bold text between **
    "\*[^\*]+\*",  # italic text between *
]

_exps = [re.compile(e) for e in _patterns]

def protect_sphinx_directives(s: str) -> Tuple[dict, str]:
    """
    Parameters:
        string containing the text to translate

    Returns:
        dictionary containing all the placeholder text as keys
        and the correct value.
    """

    i = 0
    d: Dict[str, str] = {}
    for exp in _exps:
        matches = exp.findall(s)
        if DEBUG:
            print(exp, matches)
        for match in matches:
            ph = f"XASDF{str(i).zfill(2)}"
            s = s.replace(match, ph)
            if ph in d and VERBOSE:
                print(f"Error: {ph} is already in the dictionary")
                print("new", match)
                print("old", d[ph])
            d[ph] = match
            i += 1
    return d, s


def undo_sphinx_directives_protection(placeholders: dict, translated_text: str) -> str:
    for ph, value in placeholders.items():
        translated_text = translated_text.replace(ph, value)
        if DEBUG:
            print(ph, value)
            print(translated_text)
    return translated_text


if __name__ == "__main__":
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"File not found: '{filename}'")
        sys.exit(-1)

    po = polib.pofile(filename)
    translator = GoogleTranslator(source="en", target="es")

    for entry in po:
        # If the entry has already a translation, skip.
        if SKIP_TRANSLATED_ENTRIES and entry.msgstr:
            continue

        print("\nEN|", entry.msgid)
        placeholders, temp_text = protect_sphinx_directives(entry.msgid)
        if VERBOSE:
            print(temp_text)
            print(placeholders)

        # Translate the temporary text without sphinx statements
        translated_text = translator.translate(temp_text)

        # Recover sphinx statements
        real_text = undo_sphinx_directives_protection(placeholders, translated_text)
        print("ES|", real_text)

        # Replace the po file translated entry
        entry.msgstr = real_text

    # Save the file after all the entries are translated
    po.save()
