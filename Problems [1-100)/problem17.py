# Project Euler: Problem 17
# Number letter counts

set1 = len("onetwothreefourfivesixseveneightnine")
set2 = len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
set3 = len("twentythirtyfortyfiftysixtyseventyeightyninety")
set4 = len("hundred")
set5 = len("and")
set6 = len("thousand")

a = set1 + set2 + (set3*10 + set1*8) # 1 - 99
b = (set1 * 100) + (set4 * 100 * 9) + (set5 * 99 * 9) + (a * 9) + 11  # 100 - 1000

print(a + b)