__author__ = 'sanand'

import os

os.chdir('/Users/sanand/Talix')
print(os.path.exists('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
#print(os.path._check_arg_types('tmp', 'test.txt'))
a = os.path.basename('/tmp/test.txt')
b = os.path.dirname('/tmp/test.txt')
c = os.path.splitext('/tmp/test.txt')
d = os.path.isfile("/tmp/test.txt")
print(a)
print(b)
print(c)
print(d)
print(dir(os.path))




