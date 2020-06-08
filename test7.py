__author__ = 'sanand'

import json

sacheen8457 = {
    "first_name": "Sacheen",
    "last_name": "Anand",
    "Address": "1441 Creekside Dr.",
    "City ": "Walnut Creek",
    "State": "California",
}

with open("sacheen8457.json", "w") as f:
    json.dump(sacheen8457, f)
