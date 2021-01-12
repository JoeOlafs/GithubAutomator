import sys
import os
from github import Github

folder = str(sys.argv[1])
path = os.environ.get('Progs')
token = os.environ.get('GitToken')
_dir = path + '/' + folder

g=Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(folder)

commands = [f'echo "# {repo.name}" >> README.md',
			f'echo "#{repo.name}" >> main.{sys.argv[2]}',
            'git init',
            f'git remote add origin https://github.com/{login}/{folder}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

if sys.argv[2] == "py" or sys.argv[2] == "java":
    os.mkdir(_dir)
    os.chdir(_dir)

    for c in commands:
        os.system(c)

    #os.system(f'echo "#{repo.name}" >> main.py')
    os.system('code .')

else:
    print("create <fldername>")
