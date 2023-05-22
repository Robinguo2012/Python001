import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))

# arr = np.array([
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 1, 0, 1],
#     [0, 1, 1, 1, 0]
# ])

# a = np.dot(arr, arr)
# print(np.dot(a, arr))

arr = np.array([
    [1, -1, -1, -1],
    [-1, 1, -1, -1],
    [-1, -1, 1, -1],
    [-1, -1, -1, 1],
])

a = np.dot(arr, arr)
# b = np.dot(a, arr)
# print(np.dot(a, arr))
print(a)
print(np.dot(a, arr))
