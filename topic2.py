import pandas as pd
print("__Topic datastructure_in_Pandas__")
print()
'''☐ Series

A Series is a 1-dimensional (1D) array, like a single column in a spreadsheet. It has two main parts:

Data (Values): The data itself (e.g., [10, 20, 30]).

Index: A label for each data point (e.g., [0, 1, 2] or ['a', 'b', 'c']).
'''
# 1. From a # list (Pandas creates a default index 0, 1, 2...)
s_list = pd.Series([10, 20, 30])
print("--- From a list ---")
print(s_list)
print("\n")

# 2. From a list with a custom index
s_custom_index = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("--- With custom index ---")
print(s_custom_index)
print("\n")

# 3. From a dictionary (keys become the index, values become the data)
s_dict = pd.Series({'name': 'Alice', 'age': 25, 'city': 'New York'})
print("--- From a dictionary ---")
print(s_dict)
print()

# Let's use our custom index Series
print("Series: Attributes")
print()
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'], name='MyNumbers')

# .values: Get the data as a NumPy array
print("Values:", s.values)

# .index: Get the index
print("Index:", s.index)

# .dtype: Get the data type
print("Data type:", s.dtype)

# .name: Get the name of the Series
print("Name:", s.name)

print()
print("Series Methods")
print()
# Let's use a slightly bigger Series
s = pd.Series([100, 50, 25, 90, 80, 75, 5])

# .head(n): Show the first 'n' items (default n=5)
print("--- .head(3) ---")
print(s.head(3))
print("\n")

# .tail(n): Show the last 'n' items (default n=5)
print("--- .tail(2) ---")
print(s.tail(2))
print("\n")

# .describe(): Get a quick statistical summary
print("--- .describe() ---")
print(s.describe())
