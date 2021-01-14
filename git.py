import sys
import os
from github import Github

folder = str(sys.argv[1])
path = os.environ.get('Progs')      #Add project directory to env, Name it 'Progs' or change here
token = os.environ.get('GitToken')  #Add Github token to env, Name it 'GitToken' or change it here
_dir = path + '/' + folder

g=Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(folder)

#Commands to create files and perform inital commit
commands = [f'echo "# {repo.name}" >> README.md',
			f'echo "#{repo.name}" >> main.{sys.argv[2]}',
            'git init',
            f'git remote add origin https://github.com/{login}/{folder}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

#Create and navigate to correct directory
if sys.argv[2] == "py" or sys.argv[2] == "java":
    os.mkdir(_dir)
    os.chdir(_dir)

    for c in commands:
        os.system(c)

    os.system('code .')

else:
    print("create <fldername>")
