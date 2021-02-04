# Month Name to Number of Days
month = str(input("Enter a name of a month: "))
if (
    month == "January"
    or month == "February"
    or month == "March"
    or month == "April"
    or month == "May"
    or month == "June"
    or month == "July"
    or month == "August"
    or month == "September"
    or month == "October"
    or month == "November"
    or month == "December"
):
    if (
        month == "January"
        or month == "March"
        or month == "May"
        or month == "July"
        or month == "August"
        or month == "October"
        or month == "December"
    ):
        numb_days = "31 days"
    elif month == "February":
        numb_days = "28 or 29 days"
    else:
        numb_days = "30 days"
    print("The number of days in that month is %s" % numb_days)
else:
    print("Invalid month's name, run the program again..")
