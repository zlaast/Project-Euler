# Project Euler Functions (PEF)

import math
from itertools import combinations

def soe(n):
    '''Sieve of Eratosethenes. Finds prime numbers'''

    primes = []
    number_list = [True]*(n+1)

    for i in range(2, n+1):
        if number_list[i]:
            primes.append(i)

            # Eliminate multiples. They aren't prime
            for multiple in range(i**2, n+1, i):
                number_list[multiple] = False
    
    return primes

def p_factor(num):
    """ Returns the prime factors of a number """
    
    if 'primes' not in p_factor.__dict__:
        p_factor.primes = soe(num//2)

    # Prime Factorization
    prime_factors = []
    for prime in p_factor.primes:
        if (num == 1):
            break

        while (num % prime == 0):
            prime_factors.append(prime)
            num = num // prime

    return prime_factors

def factor(num):
    """ Returns the proper factors of a number """
    prime_factors = p_factor(num)
    proper_factors = {1}

    # Proper Factors
    for length in range(1, len(prime_factors)):
        comb = combinations(prime_factors, length)
        
        for i in comb:
            proper_factors.add(math.prod(i))

    return sorted(proper_factors)