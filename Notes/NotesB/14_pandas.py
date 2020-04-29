import pandas as pd

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}

df = pd.DataFrame(data=d)
print(df['col1'])

print(df.describe())

