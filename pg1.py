__author__ = 'sanand'

cname = input("Enter the filename")
if len(cname) < 1 : cname = "mbox-short.txt"
handle = open(cname)
counts = dict()
for line in handle:
    if not line.startswith("From "): continue
    line = line.split()
    print(line)
    line = line[1]
    counts[line] = counts.get(line, 0)+ 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigword is None or count >  bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
