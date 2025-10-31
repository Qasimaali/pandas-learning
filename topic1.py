import pandas as pd
#Example (Saving to a CSV)
# 1. Create a simple DataFrame (or load one with read_csv)
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]} # we are making implicity make csv file using data frame key word notice the syntax
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n")

# 2. Modify it (e.g., add a new column)
df['job'] = ['Engineer' ,'Doctor']

print("Modified DataFrame:")
print(df)
print("\n")

# 3. Save it to a new file
# We use index=False because we usually don't want to save 
# the '0, 1' index numbers to the file.
df.to_csv('new_data.csv', index=False) 

print("Saved 'new_data.csv' successfully!")
# similar way for 
'''
# Saves to an Excel file, also without the index
df.to_excel('new_data.xlsx', index=False)'''
'''
# 'orient' controls how the JSON is structured
df.to_json('new_data.json', orient='records')'''
print()

print("next topic is Reading data: read_csv(), read_excel(), read_json()")
#df = pd.read_csv('data.csv')
#df = pd.read_excel(filename.xlsx)
#df = pd.read_json(filename.json)