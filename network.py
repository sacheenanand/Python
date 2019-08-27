__author__ = 'sanand'

import subprocess
ls_output = subprocess.call(['ls' '-l'], shell=True)
print(ls_output)


