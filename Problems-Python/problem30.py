# Project Euler: Problem 30
# Digit Fifth Powers

n = 5
search_range = n*(9**n)
sum_digits = 0

for number in range(2, search_range):
    num = [int(i) for i in str(number)]
    result = sum(map(lambda i: i**n, num))

    if result == number:
        sum_digits += number

    # This block is optional
    # For no apparent reason it allows the code
    # to execute on my computer ~200ms faster
    if result > search_range:
        break

print(sum_digits)