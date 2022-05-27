class People:
    name = ""
    age = 20


people1 = People()
people1.name = "Nguyen Van A"
people1.age = 33
print("Name: {}".format(people1.name))
print("Age: {}".format(people1.age))

print("The __init__() Function")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("Hello, my name is {}, I'm {} years old".format(self.name, self.age))


p1 = Person("Le Quoc Tuan", 33)
print(p1.name)
print(p1.age)

print("Object Methods")
p1.showInfo()

print("Delete Object Properties")
# del p1.name
# p1.showInfo() # Error: AttributeError: 'Person' object has no attribute 'name'

# The pass Statement
""" class definitions cannot be empty, but if you for some reason have a class definition with no content,
put in the pass statement to avoid getting an error.
"""
class Studen:
    pass


studen1 = Studen()
