# What Color Is That Square?
position = str(input("Enter a position(es: a1): "))
if (
    position[0] == "a" or position[0] == "c" or position[0] == "e" or position[0] == "g"
) and int(position[1]) % 2 == 0:
    print("Your color is White")
elif (
    position[0] == "b" or position[0] == "d" or position[0] == "f" or position[0] == "h"
) and int(position[1]) % 2 == 1:
    print("Your color is White")
else:
    print("Your color is Black")
