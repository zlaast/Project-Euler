# Project Euler: Problem 12
# Highly Divisible Triangular Number

import math
from collections import Counter
from PEF import soe

counter = 1
triangle_number = 1
primes = soe(20)

while True:
    # Generate Triangle Number
    counter += 1
    triangle_number += counter

    # Create copy that will be factored
    to_be_factored = triangle_number

    # Perform prime factorization on copy
    prime_factors = []
    for prime in primes:
        while(to_be_factored % prime == 0):
            to_be_factored = to_be_factored // prime
            prime_factors.append(prime)

    # Count the number of factors
    amount_of_factors = math.prod(list(map(lambda prime_count: prime_count + 1, Counter(prime_factors).values())))

    if (amount_of_factors > 500):
        print(triangle_number)
        break