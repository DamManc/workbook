# Is It a Leap Year?
year = int(input("Enter a year: "))
if year % 4 != 0:
    print("%i is not a leap year" % year)
elif year % 100 != 0:
    print("%i is a leap year" % year)
elif year % 400 != 0:
    print("%i is not a leap year" % year)
else:
    print("%i is a leap year" % year)

