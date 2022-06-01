f = open("test.txt", mode='rt')
# print(f.read())

# Return the 5 first characters of the file:
# content = f.read(5)
# print(content)
# print(f.readline())
# print(f.readline())
# print(f.readline())

for x in f:
    print(x)

f.close()  # close the file when you are finish with it.
