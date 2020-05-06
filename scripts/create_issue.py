import os
import sys
import subprocess
import print_percentage

from github import Github


if len(sys.argv) != 2:
    print('Specify PO filename')
    sys.exit(1)

pofilename = sys.argv[1]
percentage = print_percentage.get_percent_translated(pofilename)

g = Github(os.environ.get('GITHUB_TOKEN'))

repo = g.get_repo('PyCampES/python-docs-es')
# https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_issue
issue = repo.create_issue(
    title=f'Translate `{pofilename}`',
    body=f'''This file is at {percentage}% translated. It needs to reach 100% translated.

Please, comment here if you want this file to be assigned to you and an member will assign it to you as soon as possible, so you can start working on it.

Remember to follow the steps in our [Contributing Guide](https://python-docs-es.readthedocs.io/es/3.7/CONTRIBUTING.html)''',
)
print(f'Issue created at {issue.html_url}')
