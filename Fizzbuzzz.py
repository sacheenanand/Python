__author__ = 'sanand'


for num in range(1, 101):
    if num % 5 ==0 and num % 3 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("fuzz")
    elif num % 3 == 0:
        print("buzz")
    else:
        print(num)
