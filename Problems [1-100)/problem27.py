# Project Euler: Problem 27
# Quadratic Primes

from itertools import count
from PEF import soe

primes = soe(1000)  # b max
max_a = 0
max_b = 0
max_count = 0

for a in range(-999, 1000, 2):
    for b in primes:
        prime_count = 0
        for n in count(1, 2):  # Odd numbers alone
            if n*(n+a) + b in primes:
                prime_count += 1
                if prime_count > max_count:
                    max_a = a
                    max_b = b
                    max_count = prime_count
            else:
                break
print(max_a*max_b, len(primes))
