# Topic 04: Array Slicing


import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# 1. Basic slicing
print("Elements 1 to 4:", arr[1:5])

# 2. Elements from beginning
print("First Four Elements:", arr[:4])

# 3. Elements until the end
print("From Index 3:", arr[3:])

# 4. Every second element
print("Step Slicing:", arr[::2])

# 5. Reverse array
print("Reversed Array:", arr[::-1])

# 6. Two-dimensional slicing
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# First two rows
print("\nFirst Two Rows:\n", matrix[:2, :])

# First two columns
print("\nFirst Two Columns:\n", matrix[:, :2])

# Specific section
print("\nSelected Section:\n", matrix[0:2, 1:3])

# 7. Copy versus view
view = arr[1:4]
view[0] = 999

print("\nOriginal After View:", arr)

copy_arr = arr.copy()
copy_arr[0] = 888

print("Original After Copy:", arr)
print("Modified Copy:", copy_arr)
