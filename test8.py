__author__ = 'sanand'

import json

with open("sacheen8457.json") as f:
    sacheen8457 = json.load(f)
    print(sacheen8457)
    print(sacheen8457["first_name"])
    print(sacheen8457["last_name"])
    print(sacheen8457["Address"])
    print(sacheen8457["City "])
    print(sacheen8457["State"])

