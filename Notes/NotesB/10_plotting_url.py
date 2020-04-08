"""
Reading a csv from a url
Comma Separated Values from a Uniform Resource Locator

scatter plot sizes and color
"""
import csv
import requests


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

