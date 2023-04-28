# Project Euler: Problem 5
# Smallest Multiple

import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]
factors = []

for num in range(2, 21):
    list = []

    # Step 1: Perform prime factorization on each number
    for prime in primes:
        while (num % prime == 0):
            num = num / prime
            list.append(prime)

    # Step 2: Create a set, discarding duplicate numbers
    uniq_set = set(list)

    # Step 3: Discard factorizations with different numbers
    if len(uniq_set) == 1:
        factors.append(uniq_set.pop())

# Step 4: Multiply all factors
print(math.prod(factors))