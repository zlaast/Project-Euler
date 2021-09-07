# Project Euler: Problem 12
# Highly divisible triangular number

# https://www2.math.upenn.edu/~deturck/m170/wk2/numdivisors.html

from collections import Counter
from PEF import soe

counter = 1
triangle_number = 1
primes = soe(5000)

while True:
    # Increase the counter
    counter += 1

    # Generate triangle number, and store it in a temp variable
    triangle_number += counter
    temp = triangle_number

    # Perform prime factorization on temp variable
    ls = []
    for prime in primes:
        while (temp % prime == 0):
            temp //= prime
            ls.append(prime)

    # Count the number of prime factors, add one to each count, then multiply the counts
    num_divisors = 1
    factor_count = Counter(ls)
    for factor in factor_count.values():
        num_divisors *= (factor + 1)

    if (num_divisors > 500):
        break

print(triangle_number)
