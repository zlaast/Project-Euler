# Project Euler: Problem 23
# Non-abundant sums

from itertools import combinations_with_replacement
from PEF import factor, soe

n = 28124

# Find all abundant numbers and their multiples
abundants = [False]*n
for num in reversed(range(2, n)):
    if abundants[num] == False:
        if sum(factor(num)) > num:
            abundants[num] = True

            for multiple in reversed(range(num, n, num)):
                abundants[multiple] = True

# Get our list of abundant numbers
abundants = [num for num, i in enumerate(abundants) if i == True]

# Get sums of two abundants
combs = combinations_with_replacement(abundants, 2)
sums = set([sum(pair) for pair in combs])
sums = [x for x in sums if x < n]

# Get numbers that cannot be written as sum of two abundants
i = 0
total = 0
for number in range(1, n):
    if number == sums[i]:
        i += 1
    else:
        total += number

print(total)