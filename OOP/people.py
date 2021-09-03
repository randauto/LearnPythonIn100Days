class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} year old")


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def showInfo(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} year old in class {self.graduationyear}")
