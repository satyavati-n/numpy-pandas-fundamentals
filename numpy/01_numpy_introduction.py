# NUMPY FUNDAMENTALS
# Topic 01: Introduction to NumPy


# Import NumPy
import numpy as np

# 1. Display NumPy version
print("NumPy Version:", np.__version__)

# 2. Create a normal Python list
numbers = [10, 20, 30, 40, 50]

print("Python List:", numbers)

# 3. Convert Python list into NumPy array
arr = np.array(numbers)

print("NumPy Array:", arr)

# 4. Check the type
print("Type of Python List:", type(numbers))
print("Type of NumPy Array:", type(arr))

# 5. Check array dimensions
print("Array Dimensions:", arr.ndim)

# 6. Check array shape
print("Array Shape:", arr.shape)

# 7. Check total number of elements
print("Total Elements:", arr.size)

# 8. Check data type
print("Array Data Type:", arr.dtype)
