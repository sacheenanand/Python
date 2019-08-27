__author__ = 'sanand'

import os
from datetime import datetime


os.chdir('/Users/sanand/Talix')
#print(os.getcwd())
#print(os.listdir())
mod_time = (os.stat('address.txt').st_mtime)
print(datetime.fromtimestamp(mod_time))


