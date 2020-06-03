import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/lin/PycharmProjects/P2_SP20/Final/harry_potter.csv')
df = df[df['Eye colour'].notna()]  # eye color had unknown values
df = df[df['House'].notna()]  # houses had unknown values

# 1st Question
purebloods = df.loc[df["Blood status"] == 'Pure-blood']  # sorting into purebloods

hair_list = purebloods['Hair colour'].tolist()  # googled how to make data into list
freq = {}  # empty dictionary


def freq_counter(my_list, my_dict):  # converting the list into a dictionary (so it's easier to graph)
    for item in my_list:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1


freq_counter(hair_list, freq)

plt.bar(range(len(freq)), list(freq.values()), color='red')  # plotting dict as a bar graph

# labels
plt.xticks(range(len(freq)), list(freq.keys()), fontsize=6)
plt.xlabel("Hair Color")
plt.ylabel("Number of People")
plt.title("Pure-Blood Hair Color Frequencies")

plt.show()


# 2nd Question
slyth = df.loc[df["House"] == 'Slytherin']  # sorting into Slytherins

eye_list = slyth['Eye colour'].tolist()
eye_freq = {}  # empty dictionary

freq_counter(eye_list, eye_freq)  # calling function made above

plt.bar(range(len(eye_freq)), list(eye_freq.values()), color='green')  # plotting dict as a bar graph

# labels
plt.xticks(range(len(eye_freq)), list(eye_freq.keys()), fontsize=6)
plt.xlabel("Eye Color")
plt.ylabel("Number of People")
plt.title("Slytherin Eye Color Frequencies")

plt.show()


# 3rd Question
half = df.loc[df["Blood status"] == 'Half-blood']  # sorting into half-bloods

house_list = half['House'].tolist()
house_freq = {}  # empty dictionary

freq_counter(house_list, house_freq)  # calling function made above

plt.bar(range(len(house_freq)), list(house_freq.values()), color='blue')  # plotting dict as a bar graph

# labels
plt.xticks(range(len(house_freq)), list(house_freq.keys()), fontsize=6)
plt.xlabel("Hogwarts House")
plt.ylabel("Number of People")
plt.title("Hogwarts Half-Blood Frequencies")

plt.show()





