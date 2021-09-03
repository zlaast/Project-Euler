# Project Euler: Problem 3
# Largest Prime Factor

from math import sqrt
from soe import soe         # This was written by me

number = 600851475143 
primes = soe(round(sqrt(number)))

for prime in primes:
    if (number == 1):
        break

    if (number % prime == 0):
        number /= prime
        print(prime)