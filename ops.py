__author__ = 'sanand'


#Object oriented programming concepts


class Dog:

    species = "mamals"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods

    def descrption(self):
        return "{} the dog is {} years old".format(self.name, self.age)

    def behaviour(self, sound):
        return "{} says {}".format(self.name, sound)

pid12 = Dog("Bogi", 24)
pid13 = Dog("polar", 15)

print("{} is {} and {} is {} ".format(pid12.name,pid12.age, pid13.name, pid13.age))

if pid12.species == "mamals":
    print("{} is {}!".format(pid12.name, pid12.species))

#child class inherits from Dog class

class toberman(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
class bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child classes inherit attributes and
# behaviors from the parent class
pid14 = bulldog("munni" , 19)
print(pid14.descrption())

# Child classes have specific attributes
# and behaviors as well
print(pid14.run("slowly"))


class pamorin(Dog):
    def sound(self, bark):
        return "{} sounds like {}".format(self.name, bark)

pid15 = pamorin("manju" , 11)
print(pid15.behaviour("bow"))
print(pid15.sound("bow bow bow"))

print(pid12.descrption())









