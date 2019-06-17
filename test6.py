__author__ = 'sanand'

import json

alphabet_letters = ["a", "b", "c", "d", "e", "f"]
with open("alphabet_letters.json", "w") as f:
    json.dump(alphabet_letters, f)

