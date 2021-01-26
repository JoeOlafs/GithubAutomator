import sys
import os

folder = str(sys.argv[1])
path = os.environ.get('Progs')
_dir = path + '/' + folder



#os.mkdir(_dir)
os.chdir(_dir)

os.system(f'flutter create {sys.argv[1]}')

os.system('echo Project not uploaded to Github')
os.system('code .')