#Height Units
print("Enter your height:")
feet_user = int(input("feet: "))
inches_user = int(input("inches: "))
cm = feet_user * 12 * 2.54 + inches_user * 2.54
print("Your heigth in cm is %i" %cm)

