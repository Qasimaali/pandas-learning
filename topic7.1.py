#                 --- 3️⃣ Joining — DataFrame.join(). ,join() is used to combine two DataFrames based on their 
# indexes (row labels), or on a key column if specified.
import pandas as pd

# Left DataFrame
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'City': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai']
}, index=[1, 2, 3, 4])

# Right DataFrame
df2 = pd.DataFrame({
    'Salary': [50000, 60000, 55000, 70000],
    'Department': ['HR', 'IT', 'Sales', 'Finance']
}, index=[3, 4, 5, 6])

print(df1)
print(df2)
#df1.join(df2) — Default (how='left')
result = df1.join(df2)
print(result)
print()
# inner common 
result2 = df1.join(df2, how='inner')
print(result2)
# right
result3 = df1.join(df2, how='right')
print(result3)
#outer
result4 = df1.join(df2 , how = 'outer')
print(result4)

