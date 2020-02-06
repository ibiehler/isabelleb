# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list1 = [x for x in range(101)]

# b) Make a list of even numbers from 20 to 40
my_list2 = [x for x in range(20, 41) if (x ** 2) % 2 == 0]

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list3 = [x ** 2 for x in range(101)]

# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_new_list = [x for x in my_list if x > 0]


# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
from Problems import number_list

# Print the last 5 numbers in num_list
number_list1 = number_list.num_list
print(number_list1[-5:])


# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(number_list1))

# Find and print the lowest number in num_list (1pt)
print(min(number_list1))

# Find and print the average of num_list (2pts)
sum1 = 0
for i in range(len(number_list1)):
    sum1 += number_list1[i]

average = sum1/(len(number_list1))
print(average)

# Remove the lowest number from num_list (2pt)
del number_list1[number_list1.index(min(number_list1))]

# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
top_ten = []
number_list1.sort()
top_ten.append(number_list1[-10:])
print(top_ten)


# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
list_being_used = number_list.num_list
number1 = list_being_used[0]
prev_frequency = 0

for num in list_being_used:
    current_frequency = list_being_used.count(num)
    if current_frequency > prev_frequency:
        number1 = num
        prev_frequency = current_frequency


print(number1)


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
number_list2 = number_list.num_list
prime_number_list = []

# I've made a function like this before (when I did some coding during the summer) so I edited it to match...
# this question & I can show you the original one if you want
for num in range(len(number_list2)):
    number = number_list2[num]
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        if number not in prime_number_list:
            prime_number_list.append(number)

print(len(prime_number_list))


# Find the number of palindromes
# Hint: This may be easier to do with strings
palindromes = 0

for i in range(len(number_list1)):
    possible_palindrome = str(number_list1[i])
    if possible_palindrome[0] == possible_palindrome[3] and possible_palindrome[1] == possible_palindrome[2]:
        palindromes += 1

print(palindromes)


