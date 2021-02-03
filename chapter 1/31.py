#Units of Pressure
pressure = float(input("Enter a pressure in kilo-pascals: "))
psi = pressure * 0.000145
mmHg = pressure * 0.0075006
atmo = pressure / 101325
print("Your pressure in psi is: %.2f, in mmHg is: %.2f, in atmosphere")