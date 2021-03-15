first = float(input("Enter a first number: "))
second = float(input("Enter a second number: "))
third = float(input("Enter a third number: "))


def main(a, b, c):
    great_n = 0
    med_n = 0
    small_n = 0
    if a > b:
        if b > c:
            great_n = a
            med_n = b
            small_n = c
        elif a > c:
            great_n = a
            med_n = c
            small_n = b
        else:
            great_n = c
            med_n = a
            small_n = b
    elif b > a:
        if a > c:
            great_n = b
            med_n = a
            small_n = c
        elif b > c:
            great_n = b
            med_n = c
            small_n = a
        else:
            great_n = c
            med_n = b
            small_n = a
    else:
        if c > a:
            great_n = c
            med_n = a
        elif c == a:
            med_n = a
        else:
            great_n = a
            med_n = c
    print("The median is %i" % med_n)


main(first, second, third)