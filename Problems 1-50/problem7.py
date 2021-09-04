# Project Euler: Problem 7
# 10001st prime

from soe import soe

number = 0
primes_cpy = []

while True:
    primes = soe(number)
    number += 1000

    if (len(primes) > 10001):
        primes_cpy = primes
        break

print(primes_cpy[10000])

    