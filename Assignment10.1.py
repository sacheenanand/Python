__author__ = 'sanand'
#duplicate of Assignment 10
fname = input("Enter a file\n")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+ 1

print(sorted( [(v, k) for k,v in counts.items()]))
