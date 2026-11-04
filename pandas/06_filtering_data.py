# Topic 06: Filtering Data


import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

# 1. Employees with salary above 50000
print("Salary Above 50000:")
print(df[df["Salary"] > 50000])

# 2. Employees from IT department
print("\nIT Employees:")
print(df[df["Department"] == "IT"])

# 3. Multiple conditions using AND
print("\nIT Employees With Salary Above 50000:")
print(df[
    (df["Department"] == "IT") &
    (df["Salary"] > 50000)
])

# 4. Multiple conditions using OR
print("\nHR or Finance Employees:")
print(df[
    (df["Department"] == "HR") |
    (df["Department"] == "Finance")
])

# 5. Using isin()
print("\nEmployees From Bengaluru or Mumbai:")
print(df[df["City"].isin(["Bengaluru", "Mumbai"])])

# 6. Using between()
print("\nSalary Between 35000 and 60000:")
print(df[df["Salary"].between(35000, 60000)])

# 7. Using string filtering
print("\nNames Starting With A:")
print(df[df["Name"].str.startswith("A")])

# 8. Using query()
print("\nEmployees Above 40000 Salary:")
print(df.query("Salary > 40000"))

# 9. Sort filtered results
print("\nEmployees Sorted By Salary:")
print(df[df["Salary"] > 30000].sort_values(
    by="Salary",
    ascending=False
))
