# Project Euler: Problem 22
# Names scores

# Open file and separate names into a list. Use commas as the delimiter
with open("p022_names.txt") as p022_names:
    raw_names = p022_names.read()

# Split names using comma as delimiter, remove quotations, and sort
names = sorted(raw_names.replace('"', '').split(','))

# Calculate name scores
count = 0
total_score = 0
for name in names:
    count += 1
    
    # Calculate alphabetical score
    score = 0
    for letter in name:
        score += (ord(letter) - 64)

    # Calculate total score
    total_score += score*count

print(total_score)