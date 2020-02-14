'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re


def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
'''
file = open('../Searching/dictionary.txt')
list_of_words = []
word_len = 0

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        list_of_words.append(word)

length_amount = []
length_list = []
for word in list_of_words:
    new_len = len(word)
    length_amount.append(new_len)
    length_amount.sort()
    if new_len == length_amount[-1]:
        length_list.append(word)

print(length_list[-1])
'''
# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
file = open('../Searching/AliceInWonderLand.txt')
list_of_words = []
word_len = 0

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        list_of_words.append(word)

print("There are", len(list_of_words), " words in Alice In Wonderland.")

for word in list_of_words:
    word_len += len(word)

word_len = word_len/len(list_of_words)
print("The average word length in Alice In Wonderland is", word_len)

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_count = []
for word in list_of_words:
    if word == "ALICE":
        alice_count.append(word)
print("The name Alice appears", len(alice_count), "times.")


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_letter_words = []
repeated_words = []
other_list = []
for word in list_of_words:
    if len(word) == 7:
        seven_letter_words.append(word)

for word in seven_letter_words:
    frequency = seven_letter_words.count(word)
    repeated_words.append(frequency)
    repeated_words.sort()
    if frequency == repeated_words[-1]:
        other_list.append(word)

print("The seven letter word that occurs the most frequently is", other_list[-1])

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

cheshire_count = []
for word in list_of_words:
    if word == "CHESHIRE":
        cheshire_count.append(word)
print("The word Cheshire appears", len(cheshire_count), "times.")

cat_count = []
for word in list_of_words:
    if word == "CAT":
        cat_count.append(word)
print("The word cat appears", len(cat_count), "times.")

cheshire_cat_count = 0
for num in range(len(list_of_words)):
    current_word = list_of_words[num]
    if current_word == "CHESHIRE" and list_of_words[num + 1] == "CAT":
        cheshire_cat_count += 1

print("The word 'Cheshire' immediately followed by 'Cat' (Cheshire Cat) occurs", cheshire_cat_count, "times.")


