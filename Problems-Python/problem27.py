# Project Euler: Problem 27
# Quadratic Primes

from PEF import soe

max_a = 0
max_b = 0
max_count = 0

p_primes = soe(1000)
n_primes = [-p for p in p_primes]
primes = n_primes + p_primes

for a in primes:
    for b in p_primes:
        prime_count = 0
        for n in range(1001):
            if n*(n+a)+b in p_primes:
                prime_count += 1
                if prime_count > max_count:
                    max_a = a
                    max_b = b
                    max_count = prime_count
            else:
                break

print(max_a*max_b)