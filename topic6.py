import pandas as pd
# Topic : . Filtering & Conditional Operations
# Our sample data for filtering
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
condition1 = (df['department']=='IT')
condition2 = (df['salary'] > 83100)
print(df[condition1 & condition2])
# also writen as print((df['department']=='IT') & (df['salary'] > 83100) ) &-> element wise comparasion
print() 
# or | don't use 'or' keyword it gives erroe becauese we have to perform elemetn wise
print(df[condition1 | condition2])
print()
# not 
condition = (df['department'] == 'Sales')
print("\n--- NOT in 'Sales' ---")
print(df[~condition]) # Notice the ~

# -- query() method
'''
Concept: The query() method lets you write your filter as a string, 
which many people find much easier to read than the & and | symbols.'''
print("\n--- query() for 'IT' AND Salary > 83k ---")
print(df.query("department == 'IT' and salary > 83000")) # and
print("\n--- query() for 'Sales' OR 'Marketing' ---")
print(df.query("department == 'Sales' or department == 'Marketing'")) #or we are able to use or in place of | both work

#Example 3 (Using a variable): If you have a variable, you must use the @ symbol in your query string.

min_years = 5
print("\n--- query() using a variable (years >= 5) ---")
print(df.query("years_at_company >= @min_years"))

