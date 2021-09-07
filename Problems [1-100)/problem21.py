# Project Euler: Problem 21
# Amicable numbers

from PEF import prime_check as pc
from PEF import factorization as f

amicables = []
for a_ in range(1, 10001):

    if(pc(a_)):             # Skip if prime
        continue

    b = sum(f(a_))          # b = d(a)
    a = sum(f(b))           # a = d(b)

    if (pc(b)):             # Skip if prime
        continue

    if a == a_ and a != b:
        if a not in amicables and b not in amicables:
            amicables.append(a)
            amicables.append(b)

print(sum(amicables))