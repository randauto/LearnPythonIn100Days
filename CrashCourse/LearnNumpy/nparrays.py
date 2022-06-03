import numpy as np

arr = np.array(42)
# 0-D Arrays
print("0-D Arrays")
print(arr)

print("1-D Arrays")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)
print("2-D Arrays")
arr = np.array([[1, 2, 3, 4, 5], [7, 8, 9]])
print(arr)
print(arr.ndim)

print("3-D arrays")
arr = np.array([[[1, 2, 3, 4, 5], [7, 8, 9]], [[1, 2, 3, 4, 5], [7, 8, 9]], [[1, 2, 3, 4, 5], [7, 8, 9]]])
print(arr)
print(arr.ndim)