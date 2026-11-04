# PANDAS PRACTICE EXERCISES


import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

# EXERCISE 1
# Display the complete dataset.
print("Exercise 1:")
print(df)

# EXERCISE 2
# Display the first three records.
print("\nExercise 2:")
print(df.head(3))

# EXERCISE 3
# Display only Name, Department and Salary.
print("\nExercise 3:")
print(df[["Name", "Department", "Salary"]])

# EXERCISE 4
# Find employees whose salary is above 50000.
print("\nExercise 4:")
print(df[df["Salary"] > 50000])

# EXERCISE 5
# Find employees working in HR.
print("\nExercise 5:")
print(df[df["Department"] == "HR"])

# EXERCISE 6
# Calculate the average salary.
print("\nExercise 6:")
print(df["Salary"].mean())

# EXERCISE 7
# Calculate department-wise total salary.
print("\nExercise 7:")
print(df.groupby("Department")["Salary"].sum())

# EXERCISE 8
# Find the employee with the highest salary.
print("\nExercise 8:")
print(df.loc[df["Salary"].idxmax()])

# EXERCISE 9
# Count missing values in every column.
print("\nExercise 9:")
print(df.isnull().sum())

# EXERCISE 10
# Fill missing salary using the median.
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print("\nExercise 10:")
print(df[["Name", "Salary"]])

# EXERCISE 11
# Sort employees by salary in descending order.
print("\nExercise 11:")
print(df.sort_values("Salary", ascending=False))

# EXERCISE 12
# Find the number of employees in every department.
print("\nExercise 12:")
print(df["Department"].value_counts())

# EXERCISE 13
# Calculate department-wise average salary.
print("\nExercise 13:")
print(df.groupby("Department")["Salary"].mean())

# EXERCISE 14
# Create a new column called AnnualSalary.
df["AnnualSalary"] = df["Salary"] * 12

print("\nExercise 14:")
print(df[["Name", "Salary", "AnnualSalary"]])

# EXERCISE 15
# Find employees having more than 5 years of experience.
print("\nExercise 15:")
print(df[df["Experience"] > 5])
