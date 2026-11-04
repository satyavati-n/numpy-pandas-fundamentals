# Topic 03: Array Indexing


import numpy as np

# 1. One-dimensional array
arr = np.array([10, 20, 30, 40, 50])

# Access individual elements
print("First Element:", arr[0])
print("Second Element:", arr[1])
print("Last Element:", arr[-1])
print("Second Last Element:", arr[-2])

# 2. Two-dimensional array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nMatrix:\n", matrix)

# Access elements using row and column
print("\nFirst Row, First Column:", matrix[0, 0])
print("Second Row, Second Column:", matrix[1, 1])
print("Third Row, Third Column:", matrix[2, 2])

# Access complete rows
print("\nFirst Row:", matrix[0])
print("Second Row:", matrix[1])

# Access complete columns
print("\nFirst Column:", matrix[:, 0])
print("Second Column:", matrix[:, 1])

# 3. Modify an element
matrix[0, 0] = 100
print("\nModified Matrix:\n", matrix)
