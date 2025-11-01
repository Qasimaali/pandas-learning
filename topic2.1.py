import pandas as pd
print("___Topic is dataFrame datastructure in pandas")
'''
☐ DataFrame

A DataFrame is a 2-dimensional (2D) table, like a full spreadsheet. It's the most important structure in Pandas.

Analogy: A DataFrame is just a collection of Series that all share the same index. Each column is a Series.

DataFrame: Creation

The most common way to create a DataFrame is from a dictionary of lists, where each key becomes a column name and each list becomes the data for that column.
DataFrame: Creation

'''

# Data for our DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22],
    'city': ['New York', 'London', 'Tokyo']
}

# Create the DataFrame
df = pd.DataFrame(data)

print(df)
print()
print("DataFrame: Viewing Data")
# .head(2): Show the first 2 rows
print(df.head(2)) #bydefault value is five show row upto given specified limit
print()
print("topic is dataframe renaming columns")
print()
'''
Concept: You give .rename() a dictionary. The keys are the old column names, and the values are the new column names.

Important: By default, .rename() does not change your original DataFrame. It returns a new DataFrame with the changes. You have to assign this new copy back to your variable.'''
# Let's rename 'name' to 'full_name' and 'city' to 'location'
new_df = df.rename(columns={
    'name': 'full_name',
    'city': 'location'
})

print("--- New DataFrame ---")
print(new_df)
print("\n")

print("--- Original DataFrame (unchanged) ---")
print(df)