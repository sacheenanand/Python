__author__ = 'sanand'

import csv

with open("sacheen.csv", "a", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["2022", "Russia", "Russia"])
