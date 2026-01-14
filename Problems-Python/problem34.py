# Project Euler: Problem 34
# Digit Factorials

from math import factorial

sfd = 0
for i in range(3, 2999999):
    number = sum([factorial(int(x)) for x in str(i)])

    if (i == number):
        sfd += i

print(sfd)