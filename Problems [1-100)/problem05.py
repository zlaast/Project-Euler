# Project Euler: Problem 5
# Smallest Multiple

import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]
factors = []

for num in range(2, 21):
    list = set()

    # Steps 1 and 2: Perform prime factorization on each number
    # and discard duplicate factors
    for prime in primes:
        while (num % prime == 0):
            num = num / prime
            list.add(prime)

    # Step 3: Discard factorizations with different numbers
    if len(list) == 1:
        factors.append(list.pop())

# Step 4: Multiply all factors
print(math.prod(factors))