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

repo = g.get_repo('PyCampES/python-docs-es')


issues = repo.get_issues(state='open')
for issue in issues:
    if pofilename in issue.title:
        msg = f'There is a similar issue already created at {issue.html_url}.\nDo you want to create it anyways? [y/N] '
        answer = input(msg)
        if answer != 'y':
            sys.exit(1)

# https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_issue
issue = repo.create_issue(
    title=f'Translate `{pofilename}`',
    body=f'''This needs to reach 100% translated.

Current stats for `{pofilename}`:

- Fuzzy: {pofile.fuzzy_nb}
- Percent translated: {pofile.percent_translated}%
- Entries: {pofile.translated_nb} / {pofile.po_file_size}
- Untranslated: {pofile.untranslated_nb}

Please, comment here if you want this file to be assigned to you and an member will assign it to you as soon as possible, so you can start working on it.

Remember to follow the steps in our [Contributing Guide](https://python-docs-es.readthedocs.io/page/CONTRIBUTING.html).''',
)
print(f'Issue created at {issue.html_url}')
