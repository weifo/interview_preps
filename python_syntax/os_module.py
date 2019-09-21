import os
from datetime import datetime

print(os.getcwd())
# 1 change path
# os.chdir('F:/learn-python/flask')

# 2 list files
print(os.listdir())

# 3 make new dir
# os.mkdir('one')
# os.makedirs('./one/sub')

# 4 delete folder
# os.rmdir('one/sub')
# os.removedirs('one/sub')

#5 rename dir 
# os.rename('demo.txt','focus.txt')

# 6 file info
# os.stat('filename')

# 7 walk the dir
# for dirpath,dirnames,filename in os.walk('.'):
#     print(dirpath,dirnames,filename,sep='\n')

# 8 env varibles
# print(os.environ.get('FLASK_APP'))

# 9 write into a file
# with open('another.txt','w') as f:
#     f.write('that live alne dont mean you are lonely')

# 10 path 
print(os.path.split('/some/time/Idont/name.txt'))
print(os.path.abspath('another.txt'))