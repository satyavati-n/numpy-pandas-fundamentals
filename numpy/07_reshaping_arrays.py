# Topic 07: Reshaping NumPy Arrays


import numpy as np

# 1. Create an array
arr = np.arange(1, 13)

print("Original Array:", arr)

# 2. Reshape into 2 rows and 6 columns
reshaped = arr.reshape(2, 6)
print("\n2 x 6 Array:\n", reshaped)

# 3. Reshape into 3 rows and 4 columns
reshaped2 = arr.reshape(3, 4)
print("\n3 x 4 Array:\n", reshaped2)

# 4. Use -1 to automatically calculate dimension
reshaped3 = arr.reshape(2, -1)
print("\nAutomatic Shape:\n", reshaped3)

# 5. Flatten an array
matrix = np.array([[1, 2], [3, 4]])

print("\nFlatten:", matrix.flatten())

# 6. Ravel an array
print("Ravel:", matrix.ravel())

# 7. Transpose
print("\nTranspose:\n", matrix.T)

# 8. Add a new axis
one_d = np.array([10, 20, 30])

print("\nRow Vector:", one_d[np.newaxis, :])
print("Column Vector:", one_d[:, np.newaxis])

# 9. Expand dimensions
expanded = np.expand_dims(one_d, axis=0)
print("\nExpanded:", expanded)

# 10. Remove single-dimensional entries
squeezed = np.squeeze(expanded)
print("Squeezed:", squeezed)
