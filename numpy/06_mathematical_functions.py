# Topic 06: NumPy Mathematical Functions


import numpy as np

numbers = np.array([4, 9, 16, 25, 36])

# 1. Square root
print("Square Root:", np.sqrt(numbers))

# 2. Square
print("Square:", np.square(numbers))

# 3. Absolute values
negative = np.array([-10, -20, 30])
print("Absolute:", np.abs(negative))

# 4. Exponential
print("Exponential:", np.exp(np.array([1, 2, 3])))

# 5. Logarithm
print("Natural Log:", np.log(numbers))
print("Base 10 Log:", np.log10(numbers))

# 6. Trigonometric functions
angles = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(angles)

print("\nSine:", np.sin(radians))
print("Cosine:", np.cos(radians))
print("Tangent:", np.tan(radians))

# 7. Rounding
values = np.array([1.234, 2.567, 3.891])

print("\nRounded:", np.round(values, 2))
print("Floor:", np.floor(values))
print("Ceiling:", np.ceil(values))

# 8. Cumulative operations
data = np.array([10, 20, 30, 40])

print("\nCumulative Sum:", np.cumsum(data))
print("Cumulative Product:", np.cumprod(data))

# 9. Minimum and maximum
print("\nElement-wise Minimum:", np.minimum([1, 5], [2, 3]))
print("Element-wise Maximum:", np.maximum([1, 5], [2, 3]))
