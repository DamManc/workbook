#Units of Time (Again)
print("Calculate from seconds to  D:HH:MM:SS format ")
sec = int(input("Enter a total number of seconds: "))
days = sec // (1 * 24 * 60 * 60)
days_s = days * 24 * 60 * 60
hours = (sec - days_s) // (1 * 60 * 60)
hours_s = hours * 60 * 60
minutes = (sec - days_s - hours_s) // (1 * 60)
minutes_s = minutes * 60 
seconds = sec - days_s - hours_s - minutes_s
print("It is: %i:%02d:%02i:%02i"  %(days, hours, minutes, seconds))
