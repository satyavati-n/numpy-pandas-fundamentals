# Topic 03: Pandas DataFrames


import pandas as pd

# 1. Create a DataFrame
data = {
    "Employee": ["Aarav", "Diya", "Rohan", "Meera"],
    "Department": ["HR", "IT", "Finance", "HR"],
    "Age": [25, 28, 30, 26],
    "Salary": [35000, 55000, 60000, 40000]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

# 2. Select a column
print("\nEmployee Names:")
print(df["Employee"])

# 3. Select multiple columns
print("\nSelected Columns:")
print(df[["Employee", "Salary"]])

# 4. Add a new column
df["Bonus"] = df["Salary"] * 0.10

print("\nAfter Adding Bonus:")
print(df)

# 5. Modify a column
df["Salary"] = df["Salary"] + 2000

print("\nUpdated Salary:")
print(df)

# 6. Remove a column
df = df.drop(columns=["Bonus"])

print("\nAfter Removing Bonus:")
print(df)

# 7. Add a new row
new_employee = pd.DataFrame([{
    "Employee": "Kabir",
    "Department": "IT",
    "Age": 32,
    "Salary": 75000
}])

df = pd.concat([df, new_employee], ignore_index=True)

print("\nAfter Adding Employee:")
print(df)

# 8. DataFrame information
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index)
print("Data Types:\n", df.dtypes)
