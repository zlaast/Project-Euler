# Project Euler: Problem 32
# Pandigital Products

from itertools import permutations

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
perms = permutations(numbers)

sums = 0
memo = {}

for perm in perms:
    # 1 by 4
    a = perm[0]
    b = ''.join(perm[1:5])
    prod = int(a)*int(b)

    if prod < 9999:
        if prod not in memo:
            prod_str = ''.join(sorted(a + b + str(prod)))

            if prod_str == '123456789':
                memo[prod] = True
                sums += prod

    # 2 by 3
    a = ''.join(perm[:2])
    b = ''.join(perm[2:5])
    prod = int(a)*int(b)

    if prod < 9999:
        if prod not in memo:
            prod_str = ''.join(sorted(a + b + str(prod)))

            if prod_str == '123456789':
                memo[prod] = True
                sums += prod

print(sums)