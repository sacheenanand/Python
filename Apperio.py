__author__ = 'sanand'

import csv
import itertools
import operator

my_list = []

with open("bmw_3_db.csv", 'r') as csv_file:
    bmw_csv = csv.reader(csv_file)


    for row in itertools.islice(bmw_csv, 91):
        dict = {row[0]: row[16]}
        sorted_dic = sorted(dict.items(), key = operator.itemgetter(1))
        print(sorted_dic)
        dict2 = {row[0] : row[35]}
        sorted_dic2 = sorted(dict2.items(), key = operator.itemgetter(1))
        print(sorted_dic2)





















