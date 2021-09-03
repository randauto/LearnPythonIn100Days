from people import Person, Student

# human = Person()
# human.name = "Le Quoc Tuan"
# human.age = 32
# human.address = "Hanoi - VietNam"

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.showInfo()

del p1.age
# p1.showInfo()  # will error because we delete age properties

# del p1  # Delete Object.
# p1.showInfo() # ----> name 'p1' is not defined

student_a = Student("Le Quoc Tuan", 32, "Information Technology")
student_a.showInfo()
