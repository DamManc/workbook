#Volume of a Cylinder
import math
print("Volume if a Cylinder")
radius_user = float(input("Enter a radius: "))
heigth_user = float(input("Enter a heigth: "))
volume = math.pi * radius_user * radius_user * heigth_user
print("A volume of Cylinder is %.1f" %volume)