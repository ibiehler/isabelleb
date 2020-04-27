# Dictionaries (dict)

# list, tuple, int, float, bool, str, set, dict

# sets (not generally used often)
# a unique list of items (no repeats)
# uses {} instead of []
import random

my_set = {1, 2, 3, 4, 4, 5}
print(my_set)

my_list = ['milk', 'toilet paper', 'yeast', 'strawberries', 'milk']
print(set(my_list))  # change list into set


my_list = list(set(my_list))  # changing previously made set back into list
print(my_list)
print(type(my_list))


# Dictionaries
# why use them?
# they are unordered (unlike a list)
# {key1: val1, key2: val2...}
mister_lee = ['Aaron', 46, 'English', 'Python']
mr_lee = {'first name': 'Aaron', 'age': 46, 'spoken language': ['English', 'Pig Latin'], 'fav prog lang': 'python'}
print(mr_lee)

# TV shows
the_office = {'genre': ['Mockumentary', 'Sitcom'],
              'developedBy': 'Greg Daniels',
              'starring': ['Steve Carell', 'Rainn Wilson', 'John Krasinski', 'Jenna Fischer']
              }

# access to a dict
print(the_office['genre'])
# print(the_office[0]) produces error (keyerror)

# add to dictionary
the_office['num seasons'] = 9
print(the_office)
the_office['title'] = 'the office'

# change value
the_office['num seasons'] += 1
print(the_office)

# add to values
the_office['starring'].append('Mindy Kaling')
print(the_office)

# what are my keys?
print()
print(the_office.keys())  # iterable dict_key objects
print(the_office.values())  # dict_values object

# next show
parks_rec = {'title': 'Parks and Recreation',
             'created by': ['Greg Daniels', 'Michael Schur']}

shows = [the_office, parks_rec]
print()
print(shows)

# dictionaries are iterable
for key in the_office:
    print(the_office[key])

# even comprehensions work
new_dict = {x: "Hi" for x in range(10)}
print(new_dict)

# popping items
print(the_office.pop('genre'))
print(the_office)


# Using a dictionary to track (database like)
flips = [random.choice(['heads, tails']) for x in range(100)]

head_tails = {}

for flip in my_list:
    if flip == 'heads':
        if flip in head_tails:
            head_tails['heads'] += 1
        else:
            head_tails['heads'] = 1
    if flip == 'tails':
        if flip in head_tails:
            head_tails['tails'] += 1
        else:
            head_tails['tails'] = 1

print(head_tails)
