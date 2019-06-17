__author__ = 'sanand'

# Given a list of numbers of list, write a Python program
# to create a list of tuples having first element as the number and second element as the cube of the number.

list1 = [1, 2, 3, 4, 5]

results = [(val, pow(val, 3)) for val in list1]

print(results)

