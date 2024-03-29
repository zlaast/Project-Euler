# Project Euler: Problem 25
# 1000-digit Fibonacci number

i = 1
length = 0

F_n_2 = 0
F_n_1 = 1
while length < 1000:
    F_n = F_n_1 + F_n_2

    F_n_2 = F_n_1
    F_n_1 = F_n

    length = len(str(F_n))
    i += 1

print(i)