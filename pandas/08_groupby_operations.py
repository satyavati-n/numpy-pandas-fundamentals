# Topic 08: GroupBy Operations


import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

# 1. Average salary by department
print("Average Salary By Department:")
print(df.groupby("Department")["Salary"].mean())

# 2. Total salary by department
print("\nTotal Salary By Department:")
print(df.groupby("Department")["Salary"].sum())

# 3. Employee count by department
print("\nEmployee Count:")
print(df.groupby("Department")["EmployeeID"].count())

# 4. Maximum salary by department
print("\nMaximum Salary:")
print(df.groupby("Department")["Salary"].max())

# 5. Minimum salary by department
print("\nMinimum Salary:")
print(df.groupby("Department")["Salary"].min())

# 6. Multiple aggregations
print("\nMultiple Aggregations:")
print(
    df.groupby("Department")["Salary"].agg(
        ["sum", "mean", "min", "max", "count"]
    )
)

# 7. Group by multiple columns
print("\nDepartment and City:")
print(
    df.groupby(["Department", "City"])["Salary"].mean()
)

# 8. Named aggregations
summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Total_Salary=("Salary", "sum"),
    Employee_Count=("EmployeeID", "count")
)

print("\nDepartment Summary:")
print(summary)

# 9. Reset index
print("\nSummary With Normal Index:")
print(summary.reset_index())

# 10. Sort grouped results
print("\nDepartments By Average Salary:")
print(summary.sort_values(
    by="Average_Salary",
    ascending=False
))
