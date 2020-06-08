__author__ = 'sanand'
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fname = input("Enter a file\n")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)
counts = dict()

for line in handle:
    if not line.startswith("From "): continue
    words = line.split()
#    print(words)
    hour = words[5].split(":")
    counts[hour[0]] = counts.get(hour[0], 0)+ 1

lst = list()
for key, value in counts.items():
    lst.append((key,value))
lst.sort()
for key, value in lst:
    print(key, value)


