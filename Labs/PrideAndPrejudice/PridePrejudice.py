'''
Pride and Prejudice (25pts)

This lab is largely review of: lists, comprehensions, requests, string methods, matplotlib.
The only new item here is using a dictionary (dict).

We will use list, dictionary, and graphing skills to do a basic analysis of Jane Austen's Pride and Prejudice.
Your task is to create a bar graph of the 25 most common words.


A common Python pattern to count objects, produce histograms, or update stats is to make calls to a dictionary as you
iterate through a list. For example, given a list of words, you can create a dictionary to store counts and then
iterate through the list of words, checking how many times each word has appeared using your dictionary, and updating
the dictionary count now that you've seen that word again.
'''

# PSEUDO CODE
# Get text from http://www.gutenberg.org/files/1342/1342-0.txt - Use requests library. *
# Split the transcript into words - Use split and strip methods and store results in a list. *
# Create a dictionary object to store the word counts *
# Iterate through the list/text of Pride and Prejudice *
# Update word counts on your dict (10pts)  {'word1': 5, 'word2': 2...} *
# Sort words by counts in descending order (5pts) *
# Create Bar Graph (5pts) *
# Include descriptive titles and labels (5pts) *

import requests
import matplotlib.pyplot as plt
import operator

url = "http://www.gutenberg.org/files/1342/1342-0.txt"
pride = requests.get(url).text

wordlist = pride.split()
wordlist = [x.upper().strip(' "?.,:;!\\[](){}<>*-#1234567890\\\n\t') for x in wordlist]

frequencies = {}

for item in wordlist:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1


# used this link as a resource:
# https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
sorted_frequencies = dict(sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True))

print(sorted_frequencies)

keys = list(sorted_frequencies.keys())
values = list(sorted_frequencies.values())
top_25_keys = keys[:25]
top_25_values = values[:25]

plt.figure(1, tight_layout=True)
plt.barh(top_25_keys, top_25_values)
plt.title("Pride and Prejudice Top 25 Most Common Word Counts")
plt.xlabel("Word Counts")
plt.yticks(top_25_keys, top_25_keys, fontsize=4)


plt.show()

# CHALLENGE (OPTIONAL)
# Here is a list of the 1000 most common words in English:
# https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt
# Make your plot show the 25 most common words in Hamlet NOT in this list.

# MORE CHALLENGES
# look at Project Gutenberg, and try another book and see if your algorithms hold up.
# HERE IS A LIST OF NEGATIVE WORDS.  Evaluate a text for percentage of negative words.
# Try the same for positive.  Or do both to evaluate the mood of a book.  Compare Mark Twain to Edgar Allan Poe.
# https://gist.githubusercontent.com/mkulakowski2/4289441/raw/dad8b64b307cd6df8068a379079becbb3f91101a/negative-words.txt


