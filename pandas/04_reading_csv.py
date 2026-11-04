# Topic 04: Reading CSV Files


import pandas as pd
from pathlib import Path

# Locate the datasets folder
project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

# 1. Read CSV file
df = pd.read_csv(file_path)

print("Complete Dataset:")
print(df)

# 2. First five records
print("\nFirst Five Records:")
print(df.head())

# 3. Last five records
print("\nLast Five Records:")
print(df.tail())

# 4. Read specific number of rows
print("\nFirst Three Records:")
print(pd.read_csv(file_path, nrows=3))

# 5. Read specific columns
print("\nSelected Columns:")
print(pd.read_csv(
    file_path,
    usecols=["Name", "Department", "Salary"]
))

# 6. Dataset information
print("\nInformation:")
df.info()

# 7. Statistical summary
print("\nSummary:")
print(df.describe())

# 8. Save dataset to a new CSV
output_path = project_path / "datasets" / "employees_copy.csv"
df.to_csv(output_path, index=False)

print("\nDataset saved successfully!")
