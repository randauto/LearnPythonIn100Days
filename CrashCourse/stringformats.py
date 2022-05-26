print("Python String Formatting")

price = 100
txt = "The price is {} dollars"
print(txt.format(price))

# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(price))  # 100.00

# Index Numbers or Multiple Values

name = "Le Quoc Tuan"
age = 33
address = "Hanoi - VietNam"
txt = "Hi {0}, you are {1} years old and you are live in {2}"
print(txt.format(name, age, address))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Kakaka", model="Helele"))
