# PANDAS FUNDAMENTALS
# Topic 01: Introduction to Pandas


import pandas as pd

# 1. Check Pandas version
print("Pandas Version:", pd.__version__)

# 2. Create a Python dictionary
data = {
    "Name": ["Aarav", "Diya", "Rohan"],
    "Age": [25, 28, 30],
    "Salary": [35000, 55000, 60000]
}

# 3. Create a DataFrame
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# 4. Display first rows
print("\nFirst Two Rows:")
print(df.head(2))

# 5. Display last rows
print("\nLast Two Rows:")
print(df.tail(2))

# 6. Dataset information
print("\nDataset Information:")
df.info()

# 7. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 8. Column names
print("\nColumns:", df.columns)

# 9. Dataset shape
print("Shape:", df.shape)

# 10. Dataset dimensions
print("Dimensions:", df.ndim)

# 11. Total number of elements
print("Total Elements:", df.size)

# 12. Data types
print("\nData Types:")
print(df.dtypes)
