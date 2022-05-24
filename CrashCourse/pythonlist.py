# Khai bao 1 list.

myList = ["tao", "nho", "le", "man"]
print(myList)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print(len(thislist))
print(len(myList))

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

# The list() Constructor
listconstructor = list(("Apple", "Samsung", "Huawei"))
print(listconstructor)

thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # hiển thị từ index số 2 cho tới index 5-1 tức là 4. Nó sẽ không chứa index 5.

print(thislist[1:])  # hiển thị từ index số 1 cho tới hết mảng.
print(thislist[:thislist.index("apple")])
print(thislist[-4:-1])
print(thislist[3:6])

# Check if item exits.
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
