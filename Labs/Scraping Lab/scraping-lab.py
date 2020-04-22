# SCRAPING PROBLEMS
from bs4 import BeautifulSoup
import requests

# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.

# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.
# There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.
# Don't forget about our friend string.format()

# Indianapolis 10-day weather
url = "https://weather.com/weather/tenday/l/60726d811b7e36432583ede41c4600b07b8b2e94c237fa8c6c2a9085a511d43a/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# the variables
day = soup.find_all(class_='date-time')
date = soup.find_all(class_='day-detail clearfix')
description = soup.find_all(class_='description')
temp = soup.find_all(class_='temp')
humidity = soup.find_all(class_='humidity')
precipitation = soup.find_all(class_='precip')
wind = soup.find_all(class_='wind')


# sentence maker
for i in range(1, 11):
    print(day[i - 1].text + ",", date[i - 1].text, "will be", description[i].text, "with a High of",
          temp[i].text[:3] + " degrees and a low of " + temp[i].text[-3:] + ",", "humidity at",
          humidity[i].text + ".", "There is a", precipitation[i].text, "chance of rain with winds out of the",
          wind[i].text + ".")
    print("\n")




