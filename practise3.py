__author__ = 'sanand'


# to check the list and remove the even numbers

list = [10, 21, 31, 32, 44]

print("orginal list")
#print(list)

for i in list[:]:
    if i % 2 == 0:
        list.remove(i)
print(list)

l = [10, 21, 31, 32, 44, 66, 69]
def remove_odd(l):
    return [x for x in l if x % 2 != 0]
print(remove_odd(l))

