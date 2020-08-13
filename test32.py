import os

filepath = 'c:/Users/Owner/Study/python/python_study'

if os.path.exists(filepath):
    print('file or directory is exist.')

    if os.path.isfile(filepath):
        print('it is file')

    if os.path.isdir(filepath):
        print('it is directory')

else:
    print('NOT FOUND')

# 知識として
#
"""
import os
import shutil

def show_dir(path):
    print('=================')
    for dirpath, dirname, filename, in os.walk(path):
        for dirname in dirname:
            print(os.path.join(dirpath, dirname))

tmpdir = 'c:/Users/Owner/Study/python/python_study/sample'

os.mkdir(tmpdir)
os.makedirs('c:/Users/Owner/Study/python/python_study/tmp/sample2')
show_dir(tmpdir)

os.rmdir('c:/Users/Owner/Study/python/python_study/tmp/sample2')
show_dir(tmpdir)

os.removedirs(tmpdir)
shutil.tmtree(tmpdir)

shutil.copy('c:/python/src.txt', 'c:/python/dest.txt')
shutil.copytree('c:/python', 'c:/python_backup')

"""
