__author__ = 'sanand'

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print("0!" ,fact(0))
print("1!" ,fact(1))
print("2!",fact(2))
print("3!",fact(3))
print("4!",fact(4))
print("5!",fact(5))

