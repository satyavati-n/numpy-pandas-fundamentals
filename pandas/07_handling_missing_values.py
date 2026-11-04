# Topic 07: Handling Missing Values


import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

# 1. Display original dataset
print("Original Dataset:")
print(df)

# 2. Identify missing values
print("\nMissing Values:")
print(df.isnull())

# 3. Identify non-missing values
print("\nNon-Missing Values:")
print(df.notnull())

# 4. Count missing values in each column
print("\nMissing Values Per Column:")
print(df.isnull().sum())

# 5. Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# 6. Display rows containing missing values
print("\nRows With Missing Values:")
print(df[df.isnull().any(axis=1)])

# 7. Remove rows containing missing values
removed_rows = df.dropna()
print("\nAfter Removing Missing Rows:")
print(removed_rows)

# 8. Fill missing salary using mean
mean_filled = df.copy()
mean_salary = mean_filled["Salary"].mean()

mean_filled["Salary"] = mean_filled["Salary"].fillna(mean_salary)

print("\nSalary Filled Using Mean:")
print(mean_filled[["Name", "Salary"]])

# 9. Fill missing age using median
median_filled = df.copy()
median_age = median_filled["Age"].median()

median_filled["Age"] = median_filled["Age"].fillna(median_age)

print("\nAge Filled Using Median:")
print(median_filled[["Name", "Age"]])

# 10. Fill missing performance rating using mode
mode_rating = df["PerformanceRating"].mode()[0]

df["PerformanceRating"] = df["PerformanceRating"].fillna(mode_rating)

print("\nRating Filled Using Mode:")
print(df[["Name", "PerformanceRating"]])

# 11. Forward fill
forward_filled = df["Salary"].ffill()
print("\nForward Fill:")
print(forward_filled)

# 12. Backward fill
backward_filled = df["Salary"].bfill()
print("\nBackward Fill:")
print(backward_filled)

# 13. Check missing values again
print("\nMissing Values After Treatment:")
print(df.isnull().sum())
