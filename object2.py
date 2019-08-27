__author__ = 'sanand'

#from one class talking to other class

class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w



    def sacheen(self):
        return "my name is ", self.name

r1 = Robot("Arin", "white", 25)
r2 = Robot("Jerry", "Asian", 45)
print(r1.sacheen())


class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Neel", "talkative", True)

p1.Robot_owned = r2

print(p1.Robot_owned.sacheen())