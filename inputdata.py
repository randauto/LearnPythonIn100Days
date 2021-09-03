# print new line
print("Xin chao\nCac ban")

print("I am 5'9\" tall")

print(5 > 2 or 2 < 3)

myAge = 32
yourAge = 31

if myAge > yourAge:
    print("Toi lon tuoi hon ban")
elif myAge < yourAge:
    print("Toi it tuoi hon ban")
else:
    print("Toi va ban bang tuoi nhau")

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for myNumber in mylist:
    print("number %d" % myNumber)

counter = 5
while counter > 0:
    print("Counter: ", counter)
    counter -= 1

j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ', j)
    if j == 6:
        break

