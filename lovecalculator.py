name1 = input("Nhap vao ten ban: ")
name2 = input("Nhap vao ten nguoi ay: ")

combine_name = name1 + name2
lower_name = combine_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e
print(f"Total: {true}")

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l + o + v + e

love_score = str(true) + str(love)

