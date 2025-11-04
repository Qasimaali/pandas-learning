#🧩 10. Advanced Operations
#1 multiindex  You can have more than one index level (like rows with multiple keys).
import pandas as pd

data = {
    'City': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai'],
    'Year': [2023, 2024, 2023, 2024],
    'Sales': [200, 250, 180, 210]
}

df = pd.DataFrame(data)
print(df)
df.set_index(['City', 'Year'], inplace=True)
print(df)
print()
#MultiIndex allows selecting using multiple keys:
print(df.loc['Delhi'])

'''.  ---2️⃣ Stacking & Unstacking

Concept:

stack(): Converts columns into rows.

unstack(): Converts rows into columns.
Useful for reshaping MultiIndex data.'''

stacked = df.stack()
print("Stacked:\n", stacked)

unstacked = df.unstack()
print("\nUnstacked:\n", unstacked)
# 3️⃣ Melting (pd.melt)
'''Concept:
Turns wide data → long format.
Opposite of pivot().
It helps when columns represent different variables.'''

data2 = {
    'Name': ['A', 'B', 'C'],
    'Math': [80, 90, 85],
    'Science': [70, 88, 95]
}
df2= pd.DataFrame(data2)
melted = pd.melt(df2, id_vars=['Name'], var_name='Subject', value_name='Marks')
print(melted)


# 4️⃣ Window Functions (rolling, expanding)
'''Concept:
Used to calculate moving averages, sums, etc.

rolling(n) → takes the last n values.

expanding() → takes all values up to current.'''
df3 = pd.DataFrame({'Sales': [10, 20, 30, 40, 50]})
df3['Rolling_Mean'] = df3['Sales'].rolling(window=3).mean()
df3['Expanding_Sum'] = df3['Sales'].expanding().sum()
print(df3)

#5️⃣ Apply Custom Lambda Functions Concept:
#You can apply your own logic to rows or columns using apply() and lambda.
df['Discounted'] = df['Sales'].apply(lambda x: x * 0.9 if x > 30 else x)
print(df)




