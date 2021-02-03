#Heat Capacity
print("Heat Capacity")
mass_water = float(input("Enter a mass of some water in grams o milliliters: "))
temp_change = float(input("Enter a temperature change in Celsius: "))
WATER_HEAT_CAP = 4.186
ELE_PRICE = 8.9
J_TO_KWH = 2.777e-7
energy = mass_water * WATER_HEAT_CAP * temp_change 
print("Total Energy must be: %.2f Joules" %energy)
kwh = energy * J_TO_KWH
bill = kwh * ELE_PRICE
print("Your bill is %.2f" %bill)
