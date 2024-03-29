# Project Euler: Problem 26
# Reciprocal cycles

from PEF import soe

def full_reptend_check(p) -> bool:
    for k in range(1, p):
        if (10**k) % p == 1:
            if k == p-1:
                return True
            else:
                return False

primes = soe(1000)
for p in reversed(primes):
    if(full_reptend_check(p)):
        print(p)
        break