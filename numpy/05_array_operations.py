# Topic 05: NumPy Array Operations


import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

# 1. Addition
print("Addition:", a + b)

# 2. Subtraction
print("Subtraction:", a - b)

# 3. Multiplication
print("Multiplication:", a * b)

# 4. Division
print("Division:", a / b)

# 5. Power
print("Power:", a ** 2)

# 6. Modulus
print("Modulus:", a % b)

# 7. Comparison operations
print("\nGreater Than:", a > 20)
print("Equal To:", a == b)

# 8. Aggregate operations
print("\nSum:", np.sum(a))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))

# 9. Statistical operations
print("\nStandard Deviation:", np.std(a))
print("Variance:", np.var(a))

# 10. Sorting
unsorted = np.array([40, 10, 30, 20])
print("\nSorted:", np.sort(unsorted))

# 11. Unique values
values = np.array([10, 20, 10, 30, 20])
print("Unique Values:", np.unique(values))

# 12. Conditional selection
print("Values Greater Than 20:", a[a > 20])
