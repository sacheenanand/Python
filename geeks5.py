__author__ = 'sanand'


#print even numbers in a list.

list1 = [2, 4, 6, 8 , 14, 19 , 26, 10, 11, 15]
only_even = [num for num in list1 if num % 2 == 0]
print(only_even)


for num in list1:
    if num % 2 == 0:
        print(num, end = ' ')


