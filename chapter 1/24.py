#Units of Time
print("Calculate total seconds: ")
days = float(input("Enter a days: "))
hours = float(input("Enter a hours: "))
minutes = float(input("Enter a minutes: "))
seconds = float(input("Enter a seconds: "))
calc_sec = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds 
print("The Area is: %i" %calc_sec)