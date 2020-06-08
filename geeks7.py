__author__ = 'sanand'


# Python program to find sum of elements in list

'''list1 = [10, 20, 30, 50]
total = 0
for ele in range(0, len(list1)):
    total = total + list1[ele]
print(total)
'''''
list1 = [10, 20, 30, 50]
ele = 0
total =0

while(ele < len(list1)):
    total += list1[ele]
    ele += 1
print(total)


# Remove multiple elements from a list in Python

list2 = [11, 12, 14, 16, 18, 20, 22, 21, 24]

for element in list2:
    if element % 2 == 0:
        list2.remove(element)

print("New list removing even numbers",list2)



# Python program to remove multiple
# elements from a list

# creating a list
list3 = [11, 12, 14, 16, 18, 20, 22, 21, 24]

# Iterate each element in list
# and add them in variale total
for elem in list3:
    if elem % 2 != 0:
        list3.remove(elem)

    # printing modified list
print("New list after removing all even numbers: ", *list3)