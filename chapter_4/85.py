import math

side_one = float(input("Enter a value of the first side: "))
side_two = float(input("Enter a value of the second side: "))


def main(side_one, side_two):
    hypo = math.sqrt((side_one ** 2) + (side_two ** 2))
    print("The hypo is %.2f" % hypo)


main(side_one, side_two)
