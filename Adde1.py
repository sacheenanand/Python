__author__ = 'sanand'

import csv
with open("Adde.csv") as f:
    contents_of_file = csv.reader(f)
    sacheen = []
    for each_line in contents_of_file:
        sacheen += each_line
    print(sacheen)
    index_sacheen = sacheen.index("Yes")
    print(index_sacheen)
    #index_sacheen = sacheen.index("Love")
    #print(index_sacheen)
