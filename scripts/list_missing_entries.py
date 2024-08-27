import argparse
import dataclasses
import enum
import glob
import itertools
import os

import polib
import tabulate


class MissingReason(enum.StrEnum):
    FUZZY = "fuzzy"
    UNTRANSLATED = "untranslated"

    @staticmethod
    def from_poentry(poentry: polib.POEntry):
        if poentry.fuzzy:
            return MissingReason.FUZZY
        assert not poentry.translated()
        return MissingReason.UNTRANSLATED

@dataclasses.dataclass
class MissingEntry:
    reason: MissingReason
    file: str
    line: int

    @staticmethod
    def from_poentry(pofilename: str, poentry: polib.POEntry) -> "MissingEntry":
        return MissingEntry(MissingReason.from_poentry(poentry), pofilename, poentry.linenum)


def find_missing_entries(filename: str) -> list[MissingEntry]:
    po = polib.pofile(filename)
    fuzzy = po.fuzzy_entries()
    untranslated = po.untranslated_entries()
    return [MissingEntry.from_poentry(filename, entry) for entry in fuzzy + untranslated]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument("-g", "--github-mode", help="Produce output as a GitHub comment", action='store_true')
    opts = parser.parse_args()
    missing_entries = list(itertools.chain.from_iterable(map(find_missing_entries, opts.files)))
    if not missing_entries:
        print(f"All entries translated, horray!{' :tada:' if opts.github_mode else ''}")
    else:
        missing_entries.sort(key = lambda entry: (entry.file, entry.line))
        print("Entries missing translation, details follow:\n")
        print(tabulate.tabulate(missing_entries,headers=["Reason", "File", "Line"], tablefmt="github"))


if __name__ == "__main__":
    main()
