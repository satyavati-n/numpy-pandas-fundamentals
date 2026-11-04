# Topic 02: Pandas Series


import pandas as pd

# 1. Create a Series
numbers = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(numbers)

# 2. Custom index
marks = pd.Series(
    [85, 90, 78, 95],
    index=["Maths", "Science", "English", "Computer"]
)

print("\nMarks:")
print(marks)

# 3. Access elements
print("\nFirst Element:", marks.iloc[0])
print("Science Marks:", marks.loc["Science"])

# 4. Series properties
print("\nValues:", marks.values)
print("Index:", marks.index)
print("Data Type:", marks.dtype)
print("Shape:", marks.shape)
print("Size:", marks.size)

# 5. Mathematical operations
print("\nAdd 5 Marks:")
print(marks + 5)

# 6. Filtering
print("\nMarks Above 80:")
print(marks[marks > 80])

# 7. Statistical operations
print("\nSum:", marks.sum())
print("Mean:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())

# 8. Create Series from dictionary
employee_salary = pd.Series({
    "Aarav": 35000,
    "Diya": 55000,
    "Rohan": 60000
})

print("\nEmployee Salaries:")
print(employee_salary)
