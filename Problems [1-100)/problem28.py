# Project Euler: Problem 28
# Number Sprial Diagonals

dsum = 1  # ring 0
corner = 1

for ring in range(1, 501):
    for _ in range(0, 4):
        corner += 2*ring
        dsum += corner
print(dsum)