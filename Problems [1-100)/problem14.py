# Project Euler: Problem 14
# Longest chain chain

max_starting_number = 0
max_chain_length = 0
stored_chain_length = [0, 1]

for starting_number in range(1, 1000000):    
    chain_length = 0
    n = starting_number

    while n != 1:
        chain_length += 1

        if (n % 2 == 0):
            n //= 2

        else:
            n = 3*n + 1

        if (n <= starting_number):
            chain_length += stored_chain_length[n]
            stored_chain_length.append(chain_length)
            break

    if (chain_length > max_chain_length):
        max_starting_number, max_chain_length = starting_number, chain_length

print(max_starting_number, max_chain_length)