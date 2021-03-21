# Exercise 91: Gregorian Date to Ordinal Date
def checkLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


jan = 31
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
oct = 31
nov = 30


def ordinalDate(day, month, year):
    previous_days = 0
    if checkLeap(year):
        feb = 29
    else:
        feb = 28
    if month == 2:
        previous_days += jan
    elif month == 3:
        if checkLeap(year):
            previous_days += jan + feb
        else:
            previous_days += jan + feb
    elif month == 4:
        previous_days += jan + feb + mar
    elif month == 5:
        previous_days += jan + feb + mar + apr
    elif month == 6:
        previous_days += jan + feb + mar + apr + may
    elif month == 7:
        previous_days += jan + feb + mar + apr + may + jun
    elif month == 8:
        previous_days += jan + feb + mar + apr + may + jun + jul
    elif month == 9:
        previous_days += jan + feb + mar + apr + may + jun + jul + aug
    elif month == 10:
        previous_days += jan + feb + mar + apr + may + jun + jul + aug + sep
    elif month == 11:
        previous_days += jan + feb + mar + apr + may + jun + jul + aug + sep + oct
    elif month == 12:
        previous_days += jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov
    print(previous_days + day, year)


if __name__ == "__main__":
    day = int(input("Enter a day (01-31): "))
    while day < 0 or day > 31:
        day = int(input("Enter a affective day (1-31): "))
    month = int(input("Enter a month(01-12 or 1-12): "))
    while month < 1 or month > 12:
        month = int(input("Enter a affective month(01-12 or 1-12): "))
    year = int(input("Enter an year: "))

    ordinalDate(day, month, year)
