import pandas as pd
# topic : date and time in pnadas
data = {'Date': ['2024-01-01', '2024-03-15', '2024-06-10'], 'Sales': [200, 300, 400]}
df = pd.DataFrame(data)
print(df)
print()
df['Date'] = pd.to_datetime(df['Date']) # date column is string convert it into date 
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df)
#9.2 Filtering by date range
start = '2024-02-01'
end = '2024-05-01'

mask = (df['Date'] >= start) & (df['Date'] <= end)
filtered = df.loc[mask]
print(filtered)

'''
🟢 9.3 Resampling and time-based grouping
🔹 Concept:

If your data has daily, weekly, or monthly timestamps, you can use .resample() to group by time periods.'''
date_rng = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
df22 = pd.DataFrame({'Date': date_rng, 'Sales': [100,150,200,120,180,250,300,230,260,270]})
df22.set_index('Date', inplace=True)
df22.resample('W').sum() #'W' = Weekly, 'M' = Monthly, 'D' = Daily, 'Y' = Yearly.




