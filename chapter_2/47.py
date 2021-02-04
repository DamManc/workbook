# Season from Month and Day
month = str(input("Enter a name of a month: "))
day = int(input("Enter a number of a day: "))
if (
    (month == "March" and day >= 20 and day <= 31)
    or month == "April"
    or month == "May"
    or (month == "June" and day <= 20)
):
    print("The Season is: Spring")
elif (
    (month == "June" and day >= 21 and day <= 30)
    or month == "July"
    or month == "August"
    or (month == "September" and day <= 21)
):
    print("The Season is: Summer")
elif (
    (month == "September" and day >= 22)
    or month == "July"
    or month == "August"
    or (month == "December" and day <= 20)
):
    print("The Season is: Fall")
else:
    print("The Season is: Winter")