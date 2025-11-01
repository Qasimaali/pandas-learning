# topic is DATA Cleaning
import pandas as pd
import numpy as np
# make a dataframe
data = {
    'name': ['Ali', 'Bina', 'Charlie', 'Ali', 'david', 'Eva', 'Frank', 'Grace'],
    'age': [25, 30, np.nan, 25, 45, 28, 50, 30],
    'city': ['Mumbai', 'Pune', 'Mumbai', 'Mumbai', 'PUNE', 'Delhi', np.nan, 'Goa'],
    'score': [8.5, 9.0, 7.2, 8.5, 6.0, np.nan, 9.8, 7.0]
}
df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
print()
print(df.dtypes)

# TOPIC IS HANDLING MISSING VALUES
print(df.isnull()) # isnull returns dataframe of true and flase , true means data is missing or null , 
print()
print(df.isnull().sum()) # .sum() it is used to get a quick count of missing values per column
print()

# dropna() Removes rows (or columns) that contain nulls. This is the easiest option, but you lose data.
df_droped = df.dropna()
print(df_droped)
print()

# fillna() it is used to fill the missing value with choosen value a approximate guess or avg value is filled sometimes
# Fill 'age' with the mean age
age_mean = df['age'].mean()
print("mean of age is ", age_mean)
print()
df['age'] = df['age'].fillna(age_mean)

# Fill 'city' with a placeholder
df['city'] = df['city'].fillna('Unknown')

# Fill 'score' with 0
df['score'] = df['score'].fillna(0)

print("\n--- After fillna() ---")
print(df)
# interpolate() This is a smart fill. It guesses the missing value by looking at its neighbors.
df_interpolated = pd.DataFrame(data) # Reset
df_interpolated['score'] = df_interpolated['score'].interpolate()
print("\n--- After interpolate() on 'score' ---")
print(df_interpolated)
print()
# Eva's score (index 5) will be 7.9, halfway between 6.0 and 9.8

# Handling duplicate

#duplicated(): Finds the duplicates. It returns True for any row that's an exact copy of one it has already seen
print(df.duplicated())
print()
# drop_duplicates(): Removes the duplicate rows.
df_drop =df.drop_duplicates()
print(df_drop)
print()
# changing datatype
# Let's assume we've already run fillna() from step 1
df_filled = df.fillna({'age': 0}) # Fill NaNs first

df_filled['age'] = df_filled['age'].astype(int)

print("\n--- After astype() on 'age' ---")
print(df_filled.dtypes)
# 'age' is now int64, not float64