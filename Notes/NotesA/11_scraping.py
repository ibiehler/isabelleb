# Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # uniform resource locator

page = requests.get(url)
print(page)  # prints the response; 200 is a good request

# print(page.text)  # text of the webpage (not that useful)


soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())  # make it print formatted; nicer way to look at it

# find data in our soup object by tagname
# find method just gets the first one it finds
title = soup.find("title")  # look for the <title> and returns the first one
print(title)
print(title.text)

# by attribute
print("\n * 10")
authors = soup.find_all(itemprop="author")
print(authors)
print(type(authors))

for author in authors:
    print(author.text)

# by css class
print("\n" * 10)
quotes = soup.find_all(class_="quote")
print(quotes[0].prettify())

# drill down using dot notation
print(quotes[0].span)
print(quotes[0].span.text)

for quote in quotes:
    print(quote.span.text)

# use authors and quotes together
for i in range(len(quotes)):
    print(quotes[i])
    print("\t\t---{}".format(authors[i].text))
    print()


# You can also combine search terms

quotes = soup.find_all("span", class_="text", itemprop="text")

for quote in quotes:
    print(quote.text)

