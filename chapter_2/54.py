# Assessing Employees
RAISE = 2400
rating = float(input("Enter a rating: "))
if rating == 0.0:
    meaning = "Unacceptable Performance"
    employees_raise = RAISE * 0.0
elif rating == 0.4:
    meaning = "Acceptable Performance"
    employees_raise = RAISE * 0.4
elif rating >= 0.6:
    meaning = "Meritorious Performance"
    employees_raise = RAISE * 0.6
else:
    meaning = "This rating is not correct"
    employees_raise = -1
if employees_raise >= 0:
    print("The performance is a %s with a %.2f raise" % (meaning, employees_raise))
else:
    print("Your entered value is not correct, run again the program..")
