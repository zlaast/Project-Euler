# Project Euler: Problem 23
# Non-abundant sums
# https://en.wikipedia.org/wiki/Abundant_number

from PEF import factorization as f, soe

# Find all abundant numbers up to 28123
n = 28124
abundants = [False] * n

for i in range(2, n):
    if (sum(f(i)) > i):
        abundants[i] = True

# Primes aren't abundant. Remove them as well (for now)
primes = soe(n)
for prime in primes:
    abundants[prime] = False

# Find which numbers cannot be written as the sum of two abundants
sum_of_two_abundants = [True] * n
for i in range(2, n):
    if (abundants[i]):
        for ii in range(2, n):
            if (abundants[ii]):
                if (i + ii < n):
                    sum_of_two_abundants[i+ii] = False

# Sum all the integers that cannot expressed as the sum of two abundant numbers
# Starts at 1 because 1 cannot be expressed as the sum of two abundants
total = 1
for i in range(2, n):
    if (sum_of_two_abundants[i]):
        total += i

print(total)