__author__ = 'sanand'


friends = ["Sacheen!", "Arin!", "Anand!"]
for friend in friends:
    print("Thanks", friend)
print("Done!")



largest = -1
print("before" ,largest)
for num in [10, 20, 30, 35, 12, 19, 34, 136, 10, 11, 19, 22222]:
    if num > largest:
        largest = num
        print(largest, num)
print("The largest from the list is " ,largest)

count = 0
print("before", count)
for num in [10, 20, 30, 35, 12, 19, 34, 136, 10, 11, 19, 22222]:
    count += 1
    print(count, num)
print("After", count)



count = 0
print("before", count)
for num in [10, 20, 30, 35, 12, 19, 34, 136, 10, 11, 19, 22222]:
    count = count + num
    print(count, num)
print("After", count)
