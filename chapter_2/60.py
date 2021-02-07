# What Day of theWeek Is January 1?
year = int(input("Enter a year: "))
day_of_the_week = (
    year + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)
) % 7
if day_of_the_week == 0:
    name_days = "Sunday"
elif day_of_the_week == 1:
    name_days = "Monday"
elif day_of_the_week == 2:
    name_days = "Tuesday"
elif day_of_the_week == 3:
    name_days = "Wednesday"
elif day_of_the_week == 4:
    name_days = "Thursday"
elif day_of_the_week == 5:
    name_days = "Friday"
elif day_of_the_week == 6:
    name_days = "Saturday"
else:
    name_days = "ERROR"
print("%s is the day of the week for January 1 of that year" % name_days)
