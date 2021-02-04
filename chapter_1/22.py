#Area of a Triangle (Again)
import math
print("Calculate an area of a Triangle")
side_1 = float(input("Enter a side:"))
side_2 = float(input("Enter a side:"))
side_3 = float(input("Enter a side:"))
s = (side_3 + side_1 + side_2) / 2
area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
print("The Area is: %.2f" %area)