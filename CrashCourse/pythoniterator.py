myString = "adjfjadlskjflkajdlkfjuoiqeuroiqwueirouqweor"

# iterator loop
for x in myString:
    print(x)

print("Iterable")


length = len(myString)
# for i in 0..length-1:
myIt = iter(myString)
print(next(myIt))

