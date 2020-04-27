# Folium train map
import folium
import csv
from folium import plugins

'''
15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level. *
5pts - Add the name to each stop as a popup. Add a train icon to each marker. Save as an html page in the same folder. *
3pts  - Color code all of the lines (make the pink line marker pink etc.) * 
2pts - Brown is not a default color name. See if you can use the documentation for Folium to set a marker 
color through other means.

# Data set is in this folder, but can be found at:
https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD
'''

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

station_map = folium.Map(location=[41.880443, -87.644107], zoom_start=10.5)

print(data.pop(0))
lat_longs = [eval(x[-1]) for x in data]
print(lat_longs[0])


def color_for_station(d):  # stops with multiple colors will display the first color that returned true
    if d[7] == 'true':
        return "red"
    if d[8] == "true":
        return "blue"
    if d[9] == "true":
        return "green"
    if d[10] == "true":  # brown line
        return "brown"
    if d[11] == "true" or d[12] == "true":
        return "purple"
    if d[13] == "true":  # yellow line
        return 'yellow'
    if d[14] == "true":
        return "pink"
    if d[15] == "true":
        return "orange"

    return "black"  # for any unidentified stops


for i in range(len(data)):
    color = color_for_station(data[i])
    folium.Marker(location=lat_longs[i],
                  popup=data[i][3],
                  icon=folium.plugins.BeautifyIcon(border_color=color, icon='train', prefix='fa')).add_to(station_map)
    if data[i][3] == "Sheridan":  # one of the Sheridan stops has red as false even though it's part of the red line
        folium.Marker(location=lat_longs[i],
                      popup=data[i][3],
                      icon=folium.plugins.BeautifyIcon(border_color="red", icon='train', prefix='fa')).add_to(
            station_map)


station_map.save('station_map.html')

# If you have extra time, try to put some html into the popup.
