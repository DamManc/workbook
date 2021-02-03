#Free Fall
import math
g = 9.8
heigth_user = float(input("Enter a Heigth in meters: "))
vf = math.sqrt(2*heigth_user* g)
print("Final velocity is: %.2f m/s" %vf )