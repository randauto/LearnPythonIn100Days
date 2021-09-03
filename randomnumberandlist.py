# # import random
# # import my_module
# #
# # random_integer = random.randint(0, 10)
# # print(random_integer)
# # print(my_module.pi)
# #
# # random_float = random.random()
# # print(random_float)
#
# # List
#
# fruits = ["Tao", "Dua", "Mit"]
# print(len(fruits))
# print(fruits[2])
#
# # fruits.sort()
# print(fruits[0])
#
# fruits.append("Kaka")
# print(fruits)
#
# import random
#
# str_inp = "Hello,from,AskPython"
# op = str_inp.split(",")
# print(op)
#
# rdStr = random.randint(0, len(op) - 1)
# print(op[rdStr])
#
# #lay so ngau nhien trong list.
# person = random.choice(op)
# print(person)
#
# newlist = [fruits, op]
# print(newlist)

row1 = ["😁", "😥", "😤"]
row2 = ["🤩", "😒", "🥵"]
row3 = ["😲", "😴", "🤐"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

horizotal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizotal - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")
