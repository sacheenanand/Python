__author__ = 'sanand'


counts = dict()
print(" Enter a line of text")

line = input('')

wrds = line.split()

print("Words" , wrds)

print("Counting....")

for sach in wrds:
    counts[sach] = counts.get(sach, 0)+1
print(counts)

