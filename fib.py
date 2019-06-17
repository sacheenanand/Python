__author__ = 'sanand'


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
print(fib(10))

def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]
str = "Sacheen Anand"
print(reverse(str))

def fiba(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        return a
z = fib(10)
print(z)

s = "Sacheen Anand"
print(s[::-1])

# acheen + s
# cheen +  as
# heen +  cas
# een +   hcas
# en +  ehcas
# n +  eechas
#neechas


# 0 1 1 2 3 5 8 13 21 34 55 89 144