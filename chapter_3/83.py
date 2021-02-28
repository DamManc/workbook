# Maximum Integer
import random

x_max = 0
count = 0
for i in range(1, 100):
    x = int(random.random() * 100)
    print(x, end="")
    if x > x_max and i != 1:
        print(" <== Update")
        count += 1
        x_max = x
    else:
        print()
print("The maximum value found was %d" % x_max)
print("The maximum value was updated %d times" % count)
