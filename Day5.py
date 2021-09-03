# for loop

fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

for x in "le quoc tuan":
    print(x)

# break statement.
for x in fruits:
    print(x)
    if x == "banana":
        print("Dung lai o day thoi")
        break

# for with range.
for i in range(10):
    print(i)

# for with range from start to end ( not include end)
for i1 in range(3, 6):
    print(i1)

# for with range and step
for i2 in range(3, 5, 2):
    print(i2)

# Nested loops.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


for x in range("a","z"):
    print(x)