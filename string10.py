__author__ = 'sanand'


word = "sacheenanand"
print(word.count('e'))
print(len(word))
print((word.find('z')))
print(word.index('s'))
print(word[0])
print(word[0:1])
print(word[:3])
print(word[1:3])
print(word[:-3])
print(word[3:])
print(word[1:])
print(word.split(' '))
print(word.startswith('s'))
print(word.endswith('d'))
print(word.endswith('z'))
print(word.replace("sacheenanand", "arinsuvarna"))
print(word)
table = [None] * 10
print(table)
print(word.upper())
b = ' '.join(['This', 'string', 'has', 'five', 'words'])
print(b)
c = 'My, name, is, god'.split(',')
print(c)

name, age = 'sacheen', 25
string = 'My name is {0} and my age is {1}'
sf = string.format(name , age)
print(sf)
