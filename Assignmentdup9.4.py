__author__ = 'sanand'


fname = input("Enter the filename")
if len(fname) < 1: fname = "words.txt"

handle = open(fname)


di = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    wrds = line.split()
    #print(wrds)
    for w in wrds:
        print(w)
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
print(di)

largest = -1
word = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        word = k
print(word, largest)










