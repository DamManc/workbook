#Area and Volume
import math
radius_user = float(input("Enter a radius: "))
area = math.pi * radius_user * radius_user
volume = (4 / 3) * math.pi *  radius_user * radius_user * radius_user
print("areaof circle: %.2f and volume of that sphere: %.2f" %(area, volume))