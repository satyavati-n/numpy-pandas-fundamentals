# Topic 10: Data Cleaning


import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]
file_path = project_path / "datasets" / "employees.csv"

df = pd.read_csv(file_path)

# 1. Original dataset
print("Original Dataset:")
print(df)

# 2. Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Fill missing salary using median
df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)

# 6. Fill missing age using median
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

# 7. Fill missing performance rating using mode
df["PerformanceRating"] = df["PerformanceRating"].fillna(
    df["PerformanceRating"].mode()[0]
)

# 8. Remove unwanted spaces from text
df["Name"] = df["Name"].str.strip()
df["Department"] = df["Department"].str.strip()
df["City"] = df["City"].str.strip()

# 9. Convert JoinDate to datetime
df["JoinDate"] = pd.to_datetime(
    df["JoinDate"],
    errors="coerce"
)

# 10. Convert Salary to numeric
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

# 11. Check data types
print("\nData Types:")
print(df.dtypes)

# 12. Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 13. Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# 14. Save cleaned data
output_path = project_path / "datasets" / "employees_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned Dataset Saved Successfully!")
