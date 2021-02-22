# Admission Price
children = 14
senior = 18
others = 23
ages = input("Enter an age (blank line to quit): ")
total = 0
while ages != "":
    ages_n = int(ages)
    if ages_n <= 2:
        total += 0
    elif ages_n <= 12:
        total += children
    elif ages_n >= 65:
        total += senior
    else:
        total += others
    ages = input()
print("The entire cost is %.2f" % total)
