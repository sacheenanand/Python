__author__ = 'sanand'

#Given starting and end points, write a Python program to print all odd numbers in that given range.



start , end = 2 , 20

for num in range(2, 20 + 1):
    if num % 2 != 0:
        print(num, end =' ')

