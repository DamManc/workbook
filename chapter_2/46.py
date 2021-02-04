# What Color Is That Square?
position = str(input("Enter a position(es: a1): "))
if (
    position[0] == "a" or position[0] == "c" or position[0] == "e" or position[0] == "g"
) and int(position[1]) % 2 == 0:
    print("Your color is White")
else:
    print("Your color is Black")
