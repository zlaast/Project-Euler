# Project Euler: Problem 21
# Amicable numbers

from PEF import factor

amicables = []

for number in reversed(range(2, 10000)):
    if number in amicables:
        continue
    else:
        a = sum(factor(number))
        b = sum(factor(a))

        if (a != b and b == number):
            amicables.append(number)
            amicables.append(a)

print(sum(amicables))