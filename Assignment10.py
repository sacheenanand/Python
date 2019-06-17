__author__ = 'sanand'


fname = input("Enter a file\n")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+ 1
#        if word not in counts:
#            counts[word] = 1
#        else:
#           counts[word] += 1
#print(counts)

'''largest = -1
bigword = None
for k,v in counts.items():
    if v > largest:
        largest = v
        bigword = k
print(bigword, largest)
'''

lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)
lst  = sorted(lst, reverse=True)
for value, key in lst[:10]:
    print(key, value)






