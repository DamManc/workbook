# Exercise 89: Convert an Integer to Its Ordinal n


def int_to_ord(n):
    if n == 1:
        return "first"
    elif n == 2:
        return "second"
    elif n == 3:
        return "third"
    elif n == 4:
        return "fourth"
    elif n == 5:
        return "fifth"
    elif n == 6:
        return "sixth"
    elif n == 7:
        return "seventh"
    elif n == 8:
        return "eighth"
    elif n == 9:
        return "ninth"
    elif n == 10:
        return "tenth"
    elif n == 11:
        return "eleventh"
    elif n == 12:
        return "twelfth"
    else:
        return ""


def main(n):
    print("Your ordinal number is ", int_to_ord(n))


def demo(n):
    for v in range(1, 13):
        value = int_to_ord(v)
        print(v, value)


if __name__ == "__main__":
    number = int(input("Enter an integer beetwen 1 and 12: "))
    demo(number)
    main(number)

