import sys

import icu


collator = icu.Collator.createInstance(icu.Locale())
sorted_entries = sorted(sys.stdin, key=collator.getSortKey)
print("".join(sorted_entries), end='')
