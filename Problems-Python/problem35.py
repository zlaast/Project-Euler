# Project Euler: Problem 35
# Circular Primes

from collections import deque
from PEF import soe

# Setup
total = 13
primes = soe(1000000)
circular_primes = [False]*1000000

# Prologue
cpl = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
for v in cpl:
    circular_primes[v] = True

# Solution
for prime in primes:
    if circular_primes[prime] == False:
        str_prime = str(prime)
        length = len(str_prime)

        # Circulate it!
        if '0' not in str_prime:
            nums = [prime]
            buffer = deque(str_prime, maxlen=length)
            for _ in range(length - 1):
                left = buffer.popleft()
                buffer.append(left)
                nums.append(int(''.join(buffer)))

            t = 0
            for num in nums:
                if num in primes:
                    t += 1

            if t == len(nums):
                for num in nums:
                    circular_primes[num] = True
                    total += 1

print(total)