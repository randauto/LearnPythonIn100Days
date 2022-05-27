thisTuple = ("Orange", "Blue", "Gray", "Heyho",)
print(thisTuple)
# Lenght
print(len(thisTuple))

# tuple with one item

oneTuple = ("Kaka",)
print(type(oneTuple))

notOneTuple = ("One")
print(type(notOneTuple))

for x in thisTuple:
    print(x)

# loop through the index numbers

for i in range(len(thisTuple)):
    print(thisTuple[i])

# while loop
print('"Whilte loop"')
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1

# Multiply Tuples
fruits = ("apple", "banana", "cherry", "lemon",)
myTuple = fruits * 2
print(myTuple)
