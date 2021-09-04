# Project Euler: Problem 5
# Smallest Multiple

import math
from soe import soe     # This was written by me

max_product = 20
primes = soe(max_product)

factors = []
for num in range(2, max_product+1):
    ls = []
    # Perform prime factorization
    for prime in primes:
        while (num % prime == 0):
            num /= prime
            ls.append(prime)
    
    # Discard duplicates from the list
    num_set = set(ls)

    # Discard factorizations with different numbers
    if len(num_set) == 1:
        factors.append(num_set.pop())

print(math.prod(factors))


'''
How this script works:

Using the example of 2520, we perform prime factorization
2520 = 2*2*2*3*3*5*7

If we do prime factorization of the numbers from 1-10 we get:
 1 = 1
 2 = 2
 3 = 3
 4 = 2*2
 5 = 5
 6 = 2*3
 7 = 7
 8 = 2*2*2
 9 = 3*3
10 = 2*5

If we discard "1" and any factorizations with different numbers in them (6 and 10), we get:
2 = 2
3 = 3
4 = 2*2
5 = 5
7 = 7
8 = 2*2*2
9 = 3*3

If we put the factorizations into sets (which discards duplicate values) we get:
2 = 2
3 = 3
4 = 2
5 = 5
7 = 7
8 = 2
9 = 3

The result, as you may notice is [2,3,2,5,7,2,3] which when rearranged is [2,2,2,3,3,5,7] which is the prime factorization of 2520!

'''



