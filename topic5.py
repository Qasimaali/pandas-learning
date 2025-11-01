# topic Data Exploration & Summary
import pandas as pd

# Our sample data for exploration
data = {
    'employee_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Ali', 'Bina', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'department': ['Sales', 'IT', 'IT', 'Sales', 'Marketing', 'IT', 'Sales'],
    'salary': [70000, 85000, 82000, 72000, 65000, 95000, 71000],
    'years_at_company': [5, 3, 3, 4, 2, 8, 5]
}

df = pd.DataFrame(data)

print("--- Our DataFrame ---")
print(df)
print()
#           ---Descriptive Statistics---
print(df.describe()) # gives all statistica value like mean, standard diviation , count , max , min , quartile(25%),3rdqurtile(75%)
# also we can seperately caculated as

# Get the average of just the 'salary' column
avg_salary = df['salary'].mean()
print(f"\nAverage Salary: {avg_salary}")
print()

# Get the median (middle value) of 'years_at_company'
median_years = df['years_at_company'].median()
print(f"Median Years at Company: {median_years}")
print()

#            ---Counting and Sorting---

# 1 value_counts() It tells you how many times each value appears in a column
print("\n--- Department Counts (value_counts) ---")
print(df['department'].value_counts())
print()

#2 sort_values(): This does exactly what it says: it sorts your DataFrame. 
# The default is to sort in ascending order (smallest to largest).

df_sorted_multi = df.sort_values(by=['department', 'salary'], ascending=[True, False])
print("\n--- Sorted by Dept (A-Z) then Salary (High-Low) ---")
print(df_sorted_multi)
print()

# unique () :values returns a list of unique value for a specified column
print("\n--- Unique Departments ---")
print(df['department'].unique())
print()
# nunique(): returns the count of unique value


