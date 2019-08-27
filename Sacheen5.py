__author__ = 'sanand'

import os


os.chdir('/Users/sanand/Talix')
for dirpath, dirname, filnames in os.walk('/Users/sanand/Talix'):
    print('CurrentPath :', dirpath )
    print('Directorname :', dirname)
    print('Filenames :' ,filnames)

