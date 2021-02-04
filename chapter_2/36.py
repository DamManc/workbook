#Dog Years
FIRST_DOG_Y = 10.5
REM_DOG_Y = 4 
years = int(input("Enter a human years: "))
if(years < 0):
    print("Your number is negative, run another time the program with integer")
elif(years >= 2):
    value = 2 * FIRST_DOG_Y 
    rem_year = (years - 2) * REM_DOG_Y
    tot = value + rem_year
    print("Your number is %.2f dog's years" %tot)
else:
    tot = years * FIRST_DOG_Y
    print("Your number is %.2f dog's years" %tot)
