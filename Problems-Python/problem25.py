# Project Euler: Problem 25
# 1000-digit Fibonacci number
# Reference: 2

index = 1
length = 0

f2 = 0
f1 = 1
while length != 1000:
    f = f1 + f2
    f2, f1 = f1, f

    length = len(str(f))
    index += 1

print(index)