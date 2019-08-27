__author__ = 'sanand'

x = 100

if not x > 100:
    print("not is valid")
else:
    print("not is not valid")

# to check all the even integers in python 3
squares = []

for i in range(1, 100):
    if i % 2 == 0:
        squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 100) if i % 2 ==0]
print(squares2)

# python to print the name that starts with g
movies = ['gandhi', 'goa', 'anna', 'ganga']

movies1 =[]

for title in movies:
    if title.startswith('g'):
        movies1.append(title)
print(movies1)

movies2 = [title for title in movies1 if title.startswith("g")]
print(movies2)

movies3 = [('gandhi', 1900), ('goa', 1920), ('anna', 1930), ('ganga', 1940), ('gangster', 2017)]
pre2k = [title for (title, year) in movies3 if year < 2000 ]
print(pre2k)

# python to muliply the list numbers by 4
v = [2, -2, 2]

s = [4*x for x  in v]
print(s)

A = [1, 3, 5, 7, 9]
B = [2, 4, 6, 8, 10]

cartseian = [(a, b) for a in A for b in B]
print(cartseian)


#fibonacci numbers
i =1
while i <= 10:
    print(i)
    i +=1

def fibonacci(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1)+ fibonacci(n-2)
for n in range(1,10):
    print(n, ":" , fibonacci(n))

for i in range(2):
    print("Sacheen")

#var = input("enter test string")

#if len(var) < 6:
#     print("very short")
#    print("enter with more than 6 characters")


a = int(input("enter the the sides of the Triangle"))
b = int(input("enter the other sides of the triangle"))
c = int(input("enter the last side of the truanle"))

if a!=b and c!=a and b!=c:
    print(' this Triangle is called scalene triangle')
elif a == b and b == c:
    print("this Triangle is called equilateral triangle")
else:
    print(" the triangle should be isss triangle")

my_set = {10, 20, 30, 40, 50, 10, 20}

for i in my_set:
    print(i)









