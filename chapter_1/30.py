#Celsius to Fahrenheit and Kelvin
import math
print("Celsius to Fahrenheit and Kelvin")
temp = float(input("Enter a temperature in Celsius: "))
kelvin = temp + 273.15
fah = (temp * 1.8) + 32
print("The conversion is: %.2f kelvin, %.2f fahrenheit" %(kelvin, fah))