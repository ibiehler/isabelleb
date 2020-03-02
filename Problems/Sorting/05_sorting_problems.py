'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import *

# 1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
first_item = data.pop(0)
print(first_item)

# 2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)

data.sort(reverse=True, key=lambda a: a[-1])
top_people = [x for x in data[:10]]
print("\nThe names of the top ten highest scoring single seasons in NBA history (in order):")
for athlete in top_people:
    print(athlete[2])


# 3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
kobe_points = 0
for athlete in data:
    if athlete[2] == "Kobe Bryant":
        kobe_points += athlete[-1]

print("\nKobe Bryant had", kobe_points, "career points.\n")
# 4  What player has the most 3point field goals in a single season? (3pts)
maximum_player = ""
maximum_fg = 0

for athlete in data:
    if maximum_fg < (athlete[-19]):
        maximum_fg = (athlete[-19])
        maximum_player = athlete[2]

print(maximum_player, "has the most 3point field goals in a single season.\n")

# 5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
maximum_player2 = ""
maximum_ws = 0

for athlete in data:
    if maximum_ws < (athlete[25]):
        maximum_ws = (athlete[25])
        maximum_player2 = athlete[2]

print(maximum_player2, "has the highest WS/48 season of all time.\n")

# 6  Write your own question that you have about the data and provide an answer (4pts)
# Who has the longest name?
longest_name = ""
length = 0
for athlete in data:
    if length < len(athlete[2]):
        longest_name = athlete[2]
        length = len(athlete[2])
        if "-" in athlete[2]:
            length -= 1

print(longest_name, "has the longest name.\n")

# 7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)

data.sort(reverse=True, key=lambda a: a[-1])
top_100 = [x for x in data[:100]]
top_100.sort(key=lambda a: a[-10])
print(top_100[0][2], "has the worst free-throw percentage.")
print(top_100[-1][2], "has the best free-throw percentage.")


