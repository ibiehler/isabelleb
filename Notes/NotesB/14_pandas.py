import pandas as pd
import random

# lists > dicts > series/dataframes

# Pandas series (1d array)
s = [random.randrange(100) for x in range(10)]
my_series = pd.Series(s)
print(type(my_series))
print(my_series)

# Pandas DataFrame (2d spreadsheet (kinda))
# make from dict
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}

df = pd.DataFrame(data=d)
print(df['col1'])
print(df)

# print(df.describe())


# could also make it from a list/array
d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cols = ["A", "B", "C"]
df2 = pd.DataFrame(data=d, columns=cols)
print(df2)

# make a df from a csv
df3 = pd.read_csv('Beach_Weather_Stations_-_Automated_Sensors.csv')
print(type(df3))

# handy methods
print(df3.head())  # first 5 rows in df
print(df3.tail)
print(df3.info)  

