# Classifying Triangles
TYPE_FIRST = "equilateral"
TYPE_SECOND = "isosceles"
TYPE_THIRD = "scalene"
side_one = int(input("Enter a first length of a triangle's side: "))
side_two = int(input("Enter a second length of a triangle's side: "))
side_three = int(input("Enter a third length of a triangle's side: "))
if side_two == side_one == side_three:
    print("The triangle will be", TYPE_FIRST)
elif side_two != side_one != side_three:
    print("The triangle will be", TYPE_SECOND)
else:
    print("The triangle will be", TYPE_THIRD)
