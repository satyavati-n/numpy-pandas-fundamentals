# Topic 05: Selecting Data

import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

# 1. Select one column
print("Employee Names:")
print(df["Name"])

# 2. Select multiple columns
print("\nName and Salary:")
print(df[["Name", "Salary"]])

# 3. Select rows using loc
print("\nFirst Three Rows:")
print(df.loc[0:2])

# 4. Select rows using iloc
print("\nFirst Three Rows Using iloc:")
print(df.iloc[0:3])

# 5. Select a specific row
print("\nFirst Employee:")
print(df.iloc[0])

# 6. Select a specific cell using loc
print("\nFirst Employee Name:")
print(df.loc[0, "Name"])

# 7. Select a specific cell using iloc
print("\nFirst Employee Salary:")
print(df.iloc[0, 4])

# 8. Select rows and columns
print("\nSelected Data:")
print(df.loc[0:3, ["Name", "Department", "Salary"]])

# 9. Select columns by position
print("\nFirst Three Columns:")
print(df.iloc[:, 0:3])
