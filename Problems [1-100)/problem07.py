# Project Euler: Problem 7
# 10001st prime

from PEF import soe

primes = soe(120000)

if (len(primes) > 10001):
    print(primes[10000])
else:
    print("Use higher number")