# Topic 11: Pandas Practice


import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

print("Employee Dataset:")
print(df)

# QUESTION 1:
# Display the first five employees.
print("\nQ1. First Five Employees:")
print(df.head())

# QUESTION 2:
# Display employee names and salaries.
print("\nQ2. Employee Names and Salaries:")
print(df[["Name", "Salary"]])

# QUESTION 3:
# Find employees working in the IT department.
print("\nQ3. IT Employees:")
print(df[df["Department"] == "IT"])

# QUESTION 4:
# Find employees earning more than 45000.
print("\nQ4. Salary Above 45000:")
print(df[df["Salary"] > 45000])

# QUESTION 5:
# Calculate average salary.
print("\nQ5. Average Salary:")
print(df["Salary"].mean())

# QUESTION 6:
# Find the highest salary.
print("\nQ6. Highest Salary:")
print(df["Salary"].max())

# QUESTION 7:
# Count employees in each department.
print("\nQ7. Department Employee Count:")
print(df.groupby("Department")["EmployeeID"].count())

# QUESTION 8:
# Calculate average salary by department.
print("\nQ8. Department Average Salary:")
print(df.groupby("Department")["Salary"].mean())

# QUESTION 9:
# Find employees with missing values.
print("\nQ9. Employees With Missing Values:")
print(df[df.isnull().any(axis=1)])

# QUESTION 10:
# Sort employees by salary in descending order.
print("\nQ10. Salary Ranking:")
print(df.sort_values("Salary", ascending=False))

# QUESTION 11:
# Find the average age of employees.
print("\nQ11. Average Age:")
print(df["Age"].mean())

# QUESTION 12:
# Find the number of employees in each city.
print("\nQ12. Employees By City:")
print(df["City"].value_counts())
