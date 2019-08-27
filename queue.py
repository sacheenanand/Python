__author__ = 'sanand'

for i in range(10):
    if not i % 2 == 0:
        print(i + 1)


from collections import deque

queue = deque(["sacheen", "anand", "vijay", "steve"])
queue.append("jat")
queue.append("Mat")
queue.popleft()
queue.popleft()
print(queue)


squares = []

for x in range(10):
    squares.append(x ** 2)
print(squares)


squars_a = [x ** 2 for x in range(6)]
print(squars_a)

cubes = [x ** 3 for x in range(9)]
print(cubes)

sacheen = []
for x in range(10):
    sacheen.append(x ** 3)
print(sacheen)
sacheen.insert(0, 2456)
print(sacheen)


for x in range(2, 50):
    for y in range(2,50):
        if x == y:
            print(x ,y)


arin = []
for x in range(10):
    arin.append(x ** 4)
print(arin)
arin.insert(0, 24)
print(arin)
arin.insert(11, 429)
print(arin)





