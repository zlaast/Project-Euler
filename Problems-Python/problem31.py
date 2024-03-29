# Project Euler: Problem 31
# Coin Sums

coins = [200, 100, 50, 20, 10, 5, 2, 1]
target = coins[0]

coin_sums = [0]*(target + 1)
coin_sums[0] = 1

for coin in coins:
    for i in range(target):
        if coin + i <= target:
            coin_sums[coin + i] += coin_sums[i]

print(coin_sums[target])