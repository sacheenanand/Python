__author__ = 'sanand'

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a
z = fib(3)
print(z)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
