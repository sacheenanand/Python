__author__ = 'sanand'

import os

os.chdir('/Users/sanand/Talix')
print(os.getcwd())
#print(os.environ.get('Talix'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)
