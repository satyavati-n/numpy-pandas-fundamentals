# Topic 02: Creating NumPy Arrays


import numpy as np

# 1. One-dimensional array
arr1 = np.array([10, 20, 30, 40])
print("1D Array:", arr1)

# 2. Two-dimensional array
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("\n2D Array:\n", arr2)

# 3. Three-dimensional array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:\n", arr3)

# 4. Array filled with zeros
zeros = np.zeros((2, 3))
print("\nZeros:\n", zeros)

# 5. Array filled with ones
ones = np.ones((2, 3))
print("\nOnes:\n", ones)

# 6. Array filled with a specific value
full = np.full((2, 3), 7)
print("\nFull Array:\n", full)

# 7. Identity matrix
identity = np.eye(3)
print("\nIdentity Matrix:\n", identity)

# 8. Array using arange()
range_array = np.arange(1, 11)
print("\nArange:", range_array)

# 9. Array using linspace()
linear_array = np.linspace(0, 10, 5)
print("\nLinspace:", linear_array)

# 10. Empty array
empty_array = np.empty((2, 2))
print("\nEmpty Array:\n", empty_array)

# 11. Specify data type
float_array = np.array([1, 2, 3], dtype=float)
print("\nFloat Array:", float_array)
