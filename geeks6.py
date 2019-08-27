__author__ = 'sanand'

#  Print all negative numbers from given list using for loop

start, end = -9, 15

for num in range(start, end +1):
    if num < 0:
        print(num, end = " ")


#  Print all positive numbers from given list using for loop

for num in range(start, end + 1):
    if num >= 0:
        print(num, end = " ")

# #  Print all positive and negative numbers from given list using for loop
for num in range(start, end + 1):
    if num >= 0:
        print(num, end = " ")
    else:
        if num < 0:
            print(num, end = "")

# print the positive and negative numbers from a given list.
list1 = [-1, 2, 3, -5, -6, -7, 9, 11, 12]
pos_count, neg_count = 0, 0

for num in list1:
    if num < 0:
        neg_count += 1
    else:
        pos_count += 1
print("Postive numbers", pos_count)
print("Negative number", neg_count)

# using while loop to print positive numbers

list2 = [1, 2, 3, 4, 5, -9, -8, -7, -6, -5]
num = 0

'''while(num < len(list2)):
    if list2[num] >=0:
        print(list2[num], end = "")
        num += 1
'''

# Python program to print Positive Numbers in a List

# list of numbers
list3 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
pos_nos = [num for num in list3 if num >= 0]

print("Positive numbers in the list: ", pos_nos)









