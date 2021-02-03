#Body Mass Index
import math
print("Found out your BMI")
heigth = float(input("Enter your heigth in meters: "))
weigth = float(input("Enter your weigth in kilograms: "))
bmi = weigth / (heigth * heigth)
print("Your BMI is %0.2f" %bmi)