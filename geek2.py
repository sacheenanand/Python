__author__ = 'sanand'

# Given starting and end points, write a Python program to print all even numbers in that given range.

string, end = 2, 15
for num in range(2, 15):
    if num % 2 == 0:
        print(num, end = " ")
