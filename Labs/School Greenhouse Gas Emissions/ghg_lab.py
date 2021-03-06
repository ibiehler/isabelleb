
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts) *
- Data includes ONLY data for K-12 Schools. (5pts)  *
- Data includes ONLY data for 2018 reporting. (5pts)  *
- Label x and y axis and give appropriate title. (5pts)  *
- Annotate Francis W. Parker. (5pts) *
- Create a best fit line for schools shown. (5pts)  *


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.
(feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''
import csv
import requests
import numpy as np
import matplotlib.pyplot as plt


def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        content = download.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        my_list = list(reader)
        return my_list


data = get_data("https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD")

header = data.pop(0)

print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")


valid_ish_data = []
valid_data = []

for building in data:
    try:
        int(building[ghg_index])
        int(building[sqft_index])
        if building[type_index] == "K-12 School":
            valid_ish_data.append(building)
    except:
        pass


for section in valid_ish_data:
    if section[0] == "2018":
        valid_data.append(section)

print(valid_data)

ghg = [int(x[ghg_index]) for x in valid_data]
sqft = [int(x[sqft_index]) for x in valid_data]

plt.ylabel("Total Greenhouse Gas (GHG) Emmissions")
plt.xlabel("Building Square Footage")
plt.title("Energy Efficiency of Chicago Schools in 2018")


# annotation; Parker was not within the 2018 data so I annotated for Latin instead
schools = []

for school in valid_data:
    schools.append(school[2])

for i in range(len(schools)):
    if schools[i] == "Latin School of Chicago Upper School":
        plt.annotate(schools[i], xy=(sqft[i], ghg[i]), fontsize=5)


# best fit line
p = np.polyfit(sqft, ghg, 1)  # (x, y, order) linear is 1st order
print(p)

x = [x for x in range(500000)]
y = [p[0] * y + p[1] for y in x]  # linear first order

plt.plot(x, y)


# extra credit: Make schools in bottom 10 percent GHG Intensity show in red.
ghg_intensity = []
lowest_intensity = []
color = []

for intensity in valid_data:
    ghg_intensity.append(float(intensity[-4]))

ghg_intensity.sort()
lowest_intensity.append(ghg_intensity[:3])
print(lowest_intensity[0])

for intensity in valid_data:
    if lowest_intensity[0][2] >= float(intensity[-4]):
        color.append("red")
    else:
        color.append("green")


plt.figure(1, tight_layout=True)
plt.scatter(sqft, ghg, alpha=0.3, c=color)

plt.show()

