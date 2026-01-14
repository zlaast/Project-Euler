# Project Euler: Problem 35
# Circular Primes

# https://oeis.org/A004023

from itertools import combinations
from PEF import soe

n = 100
primes = soe(n)
checked_circular = [False]*n
amount = 0

for prime in primes:

    if not checked_circular[prime]:
        circular = [x for x in str(prime)]
        perms = combinations(circular, len(circular))

        i = 0
        for perm in perms:
            print(perm)
            number = int(''.join(perm))
            checked_circular[number] = True

print(amount-1)