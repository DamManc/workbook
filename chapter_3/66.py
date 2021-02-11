# No More Pennies
import math

price = str(input("Enter a price in dollar, you can stop with blank value: "))
p_float = 0
tot_no_round = 0
tot_round = 0
while price != "":
    p_float = float(price)
    price = str(input())
    tot_no_round += p_float
    p_pennies = p_float * 100
    rem_cent = p_pennies % 5
    if rem_cent < 2.5:
        p_pennies -= rem_cent
    else:
        p_pennies += 5 - rem_cent
    p_round = p_pennies * 0.01
    tot_round += p_round
print("No Cash: %.2f" % tot_no_round)
print("With Cash: %.2f" % tot_round)
