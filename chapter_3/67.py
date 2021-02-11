# Compute the Perimeter of a Polygon
import math

x_first = float(input("Enter the first x-coordinate: "))
x_first_one = x_first
y_first = float(input("Enter the first y-coordinate: "))
y_first_one = y_first
x_second = input("Enter the next x-coordinate (blank to quit): ")
dist = 0
if x_second == "":
    x_second = -1
else:
    x_second_number = float(x_second)

while x_second != -1:
    y_second = float(input("Enter the next y-coordinate: "))
    dist += math.sqrt(
        ((x_second_number - x_first) * (x_second_number - x_first))
        + ((y_second - y_first) * (y_second - y_first))
    )
    x_another = input("Enter the next x-coordinate (blank to quit): ")
    if x_another == "":
        break
    else:
        x_another_number = float(x_another)
        x_first = x_second_number
        x_second_number = x_another_number
        x_second = x_another_number
        y_first = y_second

if x_second != -1:
    x_first = x_first_one
    y_first = y_first_one
    dist += math.sqrt(
        ((x_second_number - x_first) * (x_second_number - x_first))
        + ((y_second - y_first) * (y_second - y_first))
    )
    print("The perimeter of that polygon is %.2f" % dist)
else:
    quit()
