def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def my_function1(*diachi):
    print("Dia chi: " + diachi[0])


my_function1("HaNoi", "HaNam")
