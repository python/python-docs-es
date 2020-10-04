# Use together with `pageviews.py`
# python scripts/pageviews.py | head -n 150 | grep -v whats | cut -d ' ' -f 2 | sed 's/\.html/\.po/g' | xargs -I '{}' python scripts/create_issue.py '{}'

import os
import sys
from pathlib import Path

from github import Github
from potodo._po_file import PoFileStats

if len(sys.argv) != 2:
    print('Specify PO filename')
    sys.exit(1)

pofilename = sys.argv[1]
pofile = PoFileStats(Path(pofilename))

g = Github(os.environ.get('GITHUB_TOKEN'))

repo = g.get_repo('python/python-docs-es')


issues = repo.get_issues(state='all')
for issue in issues:
    if pofilename in issue.title:

        print(f'Skipping {pofilename}. There is a similar issue already created at {issue.html_url}')
        sys.exit(1)

        msg = f'There is a similar issue already created at {issue.html_url}.\nDo you want to create it anyways? [y/N] '
        answer = input(msg)
        if answer != 'y':
            sys.exit(1)

if any([
    pofile.translated_nb == pofile.po_file_size,
    pofile.untranslated_nb == 0,
]):
    print(f'Skipping {pofilename}. The file is 100% translated already.')
    sys.exit(1)

# https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_issue
title = f'Translate `{pofilename}`'
urlfile = pofilename.replace('.po', '.html')
issue = repo.create_issue(
    title=title,
    body=f'''This needs to reach 100% translated.

The rendered version of this file will be available at https://docs.python.org/es/3.8/{urlfile} once translated.
Meanwhile, the English version is shown.

Current stats for `{pofilename}`:

- Fuzzy: {pofile.fuzzy_nb}
- Percent translated: {pofile.percent_translated}%
- Entries: {pofile.translated_nb} / {pofile.po_file_size}
- Untranslated: {pofile.untranslated_nb}

Please, comment here if you want this file to be assigned to you and an member will assign it to you as soon as possible, so you can start working on it.

Remember to follow the steps in our [Contributing Guide](https://python-docs-es.readthedocs.io/page/CONTRIBUTING.html).''',
)
print(f'Issue "{title}" created at {issue.html_url}')
