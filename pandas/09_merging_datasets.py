# Topic 09: Merging Datasets

import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parents[1]

employees = pd.read_csv(
    project_path / "datasets" / "employees.csv"
)

departments = pd.read_csv(
    project_path / "datasets" / "departments.csv"
)

# 1. Inner join
inner_merge = pd.merge(
    employees,
    departments,
    on="Department",
    how="inner"
)

print("Inner Join:")
print(inner_merge)

# 2. Left join
left_merge = pd.merge(
    employees,
    departments,
    on="Department",
    how="left"
)

print("\nLeft Join:")
print(left_merge)

# 3. Right join
right_merge = pd.merge(
    employees,
    departments,
    on="Department",
    how="right"
)

print("\nRight Join:")
print(right_merge)

# 4. Outer join
outer_merge = pd.merge(
    employees,
    departments,
    on="Department",
    how="outer"
)

print("\nOuter Join:")
print(outer_merge)

# 5. Merge with validation
validated_merge = pd.merge(
    employees,
    departments,
    on="Department",
    how="left",
    validate="many_to_one"
)

print("\nValidated Merge:")
print(validated_merge)

# 6. Concatenation
first_half = employees.iloc[:5]
second_half = employees.iloc[5:]

combined = pd.concat(
    [first_half, second_half],
    ignore_index=True
)

print("\nConcatenated Data:")
print(combined)
