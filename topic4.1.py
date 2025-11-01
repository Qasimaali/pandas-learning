# string operation
import pandas as pd
import numpy as np
data = { 'name':['Qasim' , 'AlI'],
        'age' :[12 ,14],
        'city':['kargil','leh']}
df = pd.DataFrame(data)
print(df)
print()
# to upper and lower case
df['name'] = df['name'].str.lower()
df['city'] = df['city'].str.upper() # Let's make all city names uppercase

print("\n--- After str.lower() and str.upper() ---")
print(df)
# replace find the text and replace it
df['city'] = df['city'].str.replace('KARGIL', 'ZANSKAR')
print("\n--- After str.replace() ---")
print(df)
# str.contains(): Checks if a string contains a certain substring. This is great for filtering your data.
# First, let's fill the NaN city to avoid errors
df['city'] = df['city'].fillna('Unknown')

delhi_rows = df[df['city'].str.contains('KA')] # (Assumes we ran str.upper() first)
print("\n--- After str.contains('KA') ---")
print(delhi_rows)

#Apply Functions