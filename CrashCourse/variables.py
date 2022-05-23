myName = "Le Quoc Tuan"
"""
Day la
nhung dong  
    comment
"""

x = y = z = 100
print(x + y + z)

# casting variable.
x = str(44)
print(type(x))
print(len(x))
y = int(4)
print(type(y))

myName = 'Tran Quoc Tuan'
print(myName)
a = 100
A = 200
print(a)
print(A)

# Many Values to Multiple Variables
ten, tuoi, diachi = "Le Quoc Tuan", 33, 'Ha Dong Ha noi'
print("Ten toi la: " + ten + ", nam nay toi: " + str(tuoi) + " tuoi, toi song o: " + diachi)
# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)
# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = "John"
print(x, y)

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
x = ["apple", "banana", "cherry"]  # list
print(type(x))

x = ("apple", "banana", "cherry")  # tuple
print(type(x))

x = {"name": "John", "age": 36}  # dict will mapping key and value.
print(type(x))

txt = "Hello World"
print(txt[0])
