__author__ = 'sanand'

customer_100 = {
    "Name ": "Anand Arkula ",
    "wifename" : "Vanitha",
    "kidsname" : "Sacheen Anand",
    "olderone" : "Jatheen Anand",

}

'''
for each_key in customer_100.values():
    print(each_key)


for each_value in customer_100.keys():
    print(each_value)
'''


for each_key, each_value in customer_100.items():
    print("The customer  "  + each_key  + " is  "  + each_value)
