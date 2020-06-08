__author__ = 'sanand'

import csv

with open("sacheen.csv", "w", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow(["1998", "Cricket", "India"])
    data_handler.writerow(["2002", "Cricket", "Australia"])
    data_handler.writerow(["2006", "Cricket", "crotia"])
    data_handler.writerow(["2010", "Cricket", "SL"])
    data_handler.writerow(["2014", "Cricket", "Nz"])


