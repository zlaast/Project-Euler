# Project Euler: Problem 6
# Sum square difference

sum_square = 0
square_sum = 0

for num in range(1, 101):
    sum_square += num**2

for num in range(1, 101):
    square_sum += num

square_sum = square_sum**2

print(square_sum-sum_square)
