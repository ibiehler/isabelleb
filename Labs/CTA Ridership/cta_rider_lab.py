
'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s).
Just add a comment here to explain. (2pts)
'''

import matplotlib.pyplot as plt
import csv

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(data)

# headers
headers = data.pop(0)

# get last 10 years (years)
years = [x[0] for x in data]
ten_years = years[-10:]
print(ten_years)

# get last ten years bus
bus = [int(x[1]) for x in data]
ten_bus = bus[-10:]
print(ten_bus)

# get last ten years rail
rail = [int(x[3]) for x in data]
ten_rail = rail[-10:]
print(ten_rail)

# get last ten years total
total = [int(x[-1]) for x in data]
ten_total = total[-10:]
print(ten_total)


# plot bus
plt.plot(ten_years, ten_bus, linewidth=2, label='Bus Usage', marker='o')

# plot rail
plt.plot(ten_years, ten_rail, linewidth=2, label='Rail Usage', marker='o')

# plot total
plt.plot(ten_years, ten_total, linewidth=2, label='Total Usage', marker='o')


# axis labels
plt.xlabel("Year", fontsize=15)
plt.ylabel("Ridership (Hundred Millions)", fontsize=15)

# title
plt.title("CTA Ridership (2009 - 2018)", fontsize=20)

# legend
plt.legend()

# show plot
plt.show()


# hypothesis / trend analysis (you said what trend/trends so I just analyzed one trend)

'''
After 2015, the total ridership progressively declined, possibly due to the increasing popularity of 
ride-hailing services such as Uber and Lyft. Commute time is an important factor to many people, and using ride-hailing 
services is often faster than public transportation, a factor contributing to their popularity. CTA ridership 
(especially bus) is influenced by gas prices at any given time. Another possible reason for ridership declining (mostly 
in the total and bus areas) could be low gas prices. This would also explain why rail ridership was not declining as
severely, as it does not rely on gas. 
'''

