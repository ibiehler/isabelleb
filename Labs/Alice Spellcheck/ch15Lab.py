'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# Read the file dictionary.txt into an array. Call it dictionary_list or something similar. Then, close the file.
with open('../Alice Spellcheck/dictionary.txt') as f:
    dictionary_list = [x.strip().upper() for x in f]

f.close()

# LINEAR SEARCH
# Print --- Linear Search --- & Open the file AliceInWonderLand200.txt
print("--- Linear Search ---")
alice_200 = open('../Alice Spellcheck/AliceInWonderLand200.txt')
line_number = 0


# function
def linear_search(key, my_list, line_number):
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1
    if i < (len(my_list) - 1):
        return True
    else:
        print(key, "not found in dictionary. Found in Alice in Wonderland at line", line_number)
        return False


# for loop
for line in alice_200:
    line = line.strip().upper()
    words = split_line(line)
    line_number += 1
    for word in words:
        linear_search(word, dictionary_list, line_number)


# BINARY SEARCH
print("\n--- Binary Search ---")
file = open('../Alice Spellcheck/AliceInWonderLand200.txt')

# function
line_number2 = 0


def binary_search(key, my_list, line_number):
    found = False
    lower_bound = 0
    upper_bound = len(my_list) - 1
    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
        return True
    else:
        print(key, "was not found. Found in Alice in Wonderland at line", line_number2)


for line in file:
    line = line.strip().upper()
    words = split_line(line)
    line_number2 += 1
    for word in words:
        binary_search(word, dictionary_list, line_number2)


# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.




