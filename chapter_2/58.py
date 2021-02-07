# Is It a Leap Year?
year = int(input("Enter a year: "))
rem_year_one = year % 400
rem_year_two = rem_year_one % 100
rem_year_three = rem_year_two % 4
if rem_year_one == 0 or rem_year_three == 0:
    print("%i is a leap year" % year)
else:
    print("%i is not a leap year" % year)
