#Fuel Efficiency
US_fuel_eff = float(input("Enter a fuel efficiency in MPG:  "))
us_mi_to_km = US_fuel_eff * 1.609
us_ga_to_liters = us_mi_to_km / 3.785
invers = 1 / us_ga_to_liters
ca_fuel_eff = invers * 100
print("The fuel efficiency in L/100 is: %.2f" %ca_fuel_eff)