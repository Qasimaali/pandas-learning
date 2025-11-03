# Topic :Grouping & Aggregation in Pandas
import pandas as pd

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Salary': [40000, 45000, 60000, 65000, 70000, 72000],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Bonus': [2000, 2500, 3000, 3200, 3500, 4000]
}

df = pd.DataFrame(data)
print(df)
print()
print(df.groupby('Department')['Salary'].sum())  # aggregation function sum , avg ,mean , count , agg(multiple aggreagation)
print()
# group by departmen and get the count
print(df.groupby('Department')['Salary'].count(),"department count")
print()
# groupt by department and and get the mean
print(df.groupby('Department')['Salary'].mean())
print()


print(df.groupby('Department').agg({'Salary': ['mean', 'sum'], 'Bonus': 'mean'}))
print()

# multi level grouping i.e group by more than one column
print(df.groupby(['Department', 'Gender'])['Salary'].mean())
print()
#transform()
'''
Returns a Series with the same size as the original.

Used when you want to add a new column back to the original DataFrame.'''
df['Salary_mean'] = df.groupby('Department')['Salary'].transform('mean')
print(df)


