# learn about function.
def hello(your_name="asfdasfdsaf"):
    for x in your_name:
        print(x)
    print(f"Xin chao ban {your_name}")


name = input("Nhap vao ten cua ban")
hello()
print(f"{name}")

fruits = ["Hello", "Hi", "Good morning"]
hello(fruits)


# function with return value.
def tong(a, b):
    return a + b


a = 100
b = 300

print(f"Tong cua a va b la {tong(a, b)}")


# function with out content like interface in Java
def emptyFunction():
    pass


print(emptyFunction())


# De quy.

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example REsults")
tri_recursion(6)

# lambda functions
x = lambda a: a + 10
print(x(5))

# lambda function can take any number of arguments.
x = lambda a, b: a ** b
print(x(2, 3))

x = lambda a, b, c=100: a + b * c
print(x(10, 11))

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name": "John", "age": 36}
print(type(x))

for item in x:
    if item["name"] == "John":
        print(item)
        break

