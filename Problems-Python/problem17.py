# Project Euler: Problem 17
# Number Letter Counts

# Words
ones = len("onetwothreefourfivesixseveneightnine")
teens = len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
tens = len("twentythirtyfourtyfiftysixtyseventyeightyninety")
hundred = len("hundred")
and_ = len("and")

# Below 100
below_100 = 0
below_100 += ones                               # 1-9
below_100 += teens                              # 10-19
below_100 += tens*10 + ones*8                   # 20-99

# Hundreds
hundreds = 0
hundreds += ones + hundred*9                    # 100, 200, 300...
hundreds += ones*99 + (hundred + and_)*99*9     # "one hundred and ...", "two hundred and ..."
hundreds += below_100*9                         # below_100 is repeated 9 times

print(below_100 + hundreds + len("onethousand"))