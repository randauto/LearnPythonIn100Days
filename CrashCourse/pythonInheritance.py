class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def showInfo(self):
        print(self.firstName, self.lastName)


x = Person("Le", "Tuan")
x.showInfo()


class Studen(Person):
    def __init__(self, fName, lName, graduationyear):
        super().__init__(fName, lName)
        self.graduationyear = graduationyear

    def welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationyear)


s = Studen("Nguyen", "Van A", 2022)
s.showInfo()
s.address = "Ha Noi - VietNam"
s.welcome()
