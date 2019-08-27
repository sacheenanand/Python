__author__ = 'sanand'

d = dict()

d["sacheen"] = 38
d["Arin"] = 1

for k,v in d.items():
    print(k, v)
tups = d.items()
print(tups)


c = {'a':10, 'b':12, 'c':1}
temp = list()
for k,v in c.items():
    temp.append((v, k))
print(temp)
temp = sorted(temp, reverse=True)
print(temp)

