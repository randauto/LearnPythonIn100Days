import numpy as np

# Access 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row: ', arr[0, 1])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 2nd row: ', arr[1, 4])

print("Access 3-D Arrays")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
