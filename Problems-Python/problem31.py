# Project Euler: Problem 31
# Coin Sums

count = 1                       # The 200p coin
for p200 in range(0, 2):
    for p100 in range(0, 3 - p200):
        if 200*p200 + 100*p200 > 200:
            break
        for p50 in range(0, 5 - p100):
            if 200*p200 + 100*p200 + 50*p50 > 200:
                break
            for p20 in range(0, 11 - p50):
                if 200*p200 + 100*p200 + 50*p50 + 20*p20 > 200:
                    break
                for p10 in range(0, 21 - p20):
                    if 200*p200 + 100*p200 + 50*p50 + 20*p20 + 10*p10 > 200:
                        break
                    for p5 in range(0, 41 - p10):
                        if 200*p200 + 100*p200 + 50*p50 + 20*p20 + 10*p10 + 5*p5 > 200:
                            break
                        for p2 in range(0, 101 - p5):
                            if 200*p200 + 100*p200 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 > 200:
                                break
                            for p1 in range(0, 201 - p2):
                                if p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200 == 200:
                                    count += 1
                                    # print(p1, 2*p2, 5*p5, 10*p10, 20*p20, 50*p50, 100*p100, 200*p200)

print(count)