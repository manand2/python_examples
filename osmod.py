# navigate file system, navigate fs
# change env variables

import os

# this will show us all the functions in the module
print(dir(os)) 

#get current directory
print(os.getcwd())

#navigate to desktop fs

os.chdir('/Users/manand/Deskop/')

print(os.getcwd())

# what files and folders in desktop

print(os.listdir())

#create a new folder

os.mkdir('OS-Demo-2')
# create multiple levels of directories
os.mkdirs('OS-Demo-2/subdir1')  

# deleting folders

os.removedirs('OS-Demo-2/subdir1')
os.removedir('OS-Demo-2')

# rename files
os.rename('org','new')
print(os.listdir())

# print  meta data of a file
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_time)

mod_time = os.stat('demo.txt).st_mtime
print(datetime.fromtimestamp(mod_time)

#traverse the director, it yields paths, directory within the path and files, traverses from top down
#

for dirpath, dirnames, filesnames in os.walk(/Users/manand/Deskop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print("Filew:', filenames)
    print()


# environment variables
os.chdir('/Users/manand/Deskop/')

print(os.environ.get('HOME'))

#combine file name with 'HOME' directory

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

with open(file_path, 'w') as f:
     f.write

# other methods
print(os.path.basename('/tmp/test.txt'))  # prints test.txt even though the file does not exist
os.path.dirname('/tmp/test.txt')     # prints the directory name
os.path.exists('/tmp/test.txt')  # returns false
os.path.split('/tmp/test.txt')  # printes '/tmp', 'test.txt'
 
os.path.isdir
os.path.isfile
os.path.splitext  # prints file name without extension

print(dir(os.path))

