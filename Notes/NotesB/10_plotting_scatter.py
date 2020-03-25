import csv
import matplotlib.pyplot as plt
import numpy as np

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

header = data.pop(0)
print(header)

# make a scatter of firearms_per_100  vs homicides_100k

homicide_100k = []
firearms_100 = []
countries = []

for country in data:
    try:
        homicides = float(country(5))
        firearms = float(country(-2))
        name = country[0]
        homicide_100k.append(homicides)
        firearms_100.append(firearms)
        countries.append(name)
    except:
        print(country[0], "data is inadequate.")

print(countries)

plt.figure("Homicides per Firearm Worldwide")  # add figsize

plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")

plt.show()
