#Distance Between Two Points on Earth
import math
AV_RADIUS_KM = 6371.01
lat_a = float(input("Enter the t1 coordinate of latitude in degrees of A point: "))
long_a = float(input("Enter the g1 coordinate of longitude in degrees of A point: "))
lat_b = float(input("Enter the t2 coordinate a longitude in degrees of B point: "))
long_b = float(input("Enter the g2 coordinate a longitude in degrees of B point: "))
lat_rad_a = math.radians(lat_a)
long_rad_a = math.radians(long_a)
lat_rad_b = math.radians(lat_b)
long_rad_b = math.radians(long_b)
distance = AV_RADIUS_KM * math.acos(math.sin(lat_rad_a) * math.sin(lat_rad_b) + math.cos(lat_rad_a) * math.cos(lat_rad_b) * math.cos(long_rad_a - long_rad_b))
print("The distance of A and B is: %.2f km" %distance)