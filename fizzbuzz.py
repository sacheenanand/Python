__author__ = 'sanand'
#program to fizbuzz

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("fizbizz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)


a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a+b