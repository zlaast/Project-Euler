# Project Euler: Problem 28
# Number Spiral Diagonals

total = 1  # "ring" 0
corner = 1 # "corner" of "ring" 0

for ring in range(1, 501):
    for _ in range(0, 4):
        corner += 2*ring    # 3, 5, 7, 9, 13...
        total += corner     # 1, 4, 9, 16, 25... 
print(total)