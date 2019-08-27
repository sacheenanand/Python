__author__ = 'sanand'


#Python program to find smallest number in a list


list = [1, 2, 3, 4]
list.sort()
print("the smallest number is ", list[:1])


# Python program to print all Prime numbers in an IntervalPython program to print all Prime numbers in an Interval

start, end = 2, 16

for val in range(start, end ):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
            else:
                print(val)


