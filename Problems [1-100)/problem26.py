# Project Euler: Problem 26
# Reciprocal cycles

# https://en.wikipedia.org/wiki/Repeating_decimal
# https://en.wikipedia.org/wiki/Multiplicative_order

# The length of the repetend (the repeating decimal part) is equal to the order of (10 % p)

from PEF import soe

primes = soe(1000)
cyclical = []
for p in primes:
    for k in range(1, p):
        if 10**k % p == 1:
            if k == p-1:
                cyclical.append(p)
            break

print(max(cyclical))