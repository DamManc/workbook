# Exercise 92: Ordinal Date to Gregorian Date
from es91 import *

LAST_DATE = 60


def gregorianDate(day, year, rest_day=False):
    if checkLeap(year):
        feb = 29
    else:
        feb = 28
    day_in_jan = day
    day_in_feb = day_in_jan - jan  # NUMBER OF DAYS THAT WAS PASSED MINUS JAN DAYS
    day_in_mar = day_in_feb - feb   # NUMBER OF DAYS THAT WAS PASSED MINUS (JAN DAYS + FEB DAYS)
    day_in_apr = day_in_mar - mar
    day_in_may = day_in_apr - apr
    day_in_jun = day_in_may - may
    day_in_july = day_in_jun - jun
    day_in_aug = day_in_july - jul
    day_in_sept = day_in_aug - aug
    day_in_oct = day_in_sept - sep
    day_in_nov = day_in_oct - oct
    day_in_dec = day_in_nov - nov
    n_day = 0

    if day_in_jan <= jan:  # NUMBER OF DAYS IS IN JAN ONLY IF THIS VALUE IS POSITIVE AND MINOR TO JAN DAYS
        month = 'January'
        n_day += day_in_jan
    elif day_in_feb <= feb:
        month = 'February'
        n_day += day_in_feb
    elif day_in_mar <= mar:
        month = 'March'
        n_day += day_in_mar
    elif day_in_apr <= apr:
        month = 'April'
        n_day += day_in_apr
    elif day_in_may <= may:
        month = 'May'
        n_day += day_in_may
    elif day_in_jun <= jun:
        month = 'June'
        n_day += day_in_jun
    elif day_in_july <= jul:
        month = 'July'
        n_day += day_in_july
    elif day_in_aug <= aug:
        month = 'August'
        n_day += day_in_aug
    elif day_in_sept <= sep:
        month = 'September'
        n_day += day_in_sept
    elif day_in_oct <= oct:
        month = 'October'
        n_day += day_in_oct
    elif day_in_nov <= nov:
        month = 'November'
        n_day += day_in_nov
    else:
        month = 'December'
        n_day += day_in_dec
    if rest_day:
        print("Last returned day: %s, month: %s, year: %i " % (n_day, month, year))
    else:
        print("day: %s, month: %s, year: %i " % (n_day, month, year))


if __name__ == "__main__":
    day = int(input("Enter a day (01-366): "))
    while day < 0 or day > 366:
        day = int(input("Enter a affective day (01-366): "))
    year = int(input("Enter an year: "))
    if checkLeap(year):
        gregorianDate(day, year)
    else:
        while day < 0 or day > 365:
            day = int(input("Enter a affective day (01-365). Entered year is not a Leap Year: "))
        gregorianDate(day, year)
    # call gregorianDate for print the last returned date
    if checkLeap(year):
        if day + LAST_DATE < 366:  # 366 because is a Leap Year and check if the returned date is within the year given
            gregorianDate(day + LAST_DATE, year, True)  # Last returned date for this product after 60 days
        else:
            gregorianDate((day + LAST_DATE) - 366, year + 1, True)  # call gregorianDate with new year and dates
    else:
        if day + LAST_DATE < 365:
            gregorianDate(day + LAST_DATE, year, True)  # Last returned date for this product after 60 days
        else:
            gregorianDate((day + LAST_DATE) - 365, year + 1, True)
