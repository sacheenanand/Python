__author__ = 'sanand'


# Using for loop : Iterate each element in the list
# using for loop and check if num % 2 != 0. If the condition satisfies, then only print the number.

list1 = [2, 3, 7, 9, 10, 11, 14]

for num in list1:
    if num % 2 != 0:
        print(num, end = ' ')

only_odd = [num for num in list1 if num % 2 == 1]
print(only_odd)


