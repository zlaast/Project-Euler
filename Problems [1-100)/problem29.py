# Project Euler: Problem 29
# Distinct Powers

ab = set()

for a in range(2, 101):
    for b in range(2, 101):
        ab.add(a**b)

print(len(ab))