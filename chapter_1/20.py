#Ideal Gas Law
import math
IDEAL_GAS = 8.314
pressure = float(input("Enter a pressure in Pascals of a gas: "))
volume = float(input("Enter a volume in liters of a gas: "))
temperature_k = 273.15 + float(input("Enter a temperature in Celsius of a gas:"))
n_moles = (pressure * volume) / (IDEAL_GAS * temperature_k)
print("Amount of gas in moles is: %.3f" %n_moles)