# Project Euler: Problem 2
# Even Fibonacci Numbers

fp = 0                  # previous fibonacci number
fc = 1                  # current fibonacci number
sum = 0

while fc < 4000000:
    fn = fc + fp        # fn is the next fibonacci number

    if (fn % 2 == 0):   # if next is divisible by 2
        sum += fn

    fp = fc             # current becomes previous
    fc = fn             # next becomes current

print(sum)