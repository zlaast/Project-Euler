# Project Euler: Problem 14
# Longest Collatz sequence

max_count = 0

for n in range(1, 1000000):
    count = 0
    start_num = n
    while n!= 1:
        count += 1

        if (n % 2 == 0):
            n //= 2
        else:
            n = 3*n + 1

    if (count > max_count):
        max_count = count
        print(start_num, max_count)
