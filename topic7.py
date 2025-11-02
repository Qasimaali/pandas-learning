# topic is :🧩 7. Combining & Merging DataFrames in Pandas
# 1. concatenation
import pandas as pd

'''df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['D', 'E', 'F']
})

result = pd.concat([df1, df2])
print(result)
# concatnating different column name
import pandas as pd

df3 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['A', 'B']
})

df4 = pd.DataFrame({
    'ID': [3, 4],
    'Age': [25, 30]
})

result = pd.concat([df3, df4]) # for df4 ther is no name column in that place is filled with Nan,
print(result)'''

#                 ----merging pd.merge() ,merging combines DataFrames based on common columns (keys).
df5 = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})
print(df5)
print()

# Right DataFrame
df6 = pd.DataFrame({
    'CustomerID': [3, 4, 5, 6],
    'Purchase': ['Laptop', 'Phone', 'Tablet', 'Headphones']
})
print(df6)
merge_inner = pd.merge(df5, df6, on='CustomerID', how='inner')
print(merge_inner)
print()
left_merge = pd.merge(df5 , df6 , on = 'CustomerID' , how = 'left') # All Rows from Left + Matches from Right
print(left_merge)
right_merge = pd.merge(df5 , df6 ,on ='CustomerID' , how = 'right') #All Rows from Right + Matches from Left
print(right_merge)
outer_merge = pd.merge(df5 , df6 , on = 'CustomerID' , how = 'outer') # All Rows from Both (Full Join)
print(outer_merge)







