#Area of a Regular Polygon
import math
print("Calculate an area of a regular Polygon")
side = float(input("Enter a length of a sides: "))
n = float(input("Enter a number of a slides: "))
tan = math.tan(math.pi / n)
area = (n * side * side) / (4 * tan )
print("The Area is: %.2f" %area)