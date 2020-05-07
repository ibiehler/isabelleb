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
print(df3.describe())  # basic stats

# useful attributes
print(df3.index)  # these are the rows (data key)
print(df3.columns)  # index object
print(list(df3.columns))
print(df3.dtypes)  # data types

# simple selection using []
wind_speeds = df3['Wind Speed']  # index kinda like dictionary
print(type(wind_speeds))


# we can also slice the df using .iloc[]
first_5_station_names = df3.iloc[:5, 0]  # rows, cols
print(first_5_station_names)

first_fifth_temps = df3.iloc[[0, 4], [2, 3]]
print(first_fifth_temps)
print(type(first_fifth_temps))


# World Cup data

import pandas as pd
x = 5
x  # in ipython/console, this automatically prints

df = pd.read_csv('/Users/alee/PycharmProjects/P2_SP20/Notes/NotesB/world_cup_matches.csv')  # use full path when working in console


# iloc (only useful for index number)
df.iloc[3:6]  # look at 3, 4, 5 matches
df.iloc[3:6, [4, 7]]   # cols 4 and 7 for index/rows 3to5

# loc
df.loc[3:6, ['Home Team Name', 'Away Team Name']] # use col names to slice

# all games from 1950
df_1950 = df.loc[df['Year'] == 1950]

# all games from 1950 Group 3
df_1950.loc[df['Stage'] == 'Group 3']

# alternately we could do both filters at once
df.loc[(df['Year'] == 1950) & (df['Stage'] == 'Group 3')]  # loc[(cond1) & (cond2)]


# Number of home games played by Netherlands
df.loc[df['Home Team Name'] == 'Netherlands'].count()

# All games by Netherlands
df.loc[(df['Home Team Name'] == "Netherlands") | (df['Away Team Name'] == "Netherlands")]

# print the attendance for all games in 2010
df.loc[df['Year'] == 2010]
df.loc[df['Year'] == 2010]['Attendance'].sum()
df.loc[df['Year'] == 2010]['Attendance'].mean()
df.loc[df['Year'] == 2010]['Attendance'].value_count()
df.loc[df['Year'] == 2010]['Attendance'].count()

# How many games the US played in 2014
df.loc[(df['Home Team Initials'] == "USA") | (df['Away Team Initials'] == "USA")][df['Year'] == 2014]

# how many countries participated in 1986
# hint: pd.Series objects have a method called .unique()


# how many matches had 7 or more goals
df.loc[(df['Home Team Goals'] + df['Away Team Goals']) > 7]
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
len(df.loc[df['Total Goals'] > 7])

# search idle (python's idle) and operate out of that for the hw (it won't autocomplete but it's good enough)

