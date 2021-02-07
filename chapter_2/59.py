# Next Day
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
if month == 2:
    if day == 28 or day == 29:
        day = 1
        month = 3
    else:
        day += 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        day = 1
        month += 1
    else:
        day += 1
elif month == 12:
    if day == 31:
        year += 1
        day = 1
        month = 1
else:
    if day == 31:
        day = 1
        month += 1
    else:
        day += 1
print("The next day is %03i-%02i-%02i" % (year, month, day))
