# Coin Flip Simulation
import random

flips_count_tot = 0
TOT = 10
for i in range(0, TOT):
    same_outcome = 0
    flips_count = 0
    v_new = ""
    while same_outcome < 2:
        flips_count += 1
        r = random.random()
        if r > 0.5:
            v = "H"
        else:
            v = "T"
        print(v, "", end="")
        if v == v_new:
            same_outcome += 1
        else:
            same_outcome = 0
        v_new = v
    print("(%d flips)" % flips_count)
    flips_count_tot += flips_count
avg = flips_count_tot / TOT
print("On average, %.2f flips were needed." % avg)
