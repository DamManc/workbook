# Roots of a Quadratic Function
import math

a = float(input("Enter the first value different from 0: "))
b = float(input("Enter the second value: "))
c = float(input("Enter the third value: "))
discriminant = (b ** 2) - (4 * a * c)
if discriminant < 0:
    print("The quadratic equation does not have any real roots.")
else:
    root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The first real roots is %.2f" % root_1)
    print("The second real roots is %.2f" % root_2)
