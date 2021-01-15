import sys
import os

folder = str(sys.argv[1])
path = os.environ.get('Progs')
_dir = path + '/' + folder

commands = [f'echo "# {sys.argv[1]}" >> README.md',
			f'echo "#{sys.argv[1]}" >> main.{sys.argv[2]}']

os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)

os.system('echo Project not uploaded to Github')
os.system('code .')