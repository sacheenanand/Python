__author__ = 'sanand'

import csv
with open("potions.csv") as f:
    contents = csv.reader(f)
    sacheen = []
    for each_element in contents:
        sacheen += each_element
    print(sacheen)
    index_number = sacheen.index("Draught of Peace")
    print(index_number)

