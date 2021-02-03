#Distance Units
feet_user = int(input("Enter the measurement in feet: "))
inches = feet_user * 12
yards = feet_user * 0.33333
miles = feet_user * 0.00018939
print("It is %.2f inches, %.2f yards, %.2f miles" % (inches, yards, miles))