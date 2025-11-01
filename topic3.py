import pandas as pd
# topic: Data Selection & Indexing
#concept : how to grab the specific pieces of data you want from your table or dataframe
# make a data frame , or read csv file
data = {
    'name':['Qasim','Ali','Ahmad','Jaffer'],
    'Location': ['Ladakh' , 'Kargil' , 'Kashmir' , 'Zanskar'],
    'age':[13,15,14,16]
}
df = pd.DataFrame(data)
print(df) # look for output and notice the index for each row it oftenly called row number

# selecting a single column use square bracket[[column name]] 
ages = df[['age']]
print(ages)
print()
#[[]] selecting multiple column [[column1 , column2 etc]]
name_age = df[['name' , 'age']]
print(name_age)
print()

#Selecting rows (basic slicing): You can "slice" rows just like a Python list.
# syntax dataframe_name[starting_row : ending_row(not included)] 
first_two = df[0:2]
print(first_two)
print()

# Ways of selecting data
#1 loc[] Format: df.loc[row_label, column_label]
qasim_row = df.loc[0]
print(qasim_row)
print()
# get the location for row 1
Ali_city = df.loc[1 ,'Location']
print(Ali_city)
print()

# 2 iloc[] Format: df.iloc[row_position, column_position] here df name be any thing you name your dataframe , here dataframe name is df
# Get the first row (position 0)
first_row = df.iloc[0]
print(first_row)
print()
# Get the cell at row 1, column 2 ('Los Angeles')
cell_value = df.iloc[1, 2]
print(cell_value)
print()
# Get the first two rows (positions 0, 1) and first two columns (0, 1)
subset = df.iloc[0:2, 0:2]
print(subset)
print()

'''at[] and iat[]: These are super-fast versions of loc and iloc used only for getting or setting a single cell value.

df.at[1, 'City'] (Label-based) -> 'Los Angeles'

df.iat[1, 2] (Integer-based) -> 'Los Angeles'

Key Difference: loc uses names/labels. iloc uses numbers/positions.'''


