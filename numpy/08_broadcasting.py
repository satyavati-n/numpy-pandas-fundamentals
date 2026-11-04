# Topic 08: NumPy Broadcasting

import numpy as np

# Broadcasting allows NumPy to perform operations
# on arrays with compatible shapes.

# 1. Array with scalar
arr = np.array([10, 20, 30])

print("Original:", arr)
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# 2. Arrays with compatible shapes
a = np.array([10, 20, 30])
b = np.array([1])

print("\nArray Addition:", a + b)

# 3. Two-dimensional broadcasting
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([1, 2, 3])

print("\nMatrix:\n", matrix)
print("Values:", values)

print("\nBroadcasting Result:\n", matrix + values)

# 4. Broadcasting with column vector
column = np.array([[1], [2]])

print("\nColumn Broadcasting:\n", matrix + column)

# 5. Practical example: Price increase
prices = np.array([100, 200, 300])
tax_rate = 0.18

final_prices = prices + (prices * tax_rate)

print("\nOriginal Prices:", prices)
print("Prices With 18% Tax:", final_prices)

# 6. Broadcasting with different shapes
x = np.array([[1], [2], [3]])
y = np.array([10, 20, 30])

print("\nBroadcasting Matrix:\n", x + y)
