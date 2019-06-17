__author__ = 'sanand'

table = [None]*10
print(table)

def hashing_fun(x):
    return x % 10

a = hashing_fun(15)
print(a)

b = hashing_fun(115)
print(b)


def insert_fun(table,key,value):
    table[hashing_fun(key)] = value


print(table)

c = insert_fun(table,15,'Sacheen')
print(table)

c = insert_fun(table, 20, 'dao')
print(table)

d = insert_fun(table, 20, 'Miya')
print(table)

# you can see in the table that Miya is replacing dao if the index numbe is same, to fix collision we are using list

table = [[] for y in range(10)]
print(table)

def insert_fun(table, key, value):
    table[hashing_fun(key)].append(value)

c = insert_fun(table, 20, 'dao')
print(table)

d = insert_fun(table, 20, 'Miya')
print(table)

d = insert_fun(table, 20, 'Arin')
print(table)

# you can see here the if the index is same for 2 values the the items keeps adding to the list.

'''

table = [None] * 10
print(table)
def hashing_fun[x]:
  return x % 10
def hashing_insert(table. key, value):
   table[hashing_fun(key)] = value

table = [[] for y in range(10)]
print(table)

def hashing_insert(table, key, value):
table[hashing_fun(key)].append(value)

'''




