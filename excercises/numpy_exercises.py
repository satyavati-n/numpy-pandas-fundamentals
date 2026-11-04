# NUMPY PRACTICE EXERCISES


import numpy as np

# EXERCISE 1
# Create an array containing numbers from 1 to 20.
arr = np.arange(1, 21)
print("Exercise 1:", arr)

# EXERCISE 2
# Find the sum and average of the array.
print("\nExercise 2")
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))

# EXERCISE 3
# Find all even numbers.
print("\nExercise 3")
print(arr[arr % 2 == 0])

# EXERCISE 4
# Find all numbers greater than 10.
print("\nExercise 4")
print(arr[arr > 10])

# EXERCISE 5
# Create a 3x3 matrix.
matrix = np.arange(1, 10).reshape(3, 3)
print("\nExercise 5:\n", matrix)

# EXERCISE 6
# Find the maximum and minimum values.
print("\nExercise 6")
print("Maximum:", np.max(matrix))
print("Minimum:", np.min(matrix))

# EXERCISE 7
# Calculate row-wise sums.
print("\nExercise 7")
print(np.sum(matrix, axis=1))

# EXERCISE 8
# Calculate column-wise sums.
print("\nExercise 8")
print(np.sum(matrix, axis=0))

# EXERCISE 9
# Reverse the array.
print("\nExercise 9")
print(arr[::-1])

# EXERCISE 10
# Calculate the standard deviation.
print("\nExercise 10")
print(np.std(arr))

# EXERCISE 11
# Replace all numbers greater than 15 with 0.
result = arr.copy()
result[result > 15] = 0
print("\nExercise 11:", result)

# EXERCISE 12
# Find unique elements.
values = np.array([10, 20, 10, 30, 20, 40])
print("\nExercise 12:", np.unique(values))
