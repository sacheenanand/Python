__author__ = 'sanand'


fruit = "bannana"
index = 0
while index < len(fruit):
    letter = fruit[index]

    print(index, letter)
    index += 1

for letter in fruit:
    print(letter)

word = "sacheen"
count = 0
for letter in word:
    if letter == 'e':
        count += 1
print(count)



