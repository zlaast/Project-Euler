# Project Euler: Problem 2
# Even Fibonacci Numbers

f2 = 0
f1 = 1
sum = 0

while f1 < 4000000:
    f = f1 + f2
    f2, f1 = f1, f

    if (f % 2 == 0): # if divisible by 2
        sum += f

print(sum)
    