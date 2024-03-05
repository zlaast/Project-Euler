# Project Euler: Problem 22
# Names scores

# Read file
with open('names.txt') as file:
    names = file.read()

# Turn names into a alphabetical list
names = sorted(names.replace('"', "").split(","))

# Calculate Scores
total_score = 0
chart = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for index, name in enumerate(names):
    score = 0
    for letter in name:
        score += chart.index(letter)

    total_score += score*(index+1)

print(total_score)