import pandas as pd
#Topic : Conditional selection and slicing
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        'Score': [85, 90, 88, 92]}
df = pd.DataFrame(data)
# use for filtering the data like we try to know old age int the dataframe(table) like as below example
# This asks "Is the value in the 'Age' column > 30?"
mask = df['Age'] > 30
print(mask)
print()
#  apply mask to df  ,This says "Give me all rows from df where the mask is True"
older_people = df[mask]
# Or, in one line:
print(older_people)
print()
# Multiple conditions: Use & (and) and | (or). You must use parentheses () around each condition.
# Find people older than 30 AND with a score > 90
smart_and_older = df[(df['Age'] > 30) & (df['Score'] > 90)]
print(smart_and_older)
print()

# set_index()
'''
concept
set_index(): This changes your index from the default 0, 1, 2... to one of your columns. 
This is useful if you have a unique ID, like a 'Name' or 'student_id'.'''
# Make the 'Name' column the new index
df_named = df.set_index('Name')
print(df_named)
print()
# reset_index()
'''
concept
reset_index(): This does the opposite. 
It turns the index back into a regular column and gives you the default 0, 1, 2... index again.'''
# Turn the 'Name' index back into a column
df_original = df_named.reset_index()
# Output: (back to how it started)
print(df)
