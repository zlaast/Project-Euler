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

def prime_check(num):
    ''' Checks if number is prime '''
    if num < 2:
        return False

    for value in range(2, int(math.sqrt(num) + 1)):
        if (num % value == 0):
            return False  # Number is not prime
    return True  # Number is prime

def prime_factorization(num):
    ''' Performs prime factorization on a number and returns a list '''

    prime_factors = []
    n = 2
    while True:
        if prime_check(n):
            while (num % n == 0):
                num = num // n
                prime_factors.append(n)
        if (num == 1):
            break
        n += 1
    return prime_factors

def factorization(num):
    ''' Returns all factors of a number '''

    prime_factors = prime_factorization(num)

    factors = []
    for length in range(2, len(prime_factors)):
        comb = combinations(prime_factors, length)
        
        for i in comb:
            factors.append(math.prod(i))

    factors.append(1)
    factors += prime_factors
    factors = set(factors)
    factors = sorted(factors)

    return factors
