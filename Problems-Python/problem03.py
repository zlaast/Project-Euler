# Project Euler: Problem 3
# Largest Prime Factor

from math import sqrt
from PEF import soe

number = 600851475143
primes = soe(10000)

for prime in primes:
    if (number == 1):
        break

    while (number % prime == 0):
        number = number / prime
        print(prime)

if (number != 1):
    print("Error: Generate larger prime list")