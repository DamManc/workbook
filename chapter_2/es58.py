# Is It a Leap Year?
def check_leap(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True


def main():
    year = int(input("Enter a year: "))
    if check_leap(year):
        print("It's a Leap Year!")
    else:
        print("It's Not a Leap Year!")


if __name__ == '__main__':
    main()
