__author__ = 'sanand'

def f(n):
    if n == 0 or n == 1:
      return 1
    else:
      return f(n-1) + f(n-2)
print(f(11))
# 0 1 1 2 3 5 8