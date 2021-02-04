#Date to Holiday Name
month = str(input("Enter a name of a month: "))
day = int(input("Enter a number of a day that you want to consider: "))
if(month == "January" and day == 1):
    print("The holiday's name found out is: New Year’s Day")
elif(month == "July" and day == 1):
    print("The holiday's name found out is: Canada Day")
elif(month == "December" and day == 25):
    print("The holiday's name found out is: Christmas Day")
else:
    print ("The entered month and day do not correspond to a fixed-date holiday")