# Khai bao 1 list.

myList = ["tao", "nho", "le", "man"]
print(myList)

thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)

print(len(thisList))
print(len(myList))

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

# The list() Constructor
listconstructor = list(("Apple", "Samsung", "Huawei"))
print(listconstructor)

thisList = ["apple", "banana", "cherry"]
print(thisList[-2])

# Range of Indexes
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])  # hiển thị từ index số 2 cho tới index 5-1 tức là 4. Nó sẽ không chứa index 5.

print(thisList[1:])  # hiển thị từ index số 1 cho tới hết mảng.
print(thisList[:thisList.index("apple")])
print(thisList[-4:-1])
print(thisList[3:6])

# Check if item exits.
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")

# List Comprehension
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = []
# search item not include character 'a'
for x in thisList:
    if "a" not in x:
        newlist.append(x)

print("newlist: ")
print(newlist)

# Sort Lists
thisList = [100, 50, 65, 82, 23]
thisList.sort()
print("Sort Lists")
print(thisList)
# Sort Descending
print("Sort Descending")
thisList.sort(reverse=True)
print(thisList)

# Customize Sort Function
print("Customize Sort Function")


def myFunc(n):
    return abs(n - 50)


thisList = [100, 50, 65, 82, 23]
thisList.sort(key=myFunc)
print(thisList)

# Reverse Order
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.reverse()
print("Reverse Order")
print(thisList)

# join list

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1.extend(list2)
print(list1)
